---
title: [PER-072] 接口幂等与防重放如何实现？nonce + 时间戳 + 签名的完整链路是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-072：接口幂等与防重放如何实现？nonce + 时间戳 + 签名的完整链路是什么？

**答**：
- 三要素分工：**时间戳**限制请求有效期（如 5 分钟窗口）、**nonce** 保证窗口内唯一（服务端去重）、**签名**保证参数不可篡改。
- 幂等与防重放是两件事：防重放拒绝“同一请求到达两次”，幂等保证“业务上重复提交只生效一次”（下单用客户端幂等键 idempotencyKey 落库唯一索引）。
- 签名串要覆盖方法、路径、排序后的参数、时间戳、nonce，密钥优先不下发浏览器，改为服务端网关代理签名。
- 前端还要做**交互层防重**：提交按钮 loading + 禁用，双击不产生第二个请求。

```javascript
// 前端：幂等提交封装 —— 客户端幂等键 + 防重放头
import { createHmac } from './hmac-shim'; // WebCrypto 封装

async function submitOrder(order) {
  const idempotencyKey = order.clientOrderId ?? crypto.randomUUID(); // 幂等键：重试复用同一个
  const ts = Date.now();
  const nonce = crypto.randomUUID();
  const signStr = [order.sku, order.qty, ts, nonce, idempotencyKey].join('&');
  const signature = await createHmac(signStr);

  const res = await fetch('/api/orders', {
    method: 'POST',
    headers: {
      'Idempotency-Key': idempotencyKey, // 服务端唯一索引，重复请求返回首次结果
      'X-Timestamp': String(ts),          // 超过 300s 拒绝
      'X-Nonce': nonce,                   // 服务端窗口内去重
      'X-Signature': signature,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(order),
  });
  if (res.status === 409) return res.json(); // 重复提交，返回首次订单
  if (!res.ok) throw new Error('order failed');
  return res.json();
}

// 交互层防重：按钮 loading 期间忽略后续点击
let submitting = false;
document.querySelector('#submit').addEventListener('click', async (e) => {
  if (submitting) return;
  submitting = true; e.target.disabled = true;
  try { await submitOrder({ sku: 'A1', qty: 1 }); }
  finally { submitting = false; e.target.disabled = false; }
});
```

```javascript
// 服务端（Express + Redis）：验签与 nonce 去重
app.post('/api/orders', async (req, res) => {
  const { 'x-timestamp': ts, 'x-nonce': nonce, 'x-signature': sig, 'idempotency-key': idem } = req.headers;
  if (Math.abs(Date.now() - Number(ts)) > 300000) return res.status(400).json({ msg: 'expired' });
  const expected = signHmac(SECRET, [req.body.sku, req.body.qty, ts, nonce, idem].join('&'));
  if (sig !== expected) return res.status(401).json({ msg: 'bad signature' });
  if (!(await rds.set(`nonce:${nonce}`, '1', { NX: true, EX: 300 }))) {
    return res.status(400).json({ msg: 'replayed' }); // nonce 已存在，重放拒绝
  }
  const exists = await db.query('SELECT 1 FROM orders WHERE client_order_id = $1', [idem]);
  if (exists.rowCount) return res.status(409).json(exists.rows[0]); // 幂等命中返回首次结果
  const order = await db.query('INSERT INTO orders (client_order_id, sku, qty) VALUES ($1,$2,$3) RETURNING *', [idem, req.body.sku, req.body.qty]);
  res.json(order.rows[0]);
});
```
