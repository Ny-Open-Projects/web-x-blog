---
title: [SCN-102] 老的 JSONP 接口被安全扫描标记（回调名任意注入 + 天然带 Cookie），如何平滑迁移？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-102：老的 JSONP 接口被安全扫描标记（回调名任意注入 + 天然带 Cookie），如何平滑迁移？
**答**：
- JSONP 两大风险：回调名注入 XSS（服务端把 callback 参数直接拼进 JS）、跨站 GET 天然携带 Cookie 造成数据泄露。方向是整体迁到 CORS/fetch。
- 平滑迁移：请求封装层按接口配置选择通道（已迁移走 fetch，未迁移走 JSONP），逐接口切量；JSONP 存量实现先加回调名白名单校验止血。
- 服务端 CORS 配置白名单 origin + credentials 规则，绝不能图省事配 `*`。

```javascript
// JSONP -> fetch 迁移：封装统一入口，接口级灰度切换
const FETCH_ENABLED = new Set(['/api/user/info']);   // 已迁移接口列表

export function request(api, params) {
  if (FETCH_ENABLED.has(api)) return fetchJSON(api, params);   // 新通道
  return jsonp(api, params);                                    // 未迁移走老通道
}

function fetchJSON(api, params) {
  return fetch(`${api}?${new URLSearchParams(params)}`, {
    credentials: 'include',                     // 跨域带 cookie
  }).then((r) => {
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return r.json();
  });
}

// 存量 JSONP 止血：随机回调名 + 格式校验，防回调注入 XSS
function jsonp(api, params) {
  const cb = `__jp${Math.random().toString(36).slice(2)}`;
  if (!/^__jp[a-z0-9]+$/.test(cb)) throw new Error('invalid callback');
  return new Promise((resolve, reject) => {
    window[cb] = resolve;
    const s = document.createElement('script');
    s.src = `${api}?${new URLSearchParams({ ...params, callback: cb })}`;
    s.onerror = () => reject(new Error('jsonp failed'));
    s.onload = () => { delete window[cb]; s.remove(); };
    document.head.appendChild(s);
  });
}
```
