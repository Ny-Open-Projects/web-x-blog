---
title: [SCN-1180] SCADA 大屏的生产报表自动生成（班报/日报）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1180：SCADA 大屏的生产报表自动生成（班报/日报）

**答**：
- 生成：班报（产量/能耗/报警/停机）定时自动生成（班次结束触发），推送相关人。
- 审核：报表自动生成 + 人工确认（数据异常人工修正留痕）。
- 导出：报表导出（Excel/PDF），月度汇总。

```javascript
// 班报生成
async function shiftReport(shiftEnd) {
  const data = await collectShiftData(shiftEnd);
  const report = { shift: shiftEnd.id, ...data,
    anomalies: data.alarmCount > 20 ? '报警偏多需说明' : null };
  const reviewed = await operatorConfirm(report);      // 人工确认
  await archive(report, reviewed);
  notifyDistributors(report);
  return report;
}
async function collectShiftData(s) { return { output: 0, energy: 0, alarmCount: 0 }; }
async function operatorConfirm(r) { return true; }
async function archive(r, ok) { return true; }
function notifyDistributors(r) { return true; }
```
