---
title: [SCN-1126] IoT 设备控制台的移动端适配（运维人员现场）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1126：IoT 设备控制台的移动端适配（运维人员现场）

**答**：
- 场景：运维现场用手机（扫码定位设备/查看告警/下发指令）。
- 适配：扫码直达设备详情（二维码编码设备 ID）、大按钮控制、现场拍照上传维保。
- 离线：地下室弱网——命令队列（离线缓存下发）。

```javascript
// 移动运维
function fieldOps(scanResult) {
  const device = decodeDeviceQR(scanResult);           // 扫码直达
  return {
    device,
    actions: largeButtons(['重启', '查看告警', '维保记录']),
    offlineCmd: queueCommandOffline,                   // 弱网队列下发
    photo: attachPhotoForTicket,                       // 拍照附工单
  };
}
function decodeDeviceQR(s) { return { id: s }; }
```
