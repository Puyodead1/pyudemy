from pyudemy.constants import HEADERS
from pyudemy.structs.UdemyCourse import UdemyCourse
from pyudemy.structs.UdemyLecture import UdemyLecture
from pyudemy.structs.UdemyChapter import UdemyChapter
from pyudemy.utils import RequestManager, get_course_curriculum_url, get_course_info_url, get_course_search_url, get_subscribed_courses_url


class PyUdemy:
    def __init__(self, access_token, portal_name="www") -> None:
        self.access_token = access_token
        self.portal_name = portal_name
        self.headers = HEADERS
        self.headers["X-Udemy-Authorization"] = "Bearer {}".format(
            self.access_token)
        self.headers["Authorization"] = "Bearer {}".format(self.access_token)

        self.request_manager = RequestManager(headers=self.headers)

    def get_subscribed_courses(self, page=1, page_size=12, include_archived=False) -> list[UdemyCourse]:
        url = get_subscribed_courses_url(
            self.portal_name, page, page_size, include_archived)
        res = self.request_manager.get(url)
        a = []
        for result in res:
            a.append(UdemyCourse(result))
        return a

    def search_course(self, query, page=1, page_size=12, include_archived=False) -> list[UdemyCourse]:
        url = get_course_search_url(
            query, self.portal_name, page, page_size, include_archived)
        res = self.request_manager.get(url)
        a = []
        for result in res:
            a.append(UdemyCourse(result))
        return a

    def get_course_info(self, course_id) -> UdemyCourse:
        url = get_course_info_url(course_id, self.portal_name)
        res = self.request_manager.get(url)
        return UdemyCourse(res)

    def get_course_curriculum(self, course_id, page=1, page_size=100) -> list[UdemyChapter]:
        """
        Get course curriculum. keep page size at a decently large size, low sizes will take longer to get, but too large can cause errors
        """
        url = get_course_curriculum_url(
            course_id, self.portal_name, page, page_size)
        res = self.request_manager.get(url)
        print(type(res))
        a = []
        current_chapter: UdemyChapter = None
        for result in res:
            _class = result.get("_class")
            print("_class: {}".format(_class))
            if _class == "chapter":
                if current_chapter:
                    print("[+] chapter end")
                    a.append(current_chapter)
                print("[+] chapter start")
                current_chapter = UdemyChapter(result)
            elif _class == "lecture":
                if not current_chapter:
                    raise Exception("Lecture found before chapter")
                print("[+] lecture")
                current_chapter.add_lecture(UdemyLecture(result))
        return a
