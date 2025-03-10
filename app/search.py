from typing import Type
from aiohttp import ClientSession
from .util import str_to_category
from .parse import get_objects
from .api import MULTI_SEARCH_URL, SINGLE_SEARCH_URLS_MAP
from .classes import Category, Song, Lyric, Artist, Other


async def search_all(client: ClientSession, query: str) -> list:
    async with client.get(MULTI_SEARCH_URL + query) as response:
        json = await response.json()
        sections = json["response"]["sections"]
        for section in sections:
            category = str_to_category(section["type"])
            if category is Other:
                continue
            data = section["hits"]
            return get_objects(data, category)


async def search_songs(client: ClientSession, query: str) -> list:
    return await search_single(client, Song, query)


async def search_lyrics(client: ClientSession, query: str) -> list:
    return await search_single(client, Lyric, query)


async def search_artists(client: ClientSession, query: str) -> list:
    return await search_single(client, Artist, query)


async def search_single(client: ClientSession,
                        category: Type[Category], query: str) -> list:
    url = SINGLE_SEARCH_URLS_MAP[category]
    async with client.get(url + query) as response:
        json = await response.json()
        data = json["response"]["sections"][0]["hits"]
        result = get_objects(data, category)
        return result
