from typing import Final, Type
from .classes import Category, Song, Lyric, Artist

API_URL: Final[str] = "https://genius.com/api"
SEARCH_URL: Final[str] = API_URL + "/search"
MULTI_SEARCH_URL: Final[str] = SEARCH_URL + "/multi?q="

SINGLE_SEARCH_URLS_MAP: Final[dict[Type[Category], str]] = {
    Song: SEARCH_URL + "/song?q=",
    Lyric: SEARCH_URL + "/lyric?q=",
    Artist: SEARCH_URL + "/artist?q=",
}
