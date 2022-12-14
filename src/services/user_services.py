from models.user import User
from repositories.user_repository import user_repository
from flask import session
from secrets import token_hex
from werkzeug.security import check_password_hash, generate_password_hash


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repo=user_repository):
        self._user_repo = user_repo

    def create_user(self, username, password, password_confirmation):
        self.validate_username_and_password(
            username, password, password_confirmation)

        password_hash = generate_password_hash(password)

        return self._user_repo.create_new_user(User(username=username, password=password_hash))

    def validate_username_and_password(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Käyttäjänimi ja salasana vaaditaan")

        if len(username) < 3:
            raise UserInputError("Käyttäjänimi on liian lyhyt")

        if len(username) > 20:
            raise UserInputError("Käyttäjänimi on liian pitkä")

        if len(password) < 3:
            raise UserInputError("Salasana on liian lyhyt")

        if len(password) > 100:
            raise UserInputError("Salasana on liian pitkä")

        if password != password_confirmation:
            raise UserInputError("Salasanat eivät täsmää")

    def validate_login_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Käyttäjänimi ja salasana vaaditaan")

        user = self._user_repo.find_by_username(username)

        if user is None or not check_password_hash(user.password, password):
            raise AuthenticationError("Väärä käyttäjänimi tai salasana")

        return user

    def login(self, username):
        session["user_username"] = username
        session["csrf_token"] = token_hex(16)

    def logout(self):
        del session["user_username"]
        del session["csrf_token"]

    def get_session_user_id(self):
        username = session["user_username"]
        return self._user_repo.get_id(username)

    def check_csrf(self, crsf_token):
        if crsf_token != session["csrf_token"]:
            raise AuthenticationError("CSRF eroavuus")

    def delete_all_users(self):
        return self._user_repo.delete_all_users()


user_service = UserService()
