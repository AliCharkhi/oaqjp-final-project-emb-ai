import json, requests

def emotion_detector(text_to_analyse):
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/\
    watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    MYOBJ = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json=MYOBJ, headers=HEADER)

    if response.status_code == 500:
        return {"error": "Server Error"}

    return response.text