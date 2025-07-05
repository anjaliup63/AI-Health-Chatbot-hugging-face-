import streamlit as st
from transformers import pipeline
from intent_classifier import classify_intent
from deep_translator import GoogleTranslator  # NEW: For translation

# Load the Hugging Face model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

chatbot = load_model()

# Streamlit UI
st.title("🤖 AI Health Chatbot (Hugging Face Based)")
st.markdown("Ask a health-related question (in English or Hindi) and get an AI-generated answer:")

# Input box
user_input = st.text_input("💬 Your Question:")

# When button is clicked
if st.button("Get Answer"):
    if user_input.strip() != "":
        try:
            # 🔄 Translate input to English if needed
            translated_input = GoogleTranslator(source='auto', target='en').translate(user_input)

            # Intent classification based on translated text
            intent = classify_intent(translated_input)

            # Generate answer using Hugging Face model
            with st.spinner("Thinking..."):
                result = chatbot(translated_input, max_length=100, do_sample=True)

            # Show response
            st.markdown(f"**Intent Detected:** `{intent}`")
            st.markdown("**Answer:**")
            st.write(result[0]['generated_text'])

        except Exception as e:
            st.error("⚠️ Something went wrong: " + str(e))
    else:
        st.warning("Please enter a valid question.")
