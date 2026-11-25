---
title: [OPT-049] HTTP/2 Server Push 已死？103 Early Hints 怎么用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-049：HTTP/2 Server Push 已死？103 Early Hints 怎么用？

**答**：
- H2 Push 的问题：推的资源常与缓存冲突（客户端已有）、无法根据页面实际内容判断、浪费带宽，Chrome 已在 2022 年移除支持。
- 替代方案 **103 Early Hints**：服务器在最终响应前先发一个临时响应，告诉浏览器"可以提前去请求/预加载这些资源"，浏览器主动请求，不占服务端推送带宽。
- 与 H2 Push 的本质区别：Push 是"给你"，Early Hints 是"提示你去拿"，缓存控制权回到浏览器。
- 实践中 CDN（Cloudflare/Fastly）对源站响应做学习后自动下发 103，源站只需输出正确的 preload/link 头。

```nginx
# 一一对应：Nginx 手动下发 103 Early Hints + 源站 link 头方案
# 方案一：边缘节点直接对热路径手动下发 103
server {
    listen 443 ssl http2;
    location = /page {
        # 103 是临时响应，浏览器收到后立刻并行发起 preload，不等最终 200
        add_header early-hints-link "</app.css>; rel=preload; as=style, </app.js>; rel=preload; as=script" always;
        proxy_pass http://origin;
    }
}

# 方案二（推荐）：源站输出 Link 响应头，CDN（如 Cloudflare Early Hints 开关）
# 学习后自动生成 103，源站无需感知。Node/Express 源站等价写法：
#   res.set('Link', '</app.css>; rel=preload; as=style, </hero.avif>; rel=preload; as=image; fetchpriority=high');
# 注意与页面内 <link rel=preload> 二选一，不要重复声明同一资源
```
