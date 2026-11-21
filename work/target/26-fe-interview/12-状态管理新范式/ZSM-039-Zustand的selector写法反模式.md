---
title: [ZSM-039] 列举 Zustand selector 的典型反模式及其修复
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-039：列举 Zustand selector 的典型反模式及其修复
**答**：
- 反模式一：整 store 订阅 `useStore()` 再解构——任何字段变更都重渲染；修：按字段拆 selector。
- 反模式二：selector 里创建新对象/数组不做比较——用 useShallow 或拆字段。
- 反模式三：selector 里做副作用（打点、写 storage）——渲染期副作用不可控（StrictMode 双调、并发渲染中断），移到 subscribe 或 action。
- 反模式四：selector 返回 derived 布尔但依赖手写比较逻辑错漏；修：保持 selector 纯、比较交给 Object.is/useShallow。
- 反模式五：在 selector 里缓存到外部变量假装 memo——并发渲染下不安全，用 useRef 版缓存或 useShallow。

```javascript
// 反模式二修复对照
const s1 = useStore(s => ({ a: s.a, b: s.b }))            // 差：新对象每次渲染
const s2 = useStore(useShallow(s => ({ a: s.a, b: s.b }))) // 好
const a = useStore(s => s.a)                               // 更好：拆开
```
