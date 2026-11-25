---
title: [PER-666] 移动端 H5 在 App WebView 容器里的首屏优化全景：容器侧与页面侧各做什么？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-666：移动端 H5 在 App WebView 容器里的首屏优化全景：容器侧与页面侧各做什么？

**答**：
- 容器侧（与客户端协同）：WebView **预创建与复用池**（提前建好 webview 实例，点链接直接复用省 200~500ms 启动）、离线包（静态资源本地化，弱网下秒开）、JSAPI 并行注入（bridge 脚本随 webview 创建注入，不等页面请求）、DNS/连接预建（容器提前建 TCP/TLS 连接池）。
- 页面侧：首屏数据并行请求（与 HTML 并行，容器把数据塞进启动参数）、SSR/静态化、首屏资源收敛（关键 CSS 内联 + JS defer）、图片按视口加载。
- 双侧配合的关键协议：启动参数传预取数据 + 页面标识，页面渲染前先读预取数据，避免容器预取了但页面不知道的浪费。
- 度量口径：容器口径的秒开"= 从点击到首屏可交互（含 webview 创建时间），页面口径的 LCP 会漏掉容器启动段，要统一用客户端埋点。

```javascript

// 双侧协作协议：容器预取 -> 页面消费
window.__HYBRID_BOOT = { prefetched: null, createdAt: null };   // 容器注入
function consumePrefetch(route) {
  if (window.__HYBRID_BOOT?.prefetched?.route === route) {
    return window.__HYBRID_BOOT.prefetched.data;                 // 命中容器预取，0 网络耗时
  }
  return null;
}
// 容器侧 JSAPI（示意）：创建时预取 + 注入
// bridge.call('prefetch', { route: '/detail/123', data: await fetchDetail() })
// 度量：客户端埋点 click -> firstInteractive（含容器启动），服务端无法测全
```
