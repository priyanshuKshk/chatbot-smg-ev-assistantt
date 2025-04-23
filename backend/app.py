from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.routes import chatbot_route
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

@app.route("/")
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Serve React's static files
@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)  # Allow access from local network
