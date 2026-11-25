---
title: [WCN-277] effect 执行顺序的显式声明（依赖其他 effect 的副作用）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-277：effect 执行顺序的显式声明（依赖其他 effect 的副作用）？
**答**：
- 默认注册序执行——跨组件顺序脆弱（挂载顺序变化）。
- 显式排序：effect(fn, {after: [otherEffect]})——拓扑声明。
- 替代设计：消除顺序依赖（副作用合并进一个 effect 或用 computed 纯化）。
- 规范：跨 effect 副作用依赖是坏味道——优先重构而非排序 hack。

```javascript
const e1 = effect(() => save(total.value), { name: 'save' });
const e2 = effect(() => audit(total.value), { after: ['save'] });  // 审计在保存后
// 更好：audit 用 computed 只读 save 写入的持久层信号
r
```
