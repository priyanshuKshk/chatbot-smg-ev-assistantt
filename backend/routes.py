from flask import Blueprint, request, jsonify
from backend.model import ask_bot

chatbot_route = Blueprint('chatbot', __name__)

@chatbot_route.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get("query", "")
    response = ask_bot(user_query)
    return jsonify({"response": response})