---
title: [SCN-1229] AI 应用的多会话并行（多标签页冲突）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1229：AI 应用的多会话并行（多标签页冲突）

**答**：
- 冲突：多标签页同一会话——消息乱序（各页流式并发）。
- 方案：会话锁（单写者：其他页只读+提示）、或消息合并（按 ts 排序去重，BroadcastChannel 同步）。
- 体验：检测其他页活跃（心跳），提示"已在其他窗口打开"。

```javascript
// 多标签会话
function multiTabGuard(sessionId) {
  const bc = new BroadcastChannel(`chat-${sessionId}`);
  bc.onmessage = e => {
    if (e.data.type === 'active') showReadonlyBanner();   // 其他页活跃
  };
  bc.postMessage({ type: 'active', at: Date.now() });
  return { readonly: () => setReadonly(true) };
}
```
