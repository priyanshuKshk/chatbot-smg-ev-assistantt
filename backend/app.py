from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.routes import chatbot_route
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

# Register your chatbot API blueprint
app.register_blueprint(chatbot_route)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    file_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
