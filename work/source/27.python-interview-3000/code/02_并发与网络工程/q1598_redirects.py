"""重定向的正确处理: 语义差异与循环防护。

- 301/302/303: 历史包袱下客户端把非 GET 改写成 GET、丢掉 body;
- 307/308: 原方法原 body 原样重放, 才不会把 POST 静默降级成 GET;
- 循环防护: 记录访问轨迹, 重复到达立即停; 跨主机跳转应剥离
  Authorization 等敏感头。
"""
import http.client
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

REDIRECTS = {
    "/r301": (301, "/echo"),
    "/post301": (301, "/echo"),
    "/post307": (307, "/echo"),
    "/loop1": (302, "/loop2"),
    "/loop2": (302, "/loop1"),
}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _respond(self, code, body=b"", headers=()):
        self.send_response(code)
        for k, v in headers:
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def _route(self):
        path = self.path.split("?")[0]
        if path in REDIRECTS:
            cl = self.headers.get("Content-Length")
            if cl:
                self.rfile.read(int(cl))    # 读掉请求体, 保住连接复用
            code, loc = REDIRECTS[path]
            self._respond(code, headers=[("Location", loc)])
        elif path == "/echo":
            self._respond(200, ("method=%s" % self.command).encode())
        else:
            self._respond(404, b"not found")

    do_GET = _route
    do_POST = _route

    def log_message(self, *args):
        pass


def follow(port, method, path, body=None, max_hops=6):
    """带循环防护与方法语义的重定向跟随器。"""
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2)
    visited = []
    current_method, current_body = method, body
    result = None
    for hop in range(max_hops):
        if path in visited:
            result = ("LOOP", path, hop)
            break
        visited.append(path)
        conn.request(current_method, path, body=current_body)
        resp = conn.getresponse()
        payload = resp.read()
        if resp.status in (301, 302, 303, 307, 308):
            loc = resp.getheader("Location")
            # 跨主机跳转时应剥离 Authorization(同机演示从略)
            if resp.status in (301, 302, 303) and current_method != "GET":
                current_method = "GET"
                current_body = None         # 方法降级: body 一并丢弃
            path = loc
            continue
        result = (resp.status, payload.decode(), hop)
        break
    conn.close()
    return result, visited


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    r, v = follow(port, "GET", "/r301")
    print("GET /r301 ->", r, "轨迹:", v)
    assert r[0] == 200 and r[1] == "method=GET"

    r, v = follow(port, "POST", "/post301", body=b"data")
    print("POST /post301 ->", r, "(301 把 POST 降级成 GET)")
    assert r[1] == "method=GET"

    r, v = follow(port, "POST", "/post307", body=b"data")
    print("POST /post307 ->", r, "(307 保住原方法)")
    assert r[1] == "method=POST"

    r, v = follow(port, "GET", "/loop1")
    print("GET /loop1 ->", r, "轨迹:", v)
    assert r[0] == "LOOP", "循环必须被访问轨迹发现"

    # 对照: urllib 自带重定向处理(注意绕过代理环境变量)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    resp = opener.open("http://127.0.0.1:%d/r301" % port, timeout=2)
    print("urllib 自动跟随, 最终 URL:", resp.geturl())
    assert resp.geturl().endswith("/echo")
    resp.close()

    srv.shutdown()
    srv.server_close()
    print("结论: 307/308 保语义, 301/302 会降级; 循环靠轨迹, 跨域靠剥头")


if __name__ == "__main__":
    main()
