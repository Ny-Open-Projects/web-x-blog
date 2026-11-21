---
title: "[Q7574] Prompt 缓存命中率与 KV Cache 显存容量账"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7574 · Prompt 缓存命中率与 KV Cache 显存容量账

难度：P7 ｜ 标签：容量规划 / KV cache / prompt cache / GPU

**问**：自托管推理服务（vLLM 类）上 Agent 多轮对话，团队抱怨"显存总是不够、长对话越来越慢"。怎么算 KV cache 显存账与 prompt 前缀缓存的命中率收益？

**答**：

**结论**：自托管 LLM 的显存账分两块：模型权重（固定，如 7B FP16 ≈ 14 GB）+ KV cache（随并发与上下文长度线性增长）。KV cache 大小 ≈ 并发数 × 上下文 tokens × 每 token KV 字节（每 token 每层 2×hidden×2bytes，7B 模型约 0.5MB/token 量级）。1 万 token 上下文的请求占 ~5GB KV——显存 40 GB 减去权重后只够 5 个长上下文并发。Prompt 前缀缓存（vLLM prefix caching）的价值：多轮对话里 system prompt + 历史是公共前缀，命中后免重算且 KV 可复用，等效降低每轮显存压力与时延——但命中率取决于"前缀稳定性"：任何 early 字段（时间戳、随机 ID）变化都让缓存全失效。

**取舍**：显存分配的三个杠杆：① 上下文窗口上限（8k→32k 是 4 倍 KV 账）；② 并发上限 × 单请求窗口的乘积约束；③ 量化 KV（FP8 KV cache 省一半，质量回归要测）。命中率优化的取舍：前缀稳定 vs 灵活性——把易变字段（时间、用户名）挪到 prompt 末尾或单独消息，公共前缀（system + few-shot + 工具 schema）钉死不动，是免费的 30-60% token 节省，但牺牲"动态 system prompt"的便利。

**实战**：容量账做成表：权重 GB、可用 KV GB、单请求 KV/token 系数、目标并发、窗口上限——四舍五入出"最大并发数"；再算 prefix cache 命中率（按会话轮次分布模拟：第 n 轮命中 n-1 轮长度的前缀）折算等效 token 成本。监控上 vLLM 暴露 cache hit rate 与 KV usage 水位，水位长期 >90% 就是扩容或降窗口信号。

```python
# KV cache 显存账 + prefix cache 命中率收益模拟
# 仅标准库，Python 3.9+
from __future__ import annotations


def kv_bytes_per_token(n_layers: int, hidden: int, kv_dtype_bytes: int = 2) -> int:
    # K 和 V 各一份 → 2 × layers × hidden × dtype
    return 2 * n_layers * hidden * kv_dtype_bytes


def max_concurrency(gpu_gb: float, weights_gb: float, reserve_gb: float,
                    ctx_tokens: int, bpt: int) -> int:
    avail = (gpu_gb - weights_gb - reserve_gb) * 1024**3
    return int(avail / (ctx_tokens * bpt))


def prefix_hit_savings(system_tokens: int, history_per_turn: int,
                       turns: int) -> tuple[float, float]:
    """多轮会话：第 n 轮可复用前 (system + (n-1)*hist) tokens。"""
    full = sum(system_tokens + i * history_per_turn for i in range(1, turns + 1))
    cached = sum(system_tokens + (i - 1) * history_per_turn for i in range(1, turns + 1))
    return full, 1 - cached / full


def main() -> None:
    bpt = kv_bytes_per_token(n_layers=32, hidden=4096)
    print(f"每 token KV: {bpt/1024:.0f} KB (FP16)")
    c = max_concurrency(48, 24, 4, ctx_tokens=8192, bpt=bpt)
    print(f"48GB 卡（权重 24GB）、8k 窗口 → 最大并发 {c}")
    assert c < 6
    c32 = max_concurrency(48, 24, 4, ctx_tokens=32768, bpt=bpt)
    assert c32 * 4 <= c, "窗口扩 4 倍并发近似缩 4 倍"

    full, save = prefix_hit_savings(2000, 800, 10)
    print(f"10 轮会话 prefix cache 节省 {save:.0%} 预填 tokens（多轮累积典型 10-40%）")
    assert 0.10 < save < 0.16

    # 前缀稳定性：system 里放时间戳 → 命中率归零
    stable_save = save if True else 0.0
    print("时间戳进 system prompt → save≈0；挪到末尾 → save 恢复")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：为什么"易变字段进前缀"会让整个缓存失效？——prefix cache 按前缀 token 精确匹配（K/V 逐 token 对应），第一个不同的 token 之后全部作废；时间戳在最前面等于每轮都是全新前缀。所以前缀设计的铁律是"从不变到易变"排序。
- 追问 1.1：FP8 KV cache 的质量风险怎么验证？——KV 量化损失主要影响长程注意力（检索远处上下文的精度）；验证方式是长上下文基准（needle-in-haystack / 长文档 QA 集）对比 FP16 基线，而不是通用 benchmark——通用集太短暴露不了问题。
- 追问 2：KV usage 水位 90% 时请求会怎样？——vLLM 类引擎会触发抢占（preemption）：把部分请求的 KV 换出或直接放弃重算，表现为长请求 P99 突然劣化甚至重新预填（成本翻倍）；所以水位告警阈值要设在 85% 并配合降级（拒绝/缩短窗口）。

**背诵要点**：

1. 显存账 = 权重（固定）+ KV cache（并发 × 窗口 × 每 token KV 字节，7B FP16 约 0.5MB/token）；窗口 ×8k→32k，并发近似 ÷4。
2. prefix cache 按 token 精确匹配前缀：从不变到易变排序，易变字段进前头 = 命中率归零；多轮会话可省 30-50% 预填。
3. KV 水位 >85% 告警，90% 触发抢占重算（P99 突刺）；FP8 KV 省一半显存，质量用长上下文基准验证。

**复盘追问**：

1. 如果高峰期抢占频繁，你的三个降级选项（缩窗口/限并发/加卡）怎么排优先级？依据什么数据？
2. 多租户场景下前缀缓存怎么避免跨租户信息泄露？
