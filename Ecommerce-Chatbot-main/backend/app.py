from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize Flask app and configure
app = Flask(__name__)
CORS(app)



# Dummy users for login
users = {
    "admin": "admin",  # Example username and password
    "user1": "password1"
}

@app.route("/login", methods=["POST"])
def login():
    """Handle user login and generate response"""
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    # Check if username and password are provided
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Check if the username exists and the password is correct
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route("/products", methods=["GET"])
def get_products():
    """Fetch mock products"""
    products = [
        {"id": 1, "name": "Smart Watch", "category": "Electronics", "price": 199.99, "stock": 50},
        {"id": 2, "name": "Cotton Shirt", "category": "Textiles", "price": 25.00, "stock": 75},
        {"id": 3, "name": "Novel XYZ", "category": "Books", "price": 15.00, "stock": 100},
    ]
    return jsonify(products), 200


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chatbot conversation with OpenAI"""
    data = request.json
    user_message = data.get("message")
    
    # Check if the user provided a message
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Make a request to OpenAI's API with the user's message
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can also use "gpt-3.5-turbo" or another engine
            prompt=user_message,
            max_tokens=150,  # Maximum response length
            temperature=0.7,  # Controls randomness
        )

        # Get the chatbot's response from OpenAI API
        chatbot_message = response.choices[0].text.strip()
        
        return jsonify({"response": chatbot_message}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/populate", methods=["POST"])
def populate_data():
    """Populate mock data"""
    return jsonify({"message": "Mock data added successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
