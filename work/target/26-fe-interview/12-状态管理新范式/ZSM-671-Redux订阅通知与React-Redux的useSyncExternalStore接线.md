---
title: [ZSM-671] React-Redux 的 useSelector 接线：订阅抖动与 re-render 闸门
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-671：React-Redux 的 useSelector 接线：订阅抖动与 re-render 闸门

**答**：
- React-Redux v8+ 的接线基于 useSyncExternalStore：订阅 store（每次 dispatch 通知所有订阅者），每次通知对**每个 useSelector 实例**重跑 selector + equalityFn 比较，相等则不 setState——「闸门」在 hook 层，store 层是广播（全通知），过滤靠每个 hook 自己的相等性检查。
- 与 Zustand 的关键差异：Redux store 无 selector 概念（广播到所有 listener），selector 完全在 hook 层跑——**通知成本 = useSelector 调用数 × selector 耗时**，与「结果是否变化」无关。大应用里这正是 reselect 记忆化 + 拆分 selector 的动力。
- 抖动防护：`useSyncExternalStore` 要求 getSnapshot 引用稳定——React-Redux 内部用订阅时快照缓存，selector 返回新对象时靠 `equalityFn`（默认 Object.is 或 react-redux 的 shallowEqual）挡住重渲；useSelector 自定义第二参比较函数即 shallow。
- store.subscribe 层的批处理：React-Redux 用「store 变更标志 + layout effect 校验」的批次机制，一次 dispatch 多个订阅回调只触发一轮 React 更新（订阅期校验防撕裂，同 Zustand 思路）。
- 追问钩子：`store.subscribe` 里读 getState 会读到**最新**状态（通知发生在 reducer 之后），而组件渲染期间读 store（getSnapshot）可能读到的是「订阅时」值——两处读到的值可能不同，这就是闸门存在的意义。

```javascript
// useSelector 接线骨架（v8 简化）
function useSelector(selector, equalityFn = refEquality) {
  const store = useContext(ReactReduxContext)
  const instRef = useRef(null)

  const getSnapshot = useCallback(() => {
    // selector 在 getSnapshot 里跑：React 每次渲染前都会调
    const next = selector(store.getState())
    if (instRef.current && equalityFn(instRef.current.value, next)) {
      return instRef.current.value       // 相等：返回旧引用（闸门）
    }
    instRef.current = { value: next }
    return next
  }, [store, selector, equalityFn])

  return useSyncExternalStore(store.subscribe, getSnapshot)
}

// 闸门效果
const todos = useSelector((s) => s.todos.filter((t) => t.done), shallowEqual)
// selector 每次通知都执行（广播成本），但结果浅相等时不重渲（闸门）

// 抖动典型：select 返回新数组不带 equalityFn → 每次通知都重渲
// 修法1：reselect 记忆化（输入不变输出引用不变）
const selectDone = createSelector([(s) => s.todos], (todos) => todos.filter((t) => t.done))
// 修法2：shallowEqual
const data = useSelector((s) => ({ a: s.a, b: s.b }), shallowEqual)
```
