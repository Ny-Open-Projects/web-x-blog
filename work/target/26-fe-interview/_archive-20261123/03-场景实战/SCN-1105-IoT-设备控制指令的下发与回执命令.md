---
title: [SCN-1105] IoT 设备控制指令的下发与回执（命令/影子双通道）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1105：IoT 设备控制指令的下发与回执（命令/影子双通道）

**答**：
- 命令：即时指令（开/关）走命令通道（需设备在线，回执确认）；配置类走影子（desired 期望态）。
- 前端：指令下发按钮状态（设备离线禁用）、回执超时重试（3 次）。
- 一致：影子 desired 与 reported 的 diff 展示（设备是否已同步配置）。

```javascript
// 指令下发
async function sendCommand(deviceId, cmd) {
  if (!isOnline(deviceId)) return { ok: false, reason: '设备离线，走影子配置' };
  const r = await api('/device/command', { deviceId, cmd });
  const ack = await waitAck(r.msgId, { timeout: 5000, retries: 3 });
  return { ok: ack.ok, note: ack.ok ? null : '设备未回执，请检查设备' };
}
function waitAck(msgId, o) { return new Promise(r => setTimeout(() => r({ ok: true }), 100)); }
```
