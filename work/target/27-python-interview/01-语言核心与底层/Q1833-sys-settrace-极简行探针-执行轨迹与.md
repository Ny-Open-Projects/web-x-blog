---
title: [Q1833] sys.settrace 极简行探针:执行轨迹与热点行统计
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1833 · sys.settrace 极简行探针:执行轨迹与热点行统计

> 难度:★★★★☆ | 标签:settrace, 调试, 观测

**问**:Q552 讲了 settrace 原理,用十几行写一个能用的行级探针要抓住哪些事件?

**答**:trace 函数按帧生效:全局 settrace 后每个新帧先收到 call 事件,返回值成为该帧的局部 trace——返回自身继续跟踪、返回 None 停止。极简探针只处理两类事件:call 时返回 probe 以订阅 line;line 时按 (函数名, 行号) 计数。工程细节:① 用 co_filename == __file__ 过滤,只统计本文件,否则标准库与探针自身会淹没数据;② finally 里 settrace(None) 收尾,异常路径也要恢复;③ 开销是每行一次回调,只用于开发期诊断,生产 profiling 走 cProfile 与 sys.setprofile(Q430/Q1286,后者回调次数远少)。demo 对冒泡排序给出热点行:内层比较行次数最高,与算法分析吻合——覆盖统计、简易调试器、教学演示都从这里长出来。

```python
# file: code/01_语言核心与底层/q1833_settrace_probe.py
"""sys.settrace 极简行探针:执行轨迹与热点行统计。"""
import sys
from collections import Counter

HITS = Counter()


def probe(frame, event, arg):
    if event == "call":
        return probe                     # 该帧继续跟踪 line 事件
    if event == "line":
        code = frame.f_code
        if code.co_filename == __file__:
            HITS[(code.co_name, frame.f_lineno)] += 1
        return probe
    return None                          # 返回 None 表示不再跟踪该帧


def bubblesort(xs):
    for i in range(len(xs) - 1):
        for j in range(len(xs) - 1 - i):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs


def run_probe(func, *args):
    sys.settrace(probe)
    try:
        return func(*args)
    finally:
        sys.settrace(None)


def report(top=5):
    for (name, line), n in HITS.most_common(top):
        print("  {:>4} 次  {} 第 {} 行".format(n, name, line))


if __name__ == "__main__":
    result = run_probe(bubblesort, [5, 2, 8, 1])
    print("排序结果:", result)
    print("行级热点 Top5:")
    report()
```

**追问**:1) 想看局部变量的值变化怎么办?——line 事件里读 frame.f_locals 快照,注意 Q1258 的物化成本;热点函数别在探针里做深拷贝。2) 极简行探针的实现要点?——settrace 返回自身进入行级模式;'line' 事件按 (co_name, f_lineno) 计数;返回 None 关闭行级只留调用级;只统计不打印,退出后出报告。3) 成本与边界?——纯 Python 回调数量级放慢(Q552),只限开发期;探针抛异常会被解释器忽略或中断追踪,要自己防御;3.12+ 系统应迁 sys.monitoring。4) 生产陷阱?——生产开行级探针;探针里做 IO;热点函数 f_locals 深拷贝让探针比业务还贵。
