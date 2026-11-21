---
title: [ZSM-122] 笔试：手写 SWR 乐观更新 Hook（useOptimisticMutation：快照 + 回滚 + 对账）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-122：手写 SWR 乐观更新 Hook（useOptimisticMutation：快照 + 回滚 + 对账）
**需求**：实现 `useOptimisticMutation(key, mutationFn)`，返回 `trigger(variables)`：1) 立即用 updater(cur, variables) 更新缓存；2) 快照旧值；3) mutationFn 失败回滚快照并抛错；4) 成功后用服务端返回值覆盖；5) 同一 key 并发两次 trigger 时不互相覆盖（队列化）。边界：updater 抛错不发起请求；组件卸载后不再写缓存。

```javascript
import { useRef, useEffect } from 'react'
import { mutate } from 'swr'

const chains = new Map()   // key -> Promise，实现并发串行化

export function useOptimisticMutation(key, mutationFn, updater) {
  const alive = useRef(true)
  useEffect(() => () => { alive.current = false }, [])

  return function trigger(variables) {
    const run = async () => {
      let snapshot
      await mutate(key, (cur) => {
        snapshot = cur                       // 在缓存读取时点做快照
        return updater(cur, variables)       // updater 内部抛错直接中断
      }, { revalidate: false })
      try {
        const server = await mutationFn(variables)
        if (alive.current) await mutate(key, server, { revalidate: false })
        return server
      } catch (e) {
        if (alive.current) await mutate(key, snapshot, { revalidate: false })
        throw e                              // 回滚快照并向上抛
      }
    }
    const prev = chains.get(key) ?? Promise.resolve()
    const next = prev.then(run, run)         // 同 key 串行，防互相覆盖
    chains.set(key, next)
    return next
  }
}

// 用法：点赞按钮
// const like = useOptimisticMutation(['/api/goods', id], api.like,
//   (cur, vars) => ({ ...cur, likes: cur.likes + (vars.delta || 1) }))
// like({ delta: 1 })

// 评分点：
// 1. 快照时机：在 mutate 函数式回调里取旧值
// 2. 失败回滚快照、成功用服务端真值覆盖
// 3. 同 key 并发请求串行化（链式 Promise）
// 4. 卸载守卫：不向已卸载缓存写数据
// 5. updater 抛错不发起网络请求
```
