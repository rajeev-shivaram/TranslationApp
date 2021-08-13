"""Translation App Endpoints."""

# import translation_app
import translation_service
from flask import Flask, request


app = Flask("Language Translation")


@app.route("/eng2fr", methods=["POST"])
def translate_eng2fr():
    """Translate English to French by calling translation service API"""
    text = request.form["text"]
    result = translation_service.english_to_french(text)
    return {"text": text, "translated": result}


@app.route("/fr2eng", methods=["POST"])
def translate_fr2eng():
    """Translate French to English by calling translation service API"""
    text = request.form["text"]
    result = translation_service.french_to_english(text)
    return {"text": text, "translated": result}
