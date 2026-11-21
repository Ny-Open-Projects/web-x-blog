---
title: [Q2707] 大 JSON 响应的分块写出
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2707 · 大 JSON 响应的分块写出

> 难度:★★★★ | 标签:流式响应, 性能, FastAPI

**问**:导出接口要返回几百 MB 的 JSON 数组,直接 json.dumps 会发生什么,怎么改?

**答**:json.dumps 先在内存里攒完整字符串,峰值内存是数据量的数倍,首字节也要等全量序列化完,TTFB 极差。改成生成器分块:先产出 `[`,之后每块若干元素序列化、以前置逗号拼接后产出,最后补 `]`——拼接规则写死在生成器里,内存峰值只剩单块,客户端还能边收边解析。验证口径两条:分块拼接结果必须与整体序列化逐字节一致,块内序列化的 separators 要与整体对齐(默认带空格,必须显式用紧凑分隔符,否则对不上);tracemalloc 实测峰值差一个量级。框架层用 FastAPI 的 StreamingResponse 包住生成器,chunked 编码自动处理,客户端断开还能传导回生成器提前终止。

```python
# file: code/03_Web后端开发/q2707_chunked_json.py
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
```

**追问**:
- 客户端边收边解析怎么处理半截块?——用流式 JSON 增量解析器喂进去,分块写出与流式解析是同一条流水线的两端。
- 分块大小怎么定?——网络 MTU 与压缩窗口的整数倍附近,几 KB 到几十 KB;太小帧开销大,太大失去流式收益。
