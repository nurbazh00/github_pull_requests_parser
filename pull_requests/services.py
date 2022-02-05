import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup as bs


git_api = 'https://api.github.com/repos/'

data = []


def get_pull_count(url):
    r = requests.get(url)
    if r.status_code != 200:
        return 0

    soup = bs(r.text, 'lxml')
    count = int(soup.find('div', class_='pt-3 hide-full-screen mb-5').find('a',
                id='pull-requests-tab').find('span', class_='Counter').text)
    if count == 0:
        return 0

    elif count > 30:
        return count // 30

    else:
        return 1


async def get_data(session, url, page):

    split_url = url.split('/')
    user_project = split_url[3] + '/' + split_url[4] + f'/pulls?page={page}'

    async with session.get(url=git_api+user_project) as response:
        request_json = await response.json()
        if request_json != []:
            data.append(request_json)


async def create_tasks(url, count):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for page in range(1, count+1):
            task = asyncio.create_task(get_data(session, url, page))
            tasks.append(task)

        await asyncio.gather(*tasks)