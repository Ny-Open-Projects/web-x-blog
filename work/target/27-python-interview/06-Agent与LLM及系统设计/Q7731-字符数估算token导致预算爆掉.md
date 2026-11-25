---
title: "[Q7731] 用 len(text) 估 token：中文差 1.6 倍，预算在最后一块爆掉"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7731 · 用 len(text) 估 token：中文差 1.6 倍，预算在最后一块爆掉

难度：P6 ｜ 标签：token 估算、上下文预算、BPE、成本对账

基线：Python 3.12；`len()` 数 Unicode 码点；OpenAI 兼容 `usage.prompt_tokens` 回填校准。

**问**：为控成本用 `len(text)` 当 token 数（一个字符算一个 token），超过 8000 就裁剪。英文场景挺准，中文文档一上就翻车：估出来 7000，实际 12000，请求被拒 `maximum context length exceeded`；emoji 更离谱，一个字符算 1 token，实际要 3~4 个。为什么字符数不能当 token？

**答**：
- **结论**：token 是**子词/字节级**切分单位，与"字符数"没有固定比例。经验值：英文约 4 字符/token（`len/4` 才准）；中文一个汉字平均 1.5~2 token，所以"1 字符 = 1 token"仍**低估 1.5~2 倍**，而 `len/4` 会低估 5~6 倍；emoji、罕见字常被拆成 3~4 个字节级 token。`len()` 数的是 Unicode 码点，完全不知道 BPE 怎么合并。
- **取舍**：精确计数要跑目标模型的 tokenizer（tiktoken / transformers），长文本几十毫秒 CPU，且换模型必须换 tokenizer；估算便宜但必须**按字符类别加权**（ASCII、CJK、emoji、其他各给系数）并留 20% 安全余量。生产上通常"估算做准入 + 真实 usage 做对账"。
- **实战**：① 准入用**保守**估算（宁可多裁），出口用 `usage.prompt_tokens` 回填校准系数；② 按 Unicode 区段分类计数：ASCII、CJK（U+4E00–U+9FFF）、emoji（U+1F300+）、其他；③ 上下文预算里为输出预留 `max_tokens`；④ 监控"估算 vs 实际"的偏差分布，P95 偏差 > 20% 告警。

```python
"""按字符类别加权估 token，并用真实 usage 校准系数。"""


def classify(ch: str) -> str:
    code = ord(ch)
    if code < 128:
        return "ascii"
    if 0x4E00 <= code <= 0x9FFF:
        return "cjk"
    if 0x1F300 <= code <= 0x1FAFF or 0x2600 <= code <= 0x27BF:
        return "emoji"
    return "other"


# 初始系数（token / 字符），来自经验值，之后用 usage 校准
WEIGHTS = {"ascii": 0.25, "cjk": 1.6, "emoji": 3.0, "other": 1.0}


def estimate(text: str, weights: dict[str, float] = WEIGHTS) -> float:
    total = 0.0
    for ch in text:
        total += weights[classify(ch)]
    return total


def calibrate(samples: list[tuple[str, int]]) -> dict[str, float]:
    """用真实 usage 反推各类字符的平均 token 密度（最小二乘的简化版）。"""
    sums = {k: 0.0 for k in WEIGHTS}
    chars = {k: 0 for k in WEIGHTS}
    for text, actual in samples:
        est = estimate(text)
        ratio = actual / est if est else 1.0          # 整体缩放比
        for ch in text:
            k = classify(ch)
            sums[k] += ratio * WEIGHTS[k]
            chars[k] += 1
    return {k: (sums[k] / chars[k] if chars[k] else WEIGHTS[k]) for k in WEIGHTS}


if __name__ == "__main__":
    zh = "退款政策说明：订单签收后 7 天内可申请，运费由买家承担。"
    en = "Refund policy: within 7 days after delivery, shipping is on the buyer."
    mix = zh + "\n" + en + "\n🎉 活动期间免运费 🚚"

    naive_zh = len(zh) / 4
    print(f"中文 {len(zh)} 字符 | len/4 估 {naive_zh:.1f} | 加权估 {estimate(zh):.1f}")
    print(f"英文 {len(en)} 字符 | len/4 估 {len(en) / 4:.1f} | 加权估 {estimate(en):.1f}")
    print(f"混排 {len(mix)} 字符 | len/4 估 {len(mix) / 4:.1f} | 加权估 {estimate(mix):.1f}")

    # 模拟"真实 usage"：中文 1.6、英文 0.28、emoji 3.2
    truth = {"ascii": 0.28, "cjk": 1.6, "emoji": 3.2, "other": 1.0}
    samples = [(t, round(estimate(t, truth) + 6)) for t in (zh, en, mix)]   # +6 模拟模板开销
    before = estimate(mix)
    weights2 = calibrate(samples)
    after = estimate(mix, weights2)
    print("校准后权重:", {k: round(v, 2) for k, v in weights2.items()})
    print(f"混排估算 before={before:.1f} after={after:.1f}")

    # 预算闸门
    budget = int(after * 0.8)                        # 只允许用 80% 预算
    print("保守预算:", budget, "| 原文是否超:", estimate(mix, weights2) > budget)

    print("结论：字符数不是 token 数；按类别加权 + usage 校准 + 留余量，三者缺一不可")
```

**追问一**：为什么同一段中文在不同模型上 token 数不同？
→ 解析：词表不同。Qwen/GLM 有更高效的中文词表，一个汉字可能就是一个 token；Llama 系对中文常按字节切，同样的字要 2~3 个 token。换模型必须重测系数，不能把 A 模型的预算直接套到 B 模型。

**追问二**：`max_tokens` 截断和上下文超限有什么区别？
→ 解析：上下文超限是**输入 + 输出**超过模型窗口，请求直接被拒（400）；`max_tokens` 是输出上限，达到后返回 `finish_reason="length"`，内容是**截断但不报错**。前者靠准确预算避免，后者必须检查 `finish_reason`，否则会把半截答案当完整结果落库。
