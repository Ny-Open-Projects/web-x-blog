---
title: [AIC-363] 用 AI 写技术方案 RFC，人机分工怎么切？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-363：用 AI 写技术方案 RFC，人机分工怎么切？
**答**：
- 人写：问题定义/约束条件/价值观权衡（这是方案灵魂）。
- AI 写：方案细节展开/风险清单/对比表格/时序图草稿——扩展人给定的骨架。
- 审校循环：AI 初稿 → 人标记「假设错误」处 → AI 重写 → 收敛。
- 禁止 AI 自造需求：RFC 里的每个功能点必须能追溯到问题定义，AI 添加的「顺带优化」删除。

```javascript
const rfcFlow = {
  human: ['problem', 'constraints', 'values/tradeoffs'],
  ai: ['方案细节展开', '风险清单', '对比矩阵', 'mermaid 图草稿'],
  loop: '初稿 → 人标假设错误 → 重写 → 收敛',
  rule: '每个功能点可追溯 problem，AI 自加项删除',
};
r
```
