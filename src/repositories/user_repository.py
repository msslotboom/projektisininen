from entities.user import User
import psycopg2


class UserRepository:
    def __init__(self):
        self._users = []

    def find_all(self):

        return self._users

    def find_by_username(self, username):
        users = self.find_all()

        user_with_same_username = filter(
            lambda u: u.username == username, users
        )

        user_with_same_username_list = list(user_with_same_username)

        return user_with_same_username_list[0] if len(user_with_same_username_list) > 0 else None

    def create_new_user(self, user):
        users = self.find_all()
        does_user_exist = self.find_by_username(user.username)

        if does_user_exist:
            raise Exception(
                f"Käyttäjänimi {user.username} on jo käytössä"
            )
        users.append(user)
        self._users = users
        return user

user_repository = UserRepository()