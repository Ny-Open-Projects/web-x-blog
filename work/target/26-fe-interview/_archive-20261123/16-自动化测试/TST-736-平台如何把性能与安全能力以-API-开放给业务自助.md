---
title: [TST-736] 平台如何把性能与安全能力以 API 开放给业务自助
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-736：平台如何把性能与安全能力以 API 开放给业务自助

**答**：
- 结论：能力开放=「统一 API 网关 + 能力目录 + 配额治理」，业务自助调用但平台守住资源与合规底线。
- 能力目录标准化：每个能力有明确入参/出参/SLA/计费，业务按目录发现而非私下找人。
- 网关做鉴权、限流、审计，高危能力（如高危漏洞扫描）需额外审批。
- 追问钩子：业务绕过平台直接调底层扫描器，如何治理？

```javascript
// 能力开放网关：鉴权 + 限流 + 审计
function gateway(capability, ctx, quota) {
  if (!ctx.roles.includes(capability.requiredRole)) return { ok: false, why: '无权限' };
  if (quota.used >= quota.limit) return { ok: false, why: '配额耗尽' };
  audit(ctx.team, capability.name);
  return { ok: true, endpoint: capability.endpoint };
}
function audit(team, cap) { /* 写审计日志 */ }
console.log(gateway(
  { name: 'deepScan', requiredRole: 'security', endpoint: '/scan' },
  { roles: ['dev'], team: 'A' }, { used: 0, limit: 10 }
)); // 无权限
```
