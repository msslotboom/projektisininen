from entities.user import User
from db import db


class UserRepository:
    def __init__(self):
        self._users = []

    def find_all(self):
        users = []
        query = "SELECT username, password FROM users"
        db.execute(query)
        for row in db.fetchall():
            users.append(User(row[0],row[1]))
        self._users = users
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
        
        sql = "INSERT INTO users(id, username, password) VALUES (%s,%s,%s)"
        id = len(users) + 1
        insert = (id, user.username, user.password)
        db.execute(sql,insert)

        users.append(user)
        self._users = users

        return user

user_repository = UserRepository()