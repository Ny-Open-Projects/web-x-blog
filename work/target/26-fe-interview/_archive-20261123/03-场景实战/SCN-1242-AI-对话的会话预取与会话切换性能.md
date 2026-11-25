---
title: [SCN-1242] AI 对话的会话预取与会话切换性能
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1242：AI 对话的会话预取与会话切换性能

**答**：
- 切换：会话切换性能（历史消息懒加载 + 最近消息缓存预取）。
- 预热：hover 会话列表预取最近 20 条（切换秒开）。
- 内存：切换后上一会话卸载（内存治理，1238 配合）。

```javascript
// 会话切换
async function switchSession(sessionId) {
  const cached = sessionCache.get(sessionId);
  if (cached) return render(cached);                   // 预取命中
  const msgs = await api(`/session/${sessionId}/messages`, { limit: 20 });
  render(msgs);
  sessionCache.set(sessionId, msgs);
  sessionCache.delete(previousSessionId);              // 卸载上一会话
}
```
