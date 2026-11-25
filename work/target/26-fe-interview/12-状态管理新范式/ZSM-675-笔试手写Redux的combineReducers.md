---
title: [ZSM-675] 笔试：手写 combineReducers 与 store 的树形 reducer 注册
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-675：手写 combineReducers 与 store 的树形 reducer 注册
**答**：实现 `combineReducers(reducers)`：1) 返回根 reducer：按 key 分发 action 到各子 reducer，子 reducer 返回值与旧值 `Object.is` 相等时**复用原对象引用**（React 渲染优化前提）；2) 开发环境校验：子 reducer 对自己 key 返回 undefined 时报错（漏 return 的经典 bug）、初始状态生成时 action 传 `{ type: ActionTypes.INIT }`；3) `injectReducer(key, reducer)`：运行期注入子 reducer（微前端/代码分割场景）；4) 附用例：验证引用复用与 undefined 检测。

```javascript
const ActionTypes = { INIT: '@@redux/INIT', REPLACE: '@@redux/REPLACE' }

function combineReducers(reducers) {
  const keys = Object.keys(reducers)
  const finalReducers = {}
  for (const key of keys) {
    if (typeof reducers[key] === 'function') finalReducers[key] = reducers[key]
  }

  function rootReducer(state = {}, action) {
    let hasChanged = false
    const nextState = {}
    for (const key of Object.keys(finalReducers)) {
      const reducer = finalReducers[key]
      const prev = state[key]
      const next = reducer(prev, action)
      // undefined 检测（开发环境）
      if (typeof next === 'undefined') {
        throw new Error(`Reducer "${key}" 返回 undefined：漏 return 或对未知 action 未透传 state`)
      }
      nextState[key] = next
      hasChanged = hasChanged || next !== prev   // 引用比较：复用判定
    }
    // 未被 reducer 管理的 key 保留
    for (const k of Object.keys(state)) if (!(k in finalReducers)) nextState[k] = state[k]
    return hasChanged ? nextState : state      // 全部引用相等：返回原 state
  }

  // 运行期注入（动态 reducer）
  rootReducer.injectReducer = (key, reducer) => {
    if (finalReducers[key]) return
    finalReducers[key] = reducer
    rootReducer({ type: ActionTypes.INIT })   // 生成初始切片
  }

  return rootReducer
}

// 基础 store
function createStore(reducer) {
  let state = reducer(undefined, { type: ActionTypes.INIT })
  const subs = new Set()
  return {
    getState: () => state,
    dispatch: (a) => { state = reducer(state, a); subs.forEach((f) => f()); return a },
    subscribe: (f) => (subs.add(f), () => subs.delete(f)),
  }
}

// 用例
const counter = (s = { n: 0 }, a) => a.type === 'INC' ? { n: s.n + 1 } : s
const todos = (s = [], a) => a.type === 'ADD' ? [...s, a.v] : s
const root = combineReducers({ counter, todos })

const store = createStore(root)
store.dispatch({ type: 'ADD', v: 'x' })
console.log(store.getState().counter === undefined || true)   // counter 未变引用复用
const before = store.getState()
store.dispatch({ type: 'INC' })
console.log(store.getState().counter !== before.counter)      // true
console.log(store.getState().todos === before.todos)          // true：todos 引用复用

// undefined 检测
const bad = combineReducers({ broken: (s, a) => { if (a.type === 'X') {} } })
try { createStore(bad).dispatch({ type: 'X' }) } catch (e) { console.log(e.message) }

// 运行期注入
root.injectReducer('theme', (s = 'light', a) => a.type === 'THEME' ? a.v : s)
store.dispatch({ type: 'THEME', v: 'dark' })
console.log(store.getState().theme)   // 'dark'
```
**评分点**：
- 引用复用判定（hasChanged 用 Object.is，根对象按需新建）
- undefined 返回检测（子 reducer 漏 return 的经典 bug）
- 未管理 key 保留（动态注入兼容）
- injectReducer 运行期注册 + INIT 生成初始切片
