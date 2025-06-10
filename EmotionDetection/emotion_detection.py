import json, requests

def emotion_detector(text_to_analyze):
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    MYOBJ = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=MYOBJ, headers=HEADER)

    if response.status_code == 400:
        return {
          'anger': None,
          'disgust': None,
          'fear': None,
          'joy': None,
          'sadness': None,
          'dominant_emotion': None  
        }

    elif response.status_code == 500:
        return {"error": "Server Error"}

    response_json = json.loads(response.text)
    emotions = response_json['emotionPredictions'][0]['emotion']
        
    results = {
     'anger': emotions['anger'],
     'disgust': emotions['disgust'],
     'fear': emotions['fear'],
     'joy': emotions['joy'],
     'sadness': emotions['sadness'],
     'dominant_emotion': max(emotions, key=emotions.get)
     }

    return results