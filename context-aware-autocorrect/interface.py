# interface.py
import streamlit as st
from utils.corrector import AutoCorrector

st.title("✍️ Context-Aware AutoCorrect App")

corrector = AutoCorrector("models/vocab.pkl")

input_word = st.text_input("🔤 Enter a word to check:")

col1, col2 = st.columns(2)

if col1.button("🔍 Show Suggestions"):
    if input_word:
        suggestions = corrector.suggest(input_word)
        st.write("Top Suggestions:")
        for word, score in suggestions:
            st.markdown(f"- {word} (Similarity: {score:.2f})")

if col2.button("✅ Auto Correct"):
    if input_word:
        corrected = corrector.autocorrect(input_word)
        st.success(f"AutoCorrected to: `{corrected}`")
