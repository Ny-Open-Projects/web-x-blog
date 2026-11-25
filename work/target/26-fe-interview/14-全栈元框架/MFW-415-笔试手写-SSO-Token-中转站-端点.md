---
title: [MFW-415] 笔试：手写 SSO 一次性交换码端点
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-415：SSO 中转站
**答**：实现 IdP 侧 `createCodeBroker(authn, { ttl = 10_000 } = {})`：1) `POST /issue`（已登录中心域）→ { code, redirectTo}（code=随机 128bit，存 { uid, target, exp, used:false }，目标域必须在白名单）；2) `POST /exchange { code, clientSecret }`（目标域后端调用）→ 校验（存在/未过期/未用/secret 匹配/域匹配）→ 返回 { userId, sessionSeed }→标记 used（单次）；3) 重放检测：used 命中 → 安全告警（可能是窃取重放——不只拒绝）；4) 全端点限流（code 猜测面防护——128bit 熵 + 速率双保险）。

```javascript
export function codeBroker(authn, { keys, allow = ['shop.app.com', 'pay.app.com'] } = {}) {
  const codes = new Map()   // code → { uid, target, exp, used }
  return {
    'POST /issue': async (req) => {
      const user = await authn.require(req)                     // 中心域会话
      const { target } = await body.json()
      if (!allow.includes(target)) return 400('target not registered')   // 开放重定向收敛
      const code = crypto.randomBytes(16).toString('base64url') // 128bit 熵
      codes.set(code, { uid: user.id, target, exp: Date.now() + 10_000, used: false })
      return { code, redirectTo: `https://${target}/sso/cb?code=${code}` }
    },
    'POST /exchange': async (req) => {
      const { code, clientSecret, target } = await body.json()
      if (!constantTimeEq(secretFor(target), clientSecret)) return 401()
      const rec = codes.get(code)
      if (!rec || rec.exp < Date.now()) return 400('invalid/expired')
      if (rec.used) { audit.alert('code-replay', { code: mask(code)); return 400('used') }  // 重放=告警
      rec.used = true
      return { userId: rec.uid, seed: mintProductSession(rec.uid, target) }
    },
  }
}
```
**评分点**：
- 128bit 熵 + 10s TTL + 单次消费（三重窗口收窄重放面）
- 目标域白名单（开放重定向收敛到注册表）+ secret 常时比较
- 重放不只 4xx——安全审计告警（被动拒绝不如主动发现）
- 会话种子而非直发 token（目标域自行建域内会话——信任链清晰）
