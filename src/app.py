from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")