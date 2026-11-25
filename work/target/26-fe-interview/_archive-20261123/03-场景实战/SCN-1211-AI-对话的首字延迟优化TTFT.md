---
title: [SCN-1211] AI 对话的首字延迟优化（TTFT）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1211：AI 对话的首字延迟优化（TTFT）

**答**：
- 优化：TTFT（首 token 时间）——预连接（会话建立提前）、短 system prompt、边缘推理节点。
- 体验：等待期骨架（"思考中"动效）+ 思考过程先行展示（reasoning 模型先出思考）。
- 度量：TTFT P75 与总生成时长分端/分模型统计。

```javascript
// TTFT 优化
async function chatWithTTFT(payload) {
  t0 = performance.now();
  const pre = await prewarmConnection(payload.model);   // 预连接
  const stream = await send(payload);
  return onFirstDelta(() => report({ type: 'ttft',
    ms: performance.now() - t0 }));
}
function prewarmConnection(model) { return Promise.resolve(); }
function onFirstDelta(cb) { return cb(); }
```
