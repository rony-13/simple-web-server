from aiohttp import web
import asyncio
import sys
import time

async def handle(request):
    time.sleep(1)
    print(dir(request))
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name + "\nWelcome to Simple-Web-app"
    return web.Response(text=text)

def start():
    try:
        loop = asyncio.get_event_loop()

        # App1
        app1 = web.Application()
        app1.add_routes([web.get('/', handle),web.get('/{name}', handle)])
        handler1 = app1.make_handler()
        coroutine1 = loop.create_server(handler1, '0.0.0.0', 8081)
        server1 = loop.run_until_complete(coroutine1)
        address1, port1 = server1.sockets[0].getsockname()
        print('App1 started on http://{}:{}'.format(address1, port1))

        # App2
        app2 = web.Application()
        app2.add_routes([web.get('/', handle),web.get('/{name}', handle)])
        handler2 = app2.make_handler()
        coroutine2 = loop.create_server(handler2, '0.0.0.0', 8082)
        server2 = loop.run_until_complete(coroutine2)
        address2, port2 = server2.sockets[0].getsockname()
        print('App2 started on http://{}:{}'.format(address2, port2))

        # App3
        app3 = web.Application()
        app3.add_routes([web.get('/', handle),web.get('/{name}', handle)])
        handler3 = app1.make_handler()
        coroutine3 = loop.create_server(handler3, '0.0.0.0', 8083)
        server3 = loop.run_until_complete(coroutine3)
        address3, port3 = server3.sockets[0].getsockname()
        print('App3 started on http://{}:{}'.format(address3, port3))

        try:
            running = loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server1.close()
            loop.run_until_complete(app1.shutdown())
            loop.run_until_complete(handler1.shutdown(60.0))
            loop.run_until_complete(handler1.finish_connections(1.0))
            loop.run_until_complete(app1.cleanup())

            server2.close()
            loop.run_until_complete(app2.shutdown())
            loop.run_until_complete(handler2.shutdown(60.0))
            loop.run_until_complete(handler2.finish_connections(1.0))
            loop.run_until_complete(app2.cleanup())

            server3.close()
            loop.run_until_complete(app3.shutdown())
            loop.run_until_complete(handler3.shutdown(60.0))
            loop.run_until_complete(handler3.finish_connections(1.0))
            loop.run_until_complete(app3.cleanup())

        loop.close()
    except Exception as e:
        sys.stderr.write('Error: ' + format(str(e)) + "\n")
        sys.exit(1)

if __name__ == '__main__':
    start()