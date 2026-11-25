---
title: [WEB-126] 同源策略演化出了 COOP/COEP/CORP，它们各管什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-126：同源策略演化出了 COOP/COEP/CORP，它们各管什么？
**答**：
- COOP（跨源打开者策略）：`same-origin` 让 window.open 打开的跨源页面失去 opener 引用，断开跨源窗口间的 JS 访问，防 XS-Leaks 与 opener 攻击。
- CORP（跨源资源策略）：资源声明"谁能以 no-cors 方式嵌入我"——`same-origin/same-site/cross-origin`，是站点对自己子资源的嵌入授权。
- COEP（跨源嵌入者策略）：`require-corp` 要求页面嵌入的每个跨源资源要么带 CORS 授权、要么带 CORP 允许，否则不加载——以此换取页面进入"跨源隔离"状态。
- 隔离的回报：启用 COOP+COEP 后可使用 SharedArrayBuffer、高精度计时等强能力；代价是所有第三方资源（广告、统计、字体）都要配合加头。

```http
# 站点 A 启用跨源隔离
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp

# 第三方资源站点必须配合声明，否则在 A 页面里加载失败
Cross-Origin-Resource-Policy: cross-origin

# 效果验证：启用后以下能力解锁
# const sab = new SharedArrayBuffer(1024);          // 否则抛异常
# performance.measureUserAgentSpecificMemory();     // 精确内存测量
# window.open 的跨源页拿不到 opener 引用，隔离成独立浏览上下文
```
