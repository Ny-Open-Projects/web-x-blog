---
title: [ZSM-659] reselect 的 defaultMemoize：输入比较与结果缓存的实现细节
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-659：reselect 的 defaultMemoize：输入比较与结果缓存的实现细节

**答**：
- createSelector 的核心是 defaultMemoize：闭包缓存 `{ lastArgs, lastResult }`，调用时逐个用 `defaultEqualityCheck`（Object.is）比较输入参数，全部相同直接返回 lastResult——**任何输入变化都重算**，不管变化的输入有没有影响结果。
- 已知局限（面试必答）：**单缓存槽**——selector 在两个组件交替调用时缓存互踩（A 用 input1、B 用 input2、A 再调时输入不同重算）。修法：1) 每组件实例化 selector（工厂函数 `makeGetById()`）；2) `memoizeOptions: { maxSize: 5 }`（reselect 5 的 LRU 化，createSelector.memoize 支持缓存池）。
- 输入比较的选择器：默认 Object.is 对对象输入几乎必失效——`createSelector(..., { equalityCheck: shallowEqual })` 或输入选择器产出「可比较的元组」（把对象拆成原始值字段再作为输入）。
- 结果缓存与弱缓存：`createWeakMapSelector`（reselect 5）按输入对象 WeakMap 缓存——适合「输入是动态实体对象」的场景（避免 Object.is 失效 + 免手动 LRU）。
- 追问钩子：reselect 5 的 `createSelectorWithArray` 与自动依赖收集（依赖选择器数组动态生成）解决「依赖列表手写遗漏」——但核心 memoize 语义没变。

```javascript
// defaultMemoize 骨架
function defaultMemoize(func, equalityCheck = Object.is) {
  let lastArgs = null
  let lastResult
  let hasResult = false
  return function (...args) {
    if (hasResult && args.length === lastArgs.length &&
        args.every((arg, i) => equalityCheck(arg, lastArgs[i]))) {
      return lastResult               // 全部输入 Object.is 相同 → 返回缓存
    }
    lastArgs = args
    lastResult = func.apply(this, args)
    hasResult = true
    return lastResult
  }
}

// createSelector 骨架
function createSelector(...deps) {
  const inputSelectors = deps.slice(0, -1)
  const resultFn = deps.at(-1)
  const memoized = defaultMemoize(resultFn)
  return (state, ...rest) => {
    const inputs = inputSelectors.map((s) => s(state, ...rest))
    return memoized(...inputs)
  }
}

// 单缓存槽踩踏与修法
const getDone = createSelector([getTodos], (todos) => todos.filter((t) => t.done))
// 组件A getDone(state1) 组件B getDone(state2) → 交替重算

// 修法1：工厂（每组件独立缓存）
const makeGetDone = () => createSelector([getTodos], (todos) => todos.filter((t) => t.done))
const getDoneA = makeGetDone()   // A 用 A 的

// 修法2：LRU 缓存池（reselect 5）
const getDoneLru = createSelector([getTodos], (todos) => todos.filter((t) => t.done), {
  memoizeOptions: { maxSize: 5 },
})

// 修法3：输入元组化（让 Object.is 生效）
const getDoneByStatus = createSelector(
  [(s) => s.todos, (s) => s.statusFilter],
  (todos, status) => todos.filter((t) => t.status === status),
  { equalityCheck: shallowEqual }   // 或把 todos 拆为 ids+entities 两个稳定输入
)
```
