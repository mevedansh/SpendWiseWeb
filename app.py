from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing fields."})

    users = load_users()

    for user in users:
        if user["username"] == username:
            return jsonify({"status": "error", "message": "Username already exists!"})

    users.append({"username": username, "password": password})
    save_users(users)

    return jsonify({"status": "success", "message": "User registered!"})

@app.route('/check_login', methods=['POST'])
def check_login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing fields."})

    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"status": "success", "message": "Login successful!"})

    return jsonify({"status": "error", "message": "Invalid username or password."})

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

@app.route("/")
def hello():
    return render_template("welcome_page-copy.html")


@app.route("/register")
def reg():
    return render_template("Register_page-Copy.html")

@app.route("/login")
def log():
    return render_template("login-Copy.html")

@app.route("/dashboard")
def dash():
    return render_template("dashboard-Copy.html")

@app.route("/create_trip")
def create():
    return render_template("create_trip-Copy.html")

@app.route("/personal_expense")
def perso():
    return render_template("personal_expense-Copy.html")

@app.route("/group_expense")
def group():
    return render_template("group_expense-Copy.html")

@app.route("/about_spendwise")
def about():
    return render_template("about_spendwise-Copy.html")

@app.route("/profile")
def pro():
    return render_template("profile-Copy.html")

if __name__ == "__main__" :
    app.run(debug=True)