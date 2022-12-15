from flask import Blueprint
from services.user_services import user_service
from services.citation_services import citation_service



test_controller = Blueprint("test_controller", __name__)


@test_controller.route("/test/reset_all", methods=["POST"])
def reset():
    citation_service.delete_all_citations()
    user_service.delete_all_users()

    return "reset"

@test_controller.route("/ping")
def ping():
    return "pong"
