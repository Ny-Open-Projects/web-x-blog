"""Expect 100-continue 的服务端决策: 先答应再收体(纯标准库模拟, 无真实网络)。"""
import json


class FakeConn:
    """用列表模拟半双工连接, send 写入帧, 供断言与观察。"""

    def __init__(self):
        self.sent = []
        self.body_requested = False

    def send(self, frame):
        self.sent.append(frame)

    def ask_body(self):
        self.body_requested = True


MAX_BODY = 1 << 20     # 服务端上限 1MB


def handle_request(conn, head):
    """服务端对带 Expect: 100-continue 的请求做出决策。

    决策序: 超限先拒(413 且不收体) -> 无法满足的期望(417) -> 发 100 再收体。
    """
    lines = head.split("\r\n")
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().lower()] = v.strip()
    expectations = [e.strip().lower()
                    for e in headers.get("expect", "").split(",") if e.strip()]
    if "100-continue" in expectations:
        length = int(headers.get("content-length", "0"))
        if length > MAX_BODY:
            conn.send("HTTP/1.1 413 Payload Too Large\r\n\r\n")   # 不发 100, 不收体
            return 413
        if len(expectations) > 1:
            conn.send("HTTP/1.1 417 Expectation Failed\r\n\r\n")  # 不认识的期望
            return 417
        conn.send("HTTP/1.1 100 Continue\r\n\r\n")                # 答应后再收体
        conn.ask_body()
        conn.send("HTTP/1.1 201 Created\r\n\r\n")
        return 201
    conn.send("HTTP/1.1 400 Bad Request\r\n\r\n")
    return 400


# 场景一: 正常 100-continue, 客户端先问再发
c1 = FakeConn()
s1 = handle_request(c1, "POST /upload HTTP/1.1\r\nHost: a\r\n"
                        "Expect: 100-continue\r\nContent-Length: 800\r\n\r\n")
print("场景一 -> 状态", s1, "帧序列:", [f.split()[1] for f in c1.sent],
      "收体:", c1.body_requested)
assert s1 == 201 and c1.body_requested

# 场景二: 体超限, 服务端不答应直接 413, 客户端省去整个上传
c2 = FakeConn()
s2 = handle_request(c2, "POST /upload HTTP/1.1\r\nExpect: 100-continue\r\n"
                        "Content-Length: {}\r\n\r\n".format(MAX_BODY + 1))
print("场景二 -> 状态", s2, "帧序列:", [f.split()[1] for f in c2.sent],
      "收体:", c2.body_requested)
assert s2 == 413 and not c2.body_requested

# 场景三: 携带服务端不支持的期望 -> 417
c3 = FakeConn()
s3 = handle_request(c3, "POST /upload HTTP/1.1\r\nExpect: 100-continue, 200-please\r\n"
                        "Content-Length: 10\r\n\r\n")
print("场景三 -> 状态", s3)
assert s3 == 417

print("要点: 100-continue 的价值在服务端敢于先拒绝, 把昂贵请求体挡在传输之前")
