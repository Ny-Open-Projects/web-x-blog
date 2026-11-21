---
title: [Q2040] 分块重叠率实验:召回随 overlap 回升的拐点
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2040 · 分块重叠率实验:召回随 overlap 回升的拐点

> 难度:★★★☆ | 标签:RAG, 切块, 实验

**问**:都说切块要留重叠,重叠到底该留多少?怎么用实验说话而不是拍脑袋?

**答**:把重叠率做成扫描实验:固定块长,扫 overlap 从 0 到接近块长,每组切块、建索引、用关键句集合测完整召回——关键句完整落在某块内才算召回,被切碎即失召回。曲线会清晰呈现拐点:零重叠时跨块边界的句子被腰斩,重叠加大召回单调回升,达到满召回后再加只是白烧存储。选参数的规则是达标的最低重叠率,兼顾召回与成本。演示数据里块长 12 时,重叠 0 和 2 都只有三分之一召回,重叠 4 起满召回,答案就是 4。

```python
# file: code/06_Agent与LLM及系统设计/q2040_overlap_sweep.py
"""分块重叠率实验:扫描不同 overlap,量关键句完整召回率,选收益拐点。"""


def chunk_text(text, size, overlap):
    assert 0 <= overlap < size, "overlap 必须小于块长"
    step = size - overlap
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i + size])
        if i + size >= len(text):
            break
        i += step
    return chunks


def recall_of(chunks, facts):
    """关键句完整落在某个块内才算召回,被切碎即失召回。"""
    hit = 0
    for f in facts:
        if any(f in c for c in chunks):
            hit += 1
    return hit / float(len(facts))


def sweep(text, facts, size, overlaps):
    rows = []
    for ov in overlaps:
        chunks = chunk_text(text, size, ov)
        rows.append({"overlap": ov, "chunks": len(chunks),
                     "recall": recall_of(chunks, facts)})
    return rows


def pick_min_overlap(rows, target=1.0):
    """达标的最小重叠率:召回达标里重叠最小 成本最低的那个。"""
    ok = [r for r in rows if r["recall"] >= target]
    return min(ok, key=lambda r: r["overlap"]) if ok else None


if __name__ == "__main__":
    # 三条关键句各占 9 字首尾相接,块长 12 零重叠会把后两句切碎
    facts = ["无理由退货七日有效", "超重商品收取附加费", "增值税发票电子开具"]
    text = facts[0] + facts[1] + facts[2]
    assert len(text) == 27

    rows = sweep(text, facts, size=12, overlaps=[0, 2, 4, 6, 8])
    assert rows[0]["recall"] == 1.0 / 3.0, "零重叠只有首句完整"
    assert rows[1]["recall"] == 1.0 / 3.0, "重叠 2 仍切在 9 字句中间"
    assert rows[2]["recall"] == 1.0 and rows[4]["recall"] == 1.0
    recalls = [r["recall"] for r in rows]
    assert recalls == sorted(recalls), "重叠加大召回不回退"

    best = pick_min_overlap(rows)
    assert best["overlap"] == 4, "达标的最低重叠率是 4,再高只是白烧存储"

    small = sweep(text, facts, size=8, overlaps=[0])
    assert small[0]["recall"] == 0.0, "块长 8 零重叠时三句全被切碎"
    print("重叠实验通过:召回 1/3→1.0 随重叠回升,最小达标重叠率为 4")
```

**追问**:
- 为什么召回不一定随重叠单调? 答:重叠只影响边界句的存活力,某些切法会有局部波动,实验必须全扫再下结论
- 块长和重叠要联合调吗? 答:要,先扫块长定候选,再在候选上扫重叠,两维网格才是完整实验
