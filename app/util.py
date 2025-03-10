from typing import Type
from .classes import Category, Song, Lyric, Artist, Other


def str_to_category(category_str: str) -> Type[Category]:
    match category_str:
        case "song":
            return Song
        case "lyric":
            return Lyric
        case "artist":
            return Artist
        case _:
            return Other
