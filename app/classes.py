class Category:
    def __init__(self, data):
        self._data = data


class Song(Category):
    def __init__(self, data):
        super().__init__(data)
        self.__result = self._data["result"]

    def __str__(self):
        return f"{self.artists} - {self.title}"

    @property
    def artists(self):
        return self.__result["artist_names"]

    @property
    def title(self):
        return self.__result["title"]


class Lyric(Category):
    def __init__(self, data):
        super().__init__(data)
        self.__result = self._data["result"]
        self.__highlights = self._data["highlights"]

    def __str__(self):
        return f"{self.title} - |{self.highlights}|"

    @property
    def title(self):
        return self.__result["title"]

    @property
    def highlights(self):
        return self.__highlights[0]["value"]


class Artist(Category):
    def __init__(self, data):
        super().__init__(data)
        self.__result = self._data["result"]

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__result["name"]


class Other(Category):
    pass
