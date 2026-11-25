---
title: [MFW-544] 元框架安全模型：Server Action 的 CSRF 防护与 Origin 校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-544：Server Action 的 CSRF 防护与 Origin 校验

**答**:
- Action 端点的 CSRF 面：Action = POST 到同源 URL——CSRF 攻击者可构造跨站 POST（form action 指向你的 action 端点 + 自动提交）——防线：**Origin/Host 头校验**（框架默认：Action 请求的 Origin 必须匹配 Host——跨站表单的 Origin 是攻击者域 → 拒绝）。
- Origin 校验的边界：同站子域攻击（evil.app.com vs app.com——子域劫持可伪造同站 Origin）→ 需要 token 层（session 内嵌 action token）或严格 CSP；「Origin 校验是第一道、不是唯一道」。
- Action 参数的注入面：Flight body 的反序列化——「恶意 payload 的反序列化风险」= 深度限制 + 类型白名单（RBL-502 边界的攻击者视角）；「prototype pollution」在反序列化中的防护（__proto__ 键过滤）。
- 认证上下文：action 里的 session（cookies() 读取——action 与页面同请求上下文；「action 的权限校验」不能省：前端隐藏按钮 ≠ 后端不校验（RBL-803 权限在 server）。
- 追问钩子：为什么 Action 的 CSRF 防线用「Origin 校验」而不是「CSRF token」？——token 模型（server 发 token + client 回传）需要每个表单注入 token（渐进增强的表单 RBL-512 要 SSR 生成）；Origin 校验零代码（框架层统一）且对渐进增强透明；但 Origin 不能防子域攻击与反代场景——「框架默认防线 + 业务补充 token」的分层，防线选择与攻击面匹配（RBL-944 风险锚点的技术版）。

```javascript
// 框架层的 Origin 校验（概念）
function actionGuard(req) {
  const origin = req.headers.get('origin');
  const host = req.headers.get('host');
  // 1) 无 Origin（同源 fetch 某些场景）→ 放行（POST 同源）
  // 2) Origin ≠ Host → 403（CSRF 拒绝）
  if (origin && new URL(origin).host !== host)
    return new Response('CSRF blocked', { status: 403 });
}
// action 内的权限校验（不可省略）
'use server';
export async function deleteAccount() {
  const session = await auth();                          // 服务端校验：前端隐藏 ≠ 无权限
  if (!session) throw new Error('Unauthorized');
  await db.accounts.delete(session.userId);
}
// 反序列化防护：__proto__ 过滤
function sanitizeFlightArgs(obj) {
  for (const k of Object.keys(obj))
    if (k === '__proto__' || k === 'constructor') delete obj[k];   // 原型污染
  return obj;
}
```
