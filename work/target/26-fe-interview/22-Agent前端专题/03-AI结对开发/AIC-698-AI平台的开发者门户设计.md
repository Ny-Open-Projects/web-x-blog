---
title: [AIC-698] AI 平台为什么要有「开发者门户」？怎么设计？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-698：AI 平台为什么要有开发者门户？怎么设计？

**答**：
- 结论先行：**开发者门户 =「AI 能力的自助服务前台」——让团队自助发现、申请、试用、接入 AI 能力，而不是每次都找平台团队开后门**。门户是平台化「赋能」而非「代办」的界面（AIC-398 平台团队定位）。
- 门户核心功能：1) **能力目录**：展示可用能力（补全/审查/Agent/知识问答）及说明、适用场景、SLA；2) **自助接入**：申请 API key、配额、开通能力，走审批流自动化；3) **试用沙箱**：在门户里直接试用 prompt/模型效果，不用配置环境（AIC-299 试用评估）；4) **用量与成本看板**：团队看自己的消耗、配额、成本（AIC-691）；5) **文档与示例**：接入指南、最佳实践、prompt 模板库（AIC-686）。
- 为什么重要：1) **降低接入门槛**——不用懂平台内部就能用；2) **规模化**——平台团队不用被「帮我开个权限」的请求淹没；3) **治理前台化**——配额/审批/审计从后台规则变成用户可见的自助流程。
- 设计原则：自助优先、文档即产品、可视化用量——让开发者「自己就能搞定」，平台团队聚焦能力建设。
- 追问钩子：为什么「自助接入」对平台团队是解放而非失控？——因为自助不等于无治理——审批流、配额、审计仍在后台强制，只是前置到用户自助流程里；平台团队从「人工审批每件小事」中解放，同时治理强度不降——把「人情审批」变成「系统规则」。

```typescript
type Capability = { id: string; name: string; sla: string; requiresApproval: boolean };

class DevPortal {
  constructor(private caps: Capability[]) {}

  catalog() { return this.caps.map(c => ({ ...c, tryable: true })); }

  requestAccess(capId: string, user: string): { status: string; next: string } {
    const cap = this.caps.find(c => c.id === capId);
    if (!cap) return { status: 'rejected', next: '能力不存在' };
    // 自助：需审批的走自动审批流，无需审批的立即开通
    return cap.requiresApproval
      ? { status: 'pending', next: `已提交审批（${cap.name}），预计1个工作日` }
      : { status: 'granted', next: `${cap.name} 已开通，可直接在沙箱试用` };
  }
}

const portal = new DevPortal([
  { id: 'complete', name: '代码补全', sla: 'P95<100ms', requiresApproval: false },
  { id: 'agent', name: '编码Agent', sla: 'P95<5min', requiresApproval: true },
]);
console.log(portal.catalog().length === 2);
console.log(portal.requestAccess('complete', 'alice').status === 'granted');
console.log(portal.requestAccess('agent', 'alice').status === 'pending');
```
