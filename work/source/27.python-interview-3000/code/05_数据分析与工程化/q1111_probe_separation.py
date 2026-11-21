import http.server
import threading
import time
import urllib.request

STATE = {"alive": True, "ready": False}

class ProbeHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":          # liveness:失败 -> 重启进程
            code, body = (200, "ok") if STATE["alive"] else (500, "dead")
        elif self.path == "/readyz":         # readiness:失败 -> 摘流量不重启
            code, body = (200, "ok") if STATE["ready"] else (503, "warming up")
        else:
            code, body = 404, "not found"
        self.send_response(code)
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8085), ProbeHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.2)
    for path in ("/healthz", "/readyz"):
        try:
            print(path, urllib.request.urlopen(f"http://127.0.0.1:8085{path}").status)
        except Exception as e:
            print(path, "异常:", e)
    STATE["ready"] = True
    print("预热完成后 readyz 变 200,liveness 全程不受影响")
    srv.shutdown()
