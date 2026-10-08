"""Emotion detection using the IBM Watson NLP emotion service."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the required result for blank/invalid input."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Analyze text and return five emotion scores and the dominant emotion."""
    if text_to_analyze is None or not str(text_to_analyze).strip():
        return _empty_result()

    payload = {"raw_document": {"text": str(text_to_analyze)}}

    try:
        response = requests.post(
            WATSON_URL,
            json=payload,
            headers=HEADERS,
            timeout=15,
        )
    except requests.RequestException:
        return _empty_result()

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]

    result = {name: emotions[name] for name in EMOTIONS}
    result["dominant_emotion"] = max(
        EMOTIONS, key=lambda name: result[name]
    )
    return result
