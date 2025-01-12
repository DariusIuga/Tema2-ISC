import os
import re
from datetime import datetime, timedelta, timezone

import jwt

# from flask import Flask, jsonify, redirect, render_template, request, url_for

# flag's not THIS easy to get :P
SECRET_FLAG = os.environ.get("FLAG", "<FLAG_READ_ERROR!>")

# FIXME: if this is ever leaked, user can sign its own malicious JWTs!
SECRET_KEY = "sypBbLu1hthv2hzsGyWgoFQsrI6lbRy4"

users = {}
# app = Flask(__name__, static_folder='', static_url_path='')


def create_token(username):
    payload = {
        "username": username,
        "isAdmin": True,
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=15),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


print(create_token("qwerty"))


# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/register")
# def register():
#     return render_template("register.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/profile", methods=["GET", "POST"])
# def profile():
#     token = request.cookies.get("accessToken")
#     if not token:
#         return redirect(url_for("login"))

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

#         username = payload.get("username", "")
#         if username not in users:
#             return "Invalid token", 401
#         result = None
#         if request.method == 'POST':
#             number = int(request.values.get("number"))
#             number = number * 31337
#             result = f"Result is: {number}"

#         is_admin = payload.get("isAdmin", False)
#         if not is_admin:
#             return render_template("profile.html", flag=None, result=result)

#         return render_template("profile.html", flag=SECRET_FLAG, result=result)

#     except jwt.ExpiredSignatureError:
#         return "Token has expired", 401
#     except jwt.InvalidTokenError:
#         return "Invalid token", 401

# @app.route("/logout")
# def logout():
#     response = redirect(url_for("home"))
#     response.delete_cookie("accessToken")
#     return response

# @app.route("/api/login", methods=["POST"])
# def api_login():
#     username = request.json.get("username")
#     password = request.json.get("password")

#     if not username or not password:
#         return jsonify({"error": "Username and password are required"}), 400

#     if username not in users or users[username] != password:
#         return jsonify({"error": "Invalid username or password"}), 401

#     return jsonify({"accessToken": create_token(username)}), 200

# @app.route("/api/register", methods=["POST"])
# def api_register():
#     first_name = request.json.get("firstName")
#     last_name = request.json.get("lastName")
#     email = request.json.get("email")
#     age = request.json.get("age")
#     website = request.json.get("website")
#     username = request.json.get("username")
#     password = request.json.get("password")
#     confirm_password = request.json.get("confirmPassword")

#     # Check if all the fields are provided

#     if not first_name:
#         return jsonify({"error": "First name is required"}), 400

#     if not last_name:
#         return jsonify({"error": "Last name is required"}), 400

#     if not email:
#         return jsonify({"error": "Email is required"}), 400

#     if not age:
#         return jsonify({"error": "Age is required"}), 400

#     if not website:
#         return jsonify({"error": "Website is required"}), 400

#     if not username:
#         return jsonify({"error": "Username is required"}), 400

#     if not password:
#         return jsonify({"error": "Password is required"}), 400

#     if not confirm_password:
#         return jsonify({"error": "Confirm password is required"}), 400

#     # Check if the fields are valid

#     if not first_name.isalpha() or len(first_name) < 2 or len(first_name) > 50:
#         return jsonify({"error": "First name is invalid"}), 400

#     if not last_name.isalpha() or len(last_name) < 2 or len(last_name) > 50:
#         return jsonify({"error": "Last name is invalid"}), 400

#     if not re.fullmatch(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$", email):
#         return jsonify({"error": "Email is invalid"}), 400

#     if not age.isdigit() or int(age) < 18 or int(age) > 30:
#         return jsonify({"error": "Age is invalid"}), 400

#     if not re.fullmatch(
#         r"^((https|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$",
#         website,
#     ):
#         return jsonify({"error": "Website is invalid"}), 400

#     if (
#         len(username) < 4
#         or len(username) > 20
#         or not username.isalnum()
#         or username in users
#     ):
#         return jsonify({"error": "Username is invalid"}), 400

#     if (
#         len(password) < 12
#         or len(password) > 20
#         or not re.fullmatch(
#             r"^(?=.*([A-Z]){1,})(?=.*[!@#$&*]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{8,100}$",
#             password,
#         )
#     ):
#         return jsonify({"error": "Password is invalid"}), 400

#     if confirm_password != password:
#         return jsonify({"error": "Confirm password is invalid"}), 400

#     users[username] = password
#     return jsonify({"success": "User registered successfully"}), 200


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, use_reloader=False)
