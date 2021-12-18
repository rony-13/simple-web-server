import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080/') as response:
            html = await response.text()
            print("Greetings Body:")
            print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())