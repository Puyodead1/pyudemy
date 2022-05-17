from pyudemy.constants import HEADERS
from pyudemy.structs.UdemyCourse import UdemyCourse
from pyudemy.utils import RequestManager, get_subscribed_courses_url


class PyUdemy:
    def __init__(self, access_token) -> None:
        self.access_token = access_token
        self.headers = HEADERS
        self.headers["X-Udemy-Authorization"] = f"Bearer {self.access_token}"
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        
        self.request_manager = RequestManager(headers=self.headers)

    def get_subscribed_courses(self) -> list:
        url = get_subscribed_courses_url(1, 12, False)
        res = self.request_manager.get(url)
        a = []
        for result in res:
            a.append(UdemyCourse(result))
        return a