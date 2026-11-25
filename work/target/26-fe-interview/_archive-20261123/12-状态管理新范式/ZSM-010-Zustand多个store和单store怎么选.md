---
title: [ZSM-010] Zustand 用多个小 store 还是一个大 store？按什么维度拆？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-010：Zustand 用多个小 store 还是一个大 store？按什么维度拆？
**答**：
- 默认推荐**多个小 store**：Zustand 没有 Provider 和 dispatch，多 store 成本极低，selector 天然把重渲染隔离到单个 store。
- 拆分维度：按业务域（user/cart/im）、按生命周期（页面级 store 用完销毁、全局 store 常驻）、按更新频率（高频帧数据单独拆，避免拖累低频状态）。
- 单一大 store 的适用场景：切片间频繁互相读写、需要统一持久化/迁移、devtools 想在一个时间线里看全部动作。
- 红线：不要把「所有 state 都塞一个对象」当成 Redux 习惯带过来，那是放大 selector 误用风险的根源。

```javascript
// 高频 + 低频分开：拖拽坐标每帧更新，只重渲染拖拽层
const useDrag = create(set => ({ x: 0, y: 0, move: (x, y) => set({ x, y }) }))
const useTodos = create(set => ({ todos: [], add: t => set(s => ({ todos: [...s.todos, t] }) ) }))

// 页面级 store：用工厂函数创建，路由离开时 destroy
const makePageStore = () => create(set => ({ step: 1, next: () => set(s => ({ step: s.step + 1 })) }))
const page = makePageStore()
// page.destroy()
```
