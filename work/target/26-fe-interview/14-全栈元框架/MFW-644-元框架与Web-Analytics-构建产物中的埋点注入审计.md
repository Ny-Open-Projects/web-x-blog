---
title: [MFW-644] 构建产物中的埋点注入审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-644：埋点注入审计

**答**:
- 埋点的构建审计维度：1) **覆盖审计**（关键路径的埋点存在性：下单流程的 track 调用 ⊆ 事件 schema——「漏埋」的检测：关键 action 无对应 track = 漏埋 RBL-938 监控盲区）；2) **schema 合规**（事件字段 ⊆ schema registry——未注册字段 = 脏数据 RBL-601 的 schema 校验）；3) **PII 泄漏**（事件 payload 含 email/phone/token——最小化违规 RBL-601）；4) **重复埋点**（同事件同位置多次 track——数据膨胀）。
- 审计的数据源：源码扫描（track('event') 调用点提取）× 事件 schema registry（对比）——「schema registry 是埋点的契约」（事件名/字段的白名单——类型化埋点（typed track）让 lint 可查）。
- typed track 的工程：`track('order_created', schema)`——schema 校验在编译期（TS 类型 = 埋点的 schema registry 前置 RBL-946 推理链的埋点版）。
- 追问钩子：为什么「typed track」比「schema registry 事后审计」更有效？——事后审计 = CI 红灯（发现问题在 PR 后）；typed = 编译期即报（字段拼错/类型错即时可见）；「schema 的类型化」让埋点与代码同生命周期（schema 变更 → 编译报错列出所有不合规埋点——推理链 RBL-926 的埋点版）；事后审计作为兜底（外部注入的埋点/动态事件名）。

```typescript
// typed track（编译期 schema）
type EventSchema = {
  order_created: { orderId: string; value: number };
  page_view: { path: string };
  product_viewed: { productId: string; source: string };
};
declare function track<K extends keyof EventSchema>(
  event: K, data: EventSchema[K]): void;
// track('order_created', { orderId: '1' });             ← 编译错：缺 value
// track('order_craeted', {...});                        ← 编译错：事件名拼错
// 构建审计（兜底）
function auditTracking(code: string, registry: Map<string, string[]>) {
  const findings = [];
  for (const m of code.matchAll(/track\(\s*['"](\w+)['"]\s*,\s*\{([^}]*)\}/g)) {
    const [, event, fields] = m;
    if (!registry.has(event))
      findings.push({ event, type: 'unregistered-event' });
    for (const f of fields.matchAll(/(\w+)\s*:/g))
      if (!registry.get(event)?.includes(f[1]))
        findings.push({ event, field: f[1], type: 'unregistered-field' });
    if (/email|phone|token/i.test(fields))
      findings.push({ event, type: 'pii-leak' });
  }
  return findings;
}
```
