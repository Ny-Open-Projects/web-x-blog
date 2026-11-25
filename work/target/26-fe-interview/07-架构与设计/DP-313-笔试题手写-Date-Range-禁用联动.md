---
title: [DP-313] 笔试题：手写 Date Range 禁用联动与快捷项？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-313：笔试题：手写 Date Range 禁用联动与快捷项？
**答**：实现 RangePicker 核心逻辑：1) 快捷项（近 7 天/近 30 天/本月）生成区间；2) 禁用联动：选了 start 后，minDate/start 之后禁用（防止 end < start）；3) 跨月选择（翻月保持暂定 start）；4) 输出标准区间（含时区边界：start 00:00 / end 23:59:59.999）。
**评分点**：
- 快捷项生成正确（相对今天，含时区）。
- 暂定态下禁用规则正确（start 之后可选）。
- 暂定 start 的保留跨月。
- 端点时间规范化（00:00 / 23:59:59.999）。
```javascript
function shortcuts(now = new Date()) {
  const day = 86400_000;
  const startOf = d => new Date(d.getFullYear(), d.getMonth(), d.getDate());         // 4) 端点
  const endOf = d => new Date(startOf(d).getTime() + day - 1);
  return {
    last7: [startOf(new Date(now - 6 * day)), endOf(now)],
    last30: [startOf(new Date(now - 29 * day)), endOf(now)],
    thisMonth: [startOf(new Date(now.getFullYear(), now.getMonth(), 1)), endOf(now)],
  };
}
function rangeLogic({ disabledDate, pendingStart }) {
  const isDisabled = (d) => {
    if (disabledDate?.(d)) return true;
    if (pendingStart) return d < startOfDay(pendingStart);   // 2) start 之前禁用
    return false;
  };
  const pick = (d, state) => {
    if (!state.pendingStart) return { pendingStart: d, month: d };         // 3) 翻月保留暂定
    const [a, b] = d < state.pendingStart ? [d, state.pendingStart] : [state.pendingStart, d];
    return { value: [startOfDay(a), endOf(b)], pendingStart: null };
  };
  return { isDisabled, pick, shortcuts };
}
```
