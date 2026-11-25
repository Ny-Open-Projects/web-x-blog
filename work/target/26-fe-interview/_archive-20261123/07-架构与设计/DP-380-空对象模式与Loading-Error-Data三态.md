---
title: [DP-380] 空对象模式：三态渲染的统一
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-380：空对象模式：三态统一

**答**：
- 空对象核心：null 的「有行为替代品」（EmptyList 提供 empty 状态渲染）——消灭 if (!data) 散落判断
- 三态建模：Loading 态对象/Error 态对象/Data 态对象——统一接口（render()）——组件消费态对象无需判空
- 实战形态：Result<T> 类型（{ status: 'loading'|'error'|'success', data?, error? }）+ 渲染分发（status 驱动）——数据结构消灭 if 散落
- 与空对象组件的结合：EmptyState 组件（空态插画+引导按钮——「空」也是一等公民 UI）
- 深水点：空对象与 null 的边界——「无数据」与「加载中」与「加载失败」是三种不同空对象——合并成一个 null 会丢失语义

```javascript
const AsyncResult = {
  loading: () => ({ status: 'loading', render: (ui) => ui.loading() }),
  error: (e) => ({ status: 'error', error: e, render: (ui) => ui.error(e) }),
  data: (d) => ({ status: 'success', data: d, render: (ui) => ui.data(d) }),
};
// 组件消费:
// result.render({ loading: () => <Spinner/>, error: (e) => <ErrView e={e}/>, data: (d) => <List d={d}/> })
// — 无 if 散落, 状态机即类型
```
