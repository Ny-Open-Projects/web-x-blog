---
title: [SCN-923] 政务批量导出（办件列表导出 Excel）的性能
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-923：政务批量导出（办件列表导出 Excel）的性能

**答**：
- 大数据量：导出走异步任务（后台生成 -> 下载链接），前端轮询任务状态。
- 导出列权限：按角色裁剪导出字段（敏感列脱敏）。
- 体验：导出中提示、完成后站内信/下载中心。

```javascript
// 异步导出
async function exportItems(filters) {
  const { taskId } = await api('/export/items', { filters, columns: allowedColumns() });
  return pollExport(taskId);
}
async function pollExport(taskId, { interval = 3000, max = 20 } = {}) {
  for (let i = 0; i < max; i++) {
    const r = await api(`/export/${taskId}`);
    if (r.status === 'done') return download(r.url);
    if (r.status === 'failed') throw new Error(r.reason);
    await sleep(interval);
  }
  notifyLater(taskId);                                // 超时转后台通知
}
```
