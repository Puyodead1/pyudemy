from pyudemy.structs.UdemyBase import UdemyBase
from pyudemy.structs.UdemyChapter import UdemyChapter
from pyudemy.structs.UdemyUser import UdemyUser


class UdemyCourse(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._title = data.get("title")
        self._url = data.get("url")
        self._is_paid = data.get("is_paid")
        self._price = data.get("price")
        self._price_detail = data.get("price_detail")
        self._price_serve_tracking_id = data.get("price_serve_tracking_id")
        self._visible_instructors = []
        for instructor in data.get("visible_instructors", []):
            self._visible_instructors.append(UdemyUser(instructor))

        self._image_125_h = data.get("image_125_H")
        self._image_240x135 = data.get("image_240x135")
        self._is_practice_test_course = data.get("is_practice_test_course")
        self._image_480x270 = data.get("image_480x270")
        self._published_title = data.get("published_title")
        self._tracking_id = data.get("tracking_id")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def is_paid(self):
        return self._is_paid

    @is_paid.setter
    def is_paid(self, value):
        self._is_paid = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def price_detail(self):
        return self._price_detail

    @price_detail.setter
    def price_detail(self, value):
        self._price_detail = value

    @property
    def price_serve_tracking_id(self):
        return self._price_serve_tracking_id

    @price_serve_tracking_id.setter
    def price_serve_tracking_id(self, value):
        self._price_serve_tracking_id = value

    @property
    def visible_instructors(self):
        return self._visible_instructors

    @visible_instructors.setter
    def visible_instructors(self, value):
        self._visible_instructors = value

    @property
    def image_125_h(self):
        return self._image_125_h

    @image_125_h.setter
    def image_125_h(self, value):
        self._image_125_h = value

    @property
    def image_240x135(self):
        return self._image_240x135

    @image_240x135.setter
    def image_240x135(self, value):
        self._image_240x135 = value

    @property
    def is_practice_test_course(self):
        return self._is_practice_test_course

    @is_practice_test_course.setter
    def is_practice_test_course(self, value):
        self._is_practice_test_course = value

    @property
    def image_480x270(self):
        return self._image_480x270

    @image_480x270.setter
    def image_480x270(self, value):
        self._image_480x270 = value

    @property
    def published_title(self):
        return self._published_title

    @published_title.setter
    def published_title(self, value):
        self._published_title = value

    @property
    def tracking_id(self):
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, value):
        self._tracking_id = value

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
