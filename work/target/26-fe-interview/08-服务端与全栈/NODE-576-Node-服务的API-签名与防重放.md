---
title: [NODE-576] Node 服务的 API 签名与防重放（App 端到端）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-576：API 签名与防重放
**答**:
- 目标：防止抓包重放/参数篡改/未授权调用（App API 防护——比 Web 多一层：客户端可逆向，密钥不能明文内置）。
- 签名协议：请求签名（method+path+sorted params+ts+nonce → HMAC(secret)——服务端同算法校验 NODE-363 timingSafeEqual）、时间窗（±5min）+ nonce 去重（Redis——重放拦截 NODE-397 同款）。
- 密钥管理：设备级密钥（登录后下发设备密钥——而非全局内置密钥；传输用 TLS 保护下发光）、密钥轮换（定期/泄露应急）、动态密钥（会话派生密钥——登录会话密钥签名）。
- 分层定位：签名是"提高门槛"不是绝对防线（客户端可逆向——混淆/加固增加成本 ARC-158 分级；真正裁决靠服务端业务风控 NODE-456）。
- 观测：签名失败率（客户端版本签名 bug/攻击尝试分类）、重放拦截率。
```javascript
// 服务端校验
function verifySign(req) {
  const expected = hmac(deviceSecret(req.uid),
    [req.method, req.path, sortedParams(req), req.ts, req.nonce].join('\n'));
  if (!timingSafeEq(expected, req.sign)) throw new BadSign();
  if (Math.abs(now - req.ts) > 300e3) throw new Stale();         // 时间窗
  if (!(await nonce.put(req.nonce, '300s'))) throw new Replayed(); // nonce 去重
}
```
