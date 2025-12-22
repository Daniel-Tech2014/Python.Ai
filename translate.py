import speech_recognition as sr
import pyttsx3
from googletrans import Translator  # Google Translate API

# Initialize text-to-speech engine
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    voices = engine.getProperty('voices')

    # Set voice for English or other language if supported by pyttsx3
    if language == "en":
        engine.setProperty('voice', voices[0].id)  # Default English voice
    else:
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)  # Fallback voice if available

    engine.say(text)
    engine.runAndWait()

# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")  # Use English for speech recognition
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
        return ""
    # Translate text using Google Translate API
def translate_text(text, target_language="es"):  # Default target language is Spanish (es)
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌐 Translated text: {translation.text}")
    return translation.text


# Display language options to the user
def display_language_options():
    print("🌐 Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Marathi (mr)")
    print("4. Gujarati (gu)")
    print("5. Japanese (ja)")
    print("6. Spanish (es)")

    # User selects language
    choice = input("Please select the target language number (1-9): ")
    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "mr",
        "4": "gu",
        "5": "ja",
        "6": "es",
    }

    # Main function to combine all steps
def main():
    # Step 1: Display language options and get user's choice
    target_language = display_language_options()

    # Step 2: Speech-to-Text (recognizing English speech)
    original_text = speech_to_text()
    if original_text:
        # Step 3: Translate to selected target language
        translated_text = translate_text(original_text, target_language=target_language)

        # Step 4: Text-to-Speech (Translate output and speak it)
        speak(translated_text, language="en")  # Speak the translation in English
        print("✅ Translation spoken out!")

if __name__ == "__main__":
    main()