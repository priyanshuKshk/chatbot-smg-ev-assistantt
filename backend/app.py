from flask import Flask
from flask_cors import CORS
from backend.routes import chatbot_route
from flask import send_from_directory
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

if __name__ == "__main__":
    app.run(debug=True)  # Allow access from local network
@app.route("/")
def home():
    return "Backend is running"
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend/build', 'index.html')
@app.route('/')
def serve_react():
    return send_from_directory('../frontend/build', 'index.html')
@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('../frontend/build', path)