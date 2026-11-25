---
title: [NODE-687] 开放平台（API 网关/签名/配额）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-687：开放平台怎么做？
**答**：
- 签名协议：请求签名（appKey + 时间戳 + nonce + 参数摘要 HMAC——防重放/防篡改，SCN-联想-567 token 绑定语义）；nonce 去重（Redis SETNX——重放窗口）。
- 配额与计费：租户配额（SCN-NODE-678 多租户配额）、用量计量（调用计量 → 计费——SCN-NODE-661 计量同源）、超配额策略（429 + 升级引导）。
- API 治理：版本化（v1/v2 并存——SCN-OPS-245 兼容期）、限流分级（免费/付费档）、文档与 SDK 自动生成（OpenAPI 单源——SCN-ENG-247）。
- 安全边界：回调签名（开放平台主动通知开发者——通知也验签）、数据权限（开发者申请的 scope 授权——OAuth scope 模型）。
- 追问钩子：为什么开放平台的「回调通知也要签名」——开发者验证「通知真的来自平台」（防伪造回调触发开发者侧错误业务动作）；签名协议双向对称（平台验开发者请求、开发者验平台通知）——信任链在每个方向都要闭合，单向信任是开放平台的经典漏洞。

```javascript
// 请求验签
const sig = hmac(appSecret, `${method}\n${path}\n${ts}\n${nonce}\n${paramsDigest}`);
if (!timingSafeEqual(sig, req.headers['x-sign']) || nonceUsed(nonce))
  return res.status(401).json({ code: 'SIGN_INVALID' });   // 防重放 + 防篡改
// 回调通知签名
notify(devUrl, payload, { sign: hmac(devSecret, JSON.stringify(payload)) });
```
