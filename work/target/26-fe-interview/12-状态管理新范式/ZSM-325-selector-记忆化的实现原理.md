---
title: [ZSM-325] selector 记忆化（reselect 式）是怎么实现的
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-325：selector 记忆化（reselect 式）是怎么实现的

**答**:
- 原理：缓存「上次输入参数 + 上次输出」——再次调用时逐个比较输入（引用相等），全相等直接返回缓存输出；输入是派生值时形成级联记忆
- 关键细节：默认按位置比较有限个参数（reselect 默认 1 个），超参/可变参要 `createSelectorCreator` 自定义等值函数；输出引用稳定依赖输入稳定
- 链式失效：上游 selector 输出引用变化（即使内容相同）会导致下游重算——这就是为什么上游要返回稳定引用或用 shallow 比较改造
- 每调用点一个缓存实例：selector 定义在组件内会每渲染重建缓存（记忆化失效），必须提到模块级或用 useMemo 包工厂

```javascript
function createSelector(depFns, combine) {
  let lastDeps, lastResult, hasCache = false
  return (state) => {
    const deps = depFns.map((f) => f(state))
    if (hasCache && deps.every((d, i) => Object.is(d, lastDeps[i]))) return lastResult
    lastDeps = deps
    lastResult = combine(...deps)
    hasCache = true
    return lastResult
  }
}
```
