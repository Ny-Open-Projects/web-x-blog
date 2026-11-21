def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    path = environ.get('PATH_INFO', '/')
    body = f'hello, path={path}'.encode('utf-8')
    return [body]

if __name__ == '__main__':
    import threading
    import urllib.request
    from wsgiref.simple_server import make_server

    server = make_server('127.0.0.1', 0, application)   # 端口 0:随机空闲端口,防冲突
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        # 本机若设了 http_proxy,urllib 会把回环请求交给代理,必须用空 ProxyHandler 直连
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f'http://127.0.0.1:{port}/books/42', timeout=5) as resp:
            print(resp.status, resp.read().decode('utf-8'))
    finally:
        server.shutdown()       # 收尾:退出 serve_forever 循环,进程正常结束
        thread.join(timeout=5)
