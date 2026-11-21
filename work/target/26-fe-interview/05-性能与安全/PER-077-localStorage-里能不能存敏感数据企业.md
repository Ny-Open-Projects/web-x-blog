---
title: [PER-077] localStorage 里能不能存敏感数据？企业级规范怎么定？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-077：localStorage 里能不能存敏感数据？企业级规范怎么定？

**答**：
- 结论：**access token、身份证、手机号明文、支付凭证不入 localStorage**——它对同源任意 JS 可读、不过期、被 XSS 一锅端，且随设备持久化。
- 分级规范：UI 偏好/主题/已读标记可存；短期会话数据用 sessionStorage；token 走内存 + HttpOnly Cookie；确需本地保存的业务数据先脱敏或加密，并设置过期清理。
- 存储前问三个问题：泄露后影响是什么？有没有更安全的载体（Cookie/Closure/服务端）？生命周期是否可控？
- 落地手段：封装统一 storage 模块禁用裸 `localStorage.setItem`（lint 规则拦截），敏感字段写入前脱敏或走加密通道。

```javascript
// 统一 storage 模块：分级 + 过期 + 敏感字段拦截
const SENSITIVE_KEYS = /^(token|jwt|idCard|password|accessToken|refreshToken|phone|mobile)$/i;

export const safeStorage = {
  set(key, value, { ttlMs, level = 'public' } = {}) {
    if (SENSITIVE_KEYS.test(key)) {
      // 硬约束：敏感键禁止落盘，token 走内存/Cookie，其余只允许内存
      throw new Error(`[security] 不允许在 storage 存储敏感键 ${key}`);
    }
    const payload = { v: value, level, exp: ttlMs ? Date.now() + ttlMs : null };
    const store = level === 'session' ? sessionStorage : localStorage;
    store.setItem(key, JSON.stringify(payload));
  },
  get(key) {
    const raw = (sessionStorage.getItem(key) ?? localStorage.getItem(key));
    if (!raw) return null;
    const p = JSON.parse(raw);
    if (p.exp && Date.now() > p.exp) { this.remove(key); return null; } // 过期即清理
    return p.v;
  },
  remove(key) { localStorage.removeItem(key); sessionStorage.removeItem(key); },
};

safeStorage.set('theme', 'dark', { ttlMs: 30 * 24 * 3600 * 1000 }); // 允许
safeStorage.set('accessToken', 'eyJ...', {}); // 直接抛错，阻断敏感落盘
```
