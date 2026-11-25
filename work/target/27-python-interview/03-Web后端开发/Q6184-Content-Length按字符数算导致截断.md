---
title: "[Q6184] Content-Length 按字符数算：中文响应被截断或挂死"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6184 · Content-Length 按字符数算：中文响应被截断或挂死

难度：P6 ｜ 标签：HTTP、Content-Length、UTF-8、ASGI、流式

**问**：一个自研的网关/适配层返回中文 JSON，客户端偶发 `JSONDecodeError`，或者一直挂着等 body 直到超时。抓包看到响应头 `Content-Length` 比实际字节数小。为什么会按字符算？除了手写响应，还有哪些地方会踩"字符数 ≠ 字节数"？

**答**：
结论：HTTP 的 `Content-Length` 单位是**字节**。Python 里 `len(str)` 是字符数，中文在 UTF-8 下占 3 字节，50 个字符的 JSON 可能是 62 字节——差 12 字节，客户端就会"少读 12 字节"（解析失败）或"多等 12 字节"（连接挂到超时）。框架层（Starlette/FastAPI/Django）都会替你算字节，出问题的一定是手写响应、自定义中间件、自己拼 multipart、或者把已编码的 body 又按字符切分。

取舍：让框架算最省心；必须手写时用 `len(body_bytes)`，绝不用 `len(body_str)`。流式输出有两条路：a) 不给 `Content-Length`，用 `Transfer-Encoding: chunked`（ASGI 里 `more_body=True` 自然就是 chunked）；b) 必须先给长度就累加 `len(chunk.encode())`。压缩场景更要注意：`Content-Length` 必须是**压缩后**的字节数，否则中间件和框架会打架。

实战：事故形态是"中文环境一直有问题，英文/数字环境完全正常，所以测不出来"；或者"偶发，因为只有部分响应含中文"。另一个常见是"按字符切片流式输出"，把一个 3 字节的汉字切成两半，客户端解码出 `�`。下面构造响应头 + body，演示按字符算导致 json 解析失败、按字节算正常、以及按字符切多字节的后果。

```python
import json

payload = {"code": 0, "msg": "操作成功", "data": {"name": "张三"}}
body = json.dumps(payload, ensure_ascii=False)

wrong = len(body)            # 字符数
right = len(body.encode("utf-8"))  # 字节数
print("[1] 字符数:", wrong, "| UTF-8 字节数:", right, "| 差:", right - wrong)

raw = body.encode("utf-8")
header = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {wrong}\r\n\r\n"
framed = header.encode("utf-8") + raw

head, _, stream = framed.partition(b"\r\n\r\n")
declared = int([l for l in head.split(b"\r\n") if l.lower().startswith(b"content-length")][0].split(b":")[1])
received = stream[:declared]
print("[2] 客户端按 Content-Length 只收到:", received)
try:
    json.loads(received)
except json.JSONDecodeError as e:
    print("[3] 截断的 JSON ->", type(e).__name__, "|", e)

print("[4] 修正后完整解析:", json.loads(stream[:right])["msg"])

chunk = "中文".encode("utf-8")
print("[5] 同理：按字符切分多字节也会切坏，", chunk[:2], "无法解码:",
      chunk[:2].decode("utf-8", "replace"))
```

**追问一**：长度算大了会怎样，为什么比算小更危险？—— 客户端会一直等剩余字节，连接挂到 read timeout 才失败，表现为"偶发超时、偶发 502"，而不是立即可见的解析错误。日志里看是"上游慢"，实际是协议层等一个永远不来的尾巴。算小则立即 `JSONDecodeError`，反而好查。

**追问二**：开了 gzip 之后 `Content-Length` 怎么算？—— 必须是压缩后的字节数，而且是"这次实际写出的压缩块"总长。常见错误是先算原始长度、再由压缩中间件改写 body，两者不一致 → 客户端读多/读少。正确做法是压缩中间件负责重算（或直接改成 chunked，不声明长度），不要在业务层提前写死 header。

## 背诵要点
- `Content-Length` 是字节数：`len(str)` 会把中文按 1 算，UTF-8 实际 3 字节，导致截断或挂死。
- 流式要么 chunked（不给长度），要么累加 `len(chunk.encode())`；压缩后必须用压缩后的长度。
- 长度算大比算小更隐蔽：表现为超时而非报错。

## 复盘追问
- 中文响应偶发 `JSONDecodeError`、英文正常，如何定位并修复？（字符 vs 字节、框架重算）
- 按字符切片流式输出会怎样？压缩场景长度该怎么算？（多字节切半、压缩后长度/chunked）
