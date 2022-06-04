from pyudemy.structs.UdemyAsset import UdemyAsset
from pyudemy.structs.UdemyBase import UdemyBase


class UdemyLecture(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._description = data.get("description")
        self._is_free = data.get("is_free")
        self._asset = UdemyAsset(data.get("asset"))
        self._last_watched_second = data.get("last_watched_second")
        self._download_url = data.get("download_url")
        self._sort_order = data.get("sort_order")
        self._object_index = data.get("object_index")
        self._supplementary_assets = []
        for asset in data.get("supplementary_assets", []):
            self._supplementary_assets.append(UdemyAsset(asset))

    @property
    def description(self):
        return self._description

    @property
    def is_free(self):
        return self._is_free

    @property
    def asset(self):
        return self._asset

    @property
    def last_watched_second(self):
        return self._last_watched_second

    @property
    def download_url(self):
        return self._download_url
