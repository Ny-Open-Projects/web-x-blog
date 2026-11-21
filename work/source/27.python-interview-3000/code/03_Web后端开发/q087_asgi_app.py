async def app(scope, receive, send):
    if scope['type'] == 'http':
        await receive()  # 读取 request 事件,真实场景可分段读取 body
        await send({'type': 'http.response.start',
                    'status': 200,
                    'headers': [(b'content-type', b'text/plain')]})
        await send({'type': 'http.response.body', 'body': b'hello asgi'})

if __name__ == '__main__':
    try:
        import uvicorn
    except ImportError:
        print("该题演示需要第三方库 uvicorn:pip install uvicorn,原理见正文")
        raise SystemExit(0)
    uvicorn.run(app, host='127.0.0.1', port=8000)
