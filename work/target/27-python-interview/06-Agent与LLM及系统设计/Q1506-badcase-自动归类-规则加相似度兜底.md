---
title: [Q1506] badcase 自动归类:规则加相似度兜底
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1506 · badcase 自动归类:规则加相似度兜底

> 难度:★★★☆ | 标签:RAG, badcase, 运营

**问**:badcase 一天几百条,人工归因跟不上怎么办?

**答**:两级自动归类。规则层先行:检索为空、来源不对、信息过期、格式错误、拒答 这类有明确关键词特征的直接归类,准确且可解释。相似度兜底:规则没接住的,用词面 Jaccard 与每类的典型样本算最近邻,超过阈值归入该类,否则进 other 等人工。输出按类聚合的周报,计数与归因路径都保留,便于评估规则覆盖率的演进。人工只需要处理 other 和抽查各类样本,归类本身成为分类知识库,新样本进来可以增量补充典型样本。注意规则匹配大小写统一,相似度阈值要压着误归类率调。

```python
# file: code/06_Agent与LLM及系统设计/q1506_badcase_classifier.py
"""badcase 自动归类:规则关键词先行,再按词面相似度最近邻兜底,输出分类周报。"""
from collections import Counter


RULES = [
    ("no_result", ["没有找到", "检索为空", "无结果"]),
    ("wrong_source", ["来源不对", "引用错", "答非所问"]),
    ("stale_info", ["过期", "旧版", "去年", "已更新"]),
    ("format_error", ["格式错", "json", "截断", "解析失败"]),
    ("refusal", ["无法回答", "拒绝", "抱歉不能"]),
]

CANON = {
    "no_result": ["查不到该员工的考勤记录", "搜索结果为空集"],
    "wrong_source": ["回答引用了错误的产品线文档"],
    "stale_info": ["价格还是去年的旧版信息", "政策已更新但答案没变"],
}


def tokens(text):
    t = "".join(text.split())
    return {t[i:i + 2] for i in range(len(t) - 1)} | set(t)


def classify(case):
    """先规则后相似度:规则命中直接归;否则取 Jaccard 最高的最近邻,均低则 other。"""
    text = case["question"] + " " + case.get("note", "")
    tl = text.lower()
    for label, kws in RULES:
        if any(k in tl for k in kws):
            return label, "rule"
    ct = tokens(tl)
    best, best_label = 0.0, "other"
    for label, samples in CANON.items():
        for s in samples:
            st = tokens(s)
            j = len(ct & st) / max(1, len(ct | st))
            if j > best:
                best, best_label = j, label
    return (best_label, "similarity") if best >= 0.12 else ("other", "none")


def weekly_report(cases):
    counts = Counter()
    by_route = Counter()
    for c in cases:
        label, route = classify(c)
        counts[label] += 1
        by_route[route] += 1
    return {"top": counts.most_common(), "routes": dict(by_route)}


if __name__ == "__main__":
    cases = [
        {"question": "查询张三考勤 检索为空", "note": "用户不满"},
        {"question": "答案引用了竞品文档 来源不对"},
        {"question": "这个价格还是去年的旧版信息", "note": "价格页"},
        {"question": "返回的 json 解析失败 截断了"},
        {"question": "员工考勤记录查不到 更新后缺失"},          # 相似度兜底归 no_result
        {"question": "界面配色想改成蓝色", "note": "需求建议"},   # other
    ]
    labels = [classify(c)[0] for c in cases]
    assert labels == ["no_result", "wrong_source", "stale_info", "format_error",
                      "no_result", "other"], "规则四条命中 相似度兜底一条 其余 other"
    assert classify(cases[4])[1] == "similarity"

    rep = weekly_report(cases)
    assert dict(rep["top"]) == {"no_result": 2, "wrong_source": 1, "stale_info": 1,
                                "format_error": 1, "other": 1}
    assert rep["routes"] == {"rule": 4, "similarity": 1, "none": 1}
    print("badcase 归类通过:规则 4 条 相似度兜底 1 条 other 1 条 周报计数一致")
```

**追问**:
- 归错类怎么办? 答:把人工修正反馈回写,规则库加反例、样本库换代表,归类器随反馈收敛;
- 和 Q1200 归因什么关系? 答:Q1200 回答错在检索还是生成,本题回答错在哪个类目,一个定位环节一个定位类别,可串联。
