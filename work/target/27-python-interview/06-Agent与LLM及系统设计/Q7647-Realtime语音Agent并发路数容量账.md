---
title: [Q7647] Realtime 语音 Agent 并发路数与 STT/TTS 容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7647 · Realtime 语音 Agent 并发路数与 STT/TTS 容量账

难度：P7 ｜ 标签：容量规划 / 语音 Agent / 实时

**问**：语音 Agent（用户说话 → STT → LLM → TTS → 播放）的容量账和文本 Agent 完全不同：每路会话是**持续占用**的流（音频上下行），延迟预算是"对答不尴尬"的几百毫秒级。并发路数怎么算、延迟预算怎么在各组件间分配、打断（barge-in）对容量账有什么冲击？

**答**：
- **结论**：语音容量账三笔。① **并发路数 = 独占型账**：每路会话在整个通话期间持续占用连接与流式配额（Realtime API 按音频时长计费、WebSocket 连接常驻），并发路数上限 = 网关连接容量（Q7627 同款问题）与配额的较小值，不是 QPS 而是同时在线路数——容量规划单位从"每秒请求数"换成"路数 × 平均通话时长"（Erlang 模型：`路数 = 日通话量 × 平均时长 / 86400 × 峰值系数`）。② **延迟预算分配**：端到端目标 < 800ms（超过即"对答尴尬"），拆账：VAD 静音判定 ~200ms + STT 流式增量 ~150ms + LLM 首 token（TTFT）~300ms + TTS 首音频块 ~150ms——**每一环都必须流式**，任何一环攒整段（如等完整 STT 句子再调 LLM）就毁掉全局；TTFT 预算给 LLM 的窗口极小，长上下文/P95 尾部直接超预算，所以会话历史裁剪（Q7645）在语音场景是延迟刚需不只是成本刚需。③ **打断（barge-in）冲击**：用户中途打断时，已生成的音频/计算作废——打断率上升意味着有效吞吐下降（浪费的生成 token 与 TTS 音频全烧掉），容量账要乘 `1/(1-打断浪费率)`，TTS 合成通常比 LLM 生成慢且更贵，是最需要"块级取消"的环节。
- **取舍**：一体化 Realtime API（语音进语音出，厂商统一处理 VAD/打断，延迟最优）vs 组件级拼接（STT+LLM+TTS 自由组合、成本可控、可各环节降级）——拼接方案延迟累计但每环可独立优化与计费；通话高峰的成本差可达数倍（一体化按音频时长全价计费，拼接只在说话时计费）。VAD 灵敏度调优是隐形的延迟/容量旋钮：太灵敏把用户停顿当说完（误触发），太钝增加等待延迟。
- **实战**：① 延迟打点按"语音结束→首音频播出"的口径测（用户感知），分段 span 定位最慢环节；② TTS 块级取消 + LLM 流式丢弃：打断后立刻 cancel 上游，别等生成完再扔；③ 并发路数压测要模拟真实通话时长分布（短问短答 vs 长咨询），按 Erlang C 估排队；④ 高峰策略：排队等待播报 + 超时降级到"留言回拨"，比硬扛并发稳。

```python
# 语音 Agent 容量账: Erlang 并发路数 + 延迟分段预算 + 打断浪费率
# 基线: Python 3.9+ 标准库 (数值为演示口径)
import math
from dataclasses import dataclass


@dataclass
class VoiceLatency:
    vad_ms: float = 200
    stt_ms: float = 150
    ttft_ms: float = 300
    tts_first_ms: float = 150

    def e2e(self) -> float:
        return self.vad_ms + self.stt_ms + self.ttft_ms + self.tts_first_ms

    def over_budget(self, budget_ms: float = 800) -> str:
        slowest = max([("vad", self.vad_ms), ("stt", self.stt_ms),
                       ("llm-ttft", self.ttft_ms), ("tts", self.tts_first_ms)],
                      key=lambda x: x[1])
        if self.e2e() > budget_ms:
            return f"OVER: 最慢环节 {slowest[0]}={slowest[1]}ms"
        return "ok"


def concurrent_calls(daily_calls: int, avg_sec: float, peak: float) -> int:
    """Erlang 近似: 同时在线 = 日量 x 时长 / 活跃秒数 x 峰值系数。"""
    active_sec = 8 * 3600                 # 日内 8 小时活跃
    return math.ceil(daily_calls * avg_sec / active_sec * peak)


def main() -> None:
    lat = VoiceLatency()
    assert lat.e2e() == 800               # 刚好预算边缘
    assert lat.over_budget(800) == "ok"
    slow = VoiceLatency(ttft_ms=600)      # 长上下文 TTFT 超标
    assert "llm-ttft" in slow.over_budget(800)
    # 并发: 日 5 万通, 均 90 秒, 峰值系数 3 -> ~469 路
    calls = concurrent_calls(50_000, 90, 3.0)
    assert 400 < calls < 550, calls
    # 打断浪费: 打断率 20%, 每次打断浪费平均 40% 生成量
    waste = 0.2 * 0.4                     # 8% 有效吞吐损失
    effective = 1 / (1 - waste)
    assert abs(effective - 1 / 0.92) < 1e-6
    print(f"路数≈{calls}, e2e={lat.e2e()}ms, 打断使有效容量 x{effective:.2f}")
    print("OK: 容量按同时在线路数(Erlang)非QPS; 全链路流式 + 块级取消")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"等完整 STT 句子再调 LLM"会毁掉延迟？
→ 一句话提示：串行攒段 = 每环加整句时长（常见 1-3 秒），全链路立刻超过 800ms 预算；正确姿势是 STT 增量结果直接流进 LLM、LLM 首 token 流进 TTS，各环重叠执行。

**追问 2**：打断的"块级取消"具体取消什么？
→ 一句话提示：三层取消——LLM 生成流丢弃未产出 token、TTS 停止合成并清音频队列、播放器立即静音换用户音频；任何一层不取消都会播"残留的旧回答"，是语音产品最刺眼的体验 bug。

## 背诵要点
- 语音容量单位 = 同时在线路数（Erlang：日通话量 × 均时长 / 活跃秒数 × 峰值系数），不是 QPS；每路通话期间持续占连接与配额。
- 延迟预算 <800ms 按段分：VAD 200 + STT 150 + TTFT 300 + TTS 首块 150，全链路必须流式；长上下文裁剪是延迟刚需。
- 打断浪费率 = 打断率 × 平均作废比例，容量账除以 (1-浪费率)；TTS 块级取消是最关键的体验修复。

## 复盘追问
- 一体化 Realtime API 与组件拼接的成本差从哪来？提示：一体化按音频时长全程计费（含静音），拼接只在说话时计费且各环可降级；高峰通话量大时差数倍，换延迟最优要看场景。
- 如何压测语音网关的连接容量？提示：模拟真实时长分布的 WS 长连接 + 音频流，观测句柄数/内存/每路 CPU（Q7627 长连接账），并验证打断风暴下的取消路径不泄漏。
