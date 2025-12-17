import requests

class ReqResClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, name, job):
        return requests.post(
            f"{self.base_url}/users",
            json={"name": name, "job": job}
        )
