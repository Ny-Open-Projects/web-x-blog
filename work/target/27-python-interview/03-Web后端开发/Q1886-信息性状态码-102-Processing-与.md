---
title: [Q1886] 信息性状态码 102 Processing 与 103 Early Hints
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1886 · 信息性状态码 102 Processing 与 103 Early Hints

> 难度:★★☆☆ | 标签:HTTP, 性能优化

**问**:103 Early Hints 和已经废弃的 102 Processing 是怎么回事?什么场景值得用 103?

**答**:1xx 是信息性响应,只含状态行与头、不含体,允许在最终响应之前发出多帧。102 Processing 用于告知"请求已收到仍在处理"以防客户端超时,但实践价值低,已被 RFC 9110 标记废弃。103 Early Hints 允许源站在最终响应头还没确定时,提前下发 Link 头(preload/prefetch 提示),让浏览器并行预加载 CSS/JS,削减首屏渲染的串行等待,典型场景是源站要查库才能定最终头、但静态资源清单已知。约束三条:103 只是预告,最终响应的头与体不受它影响;客户端不得把 103 当最终响应;代理要能转发而不是缓存它。工程上常由 CDN/代理生成 103(如 Nginx 的 early hints 模块),源站无需感知。

```python
# file: code/03_Web后端开发/q1886_early_hints.py
"""102 Processing 与 103 Early Hints: 信息性状态码的语义与用法(纯标准库)。"""
import json

def early_hints_frames(preloads, final_status, final_body, extra_headers=None):
    """模拟一个带 103 Early Hints 的响应帧序列。

    preloads: [(url, as_type)] 将被写进 103 帧的 Link 头。
    返回 [第一帧文本, 最终帧文本]; 1xx 帧只允许状态行加头, 不允许携带体。
    """
    link = ", ".join("<{}>; rel=preload; as={}".format(u, a) for u, a in preloads)
    head103 = "HTTP/1.1 103 Early Hints\r\nLink: {}\r\n\r\n".format(link)
    lines = ["HTTP/1.1 {} Final\r\n".format(final_status),
             "Content-Type: text/html; charset=utf-8\r\n"]
    for k, v in (extra_headers or {}).items():
        lines.append("{}: {}\r\n".format(k, v))
    lines.append("Content-Length: {}\r\n\r\n".format(len(final_body)))
    head_final = "".join(lines) + final_body
    return [head103, head_final]


def validate_informational(frame):
    """校验信息性帧的硬约束: 1xx 状态码、无消息体、可选 Link 头。"""
    head = frame.split("\r\n\r\n")[0]
    lines = head.split("\r\n")
    status = int(lines[0].split()[1])
    errors = []
    if status < 100 or status >= 200:
        errors.append("信息性状态码必须在 1xx 区间")
    if len(frame.split("\r\n\r\n", 1)) > 1 and frame.split("\r\n\r\n", 1)[1]:
        errors.append("1xx 响应不得携带消息体")
    if status == 103 and "Link:" not in head:
        errors.append("103 的价值在于 Link 提示头, 缺失则失去意义")
    return errors


frames = early_hints_frames(
    [("/style.css", "style"), ("/app.js", "script")],
    200, "<html><body>ok</body></html>",
    extra_headers={"X-Request-ID": "r-1001"})

print("第一帧 103(源站刚确定静态资源, 让浏览器并行预热):")
print(frames[0])
print("最终帧头部:")
print("\n".join(frames[1].split("\r\n\r\n")[0].split("\r\n")))
print("103 帧校验:", validate_informational(frames[0]) or "通过")

bad = "HTTP/1.1 103 Early Hints\r\n\r\nleaked-body"
print("坏样本校验:", validate_informational(bad))
print("要点: 103 不是响应的一部分而是预告, 客户端按 Link 提前建连预热, 最终响应不受影响")
```

**追问**:
- 103 会不会与最终响应里的 Link 冲突?——不会,客户端取并集,最终响应的 Link 优先级更高。
- 为什么 102 被废弃?——流式语义由最终响应的编码与超时策略解决,主动播报进度的场景 SSE/WebSocket 更合适。
