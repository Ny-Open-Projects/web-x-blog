---
title: [PER-1129] 手写一个nonce 生成与注入校验器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1129：手写一个nonce 生成与注入校验器

**答**：
- 需求：实现 nonceManager。create() 每请求生成 16 字节 base64 nonce 并记录（带 60s 过期）；validate(nonce) 校验存在且未过期（校验后删除，一次性使用）；middleware(req, res, next) 挂 res.locals.nonce 与 CSP 头；register(scriptEl) 前端侧校验 script 的 nonce 与 meta 中一致才执行标记。
- 边界：validate 过期/不存在/已用返回 false；并发生成不冲突；过期 nonce 定期清理（惰性清理即可）。
- 评分点：生成与过期；一次性消费；CSP 头注入；前端校验

```javascript
function nonceManager({ ttl = 60_000 } = {}) {
  const store = new Map();                                 // nonce -> expireAt
  function clean() {
    const now = Date.now();
    for (const [k, t] of store) if (t < now) store.delete(k);
  }
  return {
    create() {
      clean();
      const n = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(16))));
      store.set(n, Date.now() + ttl);
      return n;
    },
    validate(n) {
      const t = store.get(n);
      if (!t || t < Date.now()) return false;
      store.delete(n);                                     // 一次性
      return true;
    },
    middleware(req, res, next) {
      res.locals.nonce = this.create();
      res.setHeader('Content-Security-Policy',
        `script-src 'nonce-${res.locals.nonce}' 'strict-dynamic'; object-src 'none'`);
      next();
    },
  };
}
// 前端 register：脚本加载器执行前校验 meta nonce 一致性
function register(scriptEl, metaNonce) {
  if (scriptEl.nonce !== metaNonce) throw new Error('nonce 不匹配，拒绝执行');
  return scriptEl;
}
```
