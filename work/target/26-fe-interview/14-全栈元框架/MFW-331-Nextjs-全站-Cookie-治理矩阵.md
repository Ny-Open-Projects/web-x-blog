---
title: [MFW-331] 全站 Cookie 治理矩阵（命名/属性/生命周期）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-331：Cookie 治理矩阵

**答**:
- 矩阵字段：{ name, 目的, 属主(端), 属性(Secure/HttpOnly/SameSite/Domain), 生命周期, 加密否, 清理时机 }——没有矩阵的站点 cookie 必然滋生（历史遗留 + 第三方乱种）
- 属性铁律：会话凭证 HttpOnly+Secure+Strict（或 Lax 若需跨导航）；跨子域共享用 Domain=.app.com 但限定名单（防子域应用互读敏感 cookie——subdomain takeover 面）；业务偏好类 SameSite=Lax 且禁止 HttpOnly（JS 需读）
- 生命周期治理：登出清理清单（枚举删除全部业务 cookie——漏一个就是串号源）；过期分层（access 15min / refresh 30d / 偏好 1y）；改名走版本后缀（v2 平行期双写双读迁移）
- 审计工具：构建期 grep setCookie 调用 ↔ 矩阵登记比对（未登记的 cookie 写入 CI 报错——治理靠门禁不靠记忆）

```javascript
// 登出清理（矩阵驱动生成）
const CLEAR = cookieMatrix.filter(c => c.目的 !== '偏好').map(c => c.name)
res.setHeader('Set-Cookie', CLEAR.map(n => `${n}=; Max-Age=0; Path=/; ${domainAttr(n)}`))
// CI：扫描 res.setHeader/Set-Cookie 与 storage.set → 比对矩阵，未登记 fail
```
