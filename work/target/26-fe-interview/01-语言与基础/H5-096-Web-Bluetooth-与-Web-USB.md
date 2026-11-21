---
title: [H5-096] Web Bluetooth 与 Web USB 的模型是什么？能用来做什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-096：Web Bluetooth 与 Web USB 的模型是什么？能用来做什么？
**答**：
- 共同模式：**用户手势触发选择器**（浏览器弹设备选择框）→ 连接 → 通过 GATT（蓝牙）或接口/端点（USB）读写。
- Bluetooth：`navigator.bluetooth.requestDevice({ filters })` 按服务/名称过滤 → `server.getPrimaryService(uuid)` → `getCharacteristic` → `readValue/writeValue`；适合手环、心率带、打印机、智能灯。
- USB：`navigator.usb.requestDevice({ filters })` → `open()` → `selectConfiguration` → `claimInterface` → `transferIn/Out`；适合硬件调试工具、读卡器。
- 共同限制：仅安全上下文、需 HTTPS、Chrome/Edge 系为主；iframe 需 `allow="bluetooth; usb"`；BLE 写入有 MTU 限制需分包。
- 全部操作都需要用户在场，页面刷新后设备句柄失效需重新选择（权限不可持久化到无手势流程）。

```javascript
// Web Bluetooth：读取心率
async function readHeartRate() {
  // 1) 用户手势中选择设备（浏览器弹窗，用户确认）
  const device = await navigator.bluetooth.requestDevice({
    filters: [{ services: ['heart_rate'] }],
  });

  // 2) 连接 GATT 服务器
  const server = await device.gatt.connect();
  const service = await server.getPrimaryService('heart_rate');
  const char = await service.getCharacteristic('heart_rate_measurement');

  // 3) 订阅通知：心率实时推送
  await char.startNotifications();
  char.addEventListener('characteristicvaluechanged', (e) => {
    const dv = e.target.value;             // DataView
    const flags = dv.getUint8(0);
    const bpm = flags & 1 ? dv.getUint16(1, true) : dv.getUint8(1);
    document.getElementById('bpm').textContent = bpm;
  });

  device.addEventListener('gattserverdisconnected', () => reconnect(device));
}

// Web USB：自定义硬件通信骨架
async function usbTalk() {
  const device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x1234 }] });
  await device.open();
  await device.selectConfiguration(1);
  await device.claimInterface(0);

  await device.transferOut(1, new Uint8Array([0x01, 0x02]));   // 写端点
  const { data } = await device.transferIn(1, 64);              // 读端点
  console.log('收到：', new Uint8Array(data.buffer));
}
```
