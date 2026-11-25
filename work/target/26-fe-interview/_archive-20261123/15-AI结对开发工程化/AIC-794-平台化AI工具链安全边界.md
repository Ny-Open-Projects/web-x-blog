---
title: [AIC-794] 平台化 AI 工具链的安全边界如何设计
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-794：平台化 AI 工具链的安全边界如何设计

**答**：
- 结论先行：平台化后安全责任集中——平台必须建立清晰边界：模型调用不出域、prompt 数据脱敏、工具执行沙箱化、权限最小化、审计全留痕；边界之外的风险由平台兜底，而非每个业务方自己操心。
- 边界设计：1) 网络边界（模型网关白名单，禁止任意外连）；2) 数据边界（敏感信息出域前脱敏、审计日志脱敏存储）；3) 执行边界（Agent 工具在沙箱运行，限额超时）；4) 权限边界（RBAC，能力级授权）。
- 纵深防御：不依赖单点——即使某层失守，其他层仍能拦截；关键是「默认拒绝」而非「默认放行」。
- 追问钩子：为什么平台安全要「默认拒绝」？——平台被多业务共享，一次误放行影响面极大；白名单机制把风险收敛到显式授权的范围。

```javascript
// 默认拒绝：能力调用需显式授权
const ACL = { 'fe-team': ['complete', 'review'] };
function authorize(team, capability) {
  const allowed = ACL[team] ?? [];
  return allowed.includes(capability) ? { allow: true } : { allow: false, reason: 'default-deny' };
}
console.log(authorize('fe-team', 'review').allow);   // true（显式授权）
console.log(authorize('fe-team', 'db-write').reason); // default-deny
console.log(authorize('unknown', 'complete').allow);  // false（未知团队默认拒绝）
```
