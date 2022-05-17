class UdemyPaginatedAPIResponse:
    def __init__(self, data) -> None:
        self._count = data.get("count")
        self._next = data.get("next")
        self._previous = data.get("previous")
        self._results = data.get("results")

    @property
    def count(self) -> int:
        return self._count

    @property
    def next(self) -> str:
        return self._next

    @property
    def previous(self) -> str:
        return self._previous

    @property
    def results(self) -> list:
        return self._results

    def __repr__(self):
        return f"UdemyPaginatedAPIResponse(count={self.count}, next={self.next}, previous={self.previous}, results={self.results})"