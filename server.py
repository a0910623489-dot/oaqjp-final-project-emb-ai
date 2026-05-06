"""
此脚本启动一个 Flask 应用程序，提供情绪检测服务。
它调用 EmotionDetection 包中的 emotion_detector 函数。
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# 初始化 Flask 应用程序
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    处理情绪检测请求。
    从 URL 参数获取文本，调用检测函数并返回格式化的字符串。
    """
    # 从查询字符串获取文本
    text_to_analyze = request.args.get('textToAnalyze')

    # 调用情绪检测函数
    response = emotion_detector(text_to_analyze)

    # 提取结果（处理空响应的情况，虽然 Task 7 才正式要求 Error Handling，
    # 但建议预留或按 Task 6 的正常流程输出）
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # 如果输入无效（例如 dominant_emotion 为 None）
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # 按照 Task 6 要求的格式返回字符串
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    渲染主页模板。
    """
    return render_template('index.html')

if __name__ == "__main__":
    # 在 5000 端口启动服务器
    app.run(host="0.0.0.0", port=5000)
