from os import getenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from services.user_services import user_service

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

def redirect_to_home():
    return redirect(url_for("render_home"))

def redirect_to_register():
    return redirect(url_for("render_register"))

def redirect_to_login():
    return redirect(url_for("render_login"))

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user_service.validate_credentials(username, password)
        return redirect_to_home()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    try:
        user_service.create_user(username, password, password_confirm)
        return redirect_to_login()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()

