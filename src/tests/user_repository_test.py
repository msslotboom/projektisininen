import unittest
from repositories.user_repository import user_repository
from models.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()

    def test_create_new_user_with_valid_creditentials(self):
        user_repository.create_new_user(User(username="Jaakko", password="salasana1"))
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Jaakko")
        self.assertEqual(users[0].password, "salasana1")

    def test_user_not_created_if_user_with_username_exists(self):
        user_repository.create_new_user(User(username="Jaakko", password="salasana1"))
        
        try:
            user_repository.create_new_user(User(username="Jaakko", password="salasana2"))
        
        except:
            Exception("Käyttäjänimi Jaakko on jo käytössä")
        
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Jaakko")
        self.assertEqual(users[0].password, "salasana1")

    def test_user_found_by_username(self):
        user_repository.create_new_user(User(username="Jaakko", password="salasana1"))
        user = user_repository.find_by_username("Jaakko")

        self.assertEqual(user.username, "Jaakko")
