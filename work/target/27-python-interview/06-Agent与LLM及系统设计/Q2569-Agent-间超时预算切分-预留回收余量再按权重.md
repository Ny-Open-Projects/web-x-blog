---
title: [Q2569] Agent 间超时预算切分:预留回收余量再按权重分
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2569 · Agent 间超时预算切分:预留回收余量再按权重分

> 难度:★★★☆ | 标签:Agent, 超时, 并发

**问**:父 Agent 只剩 10 秒,要并行派 5 个子 Agent,时间怎么分才能保证自己不被拖死?

**答**:第一原则是父端先扣预留:回收结果、汇总、异常处置都要时间,这笔钱在分配前先划走,分给子任务的是剩余量。剩余量按预期代价加权,代价重的多拿,但设下限防饿死、上限防一家独大,裁剪后超支再按余量比例收回。子 Agent 拿到的是自己的绝对截止时刻,由父端当前时刻加份额算出并随任务下发,子端自查自己的钟,超时自己负责返回,父端绝不阻塞超过自己的死线。这套切分的关键洞察是:超时问题在分配时就已经决定了结果,运行期的挣扎改变不了预算不足的事实。切分参数要按历史耗时分布校准,权重来自数据不是直觉。

```python
# file: code/06_Agent与LLM及系统设计/q2569_timeout_split.py
"""Q2569 Agent 间超时预算切分:给子 Agent 分时间要留回收余量。

父 Agent 剩余 T 秒要派 N 个子任务:先扣结果回收预留,再按预期
代价加权分配,设下限防饿死、上限防一家独大;子 Agent 拿到的是
自己的绝对截止时刻,超时自己负责,父端绝不被拖过自己的死线。
"""
import time


def split_budget(parent_remaining, weights, floor, cap, reserve):
    usable = parent_remaining - reserve
    assert usable > 0, "父预算扣掉回收预留后为负"
    total_w = sum(weights)
    raw = [usable * w / total_w for w in weights]
    clipped = [min(cap, max(floor, r)) for r in raw]
    if sum(clipped) > usable:  # 上限下限裁剪后若超支,按余量比例收回
        over = sum(clipped) - usable
        room = [c - floor for c in clipped]
        total_room = sum(room)
        if total_room > 0:
            clipped = [c - over * r / total_room for c, r in zip(clipped, room)]
    return [round(c, 3) for c in clipped]


def main():
    budgets = split_budget(parent_remaining=10.0, weights=[4, 3, 1],
                           floor=0.5, cap=6.0, reserve=1.5)
    usable = 8.5
    assert sum(budgets) <= usable + 1e-6, budgets
    assert all(b >= 0.5 for b in budgets), budgets
    assert all(b <= 6.0 for b in budgets), budgets
    now = time.monotonic()
    deadlines = [now + b for b in budgets]
    assert max(deadlines) <= now + 10.0
    extreme = split_budget(10.0, [9, 9, 1], floor=0.5, cap=3.0, reserve=1.5)
    assert all(b <= 3.0 for b in extreme) and sum(extreme) <= 8.5 + 1e-6
    print("常规切分:", budgets, "合计", round(sum(budgets), 3), "预留 1.5s 给回收")
    print("封顶切分:", extreme, "← cap=3 生效,无一家独大")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:某个子任务提前完成了,余量给谁?答:还回父端的公共池,按剩余工作量重分,但每次重分都留痕避免抖动。
- 追问二:子 Agent 内部还要再派孙子怎么办?答:同样的切分规则递归下传,每层扣自己的预留,深度越深每层预算越薄。
