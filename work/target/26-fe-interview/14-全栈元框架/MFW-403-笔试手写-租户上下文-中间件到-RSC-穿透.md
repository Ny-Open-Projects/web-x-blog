---
title: [MFW-403] 笔试：手写租户上下文全链穿透（middleware→RSC→Action）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-403：租户上下文穿透
**答**：实现 `tenantChain()`：1) middleware 解析 Host→tenantId，写入请求头 `x-tenant`（内部签名防伪造——HMAC(key, tenantId+ts)）；2) RSC/Action 侧 `getTenant()`：验签读头（伪造/过期→reject）；3) 缓存 key 工厂强制含租户（tk(tag, id) = `t:${tenant}:${tag}`——漏租户编译期不可能）；4) provide 测试助手（绕过 HTTP 直接注入上下文——单测友好）。

```javascript
import { headers } from 'next/headers'
import crypto from 'node:crypto'

const sign = (v) => crypto.createHmac('sha256', SECRET).update(v).digest('hex').slice(0, 16)

// middleware
export function stamp(req) {
  const t = parseHost(req.headers.get('host'))
  res.setHeader('x-tenant', t)
  res.setHeader('x-tenant-sig', sign(t))               // 网关内签名，外网不可造
}

// 服务端统一读口
export function getTenant() {
  const h = headers()
  const t = h.get('x-tenant'), s = h.get('x-tenant-sig')
  if (!t || s !== sign(t)) throw new Error('tenant context invalid')   // 伪造/丢头 fail-fast
  return t
}
// 缓存键工厂：租户进 key 的唯一合法路径
export const tk = (tag) => `t:${getTenant()}:${tag}`
// 测试
export const as = (tenant, fn) => seedHeaderss({ 'x-tenant': tenant, 'x-tenant-sig': sign(tenant) }, fn)
```
**评分点**：
- 内部签名头（应用层读到的租户不可被外部请求伪造——信任边界在网关）
- fail-fast 校验（无头/坏签名抛错而非回默认租户——默认值即串号源）
- 键工厂强绑（业务拿不到「无租户 tag」的构造路径）
- 测试注入助手（不经 HTTP 即可测租户逻辑）
