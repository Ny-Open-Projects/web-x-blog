---
title: [SCN-1135] IoT 设备的远程调试（设备日志拉取）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1135：IoT 设备的远程调试（设备日志拉取）

**答**：
- 调试：远程拉取设备日志（设备端日志缓冲分页拉取）、实时日志流（调试期）。
- 过滤：日志级别/关键字过滤，时间范围定位。
- 安全：日志可能含敏感信息——脱敏后展示（1113 权限内）。

```javascript
// 远程日志
async function deviceLogs(deviceId, { page = 0, level } = {}) {
  const logs = await api('/device/logs', { deviceId, page, level });
  return { logs: logs.map(l => ({ ...l, msg: redact(l.msg) })),
    nextPage: logs.length === 100 ? page + 1 : null,   // 分页拉取
    stream: () => wsSubscribe(`logs/${deviceId}`) };   // 实时流（调试期）
}
}
```
