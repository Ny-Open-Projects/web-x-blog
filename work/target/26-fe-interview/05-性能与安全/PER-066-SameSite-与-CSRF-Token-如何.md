---
title: [PER-066] SameSite 与 CSRF Token 如何组合成防御矩阵？各场景怎么选？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-066：SameSite 与 CSRF Token 如何组合成防御矩阵？各场景怎么选？

**答**：
- SameSite=Strict 最强但影响外链登录态（从 Google 点进来未登录），Lax 是兼容默认（GET 顶级导航带 Cookie，跨站 POST 不带），None 必须配 Secure。
- Lax 覆盖了绝大多数 CSRF 场景（跨站 POST/表单不带 Cookie），但**同站子域**攻击和部分老浏览器不认 SameSite，所以高敏操作仍要叠加 CSRF Token 或自定义头校验。
- 组合矩阵：普通浏览接口用 Lax；支付/改密等写操作用 Lax + CSRF Token + 二次确认；需要被第三方嵌入调用时 None + Secure + Token；完全站内操作可 Strict。
- 额外兜底：校验 Origin/Referer 头、写操作统一走 JSON + 自定义头（跨站表单发不出自定义头）。

```nginx
# nginx：按场景下发不同 SameSite 策略的 Cookie
server {
    listen 443 ssl;
    server_name example.com;

    # 普通会话：Lax 平衡体验与安全
    add_header Set-Cookie "sid=$upstream_http_x_sid; Path=/; HttpOnly; Secure; SameSite=Lax" always;

    # 敏感操作会话：Strict，完全站内
    location /payment/ {
        add_header Set-Cookie "pay_sid=$upstream_http_x_pay_sid; Path=/payment; HttpOnly; Secure; SameSite=Strict" always;
        proxy_pass http://app;
    }
}
```

```javascript
// 前端配合：写操作统一 JSON + 自定义头 + CSRF Token，跨站表单无法伪造
const csrfMeta = document.querySelector('meta[name="csrf-token"]');
const csrfToken = csrfMeta?.content;

async function apiWrite(path, body) {
  return fetch(path, {
    method: 'POST',
    credentials: 'same-origin',           // 只在同站携带 Cookie
    headers: {
      'Content-Type': 'application/json', // 跨站表单发不出 application/json
      'X-CSRF-Token': csrfToken,          // 服务端校验与会话绑定的 token
      'X-Requested-With': 'XMLHttpRequest',
    },
    body: JSON.stringify(body),
  }).then((r) => { if (r.status === 403) location.assign('/login?reason=csrf'); return r; });
}
apiWrite('/api/orders', { sku: 'A1', qty: 1 });
```
