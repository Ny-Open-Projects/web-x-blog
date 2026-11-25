---
title: [SCN-1158] SCADA 大屏的班次交接数据（交接班报表）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1158：SCADA 大屏的班次交接数据（交接班报表）

**答**：
- 交接：班组产量/报警统计/异常事件自动生成交接班报表（一键生成）。
- 签名：交接双方电子签名确认（责任交接）。
- 归档：交接班报表归档（审计可查）。

```javascript
// 交接班报表
function shiftHandover(shift, alarms, production) {
  return {
    shift, production: production.total,
    alarmCount: alarms.length,
    unacked: alarms.filter(a => !a.acked).length,      // 未确认报警交接
    events: alarms.filter(a => a.priority === 'critical'),
    sign: () => dualSign(shift),                       // 双签确认
  };
}
function dualSign(s) { return api('/shift/sign', s); }
```
