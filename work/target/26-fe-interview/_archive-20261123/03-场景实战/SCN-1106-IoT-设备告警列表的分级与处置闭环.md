---
title: [SCN-1106] IoT 设备告警列表的分级与处置闭环
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1106：IoT 设备告警列表的分级与处置闭环

**答**：
- 分级：提示/一般/严重（严重告警电话+短信），处置闭环（确认→处理→恢复验证）。
- 去重：同设备同告警 5 分钟内合并（风暴抑制）。
- 工单：严重告警自动创建工单派发维护人员。

```javascript
// 告警闭环
function alarmPipeline(alarm) {
  const level = classify(alarm);                       // info/warn/critical
  const merged = dedupeAlarm(alarm, { windowMs: 5 * 60_000 });
  if (!merged.new) return { suppressed: true };
  if (level === 'critical')
    return { call: true, ticket: createTicket(alarm) };
  return { notify: ['app', 'sms'], ticket: null };
}
function classify(a) { return a.value > a.critical ? 'critical' : 'warn'; }
function dedupeAlarm(a, o) { return { new: true }; }
function createTicket(a) { return 'TK-1'; }
```
