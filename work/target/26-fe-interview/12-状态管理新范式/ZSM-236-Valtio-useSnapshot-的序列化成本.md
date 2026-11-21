---
title: [ZSM-236] Valtio 的 useSnapshot 为什么开销大怎么优化
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-236：Valtio 的 useSnapshot 为什么开销大，怎么优化

**答**：
- useSnapshot 每次渲染把 state 代理「序列化」为冻结快照（递归 clone），并记录访问路径实现属性级订阅——大对象高频渲染时这是主要开销
- 优化一：缩窄快照范围（先解构需要的子树再传给子组件）；优化二：快照后传引用（不再解构新属性会失去细粒度订阅，权衡）
- 跟踪是懒的：只有渲染中实际读取过的属性才参与比较，没读的大子树不造成重渲染——所以「读取面小」是核心
- 与 useMemo 配合无效（快照每次新引用）；真正需要稳定引用时用 `derive`/computed 派生层

```javascript
const state = proxy({ user: { name: 'a', bigList: [...] } })

function Name() {
  const snap = useSnapshot(state)
  return <p>{snap.user.name}</p>   // 只订阅 user.name 路径，bigList 变化不重渲染
}
```
