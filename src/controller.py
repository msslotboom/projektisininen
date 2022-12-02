from flask import Blueprint, render_template, request, redirect, flash
from services.user_services import user_service
from services.citation_services import citation_service
import sys

controller = Blueprint("controller", __name__)


@controller.route("/")
def render_home():
    return render_template("index.html")


@controller.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")


@controller.route("/login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user_service.validate_credentials(username, password)
        user_service.login(username)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/register")


@controller.route("/logout")
def handle_logout():
    user_service.logout()
    return redirect("/")


@controller.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")


@controller.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    try:
        user_service.create_user(username, password, password_confirm)
        return redirect("/login")
    except Exception as error:
        flash(str(error))
        return redirect("/register")


@controller.route("/new_citation", methods=["GET"])
def render_new_citation():
    return render_template("new_citation.html")


@controller.route("/new_citation", methods=["POST"])
def handle_new_citation():

    try:
        csrf_token = request.form["csrf_token"]
        print(csrf_token)
        user_service.check_csrf(csrf_token)

    except Exception as error:
        flash(str(error))
        print(error)
        return redirect("/")

    owner_id = user_service.get_session_user_id()
    authors = request.form.get("authors")
    title = request.form.get("title")
    year = request.form.get("year")
    citation_service.create_citation(owner_id, authors, title, int(year))
    return redirect("/")

@controller.route("/citations", methods=["GET"])
def render_citations():
    # try:
    #     csrf_token = request.form["crsf_token"]
    #     print(csrf_token, file=sys.stdout)
    #     user_service.check_csrf(csrf_token)
    # except Exception as error:
    #     flash(str(error))
    #     print(error, file=sys.stdout)
    #     return redirect("/")

    userid = user_service.get_session_user_id()
    print(userid, file=sys.stderr)
    citations = citation_service.get_citations(
        str(userid)
    )
    print(citations, file=sys.stdout)
    return render_template("citations.html", citations = citations)