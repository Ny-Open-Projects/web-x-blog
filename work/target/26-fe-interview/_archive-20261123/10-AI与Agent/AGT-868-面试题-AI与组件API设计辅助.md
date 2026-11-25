---
title: [AGT-868] 新组件的 API 设计（props/事件/插槽）用 AI 出草案，如何评审与定稿？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-868：新组件的 API 设计（props/事件/插槽）用 AI 出草案，如何评审与定稿

**答**：
- AI 的价值在「方案广度」：给定需求与设计系统约束，AI 生成 2~3 个 API 方案（受控/非受控、组合式/配置式）+ 各自权衡——人做选择而不是 AI 定案。
- 评审清单（AI 自查+人工复核）：受控/非受控一致性、事件命名约定、泛型与类型友好度、与既有组件 API 的一致性（设计系统内统一心智）。
- 定稿后沉淀：API 设计决策写进组件文档（为什么这样设计），成为下一个组件 AI 生成的上下文——API 设计知识滚雪球。

```javascript
async function designAPI(requirement) {
  const options = await llm.propose(requirement, {
    constraints: DS_API_CONVENTIONS,               // 设计系统约束
    count: 3, require: '每方案附权衡与适用场景',
  });
  const selfChecked = options.map(o =>
    ({ ...o, lint: apiLint(o.definition) }));      // AI自查
  return { options: selfChecked,
    decision: await human.pick(selfChecked),       // 人定案
    record: writeADR(decision) };                  // 沉淀决策
}
```

