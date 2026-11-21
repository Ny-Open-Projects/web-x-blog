---
title: [DP-300] 笔试题：手写请求重试与幂等键管理？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-300：笔试题：手写请求重试与幂等键管理？
**题目**：实现 submitOrder 的可靠提交：1) 幂等键生成（客户端 UUID，同一次提交重试共用）；2) 重试仅对网络错误/5xx（4xx 不重试）；3) 退避（指数+抖动）上限 3 次；4) 提交中防重复点击（锁）；5) 结果缓存（同幂等键重复请求直接返回首次结果）。
**评分点**：
- 幂等键作用域正确（一次用户操作一份，重试复用）。
- 重试白名单判定正确（只重试可重试错误）。
- 防重复锁与释放（成功/最终失败都释放）。
- 服务端幂等模拟（Map 键缓存响应）。
```javascript
const inflight = new Map();   // idemKey → promise（结果缓存）
let lock = false;
async function submitOrder(order) {
  if (lock) throw new Error('submitting');             // 4) 防重复点击
  lock = true;
  const idemKey = crypto.randomUUID();                 // 1) 一次操作一份
  try {
    return await retry(() => apiPost('/orders', { ...order, 'Idempotency-Key': idemKey }));
  } finally { lock = false; }
}
function apiPost(url, body) {
  const key = body['Idempotency-Key'];
  if (inflight.has(key)) return inflight.get(key);     // 5) 幂等缓存
  const p = fetch(url, { method: 'POST', body: JSON.stringify(body), headers: { 'Idempotency-Key': key } })
    .then(async (r) => {
      if (r.ok) return r.json();
      const err = new Error(`${r.status}`);
      err.retryable = r.status >= 500;                 // 2) 4xx 不重试
      throw err;
    });
  inflight.set(key, p);
  return p;
}
async function retry(fn, times = 3) {                  // 3) 指数退避+抖动
  for (let i = 0; i <= times; i++) {
    try { return await fn(); }
    catch (e) { if (i === times || !e.retryable) throw e;
      await new Promise(r => setTimeout(r, 300 * 2 ** i * (0.7 + Math.random() * 0.6))); }
  }
}
```
