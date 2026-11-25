---
title: [ZSM-024] 笔试：手写一个简化版 Zustand devtools/日志中间件
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-024：手写一个简化版 Zustand devtools/日志中间件

**答**：
- 实现中间件 `logger(config, name)`：每次 set 打印 action 名、变更前后 diff，并维护 action 历史数组。
- set 允许第三参传 action 名（如 `set({...}, false, 'cart/add')`），缺省自动生成。
- 提供 `api.getHistory()` 供调试面板读取历史。

**边界说明**：不要求对接真实 Redux DevTools 协议，console 输出即可。

```javascript
export function logger(config, name = 'store') {
  return (set, get, api) => {
    api.__history = []
    api.getHistory = () => api.__history

    const wrappedSet = (partial, replace, action) => {
      const prev = get()
      set(partial, replace)
      const next = get()
      const diff = {}
      for (const k in next) if (!Object.is(next[k], prev[k])) diff[k] = { prev: prev[k], next: next[k] }
      const entry = { action: action || `${name}/anonymous`, diff, at: Date.now() }
      api.__history.push(entry)
      console.log(`[${name}] ${entry.action}`, diff)
    }
    return config(wrappedSet, get, api)
  }
}

// 用法
const useStore = create(logger((set) => ({
  count: 0,
  inc: () => set(s => ({ count: s.count + 1 }), false, 'counter/inc'),
}), 'counter'))
// useStore.getState().inc()  →  [counter] counter/inc {count:{prev:0,next:1}}
```

**评分点**：
- 包装 set 保持签名兼容（partial, replace, actionName）。
- diff 计算基于引用/值比较，只输出变更字段。
- 历史挂在 api 上而非 state 上，避免污染渲染数据。
- 中间件先包装再调用 config，链式可组合。

## 变体与延伸（补充）

**变体与延伸**：

1. diff 用 `for (const k in next)` 会漏掉被删除的 key，怎么补 → 先取 `prev` 与 `next` 的键并集再逐个 `Object.is`，删除项记成 `{ prev, next: undefined }`。
2. 中间件包裹后 `get()` 拿到的是包装前还是包装后的 state → state 引用没变，包装的只是 `set`；若中间件要改 state 形状，必须在 `config` 执行前定好。
3. 想在 devtools 里做时间旅行（回放）怎么改 → 历史里存完整 state 快照而非 diff，回放用 `set(snapshot, true)` 替换，且回放自身不能再写入历史。
