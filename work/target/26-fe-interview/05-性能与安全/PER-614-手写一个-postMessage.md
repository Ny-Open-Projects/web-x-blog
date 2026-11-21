---
title: [PER-614] 手写一个 postMessage 安全封装：发送端强制 targetOrigin、接收端 schema 校验 + 消息签名防伪造
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-614：手写一个 postMessage 安全封装：发送端强制 targetOrigin、接收端 schema 校验 + 消息签名防伪造

**答**：
- 完整封装：发送端 `safePost(win, msg, targetOrigin)` 禁止 '*'；接收端校验 origin 白名单 + 消息带时间戳与 HMAC 签名（同源密钥）+ schema 类型校验，防止伪造与重放。
- 要点：签名密钥不能在前端硬编码——对于真正需要防伪造的场景，用消息里带一次性 nonce，接收方回调确认的握手替代；本实现演示骨架，实际密钥管理见前端加密边界卡。
- 边界：null origin（sandbox iframe）场景显式允许 `'null'` 并用 nonce 校验；重放防护靠时间戳窗口（5 分钟）+ nonce 去重。
- 评分点：重放防护与 null origin 特例。

```javascript

const W = 5 * 60 * 1000, seen = new Set();
function safePost(win, type, payload, targetOrigin) {
  if (targetOrigin === '*') throw new Error('targetOrigin 禁止 *');
  const msg = { type, payload, ts: Date.now(), nonce: crypto.randomUUID() };
  win.postMessage({ ...msg, sig: sign(msg) }, targetOrigin);
}
window.addEventListener('message', (e) => {
  if (!ALLOWED_ORIGINS.includes(e.origin) && e.origin !== 'null') return; // null 仅限 sandbox
  const m = e.data;
  if (!m || typeof m.type !== 'string' || Date.now() - m.ts > W) return;  // 过期重放
  if (seen.has(m.nonce)) return; seen.add(m.nonce);                       // nonce 去重
  if (!SIGNATURE_OK(m)) { report('postmessage-forged', m); return; }      // 签名校验
  if (!SCHEMA[m.type]?.safeParse(m.payload).success) {                    // schema 校验
    report('postmessage-schema', m); return;
  }
  handle(m);
});
function sign(m) { return hmac(JSON.stringify(m), window.__msgKey); }     // 密钥见加密边界卡
```
