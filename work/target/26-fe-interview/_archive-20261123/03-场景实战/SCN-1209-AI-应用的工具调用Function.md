---
title: [SCN-1209] AI 应用的工具调用（Function Calling）前端渲染
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1209：AI 应用的工具调用（Function Calling）前端渲染

**答**：
- 渲染：工具调用卡片（工具名/参数/执行状态/结果摘要），失败重试。
- 多步：多工具链式调用展示（步骤时间线）。
- 确认：敏感工具（发邮件/付款）执行前人工确认。

```javascript
// 工具调用渲染
function toolCallCard(call) {
  return {
    name: call.name, args: call.args,
    status: call.status,                               // running/done/failed
    result: summarize(call.result),
    confirm: SENSITIVE_TOOLS.has(call.name) && !call.confirmed,
    retry: call.status === 'failed' ? () => retryTool(call.id) : null,
  };
}
const SENSITIVE_TOOLS = new Set(['send_email', 'pay']);
```
