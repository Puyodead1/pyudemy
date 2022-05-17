from pyudemy.structs.UdemyBase import UdemyBase


class UdemyChapter(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._sort_order = data.get("sort_order")
        self._title = data.get("title")
        self._is_published = data.get("is_published")
        self._object_index = data.get("object_index")

    @property
    def sort_order(self):
        return self._sort_order

    @property
    def title(self):
        return self._title

    @property
    def is_published(self):
        return self._is_published

    @property
    def object_index(self):
        return self._object_index