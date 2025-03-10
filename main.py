import argparse
import asyncio
from aiohttp import ClientSession
from app.search import search_all, search_songs, search_lyrics, search_artists


SCRIPT_NAME = "genius_cli"

SEARCH_FUNCTION_MAP = {
    "everything": search_all,
    "songs": search_songs,
    "lyrics": search_lyrics,
    "artists": search_artists,
}


async def main(args) -> None:
    async with ClientSession() as client:
        objects = await SEARCH_FUNCTION_MAP[args.mode](client, args.query)
        for obj in objects:
            print(obj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"{SCRIPT_NAME} - access genius in cli")
    parser.add_argument("-m", "--mode",
                        choices=["everything", "songs", "lyrics", "artists"],
                        default="everything",
                        help="search mode")
    parser.add_argument("query", help="search query")

    args = parser.parse_args()

    asyncio.run(main(args))
