---
title: [AGT-807] Agent 代用户调用下游系统，身份如何贯通（不能拿超级 token）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-807：Agent 代用户调用下游系统，身份如何贯通（不能拿超级 token）

**答**：
- 标准做法：用户 OAuth 授权 Agent 委托范围（scopes），Agent 调下游带「用户 token + agent 标识」（JWT 含 act: { sub: agentId } 声明），下游按用户权限鉴权——Agent 只是放大器不是超级用户。
- 委托范围最小化：只申请任务所需 scopes（读工单不申请删工单）；scope 超出任务需要时动态申请授权。
- 审计贯通：下游系统看到的操作者=用户+代执行 Agent 标识，全链路审计可分清"用户干的还是 Agent 代干的"。

```javascript
function agentToken(userToken, agentId, scopes) {
  const claims = decode(userToken);
  return sign({ ...claims,
    act: { sub: agentId },                        // 代执行声明
    scope: scopes.join(' '),                      // 最小委托
    jti: genId(), exp: claims.exp });             // 过期随用户token
}
// 下游校验：用户身份鉴权 + act 记审计
function verifyDownstream(token) {
  const c = decode(token);
  return { user: c.sub, viaAgent: c.act?.sub, scopes: c.scope };
}
```

