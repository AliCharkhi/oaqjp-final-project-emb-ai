"""
This is the flask application used for emotion detection of provided text.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    This function gets the input text from the HTML interface and analyzes 
    the emotion of the provided text and results will be shown in specific format.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    # Return a formatted string with the sentiment label and score
    return result

@app.route("/")
def render_index_page():
    """
    This function renders the landing page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
