---
title: [Q7584] Realtime 语音 Agent 的 API 演进与迁移
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7584 · Realtime 语音 Agent 的 API 演进与迁移

难度：P6/P7 ｜ 标签：语音 Agent / API 演进 / WebSocket

**问**：旧架构是 ASR → 文本 LLM → TTS 三段式流水线（基线 Python 3.11+，openai SDK 1.x）。Realtime API（WebSocket 双向流、语音进语音出、服务端 VAD/打断）出现后，架构怎么演进？迁移要处理什么？

**答**：
- **结论**：三段式的固有缺陷是级联延迟（ASR 结束才推理、TTS 排队，端到端 2-4s）与信息丢失（韵律/打断语义在文本化时丢弃）。Realtime API 把语音作为一等模态：WebSocket/WebRTC 双向流、服务端 VAD 检测说话结束、用户可打断（barge-in，模型边听边生成、被打断时立即停）。架构演进的核心变化：客户端从"发一次请求收一个响应"变成"维护长会话事件循环"，Python 侧要处理事件状态机（session.created / input_audio_buffer.* / response.* / error）与断线重连（会话状态服务端持有，重连要重放系统指令与历史——或接受丢失）。
- **取舍**：三段式 vs Realtime：三段式可各环节独立换供应商/降级、可观测性好、token 成本可精确核算；Realtime 延迟低、自然度高，但计费按音频秒数且不透明、供应商锁定强、打断与 VAD 参数调优复杂。混合策略常见：首轮延迟敏感场景（电话客服）用 Realtime，批处理/对延迟不敏感场景保留三段式（成本更低、可换低价模型）。
- **实战**：迁移清单：① 传输层选型——客户端直连用 WebRTC（抗弱网），服务端中转用 WebSocket（可注入审计）；② 会话状态与计费核对：音频输入按分钟计费，单位经济模型要重算（对比三段式 token 成本）；③ 打断体验：客户端要停 TTS 播放并清缓冲，服务端 `response.cancel`；④ 降级路径：Realtime 不可用时自动回落三段式，且回落期间禁用打断相关交互。

```python
# Realtime 会话事件状态机与打断处理（纯标准库 asyncio 模拟）
# 基线：Python 3.11+（asyncio.TaskGroup）；实际项目用 openai SDK 1.x Realtime WS

import asyncio


class RealtimeSession:
    def __init__(self):
        self.events: asyncio.Queue[dict] = asyncio.Queue()
        self.interrupted = False
        self.active_response: asyncio.Task | None = None

    async def push(self, ev: dict) -> None:
        await self.events.put(ev)

    async def run(self) -> list[str]:
        handled: list[str] = []
        while True:
            ev = await self.events.get()
            if ev["type"] == "input_audio_buffer.speech_started":
                self.interrupted = True          # barge-in
                if self.active_response:
                    self.active_response.cancel()  # response.cancel
                handled.append("interrupt")
            elif ev["type"] == "response.audio.delta":
                if self.interrupted:
                    continue                      # 清播放缓冲
                handled.append("audio")
            elif ev["type"] == "response.done":
                self.interrupted = False
                handled.append("done")
                break
        return handled


async def demo() -> None:
    s = RealtimeSession()
    async def gen_response():
        await asyncio.sleep(10)   # 模拟长音频生成
        await s.push({"type": "response.done"})
    s.active_response = asyncio.create_task(gen_response())
    await s.push({"type": "response.audio.delta"})
    await s.push({"type": "input_audio_buffer.speech_started"})  # 用户打断
    await s.push({"type": "response.done"})
    print(await s.run())
    assert s.active_response.cancelled() or s.active_response.done()


def main() -> None:
    asyncio.run(demo())
    print("事件状态机与打断处理验证通过")


if __name__ == "__main__":
    main()
```

**追问 1**：WebRTC 和 WebSocket 在语音场景怎么选？
→ 一句话提示：浏览器/移动端直连用 WebRTC（内建抗丢包、回声消除、自动码率适配）；服务端做审计/网关中转时用 WebSocket，但要自己处理弱网重传与音频抖动缓冲。

**追问 2**：Realtime 会话断线重连的挑战？
→ 一句话提示：会话上下文在服务端且不可导出（或只有摘要），重连策略是"新会话+重放系统指令与压缩历史"，要设计成客户端幂等重放，并接受音视频上下文（说话风格）不可恢复。

## 背诵要点
- 架构演进：三段式（级联延迟 2-4s、韵律丢失）→ Realtime（语音原生、服务端 VAD、barge-in）。
- 计费变化：token 核算 → 音频时长计费，单位经济模型必须重算；Realtime 供应商锁定强，保留三段式降级路径。
- Python 侧核心：事件状态机（session/buffer/response/error）+ 打断时 cancel 任务并清播放缓冲 + 会话重放式重连。

## 复盘追问
- 为什么打断（barge-in）是语音 Agent 最难的体验点？提示：涉及客户端播放缓冲清理、服务端生成取消、VAD 阈值（呼吸声/背景音误触发打断）三层协同，任何一层慢半拍都会"抢话"。
- 迁移期间如何对拍两架构的质量？提示：同 batch 样本双跑（三段式 vs Realtime）对比转写文本与延迟分布，成本按各自计费口径归一对比。
