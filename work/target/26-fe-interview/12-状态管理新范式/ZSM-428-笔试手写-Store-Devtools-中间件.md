---
title: [ZSM-428] 笔试：手写 Store Devtools 中间件（时间线 + 跳转）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-428：手写 Store Devtools 中间件
**需求**：实现 `withDevtools(storeCreator)`：1) 包装 storeCreator：每次 setState 记录 `{ action, prev, next, ts }` 到时间线（上限 200 条）；2) devtools API：`jump(index)` 跳到第 n 条状态（整体替换 store state）；3) `pause()/resume()`：暂停时 state 变更仍生效但不再记录；4) `exportLog()` 导出时间线（脱敏钩子 sanitize 可选）；5) 时间线满 FIFO 淘汰；6) jump 后继续 set 的行为：时间线分叉——truncate 到当前点再追加。

```javascript
export function withDevtools(storeCreator, { limit = 200, sanitize } = {}) {
  return (...args) => {
    const store = storeCreator(...args)
    const log = []
    let paused = false

    const origSet = store.setState
    store.setState = (patch, action = 'anonymous') => {
      const prev = store.getState()
      origSet(patch)
      if (paused) return
      log.push({ action, prev: structuredClone(prev), ts: Date.now() })
      if (log.length > limit) log.shift()               // FIFO
    }

    return {
      ...store,
      __devtools: {
        jump(index) {
          const entry = log[index]
          if (!entry) return
          origSet(entry.prev)                            // 跳到该条之前的状态
          log.length = index + 1                         // 分叉：truncate
        },
        pause: () => (paused = true),
        resume: () => (paused = false),
        exportLog: () => log.map((e) => sanitize ? { ...e, prev: sanitize(e.prev) } : e),
      },
    }
  }
}
```
**评分点**：
- 记录 prev 快照（structuredClone 防后续变异污染时间线）
- jump 语义 = 恢复 prev + truncate 分叉（不是简单回放）
- pause 只停记录不停功能（生产灰度排查可用）
- exportLog 带 sanitize 钩子（导出防泄露）；FIFO 上限防内存膨胀
