---
title: [Q2900] HTTP 客户端的会话封装:超时、重试与代理直连
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2900 · HTTP 客户端的会话封装:超时、重试与代理直连

> 难度:★★★ | 标签:urllib, HTTP, 重试, 代理

**问**:团队里每个人都在裸写 urllib 请求,超时忘了设、代理忘了清,你会怎么收口?

**答**:封装一个 Session 对象,把容易忘的事全部收敛进去。构造时用 build_opener(ProxyHandler({})) 建一个空代理表的 opener——环境里有 http_proxy 时不清空,发往 127.0.0.1 的请求会被转手交给代理,这是本机调试最常见的翻车点;统一 timeout,不给裸 open 留任何入口;公共请求头一处维护。重试逻辑放在会话层且按状态码分类:5xx 和 URLError/OSError 这类网络层错误值得重试,4xx 是调用方的错,重试只会把事故放大。实测服务端前两次返回 503,会话层第 3 次拿到 200;对 /notfound 则直接抛 HTTPError,一次请求都不浪费。

- 超时必须显式:urllib 默认不超时,一个慢端点就能挂死一个线程;

- 重试次数用尽要把最后一次异常原样上抛,调用方需要真实的失败原因;

- 会话封装的最大价值是"默认值安全":想犯错的成本比做对更高。

```python
# file: code/02_并发与网络工程/q2900_http_session.py
# -*- coding: utf-8 -*-
"""HTTP 客户端的会话封装: 超时 + 重试 + 代理直连。

- build_opener(ProxyHandler({})): 显式空代理表, 绕过环境 http_proxy 直连;
- Session 对象: 统一 base URL、公共头、超时与重试, 调用方只关心业务;
- 状态码分类: 5xx 与网络错误才重试, 4xx 是调用方的错, 重试无意义。
"""
import json
import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 环境里有 http_proxy 时, 必须显式清空代理才不会把请求发给代理
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class Session:
    """极简 HTTP 会话: 公共配置收敛在一处。"""

    def __init__(self, base, timeout=2.0, retries=3, backoff=0.05):
        self.base = base.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.backoff = backoff
        self.headers = {"User-Agent": "py-session/1.0"}

    def get_json(self, path):
        url = self.base + path
        last = None
        for attempt in range(1, self.retries + 1):
            req = urllib.request.Request(url, headers=self.headers)
            try:
                with OPENER.open(req, timeout=self.timeout) as resp:
                    return resp.status, json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                if exc.code < 500 or attempt == self.retries:
                    raise               # 4xx 不重试; 次数用尽向上抛
                last = exc
            except (urllib.error.URLError, OSError) as exc:
                last = exc              # 网络层错误: 值得重试
            time.sleep(self.backoff * (2 ** (attempt - 1)))
        raise last


class Handler(BaseHTTPRequestHandler):
    hits = {}
    lock = threading.Lock()

    def do_GET(self):
        with Handler.lock:
            Handler.hits[self.path] = Handler.hits.get(self.path, 0) + 1
            n = Handler.hits[self.path]
        if self.path == "/flaky" and n < 3:     # 前两次故意 503
            self.send_response(503)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        body = json.dumps({"path": self.path, "hit": n}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def wait_port(port, timeout=5.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    srv.daemon_threads = True
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    assert wait_port(port)

    sess = Session("http://127.0.0.1:%d" % port)

    status, data = sess.get_json("/ok")
    print("正常请求:", status, data)

    status, data = sess.get_json("/flaky")   # 503 两次后第 3 次成功
    print("重试后成功:", status, data, "(服务端第 %d 次才给 200)" % data["hit"])
    assert data["hit"] == 3

    try:
        sess.get_json("/notfound")           # 404: 不重试, 直接抛
    except urllib.error.HTTPError as exc:
        print("4xx 不重试直接抛出: HTTP %d" % exc.code)

    srv.shutdown()
    print("要点: 会话封装收敛超时/重试/代理, 4xx 与 5xx 的重试语义分家")
```

**追问**:1) 为什么要 ProxyHandler({}) 而不是删掉环境变量?——改环境变量影响全进程且侵入性强,空代理表只影响这一个 opener,粒度刚好。2) 重试要不要带 jitter?——单客户端影响不大,但批量客户端同节拍重试会形成风暴,工程上加 jitter 更稳。3) 底层机制:urllib 的默认超时与代理从哪来?——urlopen 不传 timeout 就落到 socket 全局默认(实际等于无限阻塞);getproxies 从 http_proxy/https_proxy 环境变量读出并默认装入 opener,本机调试与容器环境最容易在这里翻车。4) 生产陷阱?——HTTPError 是 URLError 的子类,except 顺序颠倒会把 4xx 也当网络错误重试;给 POST 这类非幂等请求配自动重试,造成重复提交;重试用尽抛 last 之前不留每次尝试的轨迹,排障无从下手。

---
