---
title: [TST-777] 用 AI 做故障注入后的「UI 降级」验收：LLM-as-judge 的坑
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-777：用 AI 做故障注入后的「UI 降级」验收：LLM-as-judge 的坑

**答**：
- 结论：LLM 判断「降级 UI 是否友好」主观性强，只能做辅助，硬指标（是否有兜底文案、是否可操作）必须用确定性断言。
- 坑：LLM 对「友好」标准不稳定、受措辞影响大、可能忽略关键功能缺失；同一 UI 不同 prompt 结论不同。
- 正确用法：LLM 做初筛与建议，关键结论用 DOM 断言（元素存在、按钮可点、无白屏）兜底。
- 追问钩子：LLM 说降级页「很友好」但实际「重试按钮点不动」，如何避免？

```javascript
// 降级 UI 硬性断言（不可交给 LLM）
function assertDegradedUI(dom) {
  return {
    hasFallbackText: !!dom.querySelector('.fallback-msg'),
    hasRetryButton: !!dom.querySelector('button.retry'),
    noBlankScreen: document.body.innerText.trim().length > 0,
  };
}
const checks = assertDegradedUI({
  querySelector: s => s === '.fallback-msg' ? {} : null,
});
console.log(checks.hasFallbackText, checks.hasRetryButton);
```
