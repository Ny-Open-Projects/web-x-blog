---
title: [Q7566] 网关侧 SSE 与 WebSocket 协议转换
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7566 · 网关侧 SSE 与 WebSocket 协议转换

难度：P6 | 标签：网关、SSE、WebSocket、协议转换、背压

**问**：上游模型供应商只出 SSE 流，前端 App 用 WebSocket 长连接。网关做协议转换要处理哪些问题？断连客户端、半包、背压分别怎么办？

**答**：
- **结论**：转换器三件事：① SSE 解析——按 `\n\n` 分帧，`event:`/`data:` 字段解析成结构化事件，处理半包（TCP 分片可能把一帧切开，要缓冲到完整帧再转发）；② 扇出——一个上游流扇给多个下游 WS 连接，断连客户端立即跳过且不能阻塞转发循环（慢客户端用每连接有界缓冲，满了断开该客户端而不是拖累别人）；③ 终止语义对齐——上游 `[DONE]`/异常关闭要转换成 WS 的 close 帧与错误消息，让前端能区分"正常结束"和"上游故障"。
- **取舍**：每连接缓冲的取舍：无界缓冲 OOM，太小断连误伤慢网络用户；按 token 预算设上限（如 1MB）并统计断开率。转换层是否落盘：不落盘（纯转发）简单但断线后无法续传；落盘+游标可支持断线重连续传，成本是存储与状态管理——交互式场景建议至少支持"会话级重放最近 N 帧"。
- **实战**：监控三指标：转换延迟（上游事件到下游帧的时间差）、断连率、缓冲水位。事故高发点：SSE 的 `data:` 多行拼接（一帧多条 data 行要 join）没处理，导致 JSON 半截传给前端——解析层单测必须覆盖多行 data 与空 data 帧。

```python
"""网关侧 SSE -> WebSocket 协议转换：解析事件流并按客户端游标转发。"""
def sse_events(stream_text):
    """解析 SSE 文本流为 (event, data) 序列（按空行分帧）。"""
    ev, data = None, []
    for line in stream_text.splitlines():
        if line.startswith("event:"):
            ev = line[6:].strip()
        elif line.startswith("data:"):
            data.append(line[5:].strip())
        elif line == "":
            if data:
                yield ev or "message", "\n".join(data)
            ev, data = None, []
    if data:
        yield ev or "message", "\n".join(data)

stream = """event: token
data: {"t": "你"}

event: token
data: {"t": "好"}

event: done
data: [DONE]

"""

class WsClient:
    def __init__(self, name):
        self.name, self.frames, self.closed = name, [], False

def bridge_to_ws(stream, clients):
    for ev, payload in sse_events(stream):        # 上游 SSE 解析
        for c in clients:
            if not c.closed:                      # 已断开的客户端跳过，不阻塞转发
                c.frames.append(f"{{type:{ev}}}")
    return clients

clients = [WsClient("a"), WsClient("b")]
clients[1].closed = True
bridge_to_ws(stream, clients)
print("a 收到帧数:", len(clients[0].frames), "b(断开)收到:", len(clients[1].frames))
print("要点：协议转换要处理断连客户端（不阻塞扇出）与半包（SSE 按\\n\\n 分帧）")
```

**追问链**：
1. 追问一层：为什么慢客户端要"断开"而不是"阻塞等待"？（一个慢客户端阻塞转发循环会把延迟传染给所有客户端——队头阻塞；断开是背压的最后手段，客户端可重连续传）
2. 追问二层：断线重连续传要网关存什么？（会话的事件序列 + 每客户端游标；重连带 last_seq，网关从游标重放——所以"要不要落盘"在方案阶段就要定）

**背诵要点**：
1. SSE 按 \n\n 分帧防半包，event/data 字段解析，多行 data 要 join。
2. 扇出循环绝不阻塞：慢/断客户端用有界缓冲+断开，不传染延迟。
3. 终止语义对齐（[DONE]→close 帧）；监控转换延迟、断连率、缓冲水位。

**复盘追问**：
1. 前端反馈偶发"JSON 半截"，网关侧先查什么？（SSE 多行 data 拼接与半包缓冲）
2. 上游 [DONE] 丢失时前端会怎样？（等待态永不结束——网关要加"上游超时即合成 done 帧"的兜底）
