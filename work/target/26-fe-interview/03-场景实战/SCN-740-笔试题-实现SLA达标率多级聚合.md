---
title: [SCN-740] 笔试题——实现 SLA 达标率多级聚合（天→周→月，含部分数据标记）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-740：手写达标率多级聚合

**需求与边界**：
- 输入：天级达标记录 `[{date, ok, total, backfilled}]`；输出周/月达标率 + 数据完整度标记（含补录比例、缺天标注）。
- 边界：① 达标率 = Σok/Σtotal（加权，不是天数平均）；② 缺天（无记录）显示 unknown 不当 0；③ 补录占比 > 30% 标注 lowConfidence。

**答**：
```javascript
function aggregateSLA(days, level = 'week') {
  const groups = groupBy(days, (d) => periodKey(d.date, level));   // 周/月 key
  return Object.entries(groups).map(([key, list]) => {
    const ok = list.reduce((s, d) => s + d.ok, 0);
    const total = list.reduce((s, d) => s + d.total, 0);
    const backfilledDays = list.filter(d => d.backfilled).length;
    const missingDays = expectedPeriodDays(key, level) - list.length;   // 缺天
    return {
      key,
      rate: total ? ok / total : null,               // 无数据 = null（unknown）
      missingDays,                                    // 缺天 ≠ 0
      backfillRatio: backfilledDays / list.length,
      lowConfidence: backfilledDays / list.length > 0.3,
    };
  });
}
function periodKey(dateStr, level) {
  const d = new Date(dateStr);
  return level === 'week'
    ? `W${isoWeek(d)}-${d.getUTCFullYear()}`
    : dateStr.slice(0, 7);
}
// 注意：绝不用 mean(list.map(d => d.ok / d.total)) —— 天数平均对低流量天权重过高
```

**评分点**:
- 加权达标率（Σok/Σtotal）而非天数平均。
- 缺天显式 unknown（null），与零区分。
- 补录占比置信标注（>30% lowConfidence）。
- 周/月 key 计算含 ISO 周。
