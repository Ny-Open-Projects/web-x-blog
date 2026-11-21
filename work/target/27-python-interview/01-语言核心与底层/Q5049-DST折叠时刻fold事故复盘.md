---
title: [Q5049] DST 折叠时刻 fold 事故复盘
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5049 · DST 折叠时刻 fold 的事故复盘

> 难度:★★★★ | 标签:datetime, zoneinfo, fold, DST, 事故复盘

**问**：一次对美东客户的结算事故：11 月第一个周日凌晨 1:30 生成的账单时间戳"回到了一小时前"。DST 秋季回拨时同一本地时间出现两次，Python 的 `fold` 属性是怎么处理这个歧义的？哪些运算会踩 fold 的坑？如何设计"绝对时间存储 + 本地时间展示"来根治？

**答**：DST 秋季回拨使本地墙上时间出现**歧义**：11 月 3 日 01:30 在 America/New_York 发生两次（EDT -04:00 与 EST -05:00）。PEP 495 的解法是给 aware datetime 增加 `fold` 属性（0=第一次出现，1=第二次），`utcoffset()`/`astimezone()` 按 fold 决定偏移。事故根因通常是三选一：a) 存库用了**本地 naive 时间**，回拨后排序/区间查询错乱；b) 从字符串解析本地时间没带 `%z`/tzinfo，`astimezone(utc)` 时 fold 默认 0，把"第二次的 01:30"当成"第一次"（时间倒回一小时）；c) 用了 `pytz` 的旧姿势（`localize()` vs `normalize()`，pytz 的 fold 支持不完整）。根治架构只有一句话：**存储与计算全部用 UTC aware，本地时间只在展示层渲染**（aware → `astimezone(local)` → 格式化），入库永远是 `datetime.now(timezone.utc)`。fold 相关的运算坑：aware 时间**直接相减**按"同一 fold 假设"算出墙上差而非真实流逝（跨回拨区间差 1 小时），真实流逝要用 `datetime.now()` 取两端 aware 时间减（推荐）或先 `astimezone(utc)` 再减；`timestamp()` 方法对歧义时刻按 fold 给出不同 epoch 值。3.9+ 用 `zoneinfo`（缺 tzdata 时 macOS 系统库可用，Linux 精简容器要装 `tzdata` 包——Q2633 的部署前提）。

```python
# file: code/01_语言核心与底层/q5049_dst_fold.py
from datetime import datetime, timezone, timedelta
try:
    from zoneinfo import ZoneInfo
except ImportError:
    raise SystemExit("需要 3.9+, 或 pip install backports.zoneinfo")

NY = ZoneInfo("America/New_York")

# 1) 歧义时刻: 同一墙上时间出现两次, fold 区分
first = datetime(2024, 11, 3, 1, 30, fold=0, tzinfo=NY)   # EDT  (-04:00)
second = datetime(2024, 11, 3, 1, 30, fold=1, tzinfo=NY)  # EST  (-05:00)
print("fold=0 offset:", first.utcoffset(), "| UTC:", first.astimezone(timezone.utc).isoformat())
print("fold=1 offset:", second.utcoffset(), "| UTC:", second.astimezone(timezone.utc).isoformat())
print("真实间隔:", second.astimezone(timezone.utc) - first.astimezone(timezone.utc), "(1 小时)")

# 2) 事故复现: 直接相减得到墙上差 0, 不是真实流逝
print("直接相减:", second - first, "<- 踩坑: 按 fold 同假设算墙上差")

# 3) 事故根因 b: 解析无时区字符串, fold 默认 0, 回拨把时间倒回 1 小时
naive = datetime(2024, 11, 3, 1, 30)
as_local_second = naive.replace(tzinfo=NY, fold=1)
wrong = naive.replace(tzinfo=NY)                # fold=0
print("默认 fold=0 入库:", wrong.astimezone(timezone.utc).isoformat())
print("真实是第二次出现:", as_local_second.astimezone(timezone.utc).isoformat())

# 4) 根治姿势: 全链路 UTC, 展示层才转本地
now_utc = datetime.now(timezone.utc)
bill = {"stored_utc": now_utc.isoformat(),
        "display_ny": now_utc.astimezone(NY).strftime("%Y-%m-%d %H:%M %Z%z")}
print(bill)

# 5) 区间计算的安全模式: 先转 UTC 再减
start = datetime(2024, 11, 3, 1, 0, tzinfo=NY).astimezone(timezone.utc)
end = datetime(2024, 11, 3, 2, 0, tzinfo=NY).astimezone(timezone.utc)
print("回拨区间真实时长:", end - start, "(2 小时而非墙上 1 小时)")
```

**追问**：1) 春季快进（不存在的时间，如 3 月 2:30）fold 有意义吗？——歧义不存在，fold 无效果；但 `ZoneInfo` 不会报错，`datetime(2024,3,10,2,30,tzinfo=NY)` 会"存在"并映射到 offset 推算的 UTC——校验"本地时间是否真实存在"要自己用 round-trip（`dt.astimezone(utc).astimezone(NY)` 是否回到原值）判断。2) `datetime.now(NY)` 与 `utcnow().replace(tzinfo=NY)` 的区别？——前者正确（按 NY 当前偏移取时刻）；后者把 UTC 时刻的墙上数字硬贴 NY 标签，时间值完全错误，是比 fold 更常见的线上 bug。3) 数据库里存 UTC epoch（int）比 aware datetime 字符串好在哪？——排序/比较免解析、无格式歧义；代价是展示层必须知道目标时区与历史规则（tz 数据版本要随服务更新）。

## 背诵要点
- 秋季回拨同一本地时间出现两次：fold=0/1 区分第一次/第二次，utcoffset/astimezone 按 fold 取偏移。
- aware 时间跨回拨区间直接相减得墙上差（差 1 小时）；真实流逝先 astimezone(utc) 再减。
- 根治：存储与计算全 UTC aware，本地时间只在展示层 astimezone 渲染。

## 复盘追问
- 你的账单系统如何证明"任何时刻区间统计都经得起 DST 切换"？（提示：用回拨日与快进日各构造一组用例，对照 UTC 区间时长）
- tz 数据（IANA 规则变更，如某国取消 DST）升级时，历史数据要不要重算？（提示：历史事件以当时 epoch 为准不重算，未来排程规则按新 tz 数据重推）
