---
title: [SCN-1121] IoT 设备的命令幂等与防重复执行
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1121：IoT 设备的命令幂等与防重复执行

**答**：
- 问题：网络重试导致指令重复（阀门开两次无害但计数类指令有害）。
- 方案：指令带唯一 cmdId，设备端去重执行（已执行直接回执）；前端重试用同一 cmdId。
- 审计：重复指令上报（网络质量线索）。

```javascript
// 指令幂等
async function idempotentCommand(deviceId, cmd, cmdId = crypto.randomUUID()) {
  const r = await api('/device/command', { deviceId, cmd, cmdId });
  if (r.duplicated) return { ok: true, cached: r.result };   // 设备端去重
  return { ok: r.acked, cmdId };                       // 重试携带同一 cmdId
}
}
```
