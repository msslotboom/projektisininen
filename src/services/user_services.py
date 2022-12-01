from entities.user import User
from repositories.user_repository import user_repository
from flask import session
from secrets import token_hex

class UserInputError(Exception):
    pass

class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repo=user_repository):
        self._user_repo = user_repository

    def validate_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Käyttäjänimi ja salasana vaaditaan")
        
        user = self._user_repo.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Väärä käyttäjänimi tai salasana")

        return user
    
    def create_user(self, username, password, password_confirmation):
        self.validate_user(username, password, password_confirmation)

        user = self._user_repo.create_new_user(
            User(username, password)
        )

        return user

    def validate_user(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Käyttäjänimi ja salasana vaaditaan")
    
    def login(self, username):
        session["user_username"] = username
        session["csrf_token"] = token_hex(16)
    

    def logout(self):
        del session["user_username"]
        del session["csrf_token"]


user_service = UserService()