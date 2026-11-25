---
title: "[Q6736] DATETIME 存的是墙上时间：容器跑 UTC，DBA 看到差 8 小时"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6736 · DATETIME 存的是墙上时间：容器跑 UTC，DBA 看到差 8 小时

难度：P7 ｜ 标签：MySQL、DATETIME/TIMESTAMP、naive/aware、time_zone

基线：Python 3.12；MySQL 8.0 `DATETIME` / `TIMESTAMP`；`datetime.timezone` 固定偏移。

**问**：应用容器是 UTC，代码用 `datetime.now()`（naive）写进 MySQL `DATETIME` 列。DBA 在 CST 的客户端里看到的时间比实际早 8 小时。换成 `TIMESTAMP` 列后，同样的代码又变成"写进去 UTC、读出来按会话时区转"。同一份代码两种列类型结果不同，到底谁在转？

**答**：
- **结论**：`DATETIME` **不带时区**，MySQL 原样存取你给的"墙上时间"，一个字节都不转换；`TIMESTAMP` 内部存 UTC 秒数，写入时按会话 `time_zone` 转成 UTC，读出时再转回会话时区。Python 的 `datetime.now()` 返回 naive（无 tzinfo），驱动按字面值发送 —— 容器 UTC 下写进去的就是 UTC 墙上时间，人按 CST 读，差 8 小时。夏令时地区更糟：naive 时间在切换点会重复或凭空消失一小时。
- **取舍**：全链路 UTC 是主流。`TIMESTAMP` 自带转换、语义明确，但有 2038 上限（4 字节有符号秒），且**同一行不同时区的会话看到不同值**，排障时容易互相怀疑。`DATETIME` 无转换、范围到 9999，但"是不是 UTC"完全靠约定，一旦有人用 `now()` 就前功尽弃。
- **实战**：① 写入一律 `datetime.now(timezone.utc)`（aware），存 `DATETIME` 前显式 `astimezone(utc).replace(tzinfo=None)`；② 存 `TIMESTAMP` 则在连接初始化执行 `SET time_zone = '+00:00'`，让驱动与库都按 UTC 说话；③ 展示层再转本地时区，库里不存本地时间；④ 测试覆盖"跨日/跨时区/DST 切换"三个边界。

```python
"""DATETIME（无时区）与 TIMESTAMP（按会话时区转换）的差异。"""
from datetime import datetime, timedelta, timezone

UTC = timezone.utc
CST = timezone(timedelta(hours=8))


def write_datetime(app_tz: timezone, instant: datetime) -> datetime:
    """DATETIME 列：容器时钟是 app_tz，now() 给出该时区墙上时间，原样落库。"""
    return instant.astimezone(app_tz).replace(tzinfo=None)


def write_timestamp(instant: datetime, session_tz: timezone) -> datetime:
    """TIMESTAMP 列：先按会话时区解释，再统一转 UTC 存秒。"""
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=session_tz)   # 驱动就是这样"猜"的
    return instant.astimezone(UTC)


def read_timestamp(stored_utc: datetime, session_tz: timezone) -> datetime:
    return stored_utc.astimezone(session_tz)


if __name__ == "__main__":
    real = datetime(2026, 11, 24, 18, 33, 5, tzinfo=CST)   # 真实本地时刻
    print("真实时刻:", real.isoformat(), "=", real.astimezone(UTC).isoformat())

    # 1) 两个容器时区不同，DATETIME 列里落下两个不同的字面量
    a = write_datetime(UTC, real)      # 容器 TZ=UTC 的实例写入
    b = write_datetime(CST, real)      # 容器 TZ=Asia/Shanghai 的实例写入
    print("UTC 容器写 DATETIME:", a)
    print("CST 容器写 DATETIME:", b, "-> 同一时刻，两个值相差 8 小时")
    print("  列里混两种语义，任何按时间排序/聚合都会错乱")

    # 2) 规范写法：统一按 UTC 落库，读侧再转
    canon = write_datetime(UTC, real)
    print("规范存 UTC:", canon, "| 展示时转 CST:",
          canon.replace(tzinfo=UTC).astimezone(CST).strftime("%m-%d %H:%M"))

    # 3) TIMESTAMP：无论哪个会话写入，内部只有一个 UTC 值
    ts_a = write_timestamp(real, UTC)
    ts_b = write_timestamp(real, CST)
    print("TIMESTAMP 两路写入:", ts_a.isoformat(), ts_b.isoformat(),
          "| 相同:", ts_a == ts_b)
    print("  UTC 会话读:", read_timestamp(ts_a, UTC).strftime("%m-%d %H:%M"))
    print("  CST 会话读:", read_timestamp(ts_a, CST).strftime("%m-%d %H:%M"))

    # 4) naive/aware 混算会炸
    try:
        real - canon
    except TypeError as e:
        print("混算:", e)

    print("结论：DATETIME 不转换、语义靠约定；TIMESTAMP 按会话时区转，必须钉死 time_zone")
```

**追问一**：`datetime.now()` 和 `datetime.utcnow()` 有什么区别？
→ 解析：两者都返回 naive。`now()` 用系统本地时区，`utcnow()` 返回 UTC 墙上时间但 `tzinfo=None`，所以两者直接相减会得到错误差值且不报错——这是最阴的一类 bug。3.12 起 `utcnow()` 已弃用，正确写法是 `datetime.now(timezone.utc)`。

**追问二**：为什么 `TIMESTAMP` 会在 2038 年溢出？
→ 解析：内部是 4 字节有符号整数存 Unix 秒，上限 2147483647，对应 2038-01-19 03:14:07 UTC。MySQL 8.0.28+ 对部分场景放宽，但为长期可维护，业务时间列优先 `DATETIME` + 应用层统一 UTC。
