"""
This module initiates the Flask application for emotion detection.
It provides endpoints to render the index page and analyze text for emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Receives text from the HTML interface, sends it to the emotion_detector
    function, and returns a formatted string containing the scores.
    """
    # 获取用户输入的文本
    text_to_analyze = request.args.get('textToAnalyze')

    # 调用检测函数
    response = emotion_detector(text_to_analyze)

    # 提取主导情绪
    dominant_emotion = response.get('dominant_emotion')

    # Task 7 要求的错误处理逻辑
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # 返回符合要求的格式化输出
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page (index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    # 在 5000 端口启动服务器
    app.run(host="0.0.0.0", port=5000)
