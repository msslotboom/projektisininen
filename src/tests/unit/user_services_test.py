import unittest
from unittest.mock import Mock, ANY
from services.user_services import UserService, UserInputError
from models.user import User




class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository_mock = Mock()
        self.user_service = UserService(self.user_repository_mock)

    def test_create_user_with_password_too_short(self):
        try:
            self.user_service.create_user("a", "salasana1", "salasana1")
        except:
            UserInputError("Käyttäjänimi ei sallittu")

        self.user_repository_mock.assert_not_called()

    def test_create_user_with_valid_creditentials(self):
        self.user_service.create_user("Jaakko", "salasana1", "salasana1")

        self.user_repository_mock.create_new_user.assert_called()




