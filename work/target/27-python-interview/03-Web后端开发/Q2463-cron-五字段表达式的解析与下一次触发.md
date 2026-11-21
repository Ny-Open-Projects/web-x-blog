---
title: [Q2463] cron 五字段表达式的解析与下一次触发
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2463 · cron 五字段表达式的解析与下一次触发

> 难度:★★★★ | 标签:cron, 调度, 时间计算

**问**:手写 cron 表达式的下一次触发计算,哪些语义最容易踩坑?

**答**:两个著名坑:第一,星期字段用 0 到 6 且 0 是周日,与 Python weekday 的周一为零相差一天,换算公式是 (weekday + 1) % 7;第二,日 dom 与星期 dow 都受限时是"或"语义——0 0 13 * 5 表示 13 日或每个周五都触发,而不是同时满足,这是 POSIX cron 的规定,直觉在这里是错的。解析层支持 *、列表、区间、步进,先做字段越界校验再进集合。计算层用三级跳跃代替逐分钟扫描:月不匹配跳到下月一号,日不匹配跳到次日零点,时不匹配跳到下一整点,只有分钟级才逐分钟走,一年内的搜索压到毫秒级;循环上限护栏防止空表达式死循环。这套计算是自研调度器与"任务错过补偿"判断的基础。

```python
# file: code/03_Web后端开发/q2463_cron_next_fire.py
"""cron 五字段表达式的解析与下一次触发计算(纯标准库)。"""
from datetime import datetime, timedelta

# 字段名, 下界, 上界
FIELDS = [("minute", 0, 59), ("hour", 0, 23), ("dom", 1, 31),
          ("month", 1, 12), ("dow", 0, 6)]


def parse_field(expr, lo, hi):
    """支持 * 列表 区间 步进, 返回合法值集合。"""
    values = set()
    for part in expr.split(","):
        part = part.strip()
        step = 1
        if "/" in part:
            part, _, step_s = part.partition("/")
            step = max(int(step_s), 1)
        if part in ("*", ""):
            start, end = lo, hi
        elif "-" in part:
            a, _, b = part.partition("-")
            start, end = int(a), int(b)
        else:
            start = end = int(part)
        if start < lo or end > hi or start > end:
            raise ValueError("字段越界: {} in [{},{}]".format(part, lo, hi))
        values.update(range(start, end + 1, step))
    return values


def parse_cron(expr):
    parts = expr.split()
    if len(parts) != 5:
        raise ValueError("cron 需要 5 个字段: 分 时 日 月 周")
    return tuple(parse_field(p, lo, hi) for p, (_, lo, hi) in zip(parts, FIELDS))


def cron_dow(dt):
    """cron 的星期惯例: 0=周日, Python 的 weekday 是周一=0。"""
    return (dt.weekday() + 1) % 7


def _day_ok(dt, fields):
    """日与周的裁决: 都受限时取或, 这是 cron 的经典语义。"""
    _, _, dom, _, dow = fields
    dom_free = dom == set(range(1, 32))
    dow_free = dow == set(range(7))
    if dom_free and dow_free:
        return True
    if dom_free:
        return cron_dow(dt) in dow
    if dow_free:
        return dt.day in dom
    return dt.day in dom or cron_dow(dt) in dow


def matches(dt, fields):
    return (dt.minute in fields[0] and dt.hour in fields[1]
            and dt.month in fields[3] and _day_ok(dt, fields))


def next_fire(expr, after):
    """从 after 之后向下寻找, 用月 日 时的跳跃避免逐分钟扫五年。"""
    fields = parse_cron(expr)
    dt = (after + timedelta(minutes=1)).replace(second=0, microsecond=0)
    for _ in range(200000):
        if dt.month not in fields[3]:
            year, month = (dt.year + 1, 1) if dt.month == 12 else (dt.year, dt.month + 1)
            dt = dt.replace(year=year, month=month, day=1, hour=0, minute=0)
            continue
        if not _day_ok(dt, fields):
            dt = (dt + timedelta(days=1)).replace(hour=0, minute=0)
            continue
        if dt.hour not in fields[1]:
            dt = (dt + timedelta(hours=1)).replace(minute=0)
            continue
        if dt.minute not in fields[0]:
            dt = dt + timedelta(minutes=1)
            continue
        return dt
    raise RuntimeError("未能找到触发时刻")


f = parse_cron("0 0 13 * 5")                     # 13 日或周五 都触发
assert matches(datetime(2026, 11, 13, 0, 0), f)  # 13 日命中
assert matches(datetime(2026, 11, 6, 0, 0), f)   # 周五命中
assert not matches(datetime(2026, 11, 12, 0, 0), f)
print("或语义: 0 0 13 * 5 在 13 日与每个周五都触发, 其余日期不触发")

cases = [
    ("*/15 * * * *", datetime(2026, 11, 5, 10, 7), datetime(2026, 11, 5, 10, 15)),
    ("30 3 * * *", datetime(2026, 11, 5, 10, 7), datetime(2026, 11, 6, 3, 30)),
    ("0 9 * * 1-5", datetime(2026, 11, 6, 17, 0), datetime(2026, 11, 9, 9, 0)),
    ("0 0 1 * *", datetime(2026, 11, 5, 10, 7), datetime(2026, 12, 1, 0, 0)),
]
for expr, after, expect in cases:
    got = next_fire(expr, after)
    print("{:12s} after {} -> {}".format(expr, after, got))
    assert got == expect, (expr, got, expect)

try:
    parse_field("61", 0, 59)
except ValueError as exc:
    print("越界校验 ->", exc)
print("要点: 解析层先做越界校验, 计算层用月日时三级跳跃代替逐分钟扫描; "
      "dom 与 dow 都受限取或是 cron 最著名的反直觉语义")
```

**追问**:
- 任务错过的触发要不要补跑?——按业务定:报表类补跑,告警类作废并记录 missed,调度器要显式提供 catch_up 开关。
- 夏令时切换对 cron 的影响?——2:30 这类时刻可能不存在或出现两次,生产调度器多用 UTC 存储或明确跳过策略。
