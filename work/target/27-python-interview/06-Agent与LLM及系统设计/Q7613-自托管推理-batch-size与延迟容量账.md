---
title: [Q7613] 自托管推理 batch size 与延迟的容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7613 · 自托管 GPU 推理 batch size 与延迟/吞吐的容量账

难度：P7 ｜ 标签：容量规划 / GPU 推理 / batch

**问**：自托管 7B 模型服务，单请求 P99 2s。运营要求 QPS 提到 50，方案讨论里出现两种说法："调大 batch size 吞吐线性涨"和"batch 越大延迟越差"。batch 到底怎么调？推理服务的容量账该怎么建？

**答**：
- **结论**：LLM 推理的 batch 与传统 CV 服务不同：**prefill（处理输入）是计算密集，batch 越大 GPU 利用率越高、吞吐近线性涨；decode（逐 token 生成）是访存密集，每步的算力开销被权重加载主导，batch 内多请求几乎"搭车"免费**——所以适度 batching 的 decode 吞吐提升可观。但延迟账要分开看：batch 内所有请求共享每步 decode，**TTFT 由排队 + prefill 决定，吞吐上升后排队增加，P99 TTFT 先慢涨后陡涨**；同时 KV cache 显存是硬约束：`KV 显存 = batch × (上下文长度) × 层数 × 2 × 头数 × 维度 × 2bytes`，batch 上限常常不是算力而是显存。"线性涨"与"延迟越差"都对，拐点在显存上限与延迟 SLA 交叉处。现代推理引擎（vLLM 等）用 continuous batching + PagedAttention 把拐点推得很远——静态 batch 的老账不再适用。
- **取舍**：容量账三约束：① **显存约束**：模型权重 + KV cache 预算（`可用 KV 显存 = 显存 - 权重 - 激活`），由它反推并发 batch 上限；② **延迟约束**：P99 TTFT/TPOT SLA 定排队上限（通过 `max_num_seqs` 控制）；③ **吞吐目标**：`需要 QPS × 平均输出 token / (TPOT × batch)` 校验可达性。方案排序：先开 continuous batching（vLLM/SGLang 基线能力），再调 `max_num_seqs`/`gpu_memory_utilization`，不够再横向加卡（tensor parallel 拆权重是延迟优化，多副本是吞吐优化）；量化（INT8/AWQ）同时减权重与 KV 显存，是性价比最高的第一步。
- **实战**：步骤：① 实测三档 batch（1/8/32）的 TTFT、TPOT、tokens/s，画"吞吐-延迟"曲线找拐点；② 用显存公式算 KV 上限对照实测（`nvidia-smi` + 引擎日志）；③ 压测到 SLA 边界，记录"有效 QPS @ SLA"作为容量基线；④ 上线 autopilot：按队列深度/TTFT 动态扩副本；⑤ 复盘项：容量基线随模型/量化/输入长度分布变化要重测，KV cache 与长上下文输入是隐形的显存杀手。

```python
# 推理容量账：KV 显存约束 + 吞吐-延迟拐点（标准库模拟 vLLM 式参数）
# 基线：Python 3.9+；真实测量 vLLM 0.6+ / SGLang 基准脚本

from dataclasses import dataclass


@dataclass
class GpuPlan:
    vram_gb: float
    weights_gb: float
    activation_gb: float
    layers: int = 32
    kv_heads: int = 8
    head_dim: int = 128
    ctx_len: int = 4096
    kv_dtype_bytes: int = 2

    def kv_bytes_per_seq(self) -> float:
        """KV cache = 2(K+V) × layers × heads × dim × ctx × dtype"""
        return 2 * self.layers * self.kv_heads * self.head_dim * self.ctx_len * self.kv_dtype_bytes

    def max_batch_by_mem(self) -> int:
        avail = (self.vram_gb - self.weights_gb - self.activation_gb) * 1024**3
        return int(avail / self.kv_bytes_per_seq())


def throughput_curve(max_batch: int, tpot_s: float = 0.02, tokens_per_seq: int = 300):
    """decode 吞吐 ≈ batch / TPOT（访存密集段的搭车效应），直到排队陡增"""
    out = []
    for b in (1, 4, 8, 16, 32):
        if b > max_batch:
            break
        tps = b / tpot_s * tokens_per_seq / 60  # tokens/s → 千 token/分 演示口径
        # TTFT 上涨：排队 + prefill 竞争，batch 超 8 后陡增
        ttft = 0.4 + (b ** 1.6) / 40
        out.append((b, tps, ttft))
    return out


def main() -> None:
    gpu = GpuPlan(vram_gb=80, weights_gb=14, activation_gb=2)
    mb = gpu.max_batch_by_mem()
    assert mb > 100, "KV 显存上限应远大于实际 batch（瓶颈在延迟不在显存）"
    print(f"KV 显存上限 batch ≈ {mb}（7B/80G 场景瓶颈通常不是显存）")

    curve = throughput_curve(min(mb, 32))
    best = None
    sla_ttft = 2.0
    for b, tps, ttft in curve:
        flag = "PASS" if ttft <= sla_ttft else "SLA 破"
        print(f"  batch={b:2d}: 吞吐 {tps:6.0f} tok/s, TTFT {ttft:.2f}s {flag}")
        if ttft <= sla_ttft:
            best = (b, tps)
    assert best and best[0] >= 8, "拐点前应能稳定吃到 batch 并发收益"
    print(f"OK: SLA 内有效容量 batch={best[0]}，吞吐 {best[1]:.0f} tok/s —— 容量基线写进发布单")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 decode 阶段"batch 搭车"几乎免费而 prefill 不是？
→ 一句话提示：decode 每步的瓶颈是权重访存带宽，batch 内多个请求共用一次权重加载，算力还有大量富余；prefill 是真实计算密集（整段输入并行算），batch 叠加直接线性加计算量，TTFT 恶化明显。

**追问 2**：continuous batching 和静态 batch 的区别一句话说清？
→ 一句话提示：静态 batch 等齐一批跑完整段再换批（长短请求互相拖尾）；continuous batching 每步解码后动态加入新请求/移除完成请求（配合 PagedAttention 管理碎片化 KV），消灭"拖尾等待"，是吞吐拐点后移的根源。

## 背诵要点
- 容量账三约束：KV 显存（`2×L×H×d×ctx×dtype×batch`）、延迟 SLA（TTFT/TPOT）、吞吐目标；7B/80G 场景瓶颈通常在延迟而非显存。
- decode 搭车效应让 batch 吞吐高收益、prefill 计算密集让 TTFT 恶化；拐点 = SLA 与吞吐曲线交叉，实测三档 batch 画曲线定基线。
- 优化顺序：continuous batching（vLLM/SGLang 基线）→ 量化减 KV/权重 → 调 max_num_seqs → 横向副本（吞吐）vs TP 拆卡（延迟）。

## 复盘追问
- 输入长度分布变化为什么必须重测容量基线？提示：prefill 时间与 KV 显存都随输入长度涨，长上下文用户占比上升会让同一 batch 配置的 TTFT 与显存水位全变——基线要按输入长度分桶记录（P50/P95 输入长度）。
- tensor parallel 与多副本的取舍边界？提示：单卡装不下/单卡延迟超 SLA 才 TP（有通信开销，副本数换延迟）；吞吐不够优先加副本（线性扩、故障域小），TP 是延迟问题的手段不是吞吐问题的首选。
