---
title: [SCN-1218] AI 对话的消息队列与排队体验（高峰限流）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1218：AI 对话的消息队列与排队体验（高峰限流）

**答**：
- 高峰：模型服务限流（排队返回 429）——前端排队体验（位置/预计等待/自动重试）。
- 降级：高峰切备用模型（用户可见提示）。
- 公平：会话级限频（每会话 N 条/分钟）。

```javascript
// 高峰排队
async function sendWithQueue(payload) {
  let r = await send(payload);
  if (r.status === 429) {
    const { position, retryAfter } = r;
    showQueue(position, retryAfter);
    await sleep(retryAfter * 1000);
    return sendWithQueueFallback(payload);             // 重试或备用模型
  }
  return r;
}
function sendWithQueueFallback(p) { return send({ ...p, model: FALLBACK_MODEL }); }
```
