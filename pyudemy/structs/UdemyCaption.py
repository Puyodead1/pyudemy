from pyudemy.structs.UdemyBase import UdemyBase


class UdemyCaption(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._title = data.get("title")
        self._created = data.get("created")
        self._file_name = data.get("file_name")
        self._status = data.get("status")
        self._url = data.get("url")
        self._source = data.get("source")
        self._locale_id = data.get("locale_id")
        self._video_label = data.get("video_label")
        self._asset_id = data.get("asset_id")

    @property
    def title(self):
        return self._title

    @property
    def created(self):
        return self._created

    @property
    def file_name(self):
        return self._file_name

    @property
    def status(self):
        return self._status

    @property
    def url(self):
        return self._url

    @property
    def source(self):
        return self._source

    @property
    def locale_id(self):
        return self._locale_id

    @property
    def video_label(self):
        return self._video_label

    @property
    def asset_id(self):
        return self._asset_id