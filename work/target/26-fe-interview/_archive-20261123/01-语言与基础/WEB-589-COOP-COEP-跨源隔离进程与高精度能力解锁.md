---
title: [WEB-589] COOP/COEP：跨源隔离如何改变进程与能力边界
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-589：COOP/COEP：跨源隔离如何改变进程与能力边界

**答**：
- COOP（Cross-Origin-Opener-Policy）：把当前文档与跨源窗口（opener/openee）隔离成不同 browsing context group——本质是进程/上下文组级隔离
- COEP（Cross-Origin-Embedder-Policy）：要求页面所有子资源声明可嵌入（CORP/COEP credentialless），配合 COOP 达成 crossOriginIsolated
- crossOriginIsolated 解锁能力：SharedArrayBuffer、高精度计时（performance.now 微秒级）、WebAssembly threads、多线程 SIMD——WASM 多线程应用的前提
- 迁移成本：所有第三方资源（统计、字体、图片 CDN）必须带 CORP 头或走 COEP: credentialless，否则直接加载失败——改造清单要从资源瀑布里逐个过
- 与站点隔离关系：站点隔离按站点分进程，COOP/COEP 把隔离再收紧到 browsing context group 级，二者互补

```text
启用清单:
  1) 主文档: COOP: same-origin + COEP: require-corp (或 credentialless)
  2) 子资源: Access-Control-Allow-Origin + Cross-Origin-Resource-Policy: cross-origin
  3) iframe: 跨源 iframe 也要 COEP
  4) 验证: self.crossOriginIsolated === true → 可用 SharedArrayBuffer
```
