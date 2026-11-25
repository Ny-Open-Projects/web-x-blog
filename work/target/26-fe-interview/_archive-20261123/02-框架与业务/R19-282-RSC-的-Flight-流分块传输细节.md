---
title: [R19-282] RSC Flight 流是怎么分块传输与增量渲染的？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-282：Flight 流怎么分块传输？
**答**：
- 服务端渲染 RSC 树产出 Flight 流：每完成一个可序列化块就 flush 一行（JSON-ish + 引用标记），不整树等待。
- 引用解析：块间通过 `$L1`/`$Q2` 标记互相引用，客户端流式解析器边收边建对象图。
- Suspense 洞：异步子树输出「pending chunk」，resolve 后追加块，客户端局部更新。
- HTTP 层：chunked transfer + gzip；CDN 可缓存静态部分流（谨慎，含用户态不可缓存）。
- 调试：Next DevTools 里看 RSC payload 明文，理解引用与流块对应关系。
