---
title: [Q2841] 跨 Agent 委派的最小披露:字段投影与披露台账
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2841 · 跨 Agent 委派的最小披露:字段投影与披露台账

> 难度:★★★☆ | 标签:Agent, 多Agent, 安全

**问**:把任务委派给子 Agent 时,直接把父上下文整包传过去有什么风险?最小披露怎么做才不流于形式?

**答**:整包传递最省事也最危险:内部成本、客户隐私、别家租户的数据全跟着走,子 Agent 一旦被注入或者日志外泄,泄漏面就是整个上下文。最小披露按受派角色声明字段白名单,投影出完成该任务的最小必要集合,给了什么、扣了什么全部写进披露台账。台账是这套机制有牙齿的关键:审计能回答「run_1 到底把客户手机号给过谁」,而不是凭记忆说「应该没给」。白名单按角色配置而不是按调用点散写,新角色上线先过一轮数据分级评审。披露不足导致子任务失败,也比过度披露后再补救便宜得多。

```python
# file: code/06_Agent与LLM及系统设计/q2841_min_disclosure.py
"""Q2841 跨 Agent 委派的最小披露:字段投影与披露台账。

把任务委派给子 Agent 时,把整个上下文原样塞过去是最省事也最危险的:
成本 内部备注 客户隐私全跟着走。正确做法是按受派角色声明字段白名单,
投影出最小必要集合,给了什么 扣了什么全部进披露台账,审计可以复盘。
"""

DISCLOSURE_ALLOW = {
    "brief": ["query", "deadline"],
    "deep": ["query", "corpus_hint", "deadline"],
}


def delegate(to_agent, payload, ledger, run_id):
    """按白名单投影披露内容,并写台账。"""
    allow = DISCLOSURE_ALLOW[to_agent]
    out = {k: payload[k] for k in allow if k in payload}
    withheld = sorted(set(payload) - set(allow))
    ledger.append({
        "run": run_id,
        "to": to_agent,
        "given": sorted(out),
        "withheld": withheld,
    })
    return out


def main():
    payload = {
        "query": "对比两家供应商报价",
        "deadline": "2026-11-07",
        "corpus_hint": "procure_2026",
        "internal_cost": 87.5,          # 内部成本,不该出门
        "customer_phone": "13800001111",  # 隐私,不该出门
    }
    ledger = []
    brief = delegate("brief", payload, ledger, "run_1")
    deep = delegate("deep", payload, ledger, "run_1")
    assert sorted(brief) == ["deadline", "query"], brief
    assert sorted(deep) == ["corpus_hint", "deadline", "query"], deep
    assert "customer_phone" not in brief and "customer_phone" not in deep
    assert ledger[0]["withheld"] == ["corpus_hint", "customer_phone",
                                     "internal_cost"], ledger
    assert ledger[1]["withheld"] == ["customer_phone", "internal_cost"], ledger
    assert ledger[1]["given"] == ["corpus_hint", "deadline", "query"], ledger
    print("brief 子代理拿到:", sorted(brief))
    print("deep 子代理拿到:", sorted(deep))
    print("披露台账:", ledger[0])


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:自由文本里的 PII 怎么办? 答:白名单管结构化字段,文本字段过一遍敏感模式扫描再披露,两层叠加。
- 追问二:子 Agent 还能再委派吗? 答:可以,但白名单只能收窄不能放大,台账里记清父链,越往下可见数据越少。
