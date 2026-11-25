---
title: [AIC-928] AI 产出一段「为什么这么实现」的决策依据，如何让这些依据随代码一起入库而不是散落在聊天记录里？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-928：AI 产出一段「为什么这么实现」的决策依据，如何让这些依据随代码一起入库而不是散落在聊天记录里？
**答**：
- 核心做法是把「决策依据」结构化成 ADR（架构决策记录）或代码旁注，与代码同 PR、同 commit 提交——结论：依据必须和代码同生命周期才不会失联。
- 在 prompt 中要求 AI 产出时附带「决策理由 + 被否方案 + 约束条件」（如「选X因为Y，没选Z因为不满足W」），把这些作为产出的一部分，而非事后补。
- 评审时人核对依据是否成立：依据入库的价值在于让半年后的人（或 AI）理解「当时为何这么选」，避免重复推翻或误改。
- 追问钩子：能提出「决策依据要可检索、与代码行号关联，并作为上下文供后续 AI 改动时读取」的候选人，把依据变成了活的上下文资产。

```typescript
// 决策依据结构化，随代码入库
const decision = {
  file:'src/price.ts', lines:'42-58',
  choice:'用整数分存储金额',
  reason:'避免浮点误差导致对账不平',
  rejected:[{ option:'浮点数 + toFixed', why:'边界仍会丢精度' }],
  constraints:['需与后端分单位对齐','大促峰值精度零容忍'],
};
function toComment(d) {
  return `/* ADR: ${d.choice}\n   why: ${d.reason}\n   rejected: ${d.rejected.map(r=>r.option+'('+r.why+')').join(', ')}\n*/`;
}
console.log(toComment(decision)); // 作为注释嵌入代码，与代码同 commit 入库
```
