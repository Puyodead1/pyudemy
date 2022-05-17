class UdemyMediaSource:
    def __init__(self, data) -> None:
        self._type = data.get("type")
        self._src = data.get("src")
        self._label = data.get("label")

    @property
    def type(self) -> str:
        return self._type

    @property
    def src(self) -> str:
        return self._src

    @property
    def label(self) -> str:
        return self._label