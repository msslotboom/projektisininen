import unittest
from unittest.mock import Mock
from services.user_services import UserService, UserInputError


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = Mock()
        self.user_service = UserService(self.user_repository)

    def test_validate_user_with_username_too_short(self):
        try:
            self.user_service.create_user("a", "salasana1", "salasana1")
        except:
            UserInputError("Käyttäjänimi on liian lyhyt")

        self.user_repository.create_new_user.assert_not_called()

    def test_create_user_with_valid_creditentials(self):
        self.user_service.create_user("Jaakko", "salasana1", "salasana1")

        self.user_repository.create_new_user.assert_called()

    def test_validate_login_with_nonexistent_username(self):
        user_repository = Mock()
        user_service = UserService(user_repository)
        user_repository.find_by_username = Mock(return_value=None)

        try:
            user_service.validate_login_credentials("Jaakko", "salasana1")
        except:
            Exception()

        self.assertRaises(Exception)
    
    def test_validate_login_with_no_password(self):
        try:
            self.user_service.validate_login_credentials("Jaakko", None)
        except:
            Exception()

        self.assertRaises(Exception)
        self.user_repository.find_by_username.assert_not_called()

