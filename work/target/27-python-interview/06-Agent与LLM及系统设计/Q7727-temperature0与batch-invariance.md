---
title: "[Q7727] temperature=0 也不是确定性：batch invariant 的坑"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7727 · temperature=0 也不是确定性：batch invariant 的坑

难度：P7 ｜ 标签：推理、temperature、确定性、continuous batching

基线：Python 3.12；vLLM/TGI 等推理框架；纯 Python 模拟 near-tie logits。

**问**：为了做可复现的回归，把 `temperature=0`、`top_p=1`、固定 seed，认为输出应该逐字一致。结果同一个 prompt 单独请求和混在批量里请求，偶尔差一个 token，后续整段发散；换一台机器又不一样。temperature=0 不是贪心解码吗？为什么还不确定？

**答**：
- **结论**：`temperature=0` 只把采样变成 **argmax**，不保证浮点结果可复现。不确定性来自：① GPU 上 reduce/矩阵乘的**非确定性内核**与浮点累加顺序；② **continuous batching** 让同一请求和不同长度的请求同批，padding/mask 与内核选择（prefill vs decode、不同 tile 配置）改变数值；③ MoE 的专家路由、量化反量化、KV cache 分页都可能引入微小差异。两个 logit 相差 1e-6 时，argmax 就会翻转，后面自回归放大。
- **取舍**：要"逐字可复现"，必须固定**批组成**（单请求、固定 max_tokens）、固定硬件/驱动/框架版本、关闭非确定性内核（如 `torch.use_deterministic_algorithms`，可能降性能），甚至固定 seed 与 sampling 实现。代价是吞吐下降、无法利用动态批处理。多数业务只需要"语义稳定"，不该追求逐字一致；评估应看指标分布而不是 diff 文本。
- **实战**：① 回归基线用**多次采样 + 指标阈值**（准确率/召回/格式合法率），不要 diff 全文；② 需要严格复现时，单请求串行、固定版本、记录完整参数与硬件指纹；③ 对 near-tie 的输出做置信度过滤/二次校验，别让一个 token 翻转决定业务；④ 升级模型/框架后先跑 batch 一致性对比，确认差异量级。

```python
"""near-tie logits：batch 组成带来的 1e-6 抖动足以翻转 argmax。"""


def argmax(logits: list[float]) -> int:
    return max(range(len(logits)), key=lambda i: logits[i])


def decode(logits: list[float], temperature: float = 0.0) -> str:
    # temperature=0 -> 贪心；这里只演示首 token
    idx = argmax(logits) if temperature == 0 else 0
    return ["A", "B", "C"][idx]


if __name__ == "__main__":
    # 单独请求（无 padding）与同批（有 padding）算出的 logits
    single = [2.0000000, 1.9999998, 0.1]
    batched = [2.0000000, 2.0000001, 0.1]   # +3e-7 的数值噪声

    print("单请求 argmax:", decode(single), single)
    print("同批请求 argmax:", decode(batched), batched)
    print("是否一致:", decode(single) == decode(batched))

    # 后续自回归：首 token 不同，整段发散
    first_single = decode(single)
    first_batched = decode(batched)
    print(f"首 token {first_single} vs {first_batched} -> 后续上下文不同，整段发散")
    print("结论：temperature=0 只保证贪心，不保证浮点与批组成不变")
```

**追问一**：为什么 continuous batching 会改变同一请求的计算结果？
→ 解析：动态批处理把不同长度、不同阶段的请求拼在一起，padding 长度、attention mask、矩阵 tile 划分、prefill/decode 内核选择都会随同批请求变化。不同内核的浮点累加顺序不同，结果有 1e-6 级差异；对 near-tie 的 logits，这就够让 argmax 翻转。

**追问二**：固定 seed 能让 LLM 输出完全可复现吗？
→ 解析：seed 只控制**采样随机数**，不控制浮点非确定性、批组成、硬件内核。即使 sampling 完全相同，logits 的微小差异仍会改变 argmax 或采样边界。真正的可复现需要"确定性内核 + 固定批 + 固定版本 + 固定硬件"，成本很高，通常只在审计/评测场景做。
