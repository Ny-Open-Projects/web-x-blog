"""SSE 推送的完整最小实现: 标准库服务端与回环客户端(直连不经代理)。"""
import json
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class SSEHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/events":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Accel-Buffering", "no")  # 提醒反代别缓冲
        self.end_headers()
        try:
            for i in range(1, 4):
                payload = json.dumps({"seq": i, "text": "第%d条推送" % i}, ensure_ascii=False)
                self.wfile.write(("id: %d\n" % i).encode())
                self.wfile.write(b"event: tick\n")
                self.wfile.write(("data: %s\n" % payload).encode())
                self.wfile.write(b"\n")          # 空行才是一帧的结束
                self.wfile.flush()               # 每帧即刷, 否则缓冲会攒批
                time.sleep(0.05)
            self.wfile.write(b": heartbeat\n\n")  # 注释行做心跳, 客户端忽略
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass  # 客户端断开是常态, 不当错误记日志

    def log_message(self, fmt, *args):
        pass


def loopback_opener():
    """回环请求必须绕开 http_proxy。"""
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


server = ThreadingHTTPServer(("127.0.0.1", 0), SSEHandler)
port = server.server_address[1]
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    resp = loopback_opener().open("http://127.0.0.1:%d/events" % port, timeout=5)
    ctype = resp.headers.get("Content-Type")
    print("响应类型:", ctype)
    assert ctype.startswith("text/event-stream")

    frames, current = [], {}
    for raw in resp:                          # 逐行读到服务端关闭
        line = raw.decode("utf-8").rstrip("\n")
        if line == "":                        # 空行: 一帧结束
            if current:
                frames.append(current)
                current = {}
            continue
        if line.startswith(":"):              # 注释心跳, 直接忽略
            continue
        field, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        current[field] = value                # 同名字段叠加是 SSE 规范行为
    print("收到 %d 帧" % len(frames))
    assert len(frames) == 3
    assert [f["id"] for f in frames] == ["1", "2", "3"]
    assert all(f["event"] == "tick" for f in frames)
    first = json.loads(frames[0]["data"])
    assert first == {"seq": 1, "text": "第1条推送"}
    print("首帧:", frames[0])
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)
print("SSE 最小实现演示通过")
