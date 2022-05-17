import requests
from pyudemy.constants import SUBSCRIBED_COURSES_URL


def url_builder(url, kwargs):
    """
    Builds a url with the given parameters.
    """
    return url.format(**kwargs)

def get_subscribed_courses_url(page = 1, page_size = 12, include_archived = False):
    """
    Returns the url for the subscribed courses endpoint.
    """
    return url_builder(
        SUBSCRIBED_COURSES_URL,
        {"page": page, "page_size": page_size, "include_archived": include_archived}
    )

class RequestManager:
    def __init__(self, headers=None) -> None:
        self.headers = headers

    def _get(self, url, **kwargs):
        """
        Returns the response from the API.
        """
        return requests.get(url, **kwargs)

    def get(self, url):
        results = []

        next_url = url
        while next_url:
            r = self._get(next_url, headers=self.headers)
            r.raise_for_status()
            data = r.json()
            next_url = data.get("next")
            res = data.get("results")
            print(len(res))
            results.extend(res)

        return results