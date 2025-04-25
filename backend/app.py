from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import chatbot_route
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

from flask_cors import CORS

CORS(app, resources={r"/*": {
    "origins": [
        "http://localhost:3000", 
        "https://chatbot-smg-ev-assistant-1.onrender.com"
    ],
    "allow_headers": ["Content-Type", "Authorization"],  # Adjust headers if needed
    "expose_headers": ["Content-Type"],  # Expose necessary headers
    "supports_credentials": True  # Allow credentials if you're using them (cookies, authorization)
}})

# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

@app.route("/")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=False, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        app.run(debug=False, host="0.0.0.0", port=5000)
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)