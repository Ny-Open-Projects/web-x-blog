"""响应头与请求头过大的诊断: 431 与网关缓冲区预算(纯标准库)。"""


def header_block_bytes(start_line, headers):
    """按 HTTP 报文序列化估算头块字节数。"""
    block = start_line + "\r\n"
    for name, value in headers:
        block += "{}: {}\r\n".format(name, value)
    block += "\r\n"
    return block, len(block.encode("utf-8"))


def budget_check(block_bytes, limit=8192):
    """网关常见的单头块上限约 8KB, 超限对应 431 或截断风险。"""
    if block_bytes > limit:
        return False, "超限: {} 字节 > 上限 {} 字节, 网关将回 431".format(
            block_bytes, limit)
    usage = block_bytes / limit
    return True, "占用预算 {:.0f}%, 剩余 {} 字节".format(usage * 100, limit - block_bytes)


def cookie_bloat(n_cookies, value_size):
    """模拟 Cookie 逐个累积: 每个都是独立请求头, 一起挤占预算。"""
    headers = []
    for i in range(n_cookies):
        headers.append(("Set-Cookie" if i == 0 else "X-Dummy", "v" * value_size))
    headers.append(("Cookie", "; ".join(
        "k{}={}".format(i, "v" * value_size) for i in range(n_cookies))))
    return headers


# 场景一: 健康的响应头
block, size = header_block_bytes("HTTP/1.1 200 OK", [
    ("Content-Type", "application/json"),
    ("Cache-Control", "max-age=60"),
])
print("健康响应头: {} 字节, {}".format(size, budget_check(size)[1]))
assert budget_check(size)[0]

# 场景二: Cookie 膨胀把请求头撑爆 -> 431
for n, expect_ok in [(5, True), (20, True), (40, False), (60, False)]:
    headers = cookie_bloat(n, 120)
    _, req_size = header_block_bytes("POST /api HTTP/1.1", headers)
    ok, msg = budget_check(req_size)
    print("cookie x{:2d} -> 请求头 {} 字节, {}".format(n, req_size, msg))
    assert ok == expect_ok, (n, req_size, msg)
    if not ok:
        assert "431" in msg

# 场景三: 治理手段的量化效果
trimmed = [("Cookie", "sid=short")]              # 状态搬进服务端会话
_, trimmed_size = header_block_bytes("POST /api HTTP/1.1", trimmed)
print("治理后请求头: {} 字节, 节省 {} 字节".format(
    trimmed_size, req_size - trimmed_size))
assert trimmed_size < 100

print("治理清单: 大状态出 Cookie 进服务端会话, 值做压缩与 shorten, "
      "逐个头检查长度, 网关侧按需调大缓冲但先问为什么要这么大")
print("要点: 头大小是预算制, 431 的常见根源是 Cookie 堆积; "
      "响应头过大则会让老浏览器与中间盒悄悄截断, 表现为随机性的响应异常")
