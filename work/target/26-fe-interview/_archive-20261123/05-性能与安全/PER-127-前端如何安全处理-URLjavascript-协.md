---
title: [PER-127] 前端如何安全处理 URL？javascript: 协议、open 重定向、SSRF 要注意什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-127：前端如何安全处理 URL？javascript: 协议、open 重定向、SSRF 要注意什么？

**答**：
- URL 安全面三层：**协议白名单**（只放 http/https/mailto，拦 `javascript:`/`data:`/`vbscript:`）、**跳转白名单**（redirect/returnUrl 参数一律只允许站内相对路径）、**内网地址过滤**（前端渲染预览前过滤内网特征，真正校验在服务端）。
- 必须用 `new URL()` 统一解析后再判断，手写正则匹配字符串会被 URL 编码、协议相对地址（`//evil.com`）等变体绕过。
- 站内跳转优先保留相对路径，站外域名过白名单；`open()` 第二参传 `noopener` 防 tab-nabbing。
- SSRF 的主战场在后端，前端职责是不给后端送进内网 URL 的入口，并配合回显脱敏。

```javascript
// URL 安全面三层：协议白名单、跳转白名单、内部地址过滤
const ALLOWED_PROTOCOLS = new Set(['http:', 'https:', 'mailto:']);
const TRUSTED_HOSTS = new Set(['example.com', 'm.example.com']);

export function sanitizeUrl(input) {
  let u;
  try {
    u = new URL(input, location.origin); // 统一解析，杜绝编码变体绕过
  } catch {
    return '';
  }
  if (!ALLOWED_PROTOCOLS.has(u.protocol)) return ''; // 拦截 javascript: data: vbscript:
  if (u.hostname === location.hostname) return u.pathname + u.search; // 站内只留相对路径
  return TRUSTED_HOSTS.has(u.hostname) ? u.href : ''; // 站外过域名白名单
}

// 跳转白名单：SSO 回调、支付返回等一切 redirect 参数都过这里
export function safeRedirect(target, fallback = '/home') {
  const url = sanitizeUrl(target);
  if (!url || !url.startsWith('/') || url.startsWith('//')) return fallback; // 拒绝协议相对地址
  return url;
}

// SSRF 前端配合：渲染预览前过滤内网特征，服务端仍需二次校验
export function isPublicPreviewUrl(raw) {
  const u = new URL(sanitizeUrl(raw) || 'about:blank', location.origin);
  const blocked = [/^localhost$/i, /^127\./, /^10\./, /^192\.168\./, /^172\.(1[6-9]|2\d|3[01])\./, /\.internal$/i];
  return !blocked.some((re) => re.test(u.hostname));
}
```
