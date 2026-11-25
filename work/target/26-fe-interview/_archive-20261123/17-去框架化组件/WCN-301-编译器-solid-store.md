---
title: [WCN-301] Solid 的 store（深层响应式对象）实现原理与信号的关系？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-301：Solid 的 store（深层响应式对象）实现原理与信号的关系？
**答**：
- store 用 Proxy 代理深层对象：属性读取即创建子节点（懒建节点），写入只触发该属性的订阅者。
- 与信号关系：store 节点本质是惰性信号图——属性级细粒度自动化。
- 数组方法拦截：push/splice 翻译成「节点增删 + 订阅迁移」。
- 取舍：Proxy 有开销（每次访问走 trap）——热路径可展开为显式信号。

```javascript
const state = createStore({ user: { name: 'x' } });
createEffect(() => render(state.user.name));   // 只订阅 name 节点
setState('user', { name: 'y' });               // 只有 name 的订阅者触发
r
```
