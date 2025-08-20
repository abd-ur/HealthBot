import re
import time
import random
from pathlib import Path

import numpy as np
import streamlit as st

# App Config
st.set_page_config(page_title="LIFE – Health Care Assistant (Prototype)", page_icon="🩺", layout="centered")
st.title("🩺 Hi, I am LIFE – your personal health care assistant (Prototype)")
st.caption("For hackathon demo purposes only. This is **not** medical advice.")

# Utilities
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)
SK_MODEL_PATH = MODEL_DIR / "diabetes_model.pkl"
TF_MODEL_PATH = MODEL_DIR / "tf_model.keras"

@st.cache_resource(show_spinner=False)
def load_sklearn_model(path: Path):
    import pickle
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    if path.exists():
        with open(path, "rb") as f:
            return pickle.load(f)

    rng = np.random.RandomState(42)
    # Features: [glucose, systolic_bp, insulin, bmi, age, gender_binary]
    X = rng.normal(loc=[120, 130, 90, 26, 40, 0.5], scale=[25, 20, 40, 5, 12, 0.5], size=(600, 6))
    y = (X[:, 0] + 0.3 * X[:, 3] + 0.2 * X[:, 1] + 0.1 * X[:, 4] > 190).astype(int)
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipe.fit(X, y)

    try:
        with open(path, "wb") as f:
            pickle.dump(pipe, f)
    except Exception:
        pass
    return pipe

@st.cache_resource(show_spinner=False)
def load_tf_model(path: Path):
    try:
        import tensorflow as tf  # noqa
    except Exception:
        return None
    if not path.exists():
        return None
    import tensorflow as tf
    try:
        return tf.keras.models.load_model(path)
    except Exception:
        return None

sk_model = load_sklearn_model(SK_MODEL_PATH)
tf_model = load_tf_model(TF_MODEL_PATH)

# Simple rule-based intent engine
RULES = {
    "hi": ["Hello! How can I help you today?", "Hi there!"],
    "hello": ["Hello!"],
    "checkup": ["Shall we start your diabetes check?", "We can begin a quick screening now."],
    "diabetes": ["Want to start a diabetes screening?", "I can guide you through a quick diabetes risk check."],
    "sugar": ["Would you like a quick screening?"],
    "yes": ["Great — let’s proceed. Open the **Quick Screening** tab below."],
    "no": ["Okay — we can do this another time. Stay healthy!"],
    "bye": ["Goodbye! Take care.", "Bye! Wishing you good health."],
}
DEFAULT_RESPONSES = ["Sorry, I couldn't understand that. Try 'checkup' or ask a first‑aid question."]

INTENT_PATTERNS = [
    (re.compile(r"\b(hi|hello|hey)\b", re.I), "hi"),
    (re.compile(r"\b(checkup|diagnosis|screen)\b", re.I), "checkup"),
    (re.compile(r"\b(diabetes|sugar)\b", re.I), "diabetes"),
    (re.compile(r"\b(yes|yeah|yep|sure)\b", re.I), "yes"),
    (re.compile(r"\b(no|nope|later)\b", re.I), "no"),
    (re.compile(r"\b(bye|goodbye|see you)\b", re.I), "bye"),
]

def reply_for_text(text: str) -> str:
    text = text.strip()
    if not text:
        return random.choice(DEFAULT_RESPONSES)
    for pat, intent in INTENT_PATTERNS:
        if pat.search(text):
            return random.choice(RULES.get(intent, DEFAULT_RESPONSES))
    if re.search(r"\b(burn|burned|scald)\b", text, re.I):
        return (
            "First‑aid for minor burns: cool the area under running water for 20 minutes,"
            " remove tight items, **do not** apply ice or toothpaste, and cover with a sterile gauze."
        )
    if re.search(r"\b(cut|bleed|bleeding|wound)\b", text, re.I):
        return (
            "For bleeding: apply firm pressure with a clean cloth for 10–15 minutes, elevate if possible,"
            " and seek urgent care if bleeding is heavy or won't stop." 
        )
    return random.choice(DEFAULT_RESPONSES)

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "You can say 'checkup' to begin a quick diabetes screening, or ask a first‑aid question (e.g., ‘I have a small burn’)."}
    ]

# Sidebar: backend and model management
with st.sidebar:
    st.header("⚙️ Settings")
    backend = st.selectbox("Prediction backend", ["Scikit‑Learn", "TensorFlow (if available)"]) 
    if backend.startswith("Tensor") and tf_model is None:
        st.info("TensorFlow model not found. Falling back to Scikit‑Learn.")
        backend = "Scikit‑Learn"

    st.divider()
    st.markdown("**Model Files (optional)**")
    st.markdown("Upload a `.pkl` (sklearn) or `.keras` (TF) to override.")
    up = st.file_uploader("Upload model file", type=["pkl", "keras"], accept_multiple_files=False)
    if up is not None:
        suffix = Path(up.name).suffix.lower()
        save_path = SK_MODEL_PATH if suffix == ".pkl" else TF_MODEL_PATH
        save_path.write_bytes(up.read())
        st.success(f"Saved {up.name} → {save_path}")
        # Force reload next run
        st.experimental_rerun()

# Tabs: Chat and Quick Screening
chat_tab, screen_tab = st.tabs(["💬 Chat", "🧪 Quick Screening"]) 

with chat_tab:
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])    

    user_input = st.chat_input("Type your message…")
    if user_input is not None:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        bot_text = reply_for_text(user_input)
        with st.chat_message("assistant"):
            st.markdown(bot_text)
        st.session_state.messages.append({"role": "assistant", "content": bot_text})

with screen_tab:
    st.subheader("Diabetes Quick Screening (Demo)")
    st.caption("Enter recent vitals/lab values if available. Values are for demo only.")

    with st.form("screen_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, value=35)
            gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
            bmi = st.number_input("BMI", min_value=9.0, max_value=60.0, value=26.0, step=0.1)
        with col2:
            insulin = st.number_input("Insulin (µIU/mL)", min_value=0.0, max_value=400.0, value=90.0, step=0.1)
            glucose = st.number_input("Glucose (mg/dL)", min_value=50.0, max_value=400.0, value=120.0, step=0.1)
            sbp = st.number_input("Systolic BP (mmHg)", min_value=70.0, max_value=240.0, value=125.0, step=0.5)

        submitted = st.form_submit_button("Submit & Predict")

    if submitted:
        st.success("Your records are saved.")
        st.write({
            "Age": age,
            "Gender": gender,
            "BMI": bmi,
            "Insulin": insulin,
            "Glucose": glucose,
            "Systolic BP": sbp,
        })

        # Feature prep
        gender_bin = 1 if gender.lower().startswith("f") else 0
        features = np.array([[glucose, sbp, insulin, bmi, age, gender_bin]], dtype=float)

        pred_proba = None
        pred_label = None

        if backend == "Scikit‑Learn":
            try:
                if hasattr(sk_model, "predict_proba"):
                    pred_proba = float(sk_model.predict_proba(features)[0, 1])
                pred_label = int(getattr(sk_model, "predict")(features)[0])
            except Exception as e:
                st.error(f"Scikit‑Learn prediction error: {e}")
        else:  # TensorFlow
            try:
                import tensorflow as tf  # noqa: F401
                out = tf_model.predict(features, verbose=0)
                if out.ndim == 2 and out.shape[1] == 1:
                    pred_proba = float(out[0, 0])
                elif out.ndim == 2:
                    pred_proba = float(out[0].max())
                else:
                    pred_proba = float(out.squeeze())
                pred_label = int(pred_proba >= 0.5)
            except Exception as e:
                st.error(f"TensorFlow prediction error: {e}")

        if pred_label is not None:
            risk_text = "High" if pred_label == 1 else "Low"
            if pred_proba is not None:
                st.metric("Estimated Diabetes Risk", f"{risk_text}", f"prob≈{pred_proba:.2f}")
            else:
                st.metric("Estimated Diabetes Risk", risk_text)

            # Simple rule-of-thumb recommendations
            recos = []
            if glucose >= 200:
                recos.append("Your glucose is very high; seek medical care promptly.")
            elif glucose >= 140:
                recos.append("Elevated glucose; consider a confirmatory test and medical advice.")

            if sbp >= 140:
                recos.append("High blood pressure noted; reduce salt, monitor regularly, and consult a physician.")

            if bmi >= 30:
                recos.append("BMI in obese range; gradual weight management and activity can help.")

            if not recos:
                recos.append("Maintain a balanced diet, regular activity, and periodic screening.")

            st.markdown("### Recommendations (Prototype)")
            for r in recos:
                st.write("• ", r)

            st.info(
                "This tool is a hackathon prototype and **not** a diagnosis."
                " For concerning symptoms or abnormal values, please consult a qualified clinician."
            )
            
# Footer
st.caption("© Hackathon Prototype – Built with Streamlit, Scikit‑Learn, and optional TensorFlow.")
