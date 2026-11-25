---
title: [WEB-007] HTTP/2 Server Push 是什么？为什么后来被废弃了？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-007：HTTP/2 Server Push 是什么？为什么后来被废弃了？
**答**：
- Server Push 允许服务器在浏览器请求 HTML 时，主动把页面依赖的 CSS/JS 一并推过去，省去"收到 HTML 再发现依赖再请求"的往返。
- 实际问题：服务器不知道浏览器缓存里已有什么，经常推了已被缓存的资源，浪费带宽；也无法感知资源优先级。
- Chrome 在 106 版本移除了对 Server Push 的支持，推荐用 103 Early Hints（状态码 103 提前告知可加载的资源）替代。
- 面试要点：知道 Push 与 Early Hints 的区别，Early Hints 只是提示，最终是否请求由浏览器决定。

```nginx
# nginx http2_push 配置示例（现已不推荐，面试需说明废弃原因）
server {
    listen 443 ssl http2;
    location = /index.html {
        http2_push /static/app.css;   # 推送页面关键 CSS
        http2_push /static/app.js;
    }
}

# 替代方案 Early Hints：提前返回 103，由浏览器决定是否预加载
# add_header 层面无法发 103，需要 nginx 1.25.1+ 的 early_hints 或应用层支持
```
