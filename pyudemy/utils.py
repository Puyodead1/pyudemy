import requests
from pyudemy.constants import COURSE_CURRICULUM_URL, COURSE_INFO_URL, COURSE_SEARCH_URL, SUBSCRIBED_COURSES_URL


def url_builder(url, kwargs):
    """
    Builds a url with the given parameters.
    """
    return url.format(**kwargs)


def get_subscribed_courses_url(portal_name="www", page=1, page_size=12, include_archived=False):
    """
    Returns the url for the subscribed courses endpoint.
    """
    return url_builder(
        SUBSCRIBED_COURSES_URL,
        {"page": page, "page_size": page_size,
            "include_archived": include_archived, "portal_name": portal_name}
    )


def get_course_search_url(query, portal_name="www", page=1, page_size=12, include_archived=False):
    """
    Returns the url for the course search endpoint.
    """
    return url_builder(
        COURSE_SEARCH_URL,
        {"search": query, "page": page, "page_size": page_size,
            "include_archived": include_archived, "portal_name": portal_name}
    )


def get_course_info_url(course_id, portal_name="www"):
    """
    Returns the url for the course info endpoint.
    """
    return url_builder(
        COURSE_INFO_URL,
        {"course_id": course_id, "portal_name": portal_name}
    )


def get_course_curriculum_url(course_id, portal_name="www", page=1, page_size=100):
    """
    Returns the url for the course curriculum endpoint.
    """
    return url_builder(
        COURSE_CURRICULUM_URL,
        {"course_id": course_id, "portal_name": portal_name,
            "page": page, "page_size": page_size}
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
            print(next_url)
            r = self._get(next_url, headers=self.headers)
            r.raise_for_status()
            data = r.json()
            next_url = data.get("next")
            res = data.get("results")
            if res:
                results.extend(res)
            else:
                return data

        return results
