"""Translation App Endpoints."""

from flask import Flask, request

from language_translation import translation_service

app = Flask("Language Translation")


@app.route("/")
def hello():
    """Status."""
    return {"status": "up"}


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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
