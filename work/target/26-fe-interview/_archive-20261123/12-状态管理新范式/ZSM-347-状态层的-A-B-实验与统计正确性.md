---
title: [ZSM-347] 状态层怎么接 A/B 实验才不污染统计
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-347：状态层怎么接 A/B 实验才不污染统计

**答**:
- 实验分组是「会话级事实」：进入应用时分桶一次写入全局 store（带 sticky：storage/服务端分桶服务），渲染过程绝不重分桶——中途变组是统计污染头号来源
- 分支渲染一致性：实验开关在读路径统一入口（useExperiment('exp1')），组件树分支用同一判定值渲染；SSR 侧先分桶再渲染避免水合不一致
- 事件归因：所有相关事件自动带 expId+variant，埋点层从 store 派生注入，业务代码零感知
- 状态联动风险：实验分支使用不同 store 结构时（新旧实现）要隔离持久化 key，防止交叉污染数据

```javascript
// 分桶一次、sticky 存储
const variant = useStore((s) => s.experiments.exp1 ?? assignSticky('exp1'))   // 首次分配后固化
// 埋点自动归因
track('cart_submit', { ...payload, exp: currentExperiments() })   // 从 store 派生，业务无感
```
