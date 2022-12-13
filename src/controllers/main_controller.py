from flask import Blueprint, render_template, request, redirect, flash
from services.user_services import user_service
from services.citation_services import citation_service
from services.bibgen import bibliography_generator

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
        user_service.validate_login_credentials(username, password)
        user_service.login(username)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/login")


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
        flash(str(error))
        return redirect("/register")


@main_controller.route("/new_citation", methods=["GET"])
def render_new_citation():
    return render_template("new_citation.html")

@main_controller.route("/new_citation", methods=["POST"])
def handle_new_citation_choice():
    dropdown = request.form.get("dropdown")

    if dropdown == "book":
        return render_template("new_book.html")
    elif dropdown == "article":
        return render_template("new_article.html")
    elif dropdown == "other":
        return render_template("other_citation.html")

@main_controller.route("/new_book", methods=["POST"])
def handle_new_book_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        owner_id = user_service.get_session_user_id()
        authors = request.form.get("authors")
        title = request.form.get("title")
        editor = request.form.get("editor")
        publisher = request.form.get("publisher")
        year = request.form.get("year")
        given_id = request.form.get("given_id")
        if (year == ""): #Antaa muuten virheellisen error messagen, citation_servicen validointi kohdassa or not year ei toimi
            year = 2031
        if (given_id == ""): #Jos ID kohta jätetty tyhjäksi, etsitään sopiva ID automaattisesti
            if not citation_service.check_duplicate_given_id(authors + title):
                given_id = authors + title
            # TODO
        citation_service.create_book_citation(int(owner_id), given_id, authors, title, editor, publisher, int(year))
        return redirect("/citations")
    except Exception as error:
        print(error, file=sys.stdout)
        flash(str(error))
        return render_template("/new_book.html")


@main_controller.route("/new_article", methods=["POST"])
def handle_new_article_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        owner_id = user_service.get_session_user_id()
        authors = request.form.get("authors")
        title = request.form.get("title")
        journal = request.form.get("journal")
        year = request.form.get("year")
        given_id = request.form.get("given_id")
        if (year == ""): #Antaa muuten virheellisen error messagen, citation_servicen validointi kohdassa or not year ei toimi
            year = 2031
        if (given_id == ""): #Jos ID kohta jätetty tyhjäksi, etsitään sopiva ID automaattisesti
            if not citation_service.check_duplicate_given_id(authors + title):
                given_id = authors + title
            # TODO
        citation_service.create_article_citation(int(owner_id), given_id, authors, title, journal, int(year))
        return redirect("/citations")
    except Exception as error:
        print(error, file=sys.stdout)
        flash(str(error))
        return render_template("/new_article.html")

@main_controller.route("/new_other_citation", methods=["POST"])
def handle_new_other_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        owner_id = user_service.get_session_user_id()
        authors = request.form.get("authors")
        title = request.form.get("title")
        type = request.form.get("type")
        other = request.form.get("other")
        given_id = request.form.get("given_id")
        year = request.form.get("year")
        if (year == ""): #Antaa muuten virheellisen error messagen, citation_servicen validointi kohdassa or not year ei toimi
            year = 2031
        if (given_id == ""): #Jos ID kohta jätetty tyhjäksi, etsitään sopiva ID automaattisesti
            if not citation_service.check_duplicate_given_id(authors + title):
                given_id = authors + title
            # TODO
        citation_service.create_other_citation(int(owner_id), given_id, authors, title, type, other, int(year))
        return redirect("/citations")
    except Exception as error:
        print(error, file=sys.stdout)
        flash(str(error))
        return render_template("/new_article.html")

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
        citation_type = request.form["citation_type"]
        citation_service.delete_citation(citation_id, citation_type)
        return redirect("/citations")
    except Exception as error:
        flash(str(error))
        return redirect("/delete_citation")


@main_controller.route("/edit_citation", methods=["GET"])
def render_edit_citation():
    try:
        citation_id = request.args.get("citation_id")
        citation = citation_service.get_content_by_id(citation_id)
        return render_template("edit_citation.html", citation=citation)
    except Exception as error:
        flash(str(error))
        return redirect("/edit_citation")

@main_controller.route("/edit_citation", methods=["POST"])
def handle_edit_citation():
    try:
        csrf_token = request.form["csrf_token"]
        user_service.check_csrf(csrf_token)
        citation_id = request.form.get("citation_id")
        authors = request.form.get("authors")
        title = request.form.get("title")
        year = request.form.get("year")
        given_id = request.form.get("given_id")
        citation_service.edit_citation(citation_id, authors, title, int(year), int(given_id))
        return redirect("/citations")
    except Exception as error:
        flash(str(error))
        return redirect("/edit_citation")

@main_controller.route("/download", methods=["GET"])
def handle_download():
    user_id = user_service.get_session_user_id()
    bibliography_as_text = bibliography_generator.generate_bib_text(user_id)
    bibliography_generator.generate_bib_file(bibliography_as_text)
    return render_template("download.html")
