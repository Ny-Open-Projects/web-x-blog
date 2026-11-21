---
title: [ARC-374] PWA 离线架构如何设计？从"能缓存"到"离线可用"
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-374：PWA 离线架构如何设计？
**答**：
- 离线架构四层：资源离线（SW 缓存 ARC-373）、数据离线（IndexedDB 业务数据 + 快照）、行为离线（写操作本地队列，恢复后重放）、状态一致性（冲突解决协议）。
- 数据同步协议设计：本地记录带 dirty 标记 + 版本号；恢复在线后按序重放，服务端用幂等键去重；冲突时按业务规则合并或提示用户。
- 离线 UI 语义：明确"离线可读/可写/只读"三种模式并在 UI 显式表达（离线徽标、待同步计数），不假装在线。
- 端内 App 与 Web 的差异：小程序/Hybrid 里 SW 受限，需降级为容器级离线包（预下载资源包 + 版本管理），协议要统一设计。
- 测试是难点：离线/弱网/时序组合场景多，用 Playwright 网络条件模拟 + 真机弱网专项。
```javascript
// 离线写队列重放
async function replayQueue() {
  const q = await idb.getAll('outbox');              // {id, op, payload, idempotencyKey}
  for (const item of q) {
    try {
      await api(item.op, item.payload, { 'x-idempotency-key': item.idempotencyKey });
      await idb.delete('outbox', item.id);
    } catch (e) {
      if (isConflict(e)) return resolveConflict(item); // 版本冲突交业务合并
      return scheduleRetry(item);                      // 网络错误退避重试
    }
  }
}
navigator.onLine === true && replayQueue();            // online 事件 + 启动时
```
