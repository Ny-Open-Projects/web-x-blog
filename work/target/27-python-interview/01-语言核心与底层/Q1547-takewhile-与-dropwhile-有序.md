---
title: [Q1547] takewhile 与 dropwhile:有序流的前缀截断
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1547 · takewhile 与 dropwhile:有序流的前缀截断

> 难度:★★★☆☆ | 标签:itertools, 流式, takewhile

**问**:处理「按时间有序」的日志流,要取截止时间前的部分,takewhile 为什么比生成器条件过滤好?它的条件为什么「不可恢复」?

**答**:takewhile(pred, it) 从头消费直到 pred 首次为假,整条停机——它表达「有序流的前缀截断」,利用单调性:条件一旦破坏,后面不可能再满足。与 filter 的本质差异:filter 跳过不合格项继续找,适合无序数据;takewhile 用在已知有序的数据上,一次停机就是答案,语义上还排除了「后面再出现合格项」的错误期待。dropwhile 反向:跳过前缀直到条件首次为假,用于剥离文件头、连续注释。要点:① 迭代器不可回卷,takewhile 停机后底层迭代器已越过边界,被消费的拿不回来;② 惰性、O(前缀长度);③ 与 sorted 流、heapq.merge 的输出天然契合。

```python
# file: code/01_语言核心与底层/q1547_takewhile_prefix.py
from itertools import takewhile, dropwhile

LOG = [
    "09:00 boot ok",
    "09:05 deploy start",
    "09:10 deploy done",
    "09:15 alarm cpu",
    "09:20 alarm mem",
]


def logs_before(deadline):
    """有序流前缀截断:deadline 之前的行。"""
    return list(takewhile(lambda line: line[:5] < deadline, LOG))


def strip_comments(lines):
    """dropwhile 剥离开头连续注释,之后的行全部保留。"""
    return list(dropwhile(lambda line: line.startswith("#"), lines))


if __name__ == "__main__":
    print("before 09:12:")
    for line in logs_before("09:12"):
        print("  ", line)

    src = ["# config", "# generated", "host=db", "# comment inside", "port=5432"]
    print("after dropwhile:", strip_comments(src))

    # 与 filter 的差异:filter 跳过不合格项继续,takewhile 一旦停机就结束
    alarms = [line for line in LOG if "alarm" in line]
    print("filter finds alarms:", alarms)
    print("takewhile stops early:",
          list(takewhile(lambda l: "alarm" not in l, LOG)))

    # 迭代器不可回卷:takewhile 消费过的部分拿不回来
    it = iter(LOG)
    prefix = list(takewhile(lambda l: l < "09:16", it))
    print("prefix size:", len(prefix), "| remaining:", list(it))
```

**追问**:1) takewhile 停机后想「恢复扫描」怎么办?——takewhile 不会把停机后的元素吐回来;需要「分段」语义就自己在循环里管理状态,或用 dropwhile 接力。2) takewhile/dropwhile 的语义边界?——takewhile 取「谓词为真的前缀」,首个 False 即停(不吐回);dropwhile 跳过前缀、False 之后全部保留(含后续重新为真的);两者都是前缀工具,不是过滤器。3) 与 filter 的差别?——filter 全程扫描不短路;takewhile 短路且语义是「有序流的截断」;谓词必须与流的单调性匹配。4) 生产陷阱?——对非单调流用 takewhile(中间 False 后的真数据被吞);把 dropwhile 当过滤器(丢前缀之外的语义误解);停机点吃掉的元素以为还在。
