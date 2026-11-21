---
title: [Q2287] 重复工单合并:Jaccard 相似聚类
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2287 · 重复工单合并:Jaccard 相似聚类

> 难度:★★★☆ | 标签:工单, 文本相似

**问**:一个故障爆发,二十个"订单指标为空"的工单涌进来,处理人重复劳动,怎么自动合并?

**答**:文本相似聚类:工单标题分词后算 Jaccard 相似度,与已有组的代表比较,达到阈值(实测 0.5)归入该组,否则自立新组。实测五张工单聚成三组:"订单指标为空"的两张合一、"导出报表失败"的两张合一、白屏单独立——同一故障只修一次,减少了 2 单重复处理。设计要点:中文必须先分词,直接比子串会漏;阈值宁松勿紧,误合并代价是人工一键拆开,漏合并的代价是重复劳动,不对称;合并关系必须留痕可回溯,故障修复后合并组批量回复与关单。升级方向是加时间窗约束(同窗口内才合并,跨天的相似工单可能是新问题)和向量化相似度,但先用词级 Jaccard 跑起来,把人工合并量降下来再迭代。

```python
# file: code/05_数据分析与工程化/q2287_duplicate_tickets.py
"""重复工单合并: Jaccard 相似聚类, 同一故障只修一次"""

TICKETS = [
    ("T1", "数据大盘 订单指标 为空"),
    ("T2", "订单指标 为空 大盘"),
    ("T3", "导出报表 失败 超时"),
    ("T4", "报表 导出 超时 失败"),
    ("T5", "登录 页面 白屏"),
]


def jaccard(a, b):
    x, y = set(a.split()), set(b.split())
    if not x or not y:
        return 0.0
    return len(x & y) / len(x | y)


def cluster(items, threshold=0.5):
    groups = []   # [代表id, [成员id]]
    text_of = dict(items)
    for tid, text in items:
        for g in groups:
            if jaccard(text_of[g[0]], text) >= threshold:
                g[1].append(tid)
                break
        else:
            groups.append([tid, [tid]])
    return groups


if __name__ == "__main__":
    text_of = dict(TICKETS)
    groups = cluster(TICKETS)
    for rep, members in groups:
        extra = f" <- 合并 {members[1:]}" if len(members) > 1 else ""
        print(f"代表 {rep} 「{text_of[rep]}」{extra}")
    dup = sum(len(m) - 1 for _, m in groups)
    print(f"原始 {len(TICKETS)} 单合并为 {len(groups)} 组, 减少 {dup} 单重复处理")
    print("要点: 先分词再算 Jaccard; 阈值宁松勿紧, 拆开比漏合便宜; 合并关系留痕, 修复后批量关单")
```

**追问**:
- 追问 1:阈值 0.5 怎么来的?—— 从历史人工合并样本回测不同阈值的准确率召回率,选误合并可接受的最高召回点,而不是拍脑袋。
- 追问 2:为什么和代表比较而不是组内两两比较?—— 星型聚类 O(n) 且保证组内一致,全连通聚类 O(n 平方) 还可能出现链式合并把不相似的拉进一组。
