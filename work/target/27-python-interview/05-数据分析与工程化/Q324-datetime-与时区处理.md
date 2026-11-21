---
title: [Q324] datetime 与时区处理
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q324 · datetime 与时区处理

> 难度:★★★ | 标签:pandas, 时区

**问**:pandas 中如何处理带时区的时间?tz_convert 和 tz_localize 有什么区别?

**答**:tz_localize 给 naive 时间"赋予"时区(不改变表盘时间),tz_convert 在已有时区之间"换算"(改变表盘时间),对 naive 时间直接 tz_convert 会报错。工程要点:入库统一 UTC 存储或 UTC-naive,展示层再转本地时区;跨时区列做差会自动对齐;夏令时切换时用 `ambiguous="NaT"` 或 `nonexistent` 参数显式处理歧义时间。混用 naive 和 aware 列做运算会抛 TypeError,这其实是好事,逼你统一口径。

```python
# file: code/05_数据分析与工程化/q324_datetime_tz.py
try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    ts = pd.Series(pd.to_datetime([
        "2026-01-01 08:00:00", "2026-06-01 08:00:00"]))
    s_utc = ts.dt.tz_localize("UTC")           # 赋予时区
    print(s_utc.dt.tz_convert("Asia/Shanghai").tolist())
    # 混合时区字符串解析:统一到 UTC
    mixed = pd.Series(["2026-01-01 08:00+08:00", "2026-01-01 00:00+00:00"])
    parsed = pd.to_datetime(mixed, format="ISO8601", utc=True)
    print(parsed.tolist())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        from datetime import datetime, timezone, timedelta
        dt = datetime(2026, 1, 1, 8, 0, tzinfo=timezone(timedelta(hours=8)))
        print(dt.astimezone(timezone.utc).isoformat())  # localize/convert 等价
```

**追问**:
- tz_localize 和 tz_convert 混用会怎样?——对 aware 列再 localize 报错、对 naive 直接 convert 报错;这个 TypeError 是提醒,别用 errors 绕过。
- 夏令时切换的歧义时间怎么处理?——`ambiguous='NaT'`(或 bool 数组)与 `nonexistent='shift_forward'` 显式声明策略,默认报错。
- 为什么入库推荐 UTC-naive?——各数据源时区不一,统一转 UTC 后去掉 tz 信息存储,计算最简单;展示层最后 localize。

---
