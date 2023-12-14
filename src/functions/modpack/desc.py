import aiohttp
import json

async def modpack_desc(modpackId: str):
    url = f"https://www.modpackindex.com/api/v1/modpack/{modpackId}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                response = json.loads(await response.text())

                # Title
                title = response['data']['name']

                # Thumbnail
                thumbnail = response['data']['thumbnail_url']

                # Description
                desc = response['data']['summary']

                # Authors
                authors = ""
                for author in response['data']['authors']:
                    authors += f"- {author['name']}\n"

                # Versions
                versions = ""
                for version in response['data']['minecraft_versions']:
                    versions += f"- {version['name']}\n"
                
                # Categories
                categories = ""
                for category in response['data']['categories']:
                    categories += f"- {category['name']}\n"

                # URL
                url = response['data']['url']

                # Last Update
                last_update = response['data']['last_modified']

    return title, url, thumbnail, desc, authors, versions, categories, last_update