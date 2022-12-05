import unittest
from repositories.user_repository import user_repository
from repositories.citation_repository import citation_repository
from models.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        citation_repository.delete_all_citations()
        user_repository.delete_all_users()

    def test_create_new_user_with_valid_creditentials(self):
        user_repository.create_new_user(
            User(username="Jaakko", password="salasana_hash"))
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Jaakko")
        self.assertEqual(users[0].password, "salasana_hash")

    def test_user_not_created_if_user_with_username_exists(self):
        user_repository.create_new_user(
            User(username="Jaakko", password="salasana_hash"))

        try:
            user_repository.create_new_user(
                User(username="Jaakko", password="salasana_hash_2"))

        except:
            Exception("Käyttäjänimi Jaakko on jo käytössä")

        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Jaakko")
        self.assertEqual(users[0].password, "salasana_hash")

    def test_user_found_by_username(self):
        user_repository.create_new_user(
            User(username="Jaakko", password="salasana_hash"))
        user = user_repository.find_by_username("Jaakko")

        self.assertEqual(user.username, "Jaakko")
