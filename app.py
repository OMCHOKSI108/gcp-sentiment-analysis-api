import os
from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    """A simple homepage to show the API is running."""
    return "<h1>Sentiment Analysis API</h1><p>Send a POST request to /predict</p>"

@app.route("/predict", methods=['POST'])
def predict():
    """Performs sentiment analysis on the provided text."""
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)
        if 'text' not in data:
            return jsonify({"error": "'text' field is missing from request body."}), 400
        
        text_to_analyze = data['text']
        blob = TextBlob(text_to_analyze)
        
        # Determine sentiment based on polarity
        if blob.sentiment.polarity > 0:
            sentiment = "Positive"
        elif blob.sentiment.polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Prepare the JSON response
        return jsonify({
            "text": text_to_analyze,
            "sentiment": sentiment,
            "polarity": blob.sentiment.polarity
        })
    except Exception as e:
        # Handle potential errors, like invalid JSON
        return jsonify({"error": f"An error occurred: {str(e)}"}), 400

if __name__ == "__main__":
    # Cloud Run and other platforms provide the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)