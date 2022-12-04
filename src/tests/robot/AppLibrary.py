import requests


class AppLibrary:
    def __init__(self):
        self._url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._url}/test/reset_all")

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirm": password
        }

        requests.post(f"{self._url}/register", data=data)
