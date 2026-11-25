---
title: [SCN-1113] IoT 设备的设备证书与安全接入
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1113：IoT 设备的设备证书与安全接入

**答**：
- 安全：设备 X.509 证书接入（一机一证），证书到期预警（提前 30 天）。
- 前端：证书状态列表（即将过期设备筛选），批量换证流程。
- 异常：证书过期设备连接被拒——接入失败原因展示。

```javascript
// 证书管理
function certManagement(certs) {
  const expiring = certs.filter(c =>
    c.expireAt - Date.now() < 30 * 86400_000);
  return {
    expiring: expiring.map(c => ({ device: c.deviceId,
      days: Math.round((c.expireAt - Date.now()) / 86400_000) })),
    renew: (deviceId) => api('/cert/renew', { deviceId }),   // 批量换证
    connectFailReason: 'cert-expired',
  };
}
```
