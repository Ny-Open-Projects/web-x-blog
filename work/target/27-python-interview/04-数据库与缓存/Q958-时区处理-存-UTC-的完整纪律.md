---
title: [Q958] 时区处理: 存 UTC 的完整纪律
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q958 · 时区处理: 存 UTC 的完整纪律

> 难度:★★★☆ | 标签:时区, 数据类型

**问**:用户在东京报了订单时间不对,数据层的时区纪律应该怎么建立?

**答**:铁律是"存储统一 UTC,展示按用户时区渲染":库内 timestamp/datetime 一律 UTC(或 epoch),应用内 datetime 对象必须 timezone-aware;Python 的坑在于 naive datetime 的隐式本地化——用 `datetime.now(timezone.utc)` 代替 `datetime.now()`,反序列化统一 `fromisoformat` + 补时区;转换只在展示层 `astimezone(user_tz)`。数据库会话也显式设置时区(MySQL 连接参数 time_zone='+00:00'),避免"库是 UTC、会话却是本地"的错位。比较运算前统一成 aware,naive 与 aware 相减直接 TypeError,这反而是好防线。

```python
# file: code/04_数据库与缓存/q958_timezone.py
"""UTC 存储 + 按用户时区展示的最小闭环"""
from datetime import datetime, timezone, timedelta

def now_utc() -> datetime:
    return datetime.now(timezone.utc)             # 全库统一时区

def to_user_tz(dt: datetime, offset_hours: int) -> str:
    return dt.astimezone(timezone(timedelta(hours=offset_hours))).strftime(
        "%Y-%m-%d %H:%M")

if __name__ == "__main__":
    ts = now_utc()
    print("库存 UTC:", ts.isoformat())
    print("东京用户(+9):", to_user_tz(ts, 9))
    print("北京用户(+8):", to_user_tz(ts, 8))

    try:
        ts - datetime.now()                        # naive 与 aware 相减
    except TypeError as e:
        print("防线生效:", e)

    legacy = datetime(2026, 11, 1, 12, 0)          # 老数据无时区
    print("旧数据按 UTC 补齐:", legacy.replace(tzinfo=timezone.utc).isoformat())
```

**追问**:
- datetime.now() 错在哪?——返回服务器本地时区的 naive 时间,迁移服务器或容器时区后语义漂移,必须 now(timezone.utc)。
- 夏令时怎么处理?——用 zoneinfo(如 Asia/Tokyo 无 DST 但 America/New_York 有)做转换而不是手写固定偏移,固定偏移在 DST 切换日会错一小时。

---
