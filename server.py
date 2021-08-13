"""Translation App Endpoints."""

from flask import Flask, request

from machinetranslation import translator

app = Flask("Language Translation")


@app.route("/")
def hello():
    """Status."""
    return {"status": "up"}


@app.route("/eng2fr/<text>", methods=["GET"])
def translate_eng2fr(text):
    """Translate English to French by calling translation service API"""
    result = translator.english_to_french(text)
    return {"text": text, "translated": result}


@app.route("/fr2eng/<text>", methods=["GET"])
def translate_fr2eng(text):
    """Translate French to English by calling translation service API"""
    result = translator.french_to_english(text)
    print(result)
    return {"text": text, "translated": result}


if __name__ == '__main__':
    app.run()
