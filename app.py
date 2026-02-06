pip install googletrans==4.0.0-rc1

from googletrans import Translator

# Initialize the translator
translator = Translator()

text = input("Enter text to translate: ")
dest_lang = input("Enter target language (e.g., 'en' for English, 'fr' for French, 'hi' for Hindi): ")

translation = translator.translate(text, dest=dest_lang)
print(f"Translated Text: {translation.text}")

from googletrans import Translator

# Initialize translator
translator = Translator()

# User input
text = input("Enter text to translate: ")
dest_lang = input("Enter target language (e.g., 'en' for English, 'fr' for French, 'hi' for Hindi): ")

# Translate
translation = translator.translate(text, dest=dest_lang)

# Output result
print(f"Translated Text: {translation.text}")
