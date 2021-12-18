import time
from aiohttp import web

async def handle(request):
    time.sleep(1)
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name + "\nWelcome to Simple-Web-app"
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)