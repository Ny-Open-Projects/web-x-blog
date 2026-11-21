---
title: [Q7067] pandas 重采样与时区对齐陷阱
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7067 · pandas 重采样与时区对齐陷阱

难度：P6 | 标签：pandas 2.x、resample、时区、数据口径

**问**：按"自然日"汇总订单，报表数和 BI 平台对不上。resample 在时区、桶边界（closed/label）上有哪些口径陷阱？怎么保证和数仓口径一致？

**答**：
- **结论**：三大陷阱：① 时区——UTC 时间戳直接 resample，东八区"前一天 16:00 之后"会被算进 UTC 当天，与业务自然日错位 8 小时；正确顺序是先 `tz_convert("Asia/Shanghai")` 再 resample。② closed/label——`"1D"` 默认 left-closed/left-label，但分钟级聚合的右边界归属、`"W"` 的周起点默认周日，都要显式声明。③ 聚合口径——sum 跳过 NaN、count 数非空值、`size()` 才是行数，三者对"单量"的理解不同。
- **取舍**：在 pandas 里转时区（灵活、口径分散）vs 在数仓里统一物化日表（口径唯一、要等数仓）。生产推荐后者：分析侧只读数仓的"业务日"表，pandas 只做展示层聚合；临时分析必须显式写清时区与边界并在图表标注。
- **实战**：对不上数的最快排查路径：取一个差异日 → 找一条边界样本（本地 00:00 前后的记录）→ 看它被分到哪一天 → 检查原始时间戳是否带 tz（naive 时间戳被 `tz_localize` 还是 `tz_convert` 处理，两者差 8 小时）。DST 切换日的重采样会多/少一小时，国内业务用固定偏移时区可绕开。

```python
import pandas as pd

# 场景：按"自然日"汇总订单金额，但时间戳带 UTC 时区，业务在东八区
ts = pd.to_datetime([
    "2026-01-01 16:00:00",   # 东八区 1 月 2 日 0:00（跨日！）
    "2026-01-01 17:00:00",
    "2026-01-02 01:00:00",   # 东八区 1 月 2 日 9:00
])
df = pd.DataFrame({"amount": [10, 20, 30], "ts": ts.tz_localize("UTC")})

by_utc = df.set_index("ts").resample("1D")["amount"].sum()
by_biz = df.set_index("ts").tz_convert("Asia/Shanghai").resample("1D")["amount"].sum()
print("按 UTC 分日:", {str(k.date()): v for k, v in by_utc.items()})
print("按业务时区分日:", {str(k.date()): v for k, v in by_biz.items()})
assert by_utc.iloc[0] == 30 and by_biz.iloc[0] == 60   # UTC 16:00 已是业务时区 1/2
print("结论：先 tz_convert 到业务时区再 resample，口径才能对上报表")
```

**追问链**：
1. 追问一层：naive 时间戳该用 tz_localize 还是 tz_convert？——localize 是"给无时区时间戳赋予时区"（不移动钟面），convert 是"移动到另一时区表示"；naive 先 localize 后 convert，顺序错就整体平移 8 小时。
2. 追问二层：resample 与 groupby(日期) 的差异？——resample 按时间桶且可补全空桶（缺失日期补 0），groupby 只对已有值分桶；报表要"连续日期轴"时必须 resample 或重索引补齐。

**背诵要点**：
1. 先 tz_convert 业务时区再 resample；naive 用 localize 赋时区。
2. closed/label 默认值要显式化，周口径与 DST 日单独确认。
3. sum/count/size 口径不同；对账先抓边界样本看桶归属。

**复盘追问**：
1. BI 与报表差异稳定在 8 小时边界的一小部分数据，最先检查什么？（原始时间戳时区标注与转换链）
2. 月底最后一天的数据经常少一笔，可能是什么桶边界问题？（月度 resample 的 label 与时区组合导致归属漂移）
