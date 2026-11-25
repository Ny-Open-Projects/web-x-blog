---
title: [AGT-857] AI 生成的测试（单测/E2E）质量参差（浅断言/脆弱选择器），怎么治理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-857：AI 生成的测试（单测/E2E）质量参差（浅断言/脆弱选择器），怎么治理

**答**：
- 质量门禁四查：断言强度（变异测试：AI 测试能否杀掉注入的变异体——浅断言一验就穿）、选择器稳健性（禁用脆弱选择器：nth-child/纯文本定位）、数据独立性（测试不依赖执行顺序与外部状态）、有效性（对空实现跑测试必须失败——防"永绿测试"）。
- AI 测试与人工测试的分工：AI 生成覆盖面（边界/参数化用例），人工写核心场景与验收路径——覆盖交给 AI，正确性判断留给人类。
- 脆弱测试自动退役：flaky 检测对 AI 测试同样适用，连续 flaky 的 AI 测试自动隔离修复。

```javascript
function aiTestGate(tests) {
  return {
    mutationScore: runMutation(tests),             // 浅断言检测
    weakSelectors: tests.flatMap(t =>
      t.selectors.filter(isFragile)),              // nth-child等
    greenOnEmpty: runAgainstStub(tests).passRate > 0.9
      ? '永绿测试：对空实现仍通过' : null,          // 有效性
    flaky: flakyRate(tests) > 0.05 ? 'quarantine' : null,
  };
}
```

