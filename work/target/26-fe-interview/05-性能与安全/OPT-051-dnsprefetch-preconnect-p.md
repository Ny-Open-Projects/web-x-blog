---
title: [OPT-051] dns-prefetch、preconnect、preload 怎么组合成"连接预热决策树"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-051：dns-prefetch、preconnect、preload 怎么组合成"连接预热决策树"？

**答**：
- 三者解决的问题层次不同：dns-prefetch 只做 DNS（几十 ms）、preconnect 做 DNS+TCP+TLS（弱网下 1s+）、preload 提前下载具体资源。
- 决策树：**当前页关键路径资源** → preload；**当前页一定会用的第三方源** → preconnect；**当前页可能用/下一页用** → dns-prefetch；不要对不确定的域名滥用 preconnect。
- preconnect 是昂贵操作（占用对方服务器连接与握手算力），上限建议 3-4 个，且要配 `crossorigin` 属性与实际请求一致，否则预热作废。
- 常见坑：preconnect 了但资源走 `font.gstatic.com` 之类不同 schema/crossorigin 组合，等于白连。

```html
<!-- 一一对应：连接预热决策树落地模板 -->
<head>
  <!-- 决策① 资源在同源：不用预热，浏览器自动复用已有连接，什么都不写 -->

  <!-- 决策② 当前页一定请求的第三方源（字体/CDN）：preconnect 全量握手 -->
  <link rel="preconnect" href="https://cdn.assets.example.com" />
  <!-- 字体必须带 crossorigin，因为字体请求是匿名 CORS 模式；不带则预热的连接用不上 -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- 决策③ 首屏关键资源：preload 提升发现时机（连接已由 preconnect 预热） -->
  <link rel="preload" href="https://fonts.gstatic.com/s/harmony.woff2" as="font" type="font/woff2" crossorigin />

  <!-- 决策④ 弱可能用到（埋点、客服、下一跳域名）：只做 dns-prefetch，成本低 -->
  <link rel="dns-prefetch" href="https://tracking.example.com" />
  <link rel="dns-prefetch" href="https://api.example.com" />

  <!-- 反例（都不要写）：
       preconnect 超过 4 个域名 —— 握手竞争带宽且大多用不上
       对同源写 preconnect —— 纯冗余
       对"可能弹出第三方"域名 preconnect —— 用户不点就浪费一次完整 TLS -->
</head>
```
