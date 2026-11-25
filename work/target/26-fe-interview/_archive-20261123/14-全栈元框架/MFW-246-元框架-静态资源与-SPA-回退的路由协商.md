---
title: [MFW-246] 静态资源与 SPA 回退的路由协商（自定义服务端）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-246：静态资源与 SPA 回退协商

**答**:
- 自建/自托管服务端的路由优先级协议：精确静态文件（hash 产物）→ 特殊文件（robots/sitemap/健康检查）→ SSR 路由匹配 → SPA 回退（index.html，客户端路由接管）
- 顺序错误的经典事故：SSR 路由匹配抢在静态文件前（/static/main.js 被当页面渲染返回 HTML——JS 变成 text/html 拒执行）
- 缓存头分派：hash 产物 immutable+1y；SPA 回退与 SSR 页 no-cache/短——同一 server 不同路径族不同头（路径族分派表）
- 404 语义分层：产物缺失（构建事故——5xx 级告警）vs 业务 404（正常——2xx notFound 页）——不能都回 SPA 壳掩盖

```text
协商顺序：hash 产物(immut) → 特殊文件 → SSR 路由(no-cache) → SPA 回退(fallthrough)
事故预防：静态段前缀隔离（/static/* 永不进 SSR 匹配）
404 分层：产物缺失=5xx 告警 / 业务 404=正常页
```
