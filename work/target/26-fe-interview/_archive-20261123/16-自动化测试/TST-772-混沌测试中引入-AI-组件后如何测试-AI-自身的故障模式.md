---
title: [TST-772] 混沌测试中引入 AI 组件后，如何测试「AI 自身的故障模式」
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-772：混沌测试中引入 AI 组件后，如何测试「AI 自身的故障模式」

**答**：
- 结论：AI 组件有特有故障模式——幻觉、延迟抖动、服务不可用、输出漂移，这些要作为独立故障场景注入验证系统降级。
- 场景：模型超时、返回幻觉内容、置信度骤降、限流拒绝，看前端是否有兜底（缓存答案、降级文案、重试）。
- 断言聚焦「系统行为」而非「模型输出正确性」：是否优雅降级、是否影响核心流程。
- 追问钩子：AI 服务完全不可用，业务是否还能跑核心流程？

```javascript
// 注入 AI 服务超时，验证前端降级
function withAIFallback(aiCall, fallback) {
  try {
    const r = aiCall();
    return r && r.ok ? r.value : fallback();
  } catch {
    return fallback();
  }
}
console.log(withAIFallback(
  () => { throw new Error('AI timeout'); },
  () => '已为您转接人工客服'
));
```
