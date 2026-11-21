---
title: [PER-617] 手写一个 CSRF Token 双提交（Double-Submit）实现：无状态校验 + Token 与会话绑定防换用
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-617：手写一个 CSRF Token 双提交（Double-Submit）实现：无状态校验 + Token 与会话绑定防换用

**答**：
- 双提交模式：Token 同时放 cookie（`csrf=xxx`）与请求头/表单（`X-CSRF-Token: xxx`），服务端只比对两者一致——不需要存储（无状态），因为攻击者无法跨域读到 cookie 也无法设置目标域 cookie（除非有子域注入点）。
- 绑定升级：纯双提交的弱点是"cookie 被注入"（子域 XSS/子域 cookie 注入），升级为 `HMAC(sessionId)`——Token = 签名（会话 ID + 随机数），校验时验证签名与会话匹配，换会话即失效。
- 边界：cookie 必须非 HttpOnly（JS 要读）但配 SameSite；会话轮换（登录态变化）时 Token 要重发；子域注入风险要在 cookie 设 domain 收窄。
- 评分点：HMAC 绑定与轮换处理。

```javascript

// ---- 服务端下发 ----
function issueCsrf(sessionId) {
  const nonce = crypto.randomUUID();
  const token = `${nonce}.${hmac(sessionId + nonce, SECRET)}`;
  res.cookie('csrf', token, { sameSite: 'Lax' });          // 可读 cookie（无 HttpOnly）
  return token;
}
// ---- 服务端校验 ----
function verifyCsrf(req) {
  const cookieToken = req.cookies.csrf, headerToken = req.get('X-CSRF-Token');
  if (!cookieToken || cookieToken !== headerToken) return false;          // 双提交比对
  const [nonce, sig] = cookieToken.split('.');
  return hmac(req.session.id + nonce, SECRET) === sig;                    // 绑定会话
}
// ---- 前端拦截器 ----
const csrfToken = getCookie('csrf');
window.fetch = (input, init = {}) => {
  const method = (init.method ?? 'GET').toUpperCase();
  if (method !== 'GET') init.headers = { ...init.headers, 'X-CSRF-Token': csrfToken };
  return fetch(input, init);
};
// 会话轮换（登录/登出）-> 重新 issueCsrf 并刷新内存中的 token
```
