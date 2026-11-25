---
title: [Q7667] Realtime API 演进与接入方式迁移：WebSocket 到 WebRTC
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7667 · Realtime API 演进与接入方式迁移：WebSocket 到 WebRTC

难度：P6-P7 | 标签：版本演进、Realtime、语音 Agent

**问**：语音 Agent 早期用 Realtime API 的 WebSocket 服务端中转音频，2025 年演进里 WebRTC 接入成为官方推荐（尤其浏览器端）。这次接入方式演进解决了什么问题？服务端中转架构与 WebRTC 直连架构的迁移要点、各自适用边界是什么？

**答**：结论：WebSocket 服务端中转的结构性问题是**音频流过自己的服务器**：带宽（双向实时音频）与延迟（多两跳）都压在服务端，且服务端要做音频编解码转发——Q7647 的并发路数容量账里这部分是主要成本。WebRTC 直连让**客户端与模型端点建立 P2P/边缘会话**（ephemeral token 换取短期凭据），服务端只负责鉴权与会话管理，音频不走业务服务器；服务端中转仍适合电话/PSTN、服务端有转写/录音需求的场景。迁移要点：ephemeral token 生命周期管理、事件协议差异（WebRTC data channel 与 WebSocket 消息格式一致性）、打断（barge-in）时序验证。

取舍与实战：
1. 双架构共存期：接入层抽象 `RealtimeTransport` 接口（WS/WebRTC 两实现），按客户端能力与合规需求路由——浏览器/移动端走 WebRTC，电话网关走 WS 中转；协议事件统一映射层避免业务代码双写。
2. ephemeral token 是安全关键：短期凭据（分钟级 TTL）让客户端直连供应商而不过服务器，**业务鉴权必须在发 token 前完成**（token 一旦发出，供应商只认它）；token 续期在会话中途的处理要设计（多数实现是会话内不支持换新，超时会话要重建）。
3. 迁移验证清单：打断延迟（用户插话到 TTS 停止，WebRTC 应明显更低）、弱网下的抖动缓冲差异、data channel 消息顺序与 WS 事件幂等差异、音频格式协商（PCM16/Opus）。
4. 容量账重构：WebRTC 后业务服务器不再承担音频带宽，Q7647 的并发路数账要重算——瓶颈从带宽/CPU 转到会话控制面（ephemeral token 签发、事件转发），这是演进最大的容量红利。

```python
"""双传输架构会话控制面：ephemeral token 发放与传输选择（标准库演示）"""
import time, secrets

class EphemeralToken:
    TTL_S = 300
    def __init__(self, session_id: str):
        self.value = secrets.token_urlsafe(24)
        self.session_id = session_id
        self.issued = time.monotonic()
    def expired(self) -> bool:
        return time.monotonic() - self.issued > self.TTL_S

def choose_transport(client: str, need_recording: bool) -> str:
    if need_recording:
        return "websocket-relay"     # 服务端要过音频流才可录/转写
    if client in ("browser", "mobile"):
        return "webrtc"              # 直连模型端点，音频不过业务服务器
    return "websocket-relay"         # 电话网关/PSTN 等

tok = EphemeralToken("s1")
transport = choose_transport("browser", need_recording=False)
print(f"transport={transport}, token_expired={tok.expired()}")
assert transport == "webrtc" and not tok.expired()
# 迁移要点：会话中途 token 过期 → 必须重建会话，不支持热换
```

**追问 1**：为什么服务端录音/转写需求会强制 WebSocket 中转架构？
**提示**：WebRTC 直连时音频只在客户端与供应商边缘之间流动，业务服务器拿不到音频流；要录音/实时转写/合规留档就必须自己作为 media relay（WS 中转或 WebRTC SFU），架构选择由合规需求倒推。

**追问 2**：ephemeral token 的"TTL 300 秒但通话可能 30 分钟"矛盾怎么处理？
**提示**：token 只用于**建立**会话（SDP 协商期），会话建立后连接生命周期独立于 token TTL；重连场景才需要重新走业务鉴权换新 token——把"会话"与"凭据"两个生命周期分开建模。

## 背诵要点
- WebRTC 直连解决 WS 中转的结构性问题：音频不过业务服务器，带宽/延迟/容量账重构，瓶颈转到会话控制面。
- ephemeral token 分钟级 TTL 只管会话建立；业务鉴权在发 token 前完成，重连才换新。
- 双架构长期共存：浏览器/移动走 WebRTC，录音/转写/电话合规场景走 WS 中转；接入层抽象统一事件映射。

## 复盘追问
- 如何设计一次双架构 A/B：同话术下对比 barge-in 延迟与弱网断线率，验证迁移收益？
- 会话重建（token 过期/断线）时上下文恢复策略对用户体验的影响如何量化？
