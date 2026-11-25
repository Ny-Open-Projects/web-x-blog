---
title: [AGT-515] 给开发/客服一个对话调试面板，应该暴露哪些信息？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-515：给开发/客服一个对话调试面板，应该暴露哪些信息

**答**：
- 核心三层：请求层（最终发给模型的 messages/system/tools 快照，含被裁剪了什么）、响应层（usage/finish_reason/工具调用原始序列）、链路层（traceId、各阶段耗时、是否命中缓存/降级）。
- 支持「重放」：用记录的参数原样重发一次，验证问题是否复现；支持对比模式（新旧提示词并排跑）。
- 权限与脱敏：调试面板默认只对内部账号开放，展示前先脱敏用户消息。

```javascript
function buildDebugPanel(turn) {
  return {
    req: turn.requestSnapshot,        // 含 effectiveSystem、被裁剪消息数
    res: { usage: turn.usage, finish: turn.finishReason,
      toolCalls: turn.toolTrace },
    link: { traceId: turn.traceId, timings: turn.timings,
      cache: turn.cacheHit, degraded: turn.degradedFrom },
    actions: ['replay', 'diffPrompt'], // 重放与提示词 diff
  };
}
```

