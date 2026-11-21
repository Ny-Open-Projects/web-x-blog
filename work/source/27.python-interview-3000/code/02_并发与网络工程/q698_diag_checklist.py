import json
import socket
import ssl
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def check_dns(host: str) -> dict:
    try:
        infos = socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
        return {"layer": "DNS", "ok": True,
                "detail": f"解析到 {[i[4][0] for i in infos][:3]}"}
    except socket.gaierror as e:
        return {"layer": "DNS", "ok": False, "detail": f"{e} → 检查域名/本地DNS"}


def check_tcp(host: str, port: int, timeout: float = 1.0) -> dict:
    t0 = time.monotonic()
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return {"layer": "TCP", "ok": True,
                "detail": f"建连 {(time.monotonic() - t0) * 1000:.0f}ms"}
    except ConnectionRefusedError:
        return {"layer": "TCP", "ok": False, "detail": "refused → 服务未监听/崩溃"}
    except socket.timeout:
        return {"layer": "TCP", "ok": False, "detail": "timeout → 网络/防火墙/过载"}
    except OSError as e:
        return {"layer": "TCP", "ok": False, "detail": f"{e!r}"}


def check_http(host: str, port: int, tls: bool = False) -> dict:
    scheme = "https" if tls else "http"
    url = f"{scheme}://{host}:{port}/healthz"
    try:
        ctx = ssl._create_unverified_context() if tls else None
        r = urllib.request.urlopen(url, timeout=2, context=ctx)
        return {"layer": "HTTP", "ok": r.status == 200,
                "detail": f"{r.status} {r.read()[:40]}"}
    except urllib.error.HTTPError as e:
        return {"layer": "HTTP", "ok": False, "detail": f"{e.code} → 应用层异常"}
    except Exception as e:  # noqa: BLE001
        return {"layer": "HTTP", "ok": False, "detail": f"{e!r}"}


def diagnose(host: str, port: int) -> dict:
    report = [check_dns(host)]
    if report[-1]["ok"]:
        report.append(check_tcp(host, port))
        if report[-1]["ok"]:
            report.append(check_http(host, port))
    failed = next((r for r in report if not r["ok"]), None)
    verdict = "全部通过" if failed is None else f"故障层: {failed['layer']}"
    return {"target": f"{host}:{port}", "checks": report, "verdict": verdict}


class OKHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:
        body = b'{"status":"ok"}'
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:
        pass


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 0), OKHandler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, kwargs={"poll_interval": 0.2},
                     daemon=True).start()
    time.sleep(0.1)

    for target in (("127.0.0.1", port), ("127.0.0.1", 1), ("no-such.invalid", 443)):
        result = diagnose(*target)
        print(f"=== 诊断 {result['target']} ===")
        for c in result["checks"]:
            print(f"  [{'PASS' if c['ok'] else 'FAIL'}] {c['layer']}: {c['detail']}")
        print("  结论:", result["verdict"], "\n")
    srv.shutdown()
