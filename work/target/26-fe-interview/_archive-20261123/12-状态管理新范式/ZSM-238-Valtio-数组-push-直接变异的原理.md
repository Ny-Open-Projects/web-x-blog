---
title: [ZSM-238] Valtio 里直接 push 数组为什么能触发更新
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-238：Valtio 里直接 push 数组为什么能触发更新

**答**：
- state 是 Proxy：写操作（push/赋值/delete）被 set trap 拦截，拦截器做 COW——把目标对象浅拷贝一份替换父级引用，同时递归通知父级版本更新
- 所以「直接变异」只是写法体验，底层仍是不可变替换；React 侧拿到的是新引用快照，天然兼容并发渲染
- 边界一：Map/Set 需要 proxyMap/proxySet 包装；边界二： Proxy 里的循环引用对象共享拷贝（同一对象拷一次）但深拷贝成本仍在
- 对比 Zustand：Zustand 显式 set + 浅合并，Valtio 隐式变异追踪；团队上手快但隐式行为在调试时需 devtools 确认路径

```javascript
const state = proxy({ items: [1, 2] })
state.items.push(3)          // set trap 拦截 → items 浅拷贝替换 → 父级版本号 +1 → 渲染
state.items.splice(0, 1)     // 同理
const s = useSnapshot(state) // s.items 是冻结快照，不能 push（运行时报错防误改）
```
