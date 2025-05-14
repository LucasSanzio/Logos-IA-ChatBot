import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify, request
from flask_cors import CORS # Import CORS

# Import blueprints and logic
from routes.example_routes import example_bp
from chatbot_logic import get_bot_response # Import chatbot logic

app = Flask(__name__)
CORS(app) # Enable CORS for all routes, allowing frontend to call from different origin (e.g. file://)

# Register blueprints
app.register_blueprint(example_bp, url_prefix='/api/example')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to UCHub Chatbot API!'})

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'UP'})

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    bot_reply = get_bot_response(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    # Note: For deployment, use a production WSGI server like Gunicorn
    # Ensure NLTK resources are available. Downloads should ideally be part of setup/deployment.
    # import nltk
    # try:
    #     nltk.data.find("tokenizers/punkt")
    #     nltk.data.find("corpora/stopwords")
    # except nltk.downloader.DownloadError:
    #     print("Downloading NLTK resources (punkt, stopwords)... This might take a moment.")
    #     nltk.download("punkt", quiet=True)
    #     nltk.download("stopwords", quiet=True)
    #     print("NLTK resources downloaded.")
        
    app.run(host='0.0.0.0', port=5000, debug=True)
