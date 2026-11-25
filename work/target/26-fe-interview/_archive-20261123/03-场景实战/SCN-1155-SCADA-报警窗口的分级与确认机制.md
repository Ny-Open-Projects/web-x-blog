---
title: [SCN-1155] SCADA 报警窗口的分级与确认机制
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1155：SCADA 报警窗口的分级与确认机制

**答**：
- 分级：紧急（红闪+声音）/重要（黄）/一般（白），确认机制（值班员确认+处理备注）。
- 优先级：新报警置顶 + 未确认计数徽标；确认后移入历史区。
- 标准：符合 ISA-18.2 报警管理（优先级合理化，防报警泛滥）。

```javascript
// 报警窗口
function alarmWindow(alarms, acks) {
  const unack = alarms.filter(a => !acks.has(a.id));
  return {
    active: unack.sort((a, b) => b.priority - a.priority || b.at - a.at),
    unackCount: unack.length,
    history: alarms.filter(a => acks.has(a.id)),
    sound: unack.some(a => a.priority === 'critical'),
  };
}
function confirmAlarm(id, note, operator) {
  return api('/alarm/ack', { id, note, operator, at: Date.now() });   // 确认留痕
}
}
```
