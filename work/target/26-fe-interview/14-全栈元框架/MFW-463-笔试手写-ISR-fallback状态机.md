---
title: [MFW-463] 笔试：手写 ISR fallback 状态机
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-463：ISR fallback 三态状态机
**答**：实现 `createIsrFallback({ mode })`，mode ∈ 'blocking' | 'true' | 'false'：1) 未缓存路径首次请求：blocking → 同步渲染返回 200（首访慢但可直接 SEO）；'true' → 立即返回占位 + 触发后台生成；'false' → 直接 404（预生成清单外的路径不存在）；2) 生成完成后写缓存，'true' 的后续访问走缓存；3) 同一路径生成中再有请求：blocking 排队等待同一 promise（单飞），'true' 继续返回占位不排队；4) 生成失败保留旧值，无旧值时 blocking 返 500、'true' 继续占位。

```javascript
export function createIsrFallback({ mode, render }) {
  const cache = new Map()   // path -> { html, ok }
  const inflight = new Map()

  async function generate(path) {
    if (inflight.has(path)) return inflight.get(path) // 单飞
    const p = render(path)
      .then(html => { cache.set(path, { html, ok: true }); return html })
      .catch(e => { cache.set(path, { html: cache.get(path)?.html, ok: false }); throw e })
      .finally(() => inflight.delete(path))
    inflight.set(path, p)
    return p
  }

  return async function serve(path) {
    const hit = cache.get(path)
    if (hit?.ok) return { status: 200, body: hit.html }
    if (mode === 'false') return { status: 404, body: 'not found' }
    if (mode === 'blocking') {
      try { return { status: 200, body: await generate(path) } }
      catch { return { status: hit ? 200 : 500, body: hit?.html ?? 'error' } }
    }
    // 'true'：不等待，占位 + 后台生成
    generate(path).catch(() => {})
    return { status: 200, body: '<placeholder/>', stale: true }
  }
}
```

**评分点**：
- 三态语义分离：blocking 可 SEO / true 快但占位 / false 白名单
- 单飞 inflight 复用（blocking 排队不打爆源站）
- 失败保旧值（ISR 坏了不出白屏）
- 'false' 模式越权路径 404（枚举防护）
