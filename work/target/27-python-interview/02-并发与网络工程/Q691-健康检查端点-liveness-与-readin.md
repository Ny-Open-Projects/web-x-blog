---
title: [Q691] 健康检查端点:liveness 与 readiness
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q691 · 健康检查端点:liveness 与 readiness

> 难度:★★☆ | 标签:健康检查, K8s, 探针

**问**:/healthz 一个接口为什么 K8s 要拆成 liveness 和 readiness 两个?

**答**:语义不同:liveness 问"进程活着吗",失败触发重启容器——所以它绝不能检查外部依赖(数据库抖一下就重启自己是雪崩放大器);readiness 问"现在能接流量吗",失败只是摘除流量(从 Service endpoint 移除),依赖恢复后自动回来。readiness 检查的是"接请求的前提":依赖连通、连接池可用、预热完成、正在排水(优雅关闭时置 not-ready,先摘流再关进程,配合 Q602)。两个端点都要轻(不查重依赖、毫秒级返回),并带版本/uptime 便于巡检。

```python
# file: code/02_并发与网络工程/q691_healthz.py
import json
import socket
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 本机回环演示: 显式直连, 避免环境里的 http_proxy 把 urlopen 劫持到代理端口
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))

START = time.monotonic()
state = {"db_ok": True, "draining": False}


def wait_port(port: int, timeout: float = 3.0) -> None:
    """等服务端端口可建立 TCP 连接再发请求, 消除服务启动竞态。"""
    deadline = time.monotonic() + timeout
    while True:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            if time.monotonic() >= deadline:
                raise
            time.sleep(0.05)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _respond(self, code: int, obj: dict) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/livez":
            # liveness: 只回答进程自身活着, 绝不碰外部依赖
            self._respond(200, {"status": "alive",
                                "uptime": round(time.monotonic() - START, 1)})
        elif self.path == "/readyz":
            if state["draining"]:
                self._respond(503, {"status": "draining", "ready": False})
            elif not state["db_ok"]:
                self._respond(503, {"status": "dependency-down", "ready": False})
            else:
                self._respond(200, {"status": "ready", "checks": {"db": "ok"}})
        else:
            self._respond(404, {"error": "not found"})

    def log_message(self, fmt: str, *args) -> None:
        pass


def server(stop: threading.Event, port_box: list) -> None:
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port_box.append(srv.server_address[1])
    srv.timeout = 0.2
    while not stop.is_set():
        srv.handle_request()
    srv.server_close()


def probe(base: str, path: str) -> None:
    try:
        r = urllib.request.urlopen(base + path, timeout=2)
        print(f"  {path}: {r.status} {r.read().decode()}")
    except urllib.error.HTTPError as e:
        print(f"  {path}: {e.code} {e.read().decode()}")


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=server, args=(stop, box), daemon=True).start()
    while not box:
        time.sleep(0.01)
    wait_port(box[0])
    base = f"http://127.0.0.1:{box[0]}"

    print("正常状态:")
    probe(base, "/livez")
    probe(base, "/readyz")

    print("依赖故障 (db_ok=False) → liveness 仍 200, readiness 503:")
    state["db_ok"] = False
    probe(base, "/livez")
    probe(base, "/readyz")

    print("优雅排水 (draining=True) → readiness 503 摘流, 进程不重启:")
    state["db_ok"] = True
    state["draining"] = True
    probe(base, "/livez")
    probe(base, "/readyz")
    stop.set()
```

**追问**:1) readiness 探测间隔和超时怎么定?——间隔取"故障发现可接受时间"与"探测开销"的折中(常见 5-10s),超时要远小于间隔(1-2s),连续失败阈值 2-3 次防抖动摘流。2) liveness 为什么绝不能检查外部依赖?——DB 抖动→liveness 失败→容器重启→重启加剧 DB 压力→全局雪崩;重启动作只适用于进程内部故障(死锁、事件循环饿死),外部依赖归 readiness(摘流即可恢复)。3) 优雅关闭怎么与 readiness 配合?——收 SIGTERM 先置 not-ready 让摘流生效→排水存量连接(Q692)→退出;摘流生效要等探针间隔的时长,terminationGracePeriod 必须覆盖「摘流+排水」全程。4) 生产陷阱?——两个探针共用一套重检查,依赖抖动直接触发重启;readiness 里做重查询,探测本身压垮服务;启动慢的服务没配 startupProbe,启动期被 liveness 反复重启(CrashLoop)。

---
