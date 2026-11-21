---
title: [Q7586] 流式输出 TTFT 与吞吐的容量账
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7586 · 流式输出 TTFT 与吞吐的容量账

难度：P7 ｜ 标签：LLM 推理 / 容量规划 / SLO

**问**：流式对话产品承诺"首 token <1s、生成速度 >30 token/s"。并发用户涨到 500 后指标全线恶化。TTFT 与吞吐的容量账怎么算？扩容该按哪个指标触发？

**答**：
- **结论**：流式 LLM 的两个指标由不同资源决定：TTFT（time to first token）主要由"排队时间 + prefill 时间"决定，prefill 是计算密集（并行读 prompt），与 KV cache 占用、批调度策略强相关；吞吐（token/s）由 decode 阶段决定，是显存带宽瓶颈，并发出批（continuous batching）能提升总吞吐但会拉长单请求 TTFT——两者此消彼长，不能同时无限优化。容量账：`并发承载 ≈ 并发槽位 = 可用 KV 显存 ÷ 平均会话 KV 占用`，TTFT SLO 约束下实际可用槽位还要除以调度延迟放大系数。
- **取舍**：批大小的取舍：批越大吞吐越高、TTFT 越差（新请求排队等当前批）；continuous batching（vLLM/SGLang 默认）按 token 级插入缓解但不能消除，prefill 与 decode 混批时 prefill 长任务会阻塞 decode（要用 prefill 优先级调度/分块 prefill）。产品侧取舍：TTFT 优先（对话体验）就要限批、限制长 prompt；吞吐优先（批处理）就离线跑，别混部。
- **实战**：扩容触发器：不按 CPU/GPU 利用率（70-90% 时 TTFT 已崩），按"分位延迟预算"——TTFT P95 连续 5 分钟超 SLO 的 80% 即触发加槽位/扩容；容量规划按"高峰并发 × KV 占用 × 1.3 余量"备显存，长上下文会话（>16K prompt）单独标记限流，防止单请求吃掉数个槽位。

```python
# TTFT/吞吐容量估算器（纯标准库）
# 基线：Python 3.9+

KV_GB_PER_1K_TOKENS = 0.10   # 示例：7B 模型 FP16 每 1K token KV 占用（近似）


def kv_slots(kv_mem_gb: float, avg_ctx_tokens: int, headroom: float = 1.3) -> int:
    need = avg_ctx_tokens / 1000 * KV_GB_PER_1K_TOKENS * headroom
    return max(1, int(kv_mem_gb // need))


def ttft_ms(queue_ahead: int, prefill_ms_per_req: float = 120,
            decode_interleave_ms: float = 8) -> float:
    """排队 prefill + 前方请求穿插 decode 的近似等待"""
    return queue_ahead * prefill_ms_per_req + queue_ahead * decode_interleave_ms


def main() -> None:
    slots = kv_slots(40, avg_ctx_tokens=8000)  # 40GB KV 显存, 8K 上下文
    print(f"KV 槽位 ≈ {slots}")
    assert 25 < slots < 45
    for ahead in (0, 5, 20):
        print(f"前方{ahead}请求 -> TTFT≈{ttft_ms(ahead):.0f}ms")
    assert ttft_ms(20) > 2000  # 20 个排队即破 1s SLO
    # 长上下文单请求吃掉多倍槽位
    assert kv_slots(40, 8000) > kv_slots(40, 64000)


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 decode 阶段是显存带宽瓶颈而 prefill 是计算瓶颈？
→ 一句话提示：decode 每步只算一个 token 却要读全部权重与 KV（算术强度低，带宽受限）；prefill 一次算整个 prompt（大量矩阵乘，算术强度高），这就是批内混合调度要区分两者的原因。

**追问 2**：分块 prefill（chunked prefill）解决什么？
→ 一句话提示：把长 prompt 的 prefill 切成小块与 decode 交错执行，避免一个长 prefill 阻塞整批 decode 数百毫秒，代价是长请求自身 TTFT 略增。

## 背诵要点
- TTFT = 排队 + prefill（计算瓶颈）；吞吐 = decode（显存带宽瓶颈）；continuous batching 下两者此消彼长。
- 并发槽位 = KV 显存 ÷ (平均上下文 KV × 1.3)，长上下文请求单独标记限流。
- 扩容触发器用 TTFT P95 超 SLO 80% 连续 5 分钟，不用 GPU 利用率（70-90% 时体验已崩）。

## 复盘追问
- 为什么 GPU 利用率不高时 TTFT 也会崩？提示：批内插队与 KV 碎片导致有效槽位低于理论值，看"排队时间分布"而不是利用率。
- 对话与批处理混部在同一集群的替代方案？提示：物理隔离（不同实例/不同权重）+ 低峰时段批处理窗口，混部省的钱会被 P95 延迟违约吃掉。
