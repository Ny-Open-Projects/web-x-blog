---
title: [Q2293] Prompt 片段的分层组合与覆盖规则
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2293 · Prompt 片段的分层组合与覆盖规则

> 难度:★★★☆ | 标签:Agent, Prompt, 组合

**问**:system prompt 有全局默认、租户定制、会话临时、请求级微调四层,怎么组合才不会互相打架?

**答**:定死合并顺序与覆盖语义:按 global、tenant、session、request 从低到高逐层合并,同键高层覆盖低层(last-wins),渲染时按固定小节序输出保证可预测。危险的是"谁都能改谁",所以要有锁定键:role 这类身份锚点声明为 locked,低层设过的键高层同值不报错、异值拒绝覆盖并留痕,防止某个请求级补丁把助手身份改没。拒绝必须可观测——被拒的覆盖进 rejected 列表,审计能回答"谁想改什么没改成"。相比把四层拼成一大段文本,键值合并让冲突确定可测,而不是靠模型自己消化矛盾指令。

```python
# file: code/06_Agent与LLM及系统设计/q2293_prompt_layer_merge.py
"""Prompt 片段分层组合:全局 租户 会话 请求四层 last-wins 合并,lock 键禁止被覆盖。"""
SECTION_ORDER = ["role", "tone", "rule", "style"]


def merge_layers(layers, locked_keys=()):
    merged, rejected = {}, []
    for level, frag in layers:
        for k, v in frag.items():
            if k in locked_keys and k in merged and merged[k] != v:
                rejected.append({"key": k, "level": level})
                continue
            merged[k] = v
    return merged, rejected


def render(merged):
    return "\n".join(merged[k] for k in SECTION_ORDER if k in merged)


if __name__ == "__main__":
    merged, rejected = merge_layers([
        ("global", {"role": "你是客服助手", "tone": "正式", "style": "简洁"}),
        ("tenant", {"tone": "亲切"}),
        ("session", {"rule": "只答退货问题"}),
        ("request", {"tone": "夸张", "role": "你是诗人"}),
    ], locked_keys=("role",))
    assert merged["tone"] == "夸张", "未锁键 last-wins 高层覆盖低层"
    assert merged["role"] == "你是客服助手"
    assert rejected == [{"key": "role", "level": "request"}], "锁定键拒绝覆盖并留痕"
    text = render(merged)
    assert text.index("客服助手") < text.index("夸张"), "渲染按固定小节序"
    merged2, rejected2 = merge_layers([("global", {"role": "A"}), ("tenant", {"role": "A"})],
                                      locked_keys=("role",))
    assert rejected2 == [], "同值重复不视为覆盖"
    print("片段组合通过:分层覆盖 锁定拒绝留痕 固定序渲染")
```

**追问**:
- 层级顺序能按租户改吗? 答:不能,顺序是平台语义,可配的应该是各层内容,顺序一变所有冲突判定都会翻转
- 锁定键之外还想全局禁改怎么办? 答:发布审批时把不允许覆盖的键登记进 locked 清单,清单本身走配置变更流程
