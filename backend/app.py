from flask import Flask
from flask_cors import CORS
from backend.routes import chatbot_route

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

if __name__ == "__main__":
    app.run(debug=True)  # Allow access from local network
