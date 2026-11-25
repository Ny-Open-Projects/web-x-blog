---
title: [AGT-811] 平台接入企业 SSO（OIDC/SAML）与统一审计系统，要点是什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-811：平台接入企业 SSO（OIDC/SAML）与统一审计系统，要点是什么

**答**：
- SSO：OIDC 标准接入，token 内嵌部门/角色声明（组映射），会话与主站共享（单点登出 propagate）；服务账号（API 调用）走 client credentials 与人账号分离审计。
- 审计对接：所有治理事件（登录/工具调用/数据访问/策略拦截）输出标准审计事件流（CEF/OCSF 格式）对接企业 SIEM；审计事件不可篡改（append-only+哈希链）。
- 合规地图：哪些事件必须审计（数据导出/权限变更/策略绕过尝试）有明确清单，漏审计=合规缺陷。

```javascript
function auditEvent(evt) {
  const rec = { ...evt, ts: Date.now(),
    prev: chain.lastHash, hash: hash(JSON.stringify(evt) + chain.lastHash) };
  chain.append(rec);                              // 哈希链防篡改
  siem.emit(toOCSF(rec));
}
const MUST_AUDIT = ['data.export', 'role.change',
  'policy.bypass_attempt', 'tool.destructive'];
```

