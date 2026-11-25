---
title: [SCN-029] 第三方系统 iframe 嵌入我方页面后登录态丢失，SameSite 实战中怎么配？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-029：第三方系统 iframe 嵌入我方页面后登录态丢失，SameSite 实战中怎么配？
**答**：
- 根因：Chrome 默认 SameSite=Lax，跨站 iframe、跨站 POST 请求都不携带 Cookie，表现为"接口全部 401"。
- 需要跨站携带的场景（iframe 嵌入、SSO 跳回）必须 SameSite=None 且 Secure（HTTPS）；普通同站业务保持 Lax，写接口叠加 CSRF Token 防御。
- Cookie 属性由服务端下发，前端改不了：在应用或网关层统一追加。

```nginx
# nginx 反向代理层统一为会话 Cookie 追加安全属性
location /api/ {
    proxy_pass http://backend;
    # SameSite=None 必须搭配 Secure，仅限确需跨站携带的 Cookie
    proxy_cookie_path / "/; SameSite=None; Secure; HttpOnly";
    # 前端与接口不同源时，配合 CORS 允许凭证
    add_header Access-Control-Allow-Origin "https://www.example.com" always;
    add_header Access-Control-Allow-Credentials "true" always;
}
```
