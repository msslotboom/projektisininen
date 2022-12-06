from flask import Blueprint
from services.user_services import user_service
from services.citation_services import citation_service



test_controller = Blueprint("test_controller", __name__)


@test_controller.route("/test/reset_all", methods=["POST"])
def reset():
    user_service.delete_all_users()
    citation_service.delete_all_citations()

    return "reset"

@test_controller.route("/ping")
def ping():
    return "pong"
