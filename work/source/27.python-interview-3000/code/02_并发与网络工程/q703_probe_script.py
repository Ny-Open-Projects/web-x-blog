import json
import socket
import sys
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

EXIT_OK, EXIT_UNHEALTHY, EXIT_USAGE = 0, 1, 2
TOTAL_BUDGET = 5.0
# 探活必须直连目标: 环境/系统代理会把对 localhost 的检查劫持到代理端口
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class Target:
    def __init__(self, host: str, port: int, path: str = "/healthz") -> None:
        self.host, self.port, self.path = host, port, path


def check_tcp(t: Target, deadline: float) -> dict:
    if time.monotonic() > deadline:
        return {"check": "tcp", "ok": False, "detail": "总预算耗尽"}
    try:
        s = socket.create_connection((t.host, t.port), timeout=1)
        s.close()
        return {"check": "tcp", "ok": True, "detail": "connect ok"}
    except OSError as e:
        return {"check": "tcp", "ok": False, "detail": repr(e)}


def check_http(t: Target, deadline: float) -> dict:
    if time.monotonic() > deadline:
        return {"check": "http", "ok": False, "detail": "总预算耗尽"}
    try:
        r = OPENER.open(f"http://{t.host}:{t.port}{t.path}", timeout=2)
        ok = r.status == 200
        return {"check": "http", "ok": ok, "detail": f"status {r.status}"}
    except urllib.error.HTTPError as e:
        return {"check": "http", "ok": False, "detail": f"status {e.code}"}
    except Exception as e:  # noqa: BLE001
        return {"check": "http", "ok": False, "detail": repr(e)}


def probe(t: Target) -> tuple:
    deadline = time.monotonic() + TOTAL_BUDGET
    results = [check_tcp(t, deadline), check_http(t, deadline)]
    healthy = all(r["ok"] for r in results)
    return healthy, results


class HealthHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:
        body = b'{"status":"ok"}'
        code = 200 if self.path == "/healthz" else 404
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:
        pass


def main(argv: list) -> int:
    if len(argv) < 3:
        print("usage: probe.py <host> <port>")
        return EXIT_USAGE
    try:
        t = Target(argv[1], int(argv[2]))
    except ValueError:
        return EXIT_USAGE
    healthy, results = probe(t)
    print(json.dumps({"healthy": healthy, "checks": results}, ensure_ascii=False))
    print("human:", "HEALTHY" if healthy else "UNHEALTHY",
          "|", "; ".join(f"{r['check']}={'ok' if r['ok'] else r['detail']}"
                          for r in results))
    return EXIT_OK if healthy else EXIT_UNHEALTHY


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), HealthHandler)
    threading.Thread(target=srv.serve_forever, kwargs={"poll_interval": 0.2},
                     daemon=True).start()
    time.sleep(0.1)
    code = main(["probe.py", "127.0.0.1", str(srv.server_address[1])])
    print("退出码:", code, "(0=健康, 1=不健康, 2=用法错误)")
    sys.exit(code)
