from models.user import User
from app import db


class UserRepository:
    def find_all_users(self):
        return User.query.all()

    def find_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user

    def create_new_user(self, user: User):
        if self.find_by_username(user.username) is not None:
            raise Exception(
                f"Käyttäjänimi {user.username} on jo käytössä"
            )

        db.session.add(user)
        db.session.commit()

        return user

    def get_id(self, username):
        user = User.query.filter_by(username=username).first()
        return user.id

    def delete_all_users(self):
        return_value = User.query.delete()
        db.session.commit()

        return return_value


user_repository = UserRepository()
