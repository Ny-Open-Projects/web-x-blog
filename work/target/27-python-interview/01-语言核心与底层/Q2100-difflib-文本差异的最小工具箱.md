---
title: [Q2100] difflib:文本差异的最小工具箱
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2100 · difflib:文本差异的最小工具箱

> 难度:★★☆☆☆ | 标签:difflib, 文本比较, 工具

**问**:不引入第三方库,怎么做「相似词推荐」和「配置变更对比」?

**答**:difflib 三件套覆盖大部分文本 diff 需求:get_close_matches(word, candidates, n, cutoff) 做模糊建议——用户把 timeout 拼成 timout,按相似度排序给出候选,CLI 报错提示的经典实现;SequenceMatcher(None, a, b).ratio() 给出 0 到 1 的相似度分,阈值判断用;unified_diff(old, new, fromfile, tofile) 输出标准 unified diff 文本,配置漂移审计、日志变更摘要直接可用。原理上三者都基于 SequenceMatcher 的最长匹配块算法,对顺序敏感,适合行级与词级比较,不适合乱序集合比较(那是 set 运算的活)。纯标准库、零依赖,demo 一段代码演示全部三件。

```python
# file: code/01_语言核心与底层/q2100_difflib_min.py
"""difflib:相似度、模糊建议与统一 diff 的最小工具箱。"""
import difflib

KNOWN = ["timeout", "traceback", "template", "truncate"]


if __name__ == "__main__":
    print("拼写建议:", difflib.get_close_matches("timout", KNOWN, n=2, cutoff=0.6))
    print("相似度比率:", round(difflib.SequenceMatcher(None, "timout", "timeout").ratio(), 3))

    old = ["timeout = 30", "retries = 3", "verbose = False"]
    new = ["timeout = 60", "retries = 3", "verbose = True"]
    diff = difflib.unified_diff(old, new, fromfile="old.conf", tofile="new.conf", lineterm="")
    print("\n".join(diff))
```

**追问**:1) ratio 怎么算的?——基于最长匹配块序列的 2M/T 相似度,对顺序敏感;close_matches 的 cutoff 怎么定?——0.6 起步,候选池越大越保守,避免高频误推荐。2) 工具箱的分工?——Differ 行级 diff、SequenceMatcher 块级相似度、get_close_matches 候选推荐、unified_diff 标准 patch 格式;都是 O(n×m) 级别的通用算法。3) 性能与边界?——autojunk 启发式加速长文档(可能丢匹配);ratio 对「重排」不友好(顺序敏感);中文无空格分词问题。4) 生产陷阱?——拿 difflib 当模糊搜索引擎(它只是编辑距离类工具);候选池上万后 close_matches 慢;autojunk 对短文档反而误删匹配。
