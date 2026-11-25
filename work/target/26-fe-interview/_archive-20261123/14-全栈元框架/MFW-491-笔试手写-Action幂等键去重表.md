---
title: [MFW-491] 笔试：手写 Server Action 幂等键去重表
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-491：Server Action 幂等键去重表
**需求**：实现 `IdempotencyTable({ ttl = 600_000 })`：1) `claim(key, run)`：同 key 首次执行 run，进行中/已完成者复用结果（网络重试 + 用户双击统一防御）；2) 进行中的 key 记录 `running`，后来者等待同一 promise；3) 完成结果缓存 ttl（重试在 ttl 内拿同一结果），过期后同 key 视为新请求；4) 失败结果不缓存（失败允许立即重试）；5) 内存表用 Map + 过期惰性清理（不设定时器——serverless 环境省资源）。

```javascript
export class IdempotencyTable {
  constructor({ ttl = 600_000 } = {}) {
    this.ttl = ttl
    this.store = new Map() // key -> { state: 'running'|'done', value, at, p }
  }

  claim(key, run) {
    const e = this.store.get(key)
    if (e) {
      if (e.state === 'running') return e.p               // 等同一趟
      if (Date.now() - e.at < this.ttl) return Promise.resolve(e.value) // ttl 内复写结果
      this.store.delete(key)                               // 过期当新请求
    }
    const p = Promise.resolve()
      .then(run)
      .then(value => { this.store.set(key, { state: 'done', value, at: Date.now() }); return value })
      .catch(err => { this.store.delete(key); throw err }) // 失败不缓存
    this.store.set(key, { state: 'running', p })
    return p
  }

  sweep() { // 惰性清理：读取时顺带（演示独立方法）
    for (const [k, e] of this.store)
      if (e.state === 'done' && Date.now() - e.at > this.ttl) this.store.delete(k)
  }
}
```

**评分点**：
- running 态共享 promise（双击与网络重试都收敛到一次执行）
- 失败不缓存（可立即重试；成功才占 ttl——语义分清）
- ttl 过期当新请求（幂等窗口有限，防永久占内存）
- 无定时器惰性清理（serverless 中定时器易被冻结，惰性更稳）
