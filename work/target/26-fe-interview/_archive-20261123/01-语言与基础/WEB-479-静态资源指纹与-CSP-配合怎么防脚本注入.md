---
title: [WEB-479] 静态资源指纹与 CSP 配合怎么防脚本注入
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-479：静态资源指纹与 CSP 配合怎么防脚本注入

**答**：
- 防 XSS 脚本注入的纵深：CSP 限制来源（script-src 白名单/nonce）→ SRI 校验内容 → 不写 innerHTML
- nonce 模式：服务端每次响应生成随机 nonce，注入到 CSP 头与 `<script nonce>` 上，内联脚本也须持证上岗
- hash 模式：对固定内容的内联脚本计算 hash 写进 CSP，内容一变就失效——适合静态内联段
- SRI 配合：`integrity="sha384-..."` 保证 CDN 资源未被篡改；但动态更新的资源不适用
- 收尾话术：指纹（文件名 hash）解决「缓存正确性」，CSP/SRI 解决「内容可信性」，两者不要混为一谈

```html
<script nonce="r4nd0m" src="/app.9f3c.js" integrity="sha384-abc..." crossorigin="anonymous"></script>
```
```http
Content-Security-Policy: script-src 'self' 'nonce-r4nd0m'; ...
```
