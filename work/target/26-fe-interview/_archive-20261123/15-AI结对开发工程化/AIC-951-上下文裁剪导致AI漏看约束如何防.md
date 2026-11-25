---
title: [AIC-951] 为了省成本裁剪上下文，结果 AI 漏看了「必须处理空值」的约束导致线上 bug，如何防止？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-951：为了省成本裁剪上下文，结果 AI 漏看了「必须处理空值」的约束导致线上 bug，如何防止？
**答**：
- 根因是「把约束当普通上下文裁掉了」——结论：约束类信息必须进入不可裁剪白名单，与成本优化隔离。
- 工程手段：① 约束单独成段并标记 kind=constraint，裁剪器强制保留；② 裁剪后做「约束完整性校验」——检查所有已登记约束的关键词仍在最终上下文里，缺失则拒绝发送并告警。
- 流程手段：把「关键约束」纳入 prompt 模板的固定区（system 区），每次请求必带；约束变更需评审，避免悄悄丢失。
- 追问钩子：能提出「成本优化要有安全底线，白名单 + 完整性校验是底线守卫；省下的钱不能拿正确性换」的候选人有正确的风险意识。

```typescript
// 裁剪后校验关键约束是否仍在
const REQUIRED_CONSTRAINTS = ['必须处理空值','金额用整数分','禁止硬编码密钥'];
function verifyConstraints(finalContext) {
  return REQUIRED_CONSTRAINTS.filter(c => !finalContext.includes(c));
}
function sendWithGuard(context) {
  const missing = verifyConstraints(context);
  if (missing.length) throw new Error('约束缺失，拒绝发送: ' + missing.join(','));
  return context; // 安全后才发送
}
// 裁剪器产出 → sendWithGuard 校验 → 缺失即拦截
console.log(verifyConstraints('只说了用TS')); // ['必须处理空值','金额用整数分',...]
```
