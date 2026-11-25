---
title: [WCN-682] 组件 API 设计如何保持一致？有哪些常见的不一致反模式？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-682：组件 API 设计如何保持一致？有哪些常见的不一致反模式？

**答**：
- 结论：一致性 = 同名同义（所有组件用 variant/size/disabled）+ 同类同构（事件统一 onXxx / ds-xxx）+ 默认值统一（如 size 默认 md）。
- 反模式：同义不同名（一个用 type 一个用 variant）、布尔语义相反（disabled vs enabled）、事件命名风格混用。
- 追问钩子：如何自动检测不一致？用 API schema 汇总 + lint 规则 + 文档站「属性速查表」对比——考察工具化思维。

```javascript
const API_SCHEMA = {
  variant: { type: 'enum', values: ['primary', 'secondary'], desc: '视觉变体' },
  size: { type: 'enum', values: ['sm', 'md', 'lg'], default: 'md' },
  disabled: { type: 'boolean', default: false },
};
function checkApi(props) {
  return props.filter(p => !API_SCHEMA[p]).map(p => `未知/不一致属性: ${p}`);
}
// 反模式：某组件用 type='primary' 而非 variant → 被检出
console.log(checkApi(['variant', 'size', 'type']));
// ['未知/不一致属性: type']
```
