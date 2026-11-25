---
title: [SCN-1110] IoT 设备的批量控制（同型号批量下发）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1110：IoT 设备的批量控制（同型号批量下发）

**答**：
- 批量：同型号设备批量下发配置/指令（分批限流防指令风暴）。
- 进度：批量任务进度（成功/失败明细导出），失败重试。
- 风险：批量操作二次确认（影响设备数明示）。

```javascript
// 批量下发
async function batchCommand(deviceIds, cmd) {
  const confirmed = await confirmBulk(deviceIds.length);
  if (!confirmed) return null;
  const { taskId } = await api('/device/batch-cmd', { deviceIds, cmd });
  return { taskId, progress: () => pollBatch(taskId) };
}
async function confirmBulk(n) { return true; }
async function pollBatch(id) { return { done: 0, total: 0 }; }
```
