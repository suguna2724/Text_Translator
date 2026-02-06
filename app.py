import streamlit as st
from googletrans import Translator

# Page configuration
st.set_page_config(page_title="AI Text Translator", page_icon="🌐")

# Initialize translator
translator = Translator()

# Title
st.title("🌐 AI Text Translator")
st.write("Translate text into multiple languages easily.")

# Language dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja"
}

# Input text
text = st.text_area("✍ Enter text to translate")

# Dropdown language selection
selected_language = st.selectbox("🌍 Select Target Language", list(languages.keys()))

# Translate button
if st.button("🔄 Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text")
    else:
        try:
            dest_lang = languages[selected_language]
            translation = translator.translate(text, dest=dest_lang)

            st.success("✅ Translation Result")
            st.write(translation.text)

        except:
            st.error("❌ Translation failed. Try again later.")
