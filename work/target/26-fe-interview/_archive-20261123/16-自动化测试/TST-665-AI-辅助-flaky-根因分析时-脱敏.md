---
title: [TST-665] AI 辅助 flaky 根因分析时，脱敏与 prompt 工程怎么做？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-665：AI 辅助 flaky 根因分析时，脱敏与 prompt 工程怎么做？

**答**：
- 结论：日志/堆栈喂给模型前先过脱敏管道，只保留结构信息，敏感值替换为占位符。
- prompt 里明确要求模型输出「根因分类 + 证据行 + 置信度」，并禁止编造。
- 用 few-shot 注入历史已确认的 flaky 案例，提升归因一致性。
- 追问钩子：脱敏把关键字段也抹掉了，模型归因不准，你怎么权衡？

```javascript
function buildFlakyPrompt(failures, redact) {
  const clean = failures.map(f => ({
    error: redact(f.error),
    stack: (f.stack || '').split('\n').slice(0, 8).map(redact),
    env: f.env,
  }));
  return `分析以下失败，输出 JSON {cause,evidence,confidence}。
只允许分类: timing/order/env/assertion/unknown。
失败记录: ${JSON.stringify(clean)}`;
}
```
