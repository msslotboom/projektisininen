from flask import Blueprint, render_template, request, redirect, flash
from repositories.user_repository import user_repository
from repositories.citation_repository import citation_repository
from services.user_services import user_service
from services.citation_services import citation_service
from services.bibgen import bibliography_generator
import sys

main_controller = Blueprint("main_controller", __name__)


@main_controller.route("/")
def render_home():
    return render_template("index.html")


@main_controller.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")


@main_controller.route("/login", methods=["POST"])
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


@main_controller.route("/logout")
def handle_logout():
    user_service.logout()
    return redirect("/")


@main_controller.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")


@main_controller.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    try:
        user_service.create_user(username, password, password_confirm)
        user_service.login(username)
        return redirect("/")
    except Exception as error:
        print(error)
        flash(str(error))
        return redirect("/register")


@main_controller.route("/new_citation", methods=["GET"])
def render_new_citation():
    return render_template("new_citation.html")


@main_controller.route("/new_citation", methods=["POST"])
def handle_new_citation():

    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        owner_id = user_service.get_session_user_id()
        authors = request.form.get("authors")
        title = request.form.get("title")
        year = request.form.get("year")
        citation_service.create_citation(owner_id, authors, title, int(year))
        return redirect("/citations")
    except Exception as error:
        return render_template("error.html", message=error)



@main_controller.route("/citations", methods=["GET"])
def render_citations():
    user_id = user_service.get_session_user_id()
    citations = citation_service.get_citations(user_id)
    return render_template("citations.html", citations=citations)

@main_controller.route("/delete_citation", methods=["POST"])
def handle_delete_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        citation_id = request.form["citation_id"]
        citation_service.delete_citation(citation_id)
        return redirect("/citations")
    except Exception as error:
        return render_template("error.html", message=error)
    
@main_controller.route("/edit_citation", methods=["GET"])
def render_edit_citation():
    try:
        citation_id = request.args.get("citation_id")
        citation = citation_service.get_content_by_id(citation_id)
        return render_template("edit_citation.html", citation=citation)
    except Exception as error:
        return render_template("error.html", message=error)

@main_controller.route("/edit_citation", methods=["POST"])
def handle_edit_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        citation_id = request.form.get("citation_id")
        authors = request.form.get("authors")
        title = request.form.get("title")
        year = request.form.get("year")
        citation_service.edit_citation(citation_id, authors, title, int(year))
        return redirect("/citations")
    except Exception as error:
        return render_template("error.html", message=error)

@main_controller.route("/download", methods=["GET"])
def handle_download():
    user_id = user_service.get_session_user_id()
    bibliography_generator.generate_bib_file(user_id)
    return render_template("download.html")
