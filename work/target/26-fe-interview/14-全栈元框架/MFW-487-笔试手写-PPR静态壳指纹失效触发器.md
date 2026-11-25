---
title: [MFW-487] 笔试：手写 PPR 静态壳指纹与失效触发器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-487：PPR 静态壳指纹与失效触发器
**答**：实现 `ShellRegistry`：1) `publish(route, shellHtml, { deps })`：发布壳并计算指纹 = hash(html)；同路由重复 publish 指纹不变则跳过（幂等构建）；2) `invalidateByDep(dep)`：deps 含该 dep 的路由壳失效——但只失效壳的"静态部分描述"，洞数据独立缓存；3) 失效立即生效（下次请求重建壳），提供 `rebuildQueue` 保证重建串行（防重建风暴）；4) `status(route)` 返回 { fingerprint, publishedAt, valid }——可观测壳生命周期。

```javascript
import { createHash } from 'node:crypto'

export class ShellRegistry {
  constructor() { this.shells = new Map(); this.queue = []; this.draining = false }

  publish(route, html, { deps = [] } = {}) {
    const fp = createHash('sha1').update(html).digest('hex').slice(0, 12)
    const cur = this.shells.get(route)
    if (cur?.fingerprint === fp) return { skipped: true, fingerprint: fp }
    this.shells.set(route, { fingerprint: fp, html, deps, publishedAt: Date.now(), valid: true })
    return { skipped: false, fingerprint: fp }
  }

  invalidateByDep(dep) {
    const hit = []
    for (const [route, s] of this.shells)
      if (s.deps.includes(dep)) { s.valid = false; hit.push(route); this.enqueue(route) }
    return hit
  }

  enqueue(route) { // 重建串行：防失效风暴同时重建打爆源站
    if (!this.queue.includes(route)) this.queue.push(route)
    this.drain()
  }
  async drain() {
    if (this.draining) return
    this.draining = true
    while (this.queue.length) {
      const r = this.queue.shift()
      await rebuildShell(r)            // 实际重建（略）
      this.shells.get(r).valid = true
    }
    this.draining = false
  }

  status(route) {
    const s = this.shells.get(route)
    return s && { fingerprint: s.fingerprint, publishedAt: s.publishedAt, valid: s.valid }
  }
}
```

**评分点**：
- 指纹幂等发布（同内容不重复发布——构建可重跑）
- 依赖图失效只标记不阻塞读（valid=false 即重建，旧壳可继续服务）
- 重建串行队列（失效风暴串行化——重建风暴是 PPR 上线头号事故）
- status 暴露指纹/有效期（壳生命周期可审计）
