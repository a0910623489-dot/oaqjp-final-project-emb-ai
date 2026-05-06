from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    处理来自网页前端的情绪检测请求。
    """
    # 从 URL 参数 textToAnalyze 中获取用户输入的文本
    text_to_analyze = request.args.get('textToAnalyze')

    # 调用之前编写的情绪检测函数
    response = emotion_detector(text_to_analyze)

    # 提取主导情绪，用于 Task 7 的错误处理判断
    dominant_emotion = response.get('dominant_emotion')

    # 【Task 7 核心改动】：如果主导情绪为空，返回错误提示
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # 【Task 6/7 要求格式】：返回格式化后的情绪得分字符串
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
    渲染主页（index.html）
    """
    return render_template('index.html')

if __name__ == "__main__":
    # 启动 Flask 服务，监听 5000 端口
    app.run(host="0.0.0.0", port=5000)
