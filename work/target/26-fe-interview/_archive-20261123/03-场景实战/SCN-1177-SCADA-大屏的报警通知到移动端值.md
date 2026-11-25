---
title: [SCN-1177] SCADA 大屏的报警通知到移动端（值班工程师）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1177：SCADA 大屏的报警通知到移动端（值班工程师）

**答**：
- 推送：紧急报警推值班工程师手机（App/电话语音），值班表轮转路由。
- 确认：移动端远程确认（确认前需查看详情，防盲确认）。
- 到场：到场打卡（NFC/定位）关联处理时效。

```javascript
// 移动报警
function mobileAlarmRoute(alarm, oncall) {
  return {
    push: { to: oncall.engineer, channel: ['app', 'voice-call'],
      ack: { requireView: true, timeoutS: 300 } },     // 5 分钟未确认升级
    onSite: () => nfcCheckIn(alarm.deviceId),          // 到场打卡
  };
}
function nfcCheckIn(id) { return true; }
```
