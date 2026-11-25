---
title: [SCN-1172] SCADA 大屏的报警声音设计与人员响应
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1172：SCADA 大屏的报警声音设计与人员响应

**答**：
- 声音：分级报警音（紧急连续音/重要间歇音），音量可调（车间噪声大）。
- 响应：报警响应超时升级（班组长→主任），响应记录（MTTA）。
- 静音：静音权限管理（不可随意静音，静音需确认原因）。

```javascript
// 报警声音
function alarmSound(alarm, noise) {
  const vol = noise > 70 ? 1.0 : 0.7;                  // 车间噪声适配
  return {
    pattern: alarm.priority === 'critical' ? 'continuous' : 'beep',
    volume: vol,
    mute: muteWithReason(alarm),                       // 静音需原因
    mtta: trackResponse(alarm),
  };
}
function muteWithReason(a) { return { requireReason: true }; }
function trackResponse(a) { return 0; }
```
