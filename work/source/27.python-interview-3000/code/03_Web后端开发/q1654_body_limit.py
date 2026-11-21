"""请求体大小限制: Content-Length 前置检查 + 流式计数兜底(纯标准库)。"""

MAX_BODY = 1024 * 1024                       # 1 MiB


class PayloadTooLarge(Exception):
    pass


def precheck(headers):
    """读体之前先看 Content-Length, 超限直接拒绝, 一个字节都不收。"""
    raw = headers.get("Content-Length")
    if raw is None:
        return None
    try:
        length = int(raw)
    except ValueError:
        return 400
    return 413 if length > MAX_BODY else None


def read_with_limit(chunks):
    """chunked 无长度场景: 边读边数, 一超限立刻掐断, 不给慢速攻击喂内存。"""
    total = 0
    for chunk in chunks:
        total += len(chunk)
        if total > MAX_BODY:
            raise PayloadTooLarge(f"流式读超过 {MAX_BODY}B")
        yield chunk


print("CL=2MiB  ->", precheck({"Content-Length": str(2 * 1024 * 1024)}))
print("CL=64KiB ->", precheck({"Content-Length": "65536"}), "(放行)")
print("CL=abc   ->", precheck({"Content-Length": "abc"}))

chunks = [b"x" * (512 * 1024)] * 3           # 共 1.5 MiB, 无 Content-Length
try:
    for _ in read_with_limit(chunks):
        pass
except PayloadTooLarge as e:
    print("流式拦下:", e)
print("要点: 应用层限额是最后防线, 网关层 client_max_body_size 是第一道, 两层都要有")
