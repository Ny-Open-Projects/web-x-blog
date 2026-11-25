---
title: [V3-309] effect 嵌套与 EffectScope 作用域树是什么关系？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-309：effect 嵌套与 EffectScope 作用域树是什么关系？
**答**：
- 全局维护 `activeEffectScope` 栈；`effect/watch/computed` 创建时自动挂到当前激活 scope，形成树结构，父 scope stop 时递归停掉全部子级。
- 组件 setup 本身运行在一个组件级 EffectScope 里，这就是为什么 setup 里创建的 watch 不用手动清理。
- effect 嵌套：内层 effect 运行时会把外层压栈保存，结束后恢复——所以嵌套的 watchEffect 不会互相劫持收集目标。
- 手动场景：在组件外（工具函数、store）创建响应式副作用必须包 `effectScope()`，否则要么泄漏要么挂错到调用方的 scope。
- 注意 `detached: true` 的 scope 不随父级停止而停止，适合「跟随父组件但独立销毁」的场景。
```javascript
const scope = effectScope()
scope.run(() => {
  watchEffect(() => console.log(count.value)) // 自动归入 scope
})
scope.stop() // 级联停止子 effect
```
