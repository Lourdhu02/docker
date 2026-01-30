from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key (keep strong in real apps)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Fake DB (for learning)
users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"msg": "User already exists"}), 400

    users[username] = generate_password_hash(password)
    return jsonify({"msg": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"msg": "Invalid credentials"}), 401

    if not check_password_hash(users[username], password):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Welcome {current_user}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
