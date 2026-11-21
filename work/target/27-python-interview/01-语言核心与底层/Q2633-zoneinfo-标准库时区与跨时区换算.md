---
title: [Q2633] zoneinfo:标准库时区与跨时区换算
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2633 · zoneinfo:标准库时区与跨时区换算

> 难度:★★★☆☆ | 标签:zoneinfo, 时区, datetime, 3.9 新特性

**问**:3.9 之前处理时区要装 pytz,现在标准库怎么用?

**答**:`zoneinfo.ZoneInfo("Asia/Shanghai")` 用 IANA 时区名构造 tzinfo 对象,数据源优先系统 tz 数据库(macOS/Linux 自带),Windows 装官方 `tzdata` 包兜底。与 pytz 最大的区别:ZoneInfo 是「正确」的 tzinfo——直接 `datetime.replace(tzinfo=ZoneInfo(...))` 即可,不需要 pytz 的 `localize` 魔法。跨时区换算就是 `astimezone`, aware 时间比较与运算都按绝对时刻进行。两条铁律:naive 与 aware 的 datetime 不可比较,混用会抛 TypeError;跨过 DST 边界做「加小时」运算时,aware datetime 加 timedelta 保持钟面时间,涉及歧义时刻要留意 `fold` 属性,换算到 UTC 再加才符合直觉。

```python
# file: code/01_语言核心与底层/q2633_zoneinfo.py
"""zoneinfo:标准库时区的构造、换算与比较规则。"""
from datetime import datetime
from zoneinfo import ZoneInfo

SH = ZoneInfo("Asia/Shanghai")
NY = ZoneInfo("America/New_York")

if __name__ == "__main__":
    naive = datetime(2026, 1, 15, 9, 0)
    sh = naive.replace(tzinfo=SH)
    ny = sh.astimezone(NY)
    print("上海:", sh, "offset", sh.utcoffset())
    print("纽约:", ny, "offset", ny.utcoffset())

    print("aware 比较按绝对时刻:", sh < datetime(2026, 1, 15, 23, 0, tzinfo=SH))

    try:
        sh < naive
    except TypeError as exc:
        print("naive 与 aware 不可比较:", exc)

    utc = sh.astimezone(ZoneInfo("UTC"))
    print("统一到 UTC 再运算:", utc)
```

**追问**:1) 系统没有 tz 数据时 ZoneInfo 会怎样?——抛 ZoneInfoNotFoundError,官方 tzdata pip 包是最小修复,生产镜像里建议预装。2) 跨时区换算的正解?——aware datetime 的 astimezone 互相转换(Q504);DST 歧义/不存在时间靠 fold 参数;PyTZ 式的 localize 不再需要(zoneinfo 原生 aware)。3) 与 naive 数据的迁移?——存量 naive 数据要按「业务所属时区」补 tzinfo;UTC 存储是正解;zoneinfo 缓存(ZoneInfo 键值缓存)注意测试隔离。4) 生产陷阱?——精简镜像没 tzdata;DST 切换日的本地时间比较;缓存 ZoneInfo 对象被测试污染;用固定 offset 表达时区(忽略 DST)。
