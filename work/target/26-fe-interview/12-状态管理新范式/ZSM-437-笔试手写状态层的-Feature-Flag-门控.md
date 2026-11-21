---
title: [ZSM-437] 笔试：手写状态层 Feature Flag 门控（读取一致性 + 快照）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-437：手写状态层 Feature Flag 门控
**需求**：实现 `createFlagGate(defaults)`：1) `get(key)` 读 flag（未加载时返回 default 保守值）；2) `load(remoteFlags)`：异步加载后热生效；但「状态相关 flag」要求快照一致性——`snapshot()` 冻结当前 flag 集，组件用快照渲染（同一渲染批次内 flag 不漂移）；3) `useFlag(key)` 在渲染中读快照；4) flag 变更默认「下次刷新生效」开关（strict 模式：状态 flag 变更直接抛错阻止热切）；5) `onChange(key, fn)` 订阅变更（非 strict flag 才支持热切）。

```javascript
export function createFlagGate(defaults = {}, { strictKeys = [] } = {}) {
  let flags = { ...defaults }
  let snap = { ...flags }
  const listeners = new Map()

  function load(remote) {
    for (const [k, v] of Object.entries(remote)) {
      if (strictKeys.includes(k) && snap[k] !== v && flags[k] !== v)
        throw new Error(`flag ${k} requires refresh`)      // strict：状态 flag 禁热切
      flags[k] = v
      listeners.get(k)?.forEach((fn) => fn(v))
    }
    snap = { ...flags }                                     // 更新快照
  }

  return {
    get: (key) => snap[key] ?? defaults[key],
    load,
    snapshot: () => ({ ...snap }),                          // 渲染批次一致性
    onChange: (key, fn) => { if (strictKeys.includes(key)) throw new Error('strict flag no hot-change')
      if (!listeners.has(key)) listeners.set(key, new Set()); listeners.get(key).add(fn)
      return () => listeners.get(key).delete(fn) },
  }
}

// React 侧：每次渲染用同一快照
function useFlag(gate, key) {
  const snap = useRef(gate.snapshot()).current
  return snap[key]
}
```
**评分点**：
- 快照一致性（同一渲染内 flag 不漂移——tearing 同源问题）
- strict flag 禁止热切（状态结构 flag 热切 = 数据损坏）
- 保守默认值（未加载时按旧行为，不让 flag 依赖阻塞首屏）
- onChange 与 strict 互斥（语义自洽）
