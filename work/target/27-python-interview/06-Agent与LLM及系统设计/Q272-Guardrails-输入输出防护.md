---
title: [Q272] Guardrails 输入输出防护
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q272 · Guardrails 输入输出防护

> 难度:★★★★ | 标签:Agent, 安全

**问**:什么是 Guardrails?输入侧和输出侧分别拦什么?

**答**:Guardrails 是围绕 LLM 的输入输出双向防护层。输入侧拦:Prompt 注入、越狱企图、敏感信息(身份证、密钥)、超出业务范围的请求;输出侧拦:有害内容、违规合规风险、泄露内部信息(PII、密钥)、格式不合格。实现分规则层(正则、关键词,快且便宜)和模型层(轻量分类器/LLM 审核,覆盖面广)。设计要点:护栏动作要分级(拦截/脱敏改写/警告放行),且护栏本身要低延迟、可灰度、可观测,避免成为故障点。

```python
# file: code/06_Agent与LLM及系统设计/q272_guardrails.py
"""双层 Guardrails:规则层拦敏感信息,模型层 stub 判有害,支持脱敏改写。"""
import re

PII_PATTERNS = {
    "手机号": r"1[3-9]\d{9}",
    "身份证": r"\d{17}[\dXx]",
    "密钥": r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,})",
}


class Guardrails:
    def __init__(self, toxicity_classifier=None):
        self.cls = toxicity_classifier or (lambda t: False)  # 默认无害

    def inspect_input(self, text: str) -> tuple[str, str]:
        """返回 (处理后的文本, 动作)。动作: pass / redact / block"""
        if self.cls(text):
            return text, "block"
        redacted = text
        for name, pat in PII_PATTERNS.items():
            redacted = re.sub(pat, f"[{name}已脱敏]", redacted)
        return redacted, "redact" if redacted != text else "pass"

    def inspect_output(self, text: str) -> tuple[str, str]:
        for name, pat in PII_PATTERNS.items():
            if re.search(pat, text):
                return re.sub(pat, f"[{name}已脱敏]", text), "redact"
        return text, "pass"


def fake_toxicity_classifier(text: str) -> bool:
    return "怎么制作危险品" in text


if __name__ == "__main__":
    g = Guardrails(fake_toxicity_classifier)
    cases = ["我的手机号是13812345678,帮我注册",
             "key 是 sk-abcdefghijklmnop1234 请保存",
             "怎么制作危险品"]
    for c in cases:
        out, action = g.inspect_input(c)
        print(f"[输入:{action}] {out}")
    out, action = g.inspect_output("回复:用户邮箱 user@x.com,手机 13900001111")
    print(f"[输出:{action}] {out}")
```

**追问**:
- 护栏动作怎么分级?——拦截(高危)、脱敏改写(PII)、警告放行(低风险);一刀切拦截会把误伤率变可用性问题。
- 护栏自身故障怎么办?——护栏挂了是放行(fail-open)还是阻断(fail-close)按业务风险定;护栏要低延迟,超时策略预定义。
- 模型层护栏的延迟怎么压?——轻量小模型/分类器做初筛,LLM 审核只接可疑样本;串行全量 LLM 审核会把 TTFT 翻倍。
