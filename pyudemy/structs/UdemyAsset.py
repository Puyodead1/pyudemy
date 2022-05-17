from pyudemy.structs.UdemyBase import UdemyBase
from pyudemy.structs.UdemyCaption import UdemyCaption
from pyudemy.structs.UdemyMediaSource import UdemyMediaSource


class UdemyAsset(UdemyBase):
    def __init__(self, data):
        super().__init__(data)
        self._asset_type = data.get("asset_type")
        self._length = data.get("length")
        self._captions = []
        for caption in data.get("captions"):
            self._captions.append(UdemyCaption(caption))
        self._external_url = data.get("external_url")
        self._media_license_token = data.get("media_license_token")
        self._media_sources = []
        for media_source in data.get("media_sources"):
            self._media_sources.append(UdemyMediaSource(media_source))
        self._course_is_drmed = data.get("course_is_drmed")
        self._download_urls = data.get("download_urls") # unknown type
        self._slide_urls = data.get("slide_urls") # unknown type
        self._slides = data.get("slides") # unknown type
        self._thumbnail_sprite = data.get("thumbnail_sprite")
        self._title = data.get("title")
        self._status = data.get("status")
        self._filename = data.get("filename")
        self._time_estimation = data.get("time_estimation")
    
    @property
    def asset_type(self):
        return self._asset_type

    @property
    def length(self):
        return self._length

    @property
    def external_url(self):
        return self._external_url

    @property
    def media_license_token(self):
        return self._media_license_token

    @property
    def media_sources(self):
        return self._media_sources

    @property
    def course_is_drmed(self):
        return self._course_is_drmed

    @property
    def download_urls(self):
        return self._download_urls

    @property
    def slide_urls(self):
        return self._slide_urls

    @property
    def slides(self):
        return self._slides

    @property
    def thumbnail_sprite(self):
        return self._thumbnail_sprite

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @property
    def filename(self):
        return self._filename

    @property
    def time_estimation(self):
        return self._time_estimation

    @property
    def captions(self):
        return self._captions

    @property
    def course_is_drmed(self):
        return self._course_is_drmed