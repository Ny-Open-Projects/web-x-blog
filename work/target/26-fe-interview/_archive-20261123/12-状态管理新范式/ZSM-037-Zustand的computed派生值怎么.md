---
title: [ZSM-037] Zustand 怎么实现 computed 派生值？为什么不能在 selector 里做昂贵计算？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-037：Zustand 怎么实现 computed 派生值？为什么不能在 selector 里做昂贵计算？
**答**：
- Zustand 没有 computed 概念。轻量派生：selector 里做简单映射（且保证返回稳定引用）；组件内 useMemo；跨组件复用就抽成自定义 hook。
- 昂贵计算不能放 selector：store 任何变更都会跑一遍所有订阅者的 selector，O(n) 计算会被每次无关变更放大。
- 需要真正的记忆化派生（多输入依赖）：用 subscribeWithSelector 或引入 computed 中间件，输入不变就复用结果。
- 也可在 set 时顺手维护派生字段（反规范化），以空间换稳定，但要小心双源失真。

```javascript
// 反例：每次任意变更都全量过滤
const bad = useStore(s => s.items.filter(i => i.stock > 0)) // 新数组 + O(n)

// 正例：组件内 useMemo，依赖引用稳定才重算
function StockList() {
  const items = useStore(s => s.items)
  const inStock = useMemo(() => items.filter(i => i.stock > 0), [items])
}
```
