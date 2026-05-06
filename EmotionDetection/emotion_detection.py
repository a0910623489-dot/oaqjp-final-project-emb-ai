import requests
import json

def emotion_detector(text_to_analyze):
    """
    使用 Watson NLP 预测情绪，并包含针对空输入的错误处理。
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Task 7: 处理状态码为 400 的情况（空输入）
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # 将响应文本转换为字典
    formatted_response = json.loads(response.text)
    
    # 提取情绪分值
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 创建包含分值的字典
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # 寻找分值最高的情绪 (Dominant Emotion)
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion
    
    return result
