from flask import Flask
from flask_cors import CORS
from routes import chatbot_route

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})
# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

if __name__ == "__main__":
    app.run(debug=True)