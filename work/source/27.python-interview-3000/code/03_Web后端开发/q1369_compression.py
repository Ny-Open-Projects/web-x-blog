"""响应压缩决策与级别实测(纯标准库)。"""
import json
import time
import zlib

COMPRESSIBLE = {"application/json", "text/html", "text/plain"}
MIN_BYTES = 860


def should_compress(content_type, body, accept_encoding):
    if "gzip" not in accept_encoding.lower():
        return None
    if content_type not in COMPRESSIBLE or len(body) < MIN_BYTES:
        return None
    return 6                                     # 默认建议级别


def gzip_bytes(data, level):
    co = zlib.compressobj(level, zlib.DEFLATED, 16 + zlib.MAX_WBITS)
    return co.compress(data) + co.flush()


body = json.dumps([{"id": i, "name": "商品名称示例数据" * 3} for i in range(40)],
                  ensure_ascii=False).encode("utf-8")
print("原始大小:", len(body), "决策级别:", should_compress("application/json", body, "gzip, deflate"))
print("不该压:", should_compress("image/png", body, "gzip"), should_compress("application/json", body[:100], "gzip"))
for level in (1, 6, 9):
    t0 = time.perf_counter()
    out = gzip_bytes(body, level)
    cost = (time.perf_counter() - t0) * 1000
    print(f"level={level} 压缩后 {len(out)}B 比率 {len(out) / len(body):.0%} 耗时 {cost:.2f}ms")
