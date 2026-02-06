import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Text Translator", page_icon="🌐")

st.title("🌐 AI Text Translator")
st.write("Translate text into multiple languages easily.")

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

text = st.text_area("✍ Enter text to translate")

selected_language = st.selectbox("🌍 Select Target Language", list(languages.keys()))

if st.button("🔄 Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text")
    else:
        try:
            dest_lang = languages[selected_language]

            translated = GoogleTranslator(source="auto", target=dest_lang).translate(text)

            st.success("✅ Translation Result")
            st.write(translated)

        except:
            st.error("❌ Translation failed")
