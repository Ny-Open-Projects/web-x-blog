---
title: [Q1065] Top-N 路径分析
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1065 · Top-N 路径分析

> 难度:★★★☆ | 标签:分析, 路径

**问**:想看用户在支付页前后都去了哪些页面,Top-N 转移路径怎么实现?

**答**:把每个用户的事件按时间排序,统计相邻事件的转移对 `(前一步 -> 后一步)` 的计数,再按计数取 Top-N,就能得到主要流转路径,画成桑基图展示。要点:先做会话切分(30 分钟无操作切断),跨会话的转移没有业务意义;循环路径(首页->列表->首页)按对保留,不强行去环;页面层级多时可先归并到业务大类,避免长尾稀释。深度路径用 2 跳以上 n-gram,但要注意组合爆炸,按会话长度截断。

```python
# file: code/05_数据分析与工程化/q1065_top_paths.py
from collections import Counter, defaultdict

events = [
    ("u1", "home"), ("u1", "list"), ("u1", "item"), ("u1", "pay"),
    ("u2", "home"), ("u2", "list"), ("u2", "home"), ("u2", "list"), ("u2", "pay"),
    ("u3", "list"), ("u3", "item"),
]
by_user = defaultdict(list)
for user, page in events:
    by_user[user].append(page)

transitions = Counter()
for seq in by_user.values():
    for a, b in zip(seq, seq[1:]):
        transitions[f"{a}->{b}"] += 1

for path, cnt in transitions.most_common(5):
    print(path, cnt)
print("转移对计数即路径骨架,可直接渲染桑基图")
```

**追问**:
- 追问 1:为什么先切会话?—— 用户次日再来的跳转与上次浏览无关,跨会话转移会污染路径语义。
- 追问 2:桑基图节点层级怎么定?—— 按转移深度分层,每层取 Top-K 节点,其余并入 other 防止图爆炸。
