"""Connect to IBM Watson for Translation service"""
import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException, LanguageTranslatorV3

URL_LT = os.environ.get("url_lt", "")
APIKEY_LT = os.environ.get("apikey_lt")
VERSION_LT = "2018-05-01"


def get_language_translator() -> LanguageTranslatorV3:
    """create a Language transaltion model"""
    authenticator = IAMAuthenticator(APIKEY_LT)
    language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
    language_translator.set_service_url(URL_LT)
    return language_translator


LANGUAGE_TRANSLATOR = get_language_translator()


def english_to_french(english_text: str) -> str:
    """Translate from English to French

    Args:
        english_text (str): english text being translated

    Returns:
        str: translated french string
    """
    try:
        lang_response = LANGUAGE_TRANSLATOR.translate(
            text=english_text, model_id="en-fr"
        )
        resp = lang_response.get_result()
        return resp["translations"][0]["translation"]
    except ApiException as api_err:
        return (api_err.code, api_err.message)


def french_to_english(french_text: str) -> str:
    """French to English Translation

    Args:
        french_text (str): French

    Returns:
        str: English
    """
    try:
        lang_response = LANGUAGE_TRANSLATOR.translate(
            text=french_text, model_id="fr-en"
        )
        resp = lang_response.get_result()
        return resp["translations"][0]["translation"]
    except ApiException as api_err:
        return (api_err.code, api_err.message)
