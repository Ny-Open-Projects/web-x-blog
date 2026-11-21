"""大 JSON 响应的分块写出: 生成器边算边写, 不攒完整字符串(缺库降级)。"""
import json
import tracemalloc

try:
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse
    from fastapi.testclient import TestClient
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("未安装 fastapi/httpx, 框架部分跳过, 标准库演示生成器分块核心")

ITEMS = [{"id": i, "name": "item-%05d" % i, "tags": ["a", "b"]} for i in range(2000)]


def iter_json_array(items, chunk_size=500):
    """逐块产出 JSON 数组文本: 首块补 [ 后缀, 后续块自带前置逗号。

    内存里永远只有当前块, TTFB 提前到第一个块就绪时, 客户端可边收边解析。
    """
    yield "["
    first = True
    for i in range(0, len(items), chunk_size):
        piece = ",".join(json.dumps(x, ensure_ascii=False, separators=(",", ":"))
                         for x in items[i:i + chunk_size])
        yield piece if first else "," + piece
        first = False
    yield "]"


EXPECTED = json.dumps(ITEMS, ensure_ascii=False, separators=(",", ":"))

tracemalloc.start()
full = json.dumps(ITEMS, ensure_ascii=False)
full_peak = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
sizes = []
for piece in iter_json_array(ITEMS):
    sizes.append(len(piece))
stream_peak = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

assert "".join(iter_json_array(ITEMS)) == EXPECTED, "分块拼接必须与整体序列化逐字节一致"
assert full_peak > stream_peak * 5, (full_peak, stream_peak)
print("整体序列化峰值 %d KB, 分块峰值 %d KB, 单块最大 %d KB"
      % (full_peak // 1024, stream_peak // 1024, max(sizes) // 1024))
assert "".join(iter_json_array([])) == "[]"

if HAS_FASTAPI:
    app = FastAPI()

    @app.get("/items")
    def items():
        return StreamingResponse(iter_json_array(ITEMS), media_type="application/json")

    r = TestClient(app).get("/items")
    assert r.status_code == 200 and r.json() == ITEMS
    print("FastAPI StreamingResponse 输出与整体序列化一致, 分块随生成器逐段下发")
