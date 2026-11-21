---
title: [ZSM-402] 笔试：手写竞态守卫（只接受最新请求结果）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-402：手写竞态守卫（只接受最新请求结果）
**需求**：实现 `useLatest(queryFn, deps)` 语义的纯函数版 `createLatestRunner()`：1) `run(key, asyncFn)` 发起执行；2) 同 key 新 run 立即使旧 run「过期」——旧结果 resolve 后被丢弃且旧请求被 abort（asyncFn 收到 signal）；3) `get(key)` 返回最新完成结果或 undefined；4) 过期请求的 reject（abort）不抛给调用方；5) 支持 `cancelAll()`。

```javascript
export function createLatestRunner() {
  const runs = new Map()   // key → { version, ac, promise }

  function run(key, asyncFn) {
    const prev = runs.get(key)
    if (prev) prev.ac.abort()                       // 旧请求 abort
    const version = (prev?.version ?? 0) + 1
    const ac = new AbortController()
    const promise = asyncFn(ac.signal)
      .then((data) => {
        if (runs.get(key)?.version === version) runs.set(key, { version, ac, promise, data })
        return data
      })
      .catch((e) => {
        if (e?.name !== 'AbortError') throw e        // abort 静默
      })
    runs.set(key, { version, ac, promise })
    return promise
  }

  return {
    run,
    get: (key) => runs.get(key)?.data,
    cancelAll: () => runs.forEach((r) => r.ac.abort()),
  }
}
```
**评分点**：
- 版本号判定「过期」：结果到达时先比对 version 再写缓存（旧结果不覆盖新）
- abort 要真正传给 asyncFn（底层 fetch 可取消），不只是逻辑丢弃
- AbortError 静默不外抛，其他错误正常传播
- cancelAll 清理全部在途，防组件卸载后写入
