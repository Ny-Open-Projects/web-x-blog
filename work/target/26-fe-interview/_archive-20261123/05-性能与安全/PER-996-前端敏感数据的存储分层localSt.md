---
title: [PER-996] 前端敏感数据的存储分层：localStorage 会话风险与替代方案
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-996：前端敏感数据的存储分层：localStorage 会话风险与替代方案

**答**：
- 风险：XSS 一旦发生，localStorage 的 token 全裸奔；cookie HttpOnly 则 JS 读不到但可携带，配合 CSRF 防护使用。
- 分层：高敏 token → HttpOnly Cookie（SameSite=Lax/Strict）；普通 UI 状态 → sessionStorage；长期偏好 → localStorage（非敏感）。
- 深水：必须在 JS 用的短期凭证放内存 + 定时刷新（闭包持有），页面刷新走 Cookie 换新，避免落盘。
- 泄漏面盘点：打包产物里硬编码的密钥/内部 URL 用构建期扫描清除。

```javascript
// 内存态 token 管理
let accessToken = null;                       // 不落盘
export const auth = {
  set(t) { accessToken = t; },
  get() { return accessToken; },
  async refresh() {
    const r = await fetch('/auth/refresh', { credentials: 'include' });
    accessToken = (await r.json()).token;     // Cookie HttpOnly 换新
  },
};
// 刷新竞态：并发请求 401 时共享同一个 refresh Promise
let refreshing = null;
export function refreshOnce() { return refreshing ??= auth.refresh().finally(() => refreshing = null); }
```
