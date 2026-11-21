---
title: [Q1215] 综合设计:多 Agent 研究助手
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1215 · 综合设计:多 Agent 研究助手

> 难度:★★★★ | 标签:综合设计, 架构

**问**:设计一个"给定研究问题,产出带引用报告"的多 Agent 系统,你会怎么搭?

**答**:最小可行架构:规划者(问题拆解为 2-4 个检索式,输出 DAG)、两个检索员(并行跑 RAG 链路:改写→混合检索→rerank→溯源,各自独立上下文防注入扩散)、写作者(聚合两路证据,带 [n] 引用生成报告)、审校者(跑忠实度校验 Q1195 + 覆盖度检查,不通过退回写作或标记缺证据)。全流程套预算(步数/token)与检查点(Q1147),失败可续跑。关键取舍:检索员用相同工具不同视角(一个广度一个深度)保持独立性,聚合才有效;报告必须句句有引用,无来源句直接删。

```python
# file: code/06_Agent与LLM及系统设计/q1215_research_assistant.py
"""研究助手骨架:规划 -> 双检索员 -> 写作 -> 忠实度审校,预算与检查点内建。"""
import hashlib, math


def embed(text, dim=32):
    v = [0.0] * dim
    for tok in text.split():
        v[int(hashlib.md5(tok.encode()).hexdigest(), 16) % dim] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


CORPUS = ["七天无理由退货 运费买家承担", "质量问题退货 运费商家承担", "退款 3 个工作日 到账", "会员退货 免运费 险"]


def retrieve(q, k=2):
    qv = embed(q)
    ranked = sorted(CORPUS, key=lambda d: cosine_v(qv, embed(d)), reverse=True)
    return ranked[:k]


def cosine_v(a, b):
    return sum(x * y for x, y in zip(a, b))


def planner(question):
    """规则桩:拆解为广度+深度两路检索式。"""
    return {"broad": question + " 政策 概览", "deep": question + " 细则 例外"}


def researcher(sub_query, perspective):
    hits = retrieve(sub_query)
    return {"perspective": perspective, "evidence": hits}


def writer(question, evidences, used):
    """聚合证据生成带引用句子;无来源句直接不写。"""
    lines = []
    for i, ev in enumerate(evidences, 1):
        if ev and ev not in used:
            used.add(ev)
            lines.append(f"{ev} [{i}]")
    return " ".join(lines)


def faithfulness_check(report, evidences):
    joined = " ".join(evidences)
    bad = []
    for sent in report.split(" "):
        if "[" in sent or not sent:
            continue
        if not set(sent) & set(joined.replace(" ", "")):
            bad.append(sent)
    return bad


def run(question, budget_steps=6):
    used, steps = set(), 0
    subs = planner(question)
    evs = []
    for name, sub in subs.items():            # 两个检索员并行(此处顺序模拟)
        steps += 1
        assert steps <= budget_steps, "预算熔断"
        evs += [e for e in researcher(sub, name)["evidence"] if e not in evs]
    report = writer(question, evs, used)
    bad = faithfulness_check(report, evs)
    return {"report": report, "evidence_count": len(evs), "unfaithful": bad, "steps": steps}


if __name__ == "__main__":
    out = run("退货政策")
    print("报告:", out["report"])
    print("证据数:", out["evidence_count"], "无据句:", out["unfaithful"], "步数:", out["steps"])
    assert out["evidence_count"] >= 3, "两路检索聚合覆盖多面"
    assert not out["unfaithful"], "报告句必须句句有据"
    assert out["steps"] <= 6
    print("规划-双检索-写作-审校 主链路在预算内闭环")
```

**追问**:
- 两个检索员结果大量重叠怎么办?答:重叠说明问题面窄,规划者根据重叠率收缩为单路;反之高互补时才值得双路,重合率本身是规划反馈信号。
- 报告生成后引用编号怎么稳定?答:证据表在写作前定稿并冻结顺序,引用编号与证据表绑定,审校退回重写时编号表不变,只增不重排。
