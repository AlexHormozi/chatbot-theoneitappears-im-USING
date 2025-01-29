from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/")
def home():
    return "Chatbot API is running!"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message", "")

    bot_response = f"You said: {user_message}"
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
