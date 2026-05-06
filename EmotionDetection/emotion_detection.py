import requests
import json

def emotion_detector(text_to_analyze):
    """
    使用 Watson NLP 预测情绪，并返回格式化后的情绪得分及主导情绪。
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # 将响应文本转换为字典
    formatted_response = json.loads(response.text)
    
    # 提取情绪分值
    # 注意：Watson NLP 的响应结构中情绪通常位于 ['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 寻找分值最高的情绪 (Dominant Emotion)
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_list, key=emotion_list.get)
    
    # 构建最终输出字典
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
