---
title: [AGT-578] 工具失败重试时（网络抖动），前端如何防止重复执行副作用？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-578：工具失败重试时（网络抖动），前端如何防止重复执行副作用

**答**：
- 每次工具调用带唯一 idempotencyKey（turnId + 调用序号），重试复用同一 key，服务端据此幂等——前端 UI 只需把"重试"渲染为同一节点的状态回退而非新节点。
- 重试 UI 状态：节点回到 running 前显示"重试中(第 n 次)"，历史失败原因保留在展开区；超过重试上限后节点锁定为 failed，只能"换个方式继续"（交给 Agent 重新规划）。
- 只读工具可以乐观重试（无副作用），写入类必须走幂等 key，UI 上写入类的重试按钮要延迟出现（防手抖连点）。

```javascript
async function retryToolCall(tc, attempt = tc.attempts + 1) {
  if (attempt > MAX_RETRY(tc.risk)) return lockAsFailed(tc);
  if (tc.sideEffect) await delay(1000);          // 写入类防抖 1s
  markRetrying(tc, attempt);                     // 同节点回退状态
  return api.callTool({ ...tc, idempotencyKey: tc.key }); // 复用 key
}
```

