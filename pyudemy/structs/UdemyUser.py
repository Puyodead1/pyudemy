from pyudemy.structs.UdemyBase import UdemyBase


class UdemyUser(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._title = data.get("title")
        self._name = data.get("name")
        self._display_name = data.get("display_name")
        self._job_title = data.get("job_title")
        self._image_50x50 = data.get("image_50x50")
        self._image_100x100 = data.get("image_100x100")
        self._initials = data.get("initials")
        self._url = data.get("url")

    @property
    def title(self):
        return self._title

    @property
    def name(self):
        return self._name

    @property
    def display_name(self):
        return self._display_name

    @property
    def job_title(self):
        return self._job_title

    @property
    def image_50x50(self):
        return self._image_50x50

    @property
    def image_100x100(self):
        return self._image_100x100

    @property
    def initials(self):
        return self._initials

    @property
    def url(self):
        return self._url