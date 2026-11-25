---
title: [AIC-998] 遗留系统有大量「只可意会」的领域知识（老员工的潜规则），如何喂给 AI 辅助迁移又不失真？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-998：遗留系统有大量「只可意会」的领域知识（老员工的潜规则），如何喂给 AI 辅助迁移又不失真？
**答**：
- 领域知识大多「隐性」——结论：第一步是把它「外化」为可验证的资产：通过访谈老员工 + 挖掘 commit/工单/测试用例，把潜规则写成显式规则与案例。
- 外化要经过「验证」而非直接采信：老员工的记忆可能过时，写出的规则要用遗留代码的实际行为与历史数据交叉验证；有冲突时以代码与数据为准并标注争议。
- 喂给 AI 要「结构化 + 带出处」：规则条目附来源（哪次事故/哪个提交）与 applicability（适用模块），让 AI 知道何时用、并让人可追溯校验；避免一股脑塞聊天记录导致失真放大。
- 追问钩子：能提出「领域知识喂给 AI 的正确姿势是『人机协作共建知识库 + 定期校准』，而非一次性灌输——知识会演进，失真会累积」的候选人理解知识的动态性。

```typescript
// 领域知识条目：结构化 + 带出处 + 可验证
const knowledge = [
  { rule:'退款金额必须向下取整到分', source:'INC-1998事故', module:'refund', verified:true },
  { rule:'VIP用户跳过限流', source:'老员工口述', module:'limit', verified:false }, // 待验证
];
function usableKnowledge(kb, module) {
  return kb.filter(k=>k.module===module && k.verified) // 只喂已验证的
    .map(k=>`规则:${k.rule} (出处:${k.source})`);
}
console.log(usableKnowledge(knowledge,'refund'));
// 未验证条目进入待核清单，由人用代码/数据交叉验证后再入知识库
```
