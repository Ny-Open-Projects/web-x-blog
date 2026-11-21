---
title: [Q373] 时间处理:naive 与 aware、时区转换
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q373 · 时间处理:naive 与 aware、时区转换

> 难度:★★★ | 标签:datetime, 时区, zoneinfo

**问**:什么是 naive datetime?为什么生产代码强烈建议存 UTC?

**答**:naive 是不带 tzinfo 的 datetime,解释它依赖"你以为的时区",跨环境和夏令时会出错;aware 携带 tzinfo 可精确换算。生产规范:①存储与传输一律 UTC(数据库存 UTC 或时间戳);②展示时再转本地时区;③Python 3.9+ 用 `zoneinfo.ZoneInfo` 处理 IANA 时区,能正确处理夏令时;④比较、运算只在同类(最好都 aware)之间做,naive 与 aware 比较 直接抛 TypeError,这是好事。

```python
# file: code/02_并发与网络工程/q373_timezone.py
"""时区处理:naive vs aware、UTC 存储、本地展示。"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

if __name__ == "__main__":
    # 1. 正确方式:创建带时区的 aware 时间
    now_utc = datetime.now(timezone.utc)
    print("UTC   :", now_utc.isoformat())

    # 2. 转上海时区展示,自动处理 +8
    sh = now_utc.astimezone(ZoneInfo("Asia/Shanghai"))
    print("上海  :", sh.isoformat())

    # 3. 夏令时验证:纽约 7 月与 12 月偏移不同
    ny_summer = datetime(2026, 7, 1, 12, tzinfo=ZoneInfo("America/New_York"))
    ny_winter = datetime(2026, 12, 1, 12, tzinfo=ZoneInfo("America/New_York"))
    print("NY 夏令时偏移:", ny_summer.utcoffset(), "冬季:", ny_winter.utcoffset())

    # 4. 危险方式:naive + replace 只改字段不换算,是错误示范
    naive = datetime(2026, 11, 1, 10, 0, 0)
    wrong = naive.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
    correct = naive.replace(tzinfo=ZoneInfo("Asia/Shanghai")).astimezone(timezone.utc)
    print("错误理解:", wrong, "正确换算:", correct)

    # 5. aware 之间才能安全比较与做差
    print("时间差:", now_utc - ny_winter.astimezone(timezone.utc))
```

**追问**:
- `datetime.utcnow()` 为什么被废弃?返回 naive 对象,极易被误当本地时间;改用 `datetime.now(timezone.utc)`。
- pytz 和 zoneinfo 用哪个?新代码用标准库 zoneinfo;pytz 的 localize/normalize 奇异 API 是历史包袱。
