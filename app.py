import streamlit as st
import tensorflow as tf

from utils.preprocess import preprocess_image
from utils.history_loader import load_history
from models.patient_history_model import analyze_history
from agents.medical_agent import medical_agent

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(page_title="AI Pneumonia Detection", layout="wide")

st.title("AI Agent Pneumonia Diagnosis System")
st.write("Upload an X-ray and patient medical history to predict pneumonia risk.")

# --------------------------------------------------
# Load trained CNN model
# --------------------------------------------------

@st.cache_resource
def load_cnn():

    model = tf.keras.models.load_model("trained_models/pneumonia_model_ga.h5")

    return model

model = load_cnn()

# --------------------------------------------------
# Sidebar patient history upload
# --------------------------------------------------

st.sidebar.header("Patient Medical History")

history_file = st.sidebar.file_uploader(
    "Upload patient history (CSV or JSON)",
    type=["csv","json"]
)

# --------------------------------------------------
# X-ray Upload
# --------------------------------------------------

uploaded_xray = st.file_uploader(
    "Upload Chest X-ray Image",
    type=["jpg","jpeg","png"]
)

# --------------------------------------------------
# Run Diagnosis
# --------------------------------------------------

if st.button("Run Diagnosis"):

    if uploaded_xray is None:

        st.warning("Please upload an X-ray image")

    else:

        st.subheader("Uploaded X-ray")

        st.image(uploaded_xray, width=300)

        # -----------------------------------------
        # Image preprocessing
        # -----------------------------------------

        img = preprocess_image(uploaded_xray)

        # -----------------------------------------
        # CNN Prediction
        # -----------------------------------------

        prediction = model.predict(img)[0][0]

        # -----------------------------------------
        # Patient history analysis
        # -----------------------------------------

        history_prob = 0

        if history_file:

            history = load_history(history_file)

            st.write("Loaded History:", history)

            history_prob = analyze_history(history)

            st.subheader("Patient History")

            st.json(history)

        # -----------------------------------------
        # AI Agent decision
        # -----------------------------------------

        final_risk, diagnosis, explanation = medical_agent(
            prediction,
            history_prob
        )

        # ------------------------------------------------
        # Display results
        # ------------------------------------------------

        st.subheader("Diagnosis Result")

        st.metric(
            label="Pneumonia Risk",
            value=f"{final_risk*100:.2f}%"
        )

        st.progress(int(final_risk*100))

        st.write("### Diagnosis")
        st.write(diagnosis)

        st.write("### AI Explanation")
        st.write(explanation)

        # ------------------------------------------------
        # Debug outputs (for project explanation)
        # ------------------------------------------------

        st.subheader("Model Debug Information")

        st.write("CNN Pneumonia Probability:", float(prediction))

        st.write("Patient History Risk:", float(history_prob))

        