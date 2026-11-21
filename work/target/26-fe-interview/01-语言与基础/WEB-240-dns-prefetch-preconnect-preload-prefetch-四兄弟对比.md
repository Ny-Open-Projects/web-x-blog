---
title: [WEB-240] dns-prefetch/preconnect/preload/prefetch 四兄弟对比
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 性能]
type: 面试题
---

## WEB-240：dns-prefetch/preconnect/preload/prefetch 四兄弟对比

**答**：
- dns-prefetch：只提前解析 DNS，开销最小，第三方域名用 `<link rel="dns-prefetch" href="//api.xx.com">`。
- preconnect：提前 DNS+TCP+TLS 完整建连，用于「确定马上要用」的关键第三方域（CDN、鉴权 API），暖连接省 1~2 个 RTT。
- preload：提前加载当前页面必需资源（字体、关键脚本），`as` 必须正确，优先级高，不用会告警。
- prefetch/modulepreload：加载下一页/导航可能用的资源，空闲时低优先级下载，缓存到 HTTP cache；SPA 代码分包预取常用。
- 使用纪律：preload 只给真正关键资源（LCP 元素、首屏字体），滥用会抢带宽反伤性能；字体要 `font-display: swap` 配合。

```html
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<link rel="dns-prefetch" href="https://stats.example.com">
<link rel="preload" href="/fonts/hero.woff2" as="font" type="font/woff2" crossorigin>
<link rel="prefetch" href="/next-page-data.json" as="fetch">
```

**评分点**：
- 四者作用层级（DNS/连接/当前页资源/下一页资源）区分清楚
- 知道 preload 的 as 与 crossorigin 必须与实际请求一致否则二次下载
- 能结合 LCP/字体场景说用法
