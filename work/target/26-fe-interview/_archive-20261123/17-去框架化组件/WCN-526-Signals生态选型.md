---
title: [WCN-526] Signals 生态生产选型：Solid / Preact / Vue / TC39 polyfill 如何按「迁移成本 × 性能 × 生态成熟度」权衡？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-526：Signals 生态生产选型：Solid / Preact / Vue / TC39 polyfill 如何按「迁移成本 × 性能 × 生态成熟度」权衡？

**答**：
- 结论：选型看三个坐标——已有技术栈亲和度、运行时性能诉求、长期标准化风险。
- React 栈优先 @preact/signals-react（最小改造）；全新高性能项目选 Solid；Vue 栈直接用 Vue 自带 ref。
- TC39 polyfill 适合想押注标准、愿意忍受 API 变动的团队，生产要锁版本。
- 追问：如何降低锁死风险？（答：业务层封装统一 useSignal 适配层，底层可替换）

```javascript
const MATRIX = {
  solid:    { migration: '高', perf: '最高', eco: '中', note: '编译配套才发挥极致' },
  preact:   { migration: '低', perf: '高', eco: '高', note: 'React 栈最小改造' },
  vue:      { migration: '低', perf: '高', eco: '高', note: '用内置 ref，勿混两套' },
  tc39poly: { migration: '中', perf: '中', eco: '低', note: '押标准，锁版本' },
};
function pick(stack) { return stack === 'react' ? 'preact' : stack === 'vue' ? 'vue' : 'solid'; }

// 业务层封装统一适配层，底层可替换降低锁死风险
const useSignal = (v) => pick(currentStack) === 'preact' ? preactSignal(v) : solidSignal(v);
```
