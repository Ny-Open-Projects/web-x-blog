---
title: [WEB-515] HTTP/3 下前端的资源加载策略要改什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-515：HTTP/3 下前端的资源加载策略要改什么

**答**：
- 域名分片的旧行为要停：H3 单连接多路复用，多域名反而增加握手与证书成本，收敛到 1~2 个域名
- 资源内联重新权衡：H2/H3 下请求便宜了，小文件内联收益下降；但 0-RTT 让「首包就带请求」更值钱
- 优先级要显式声明：H3 的流优先级靠 `priority` 提示（fetch priority / Importance 属性），关键资源标 high
- Server Push 已死：H2 Push 都被废弃，H3 不要再指望它，改用 preload/103 Early Hints
- 面试钩子：能提「Early Hints(103) 是现代版的 Server Push 替代」是明显加分

```html
<link rel="preload" as="style" href="/main.css" fetchpriority="high">
<img src="/hero.webp" fetchpriority="high">
<script src="/analytics.js" defer fetchpriority="low"></script>
```
