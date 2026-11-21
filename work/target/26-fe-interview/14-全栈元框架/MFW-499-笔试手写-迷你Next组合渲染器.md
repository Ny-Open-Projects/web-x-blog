---
title: [MFW-499] 笔试：手写迷你 Next（组合渲染器收官）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-499：迷你 Next——静态/ISR/流式组合渲染器（收官大题）
**需求**：实现 `createMiniNext({ routes, render, ttl })`：1) routes = { '/about': 'static', '/feed': 'stream', '/p/:id': 'isr' }；2) 请求分派：static 直接读预渲染产物（构建期注入）；isr 走缓存 + 过期单飞再生成（旧值先行）；stream 用分块渲染：先写壳，各段 promise 完成按序写出（乱序到达也要按段序输出）；3) 统一错误路径：渲染异常返回降级页 + x-render-error 头；4) 中间件层：每请求 `x-mnw-*` 头注入 trace，全部渲染模式走同一入口（组合而非分裂——元框架本质）。

```javascript
export function createMiniNext({ routes, render, ttl = 30_000 }) {
  const statics = new Map(), isr = new Map(), inflight = new Map()

  return async function serve(req) {
    const { pathname } = new URL(req.url)
    const mode = matchRoute(routes, pathname)
    const trace = { t: Date.now(), mode, path: pathname }
    const headers = { 'x-mnw-mode': mode, 'x-mnw-trace': JSON.stringify(trace) }

    if (mode === 'static')
      return reply(statics.get(pathname) ?? render(pathname), headers)

    if (mode === 'isr') {
      const c = isr.get(pathname)
      if (c && Date.now() - c.at < ttl) return reply(c.html, headers)
      if (inflight.has(pathname)) return reply(c?.html ?? '<loading/>', headers) // 单飞
      const p = render(pathname).then(html => { isr.set(pathname, { html, at: Date.now() }); inflight.delete(pathname) })
      inflight.set(pathname, p)
      return reply(c?.html ?? '<loading/>', { ...headers, 'x-mnw-stale': String(!c) })
    }

    // stream：壳先行 + 按段序写出
    const parts = render(pathname) // 返回 { shell, segments: [Promise] }
    let out = parts.shell
    for (const p of parts.segments) {
      try { out += await p } catch { out += '<section>err</section>' }
    }
    return reply(out, headers)
  }

  function reply(html, headers) {
    return new Response(html, { headers: { ...headers, 'content-type': 'text/html' } })
  }
}

function matchRoute(routes, path) {
  for (const [k, v] of Object.entries(routes)) {
    if (k.includes(':')) {
      const re = new RegExp('^' + k.replace(/:[^/]+/g, '[^/]+') + '$')
      if (re.test(path)) return v
    } else if (k === path) return v
  }
  return 'static'
}
```

**评分点**：
- 三种模式同一入口分派（元框架本质：渲染策略组合而非多套服务）
- ISR 单飞 + 旧值先行（过期再生成不阻塞响应）
- 流式按段序输出（乱序完成也要保序——流式正确性核心）
- 统一 trace 头贯穿所有模式（可观测性不分渲染策略）
