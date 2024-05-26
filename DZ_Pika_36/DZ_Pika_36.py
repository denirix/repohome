import aiohttp
import asyncio

async def fetch_repositories(user):
    url = f"https://api.github.com/users/{user}/repos"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                repositories = await response.json()
                return repositories
            else:
                print(f"Failed to fetch repositories for user {user}.")
                return []

async def main(users):
    tasks = [fetch_repositories(user) for user in users]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for user, repositories in zip(users, results):
        if repositories:
            print(f"Repositories for user '{user}':")
            for repo in repositories:
                print(repo["name"])
            print()
        else:
            print(f"No repositories found for user '{user}'.")
            print()

if __name__ == "__main__":
    users = ['Arantir1', 'EgorTimofeychik', 'maximax15', 'letov2110', 'denirix', 'Noowkies', 'NikDychek', 'marinamonit', 'PolonskyIllya', 'temabuchka88', 'LuydmilaKot', 'katherinepcholka', 'telenchenkosergey']
    asyncio.run(main(users))
