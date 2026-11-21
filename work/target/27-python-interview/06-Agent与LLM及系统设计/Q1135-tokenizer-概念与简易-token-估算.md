---
title: [Q1135] tokenizer 概念与简易 token 估算器
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1135 · tokenizer 概念与简易 token 估算器

> 难度:★★★☆ | 标签:tokenizer, 成本

**问**:面试常问 token 是什么,不装 SDK 能不能估 token?怎么估?

**答**:token 是模型词表里的最小单位,英文约 1 token ≈ 0.75 个单词,中文约 1 个汉字对应 0.5~1 个 token(BPE 切分后波动大)。没有 tokenizer 时用启发式估算:中文按字符数 ×1,英文按"词数 ×1.3",标点与空白单独计入,再留 10% 安全余量。估算器用于预算控制与费用预估,精度要求 ±20% 即可;计费、上下文裁剪等关键路径仍应以真实 tokenizer 或 API 返回的 usage 为准。

```python
# file: code/06_Agent与LLM及系统设计/q1135_token_estimator.py
"""启发式 token 估算器:中文按字、英文按词,带安全余量,用于预算控制。"""
import re


def estimate_tokens(text: str, margin: float = 0.1) -> int:
    if not text:
        return 0
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))            # 中文字符
    no_cjk = re.sub(r"[\u4e00-\u9fff]", " ", text)
    words = len(re.findall(r"[A-Za-z0-9]+", no_cjk))           # 英文词/数字串
    punct = len(re.findall(r"[^\s\w\u4e00-\u9fff]", no_cjk))   # 标点符号
    raw = cjk * 1.0 + words * 1.3 + punct * 0.5
    return int(raw * (1 + margin))


if __name__ == "__main__":
    cases = [
        ("你好,世界", 6),
        ("hello world foo", 6),
        ("混合文本 mixed 123!", 12),
    ]
    for text, upper in cases:
        est = estimate_tokens(text)
        print(f"{text!r} -> 估算 {est} tokens")
        assert est <= max(upper + 6, 10), "估算严重偏大"
    long_text = "这是一个用于回归测试的较长中文句子。" * 50
    est = estimate_tokens(long_text)
    print(f"长文本 {len(long_text)} 字符 -> 估算 {est} tokens")
    assert 0.5 <= est / len(long_text) <= 1.6, "比例失真"
    print("估算器通过")
```

**追问**:
- 为什么不直接用 `len(text)`?答:英文按字符估会偏差 4 倍以上,中英混合文本必须分语言类别统计。
- 上下文裁剪为什么不能只依赖估算器?答:裁剪过头会丢关键上下文,应在估算器之上留真实 tokenizer 的最终校验或依赖 API usage 回报做反馈修正。
