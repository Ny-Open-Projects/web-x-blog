# -*- coding: utf-8 -*-
"""urllib opener 链定制: 代理豁免与重定向闸门都长在 Handler 上。

- build_opener 把一串 Handler 拧成链条, 每种 HTTP 事件找对应的 Handler 处理;
- ProxyHandler({}) 顶掉环境里的 http_proxy, 内网联调必备;
- 自定义 HTTPRedirectHandler 可以限跳数、禁跨站, 把跟随重定向的权力收回来。
"""
import http.server
import socketserver
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

CALLS = []


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        CALLS.append(self.path)
        routes = {
            "/target": (200, "final-page"),
            "/redirect": (302, "/target"),
            "/chain": (302, "/redirect"),
            "/loop": (302, "/loop"),
        }
        code, target = routes[self.path]
        if code == 302:
            self.send_response(302)
            self.send_header("Location", target)
            self.send_header("Content-Length", "0")
            self.end_headers()
        else:
            body = target.encode()
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, *args):
        pass


class CountingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True


class TooManyRedirects(Exception):
    pass


class LimitedRedirectHandler(urllib.request.HTTPRedirectHandler):
    """限两跳、禁跨站的重定向处理器。"""

    max_redirects = 2

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        count = getattr(req, "hop_count", 0) + 1
        if count > self.max_redirects:
            raise TooManyRedirects("超过 %d 跳: %s" % (self.max_redirects, newurl))
        here = urllib.parse.urlsplit(req.full_url)
        dest = urllib.parse.urlsplit(newurl)
        if (here.scheme, here.netloc) != (dest.scheme, dest.netloc):
            raise TooManyRedirects("拒绝跨站重定向: %s://%s -> %s://%s" %
                                   (here.scheme, here.netloc,
                                    dest.scheme, dest.netloc))
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        newreq.hop_count = count                 # 计数随新请求继续旅行
        return newreq


def build_opener():
    return urllib.request.build_opener(
        urllib.request.ProxyHandler({}),         # 豁免环境代理, 直连回环
        LimitedRedirectHandler())


def main():
    srv = CountingServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    base = "http://127.0.0.1:%d" % port
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.1)
    opener = build_opener()

    r = opener.open(base + "/target", timeout=3)
    print("直达:", r.status, r.read().decode())

    r = opener.open(base + "/redirect", timeout=3)
    print("一跳重定向:", r.status, r.read().decode())

    r = opener.open(base + "/chain", timeout=3)
    print("两跳重定向:", r.status, r.read().decode())
    assert r.url == base + "/target"

    try:
        opener.open(base + "/loop", timeout=3)
        raise AssertionError("自环重定向必须被闸门拦下")
    except TooManyRedirects as e:
        print("闸门拦截:", e)

    print("服务端共收到:", CALLS)
    assert CALLS.count("/loop") == 3, "两跳闸门让自环在第三次被斩断"
    srv.shutdown()


if __name__ == "__main__":
    main()
