from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name, email, password = data['name'], data['email'], data['password']

    for user in users:
        if user['email'] == email:
            return jsonify({"message": "User already exists!"}), 400

    users.append({"name": name, "email": email, "password": password})
    return jsonify({"message": "Registration successful!"}), 200

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email, password = data['email'], data['password']

    user = next((user for user in users if user['email'] == email and user['password'] == password), None)
    if not user:
        return jsonify({"message": "Invalid email or password!"}), 400

    return jsonify({"message": "Login successful!", "name": user['name']}), 200

if __name__ == "__main__":
    app.run(debug=True)
