---
title: [MFW-416] 笔试：手写最小 SSR 服务器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-416：最小 SSR 服务器
**答**：实现 `createMiniServer({ routes, render, assetDir, timeoutMs = 3000 } )`：1) 协商顺序（RBL-497/246）：hash 静态文件 → 退役/健康端点 → SSR 路由匹配 → SPA 回退 404 页；2) SSR 用 renderToPipeableStream 流式（Shell 先写 header——TTFB 前置）+ 整体 deadline（超时切精简错误流——已发头部不能换状态码，输出内联错误卡）；3) 水合数据注入（window.__PRESET__ 转义 `</script`——XSS）；4) 静态文件 immutable+1y / 页面 no-store（路径族分派表）；5) 优雅停机（SIGTERM 摘流排水——MFW-285）。

```javascript
import { renderToPipeableStream } from 'react-dom/server'

export function createMiniServer({ routes, renderApp, pub, { ttlMs = 3000 } = {}) {
  return (req, res) => {
    const p = new URL(req.url, 'x').pathname
    const asset = tryStatic(p)                                   // ① hash 产物 immutable
    if (asset) return pipeAsset(res, asset)
    if (p === '/healthz') return res.end('ok')
    const route = matchRoutes(routes, p)                          // ③ SSR
    if (!route) return sendShell404(res)                          // ④ SPA 回退/404 壳

    res.setHeader('Content-Type', 'text/html; charset=utf-8')
    res.setHeader('Cache-Control', 'no-store')
    let done = false
    const { pipe, abort } = renderToPipeableStream(
      renderApp(route, { budget: leftMs(t0, ttlMs)}), {
        onShellReady() { if (!res.writableEnded) { res.writeHead(200); injects(bootstrap(flight)) ; pipe(res) } },
        onShellError() { if (!res.headersSent) res.writeHead(500); res.end(miniError()) },
        onError(e) { log.warn('seg', e) },                     // 段错不炸整页（降级卡语义）
      })
    res.on('close', () => !done && abort())                    // 客户端断开→终止 DB 链
    timer(3000, () => { if (!done) { abort(); res.end(inlineTimeoutCard()) } })   // deadline
  }
}
// 注入转义：JSON.stringify(state).replace(/</g,'\\u003c')
```
**评分点**：
- 协商四层顺序正确（静态→健康→SSR→回退；头族分派）
- Shell 先写（TTFB 前置）+ deadline 后 inline 错误卡（头部已发不能改状态码——流式约束的正确处理）
- `</script` 转义（注入 XSS 经典点）
- res.close→abort（客户端断开传播到数据层——孤儿 IO 防线）
