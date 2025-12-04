"""
Flask app providing an emotion detection API endpoint and UI renderer.
Runs locally on port 5000 and exposes `/emotionDetector`.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detection():
    """
    Receive text through query param `textToAnalyze`,
    run emotion detection and return emotions with dominant one.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return ("Invalid input!", 400)

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return ("Invalid input!", 400)

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant = response.get("dominant_emotion")

    return (
        f"For the given statement, system response is anger: {anger}, "
        f"disgust: {disgust}, fear: {fear}, joy: {joy}, sadness: {sadness}. "
        f"The dominant emotion is {dominant}.",
        200,
    )


@app.route("/")
def index():
    """
    Render main HTML page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
