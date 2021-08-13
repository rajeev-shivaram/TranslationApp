"""Translation App"""

from ibm_watson import ApiException

from translation_service import LANGUAGE_TRANSLATOR


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
