import streamlit as st
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

# Streamlit UI
st.set_page_config(page_title="Text Summarization Dashboard", layout="wide")

st.title("📄 AI-Powered Text Summarization")
st.write("Enter your text below, and the model will generate a concise summary.")

# User input
input_text = st.text_area("Paste your text here:", height=200)

# Summary length options
min_length = st.slider("Minimum summary length", min_value=10, max_value=100, value=30)
max_length = st.slider("Maximum summary length", min_value=50, max_value=300, value=100)

# Summarize button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
            st.subheader("🔍 Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown("🔹 Built with [Hugging Face Transformers](https://huggingface.co) & [Streamlit](https://streamlit.io)")
