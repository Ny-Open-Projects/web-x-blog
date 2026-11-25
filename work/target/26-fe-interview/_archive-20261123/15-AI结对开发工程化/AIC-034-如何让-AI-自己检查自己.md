---
title: [AIC-034] 什么是「自我检查式 Prompt」（Self-Check）？让 AI 生成后自查一轮能提升多少质量？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-034：什么是「自我检查式 Prompt」（Self-Check）？让 AI 生成后自查一轮能提升多少质量？
**答**：
- Self-Check 是把「生成」和「验收」拆成两次调用：第一次产出代码，第二次以评审者身份对照需求清单逐项检查并给出修订版。
- 提升明显的原因：同一模型「写」和「审」的注意力分配不同，生成时的遗漏（边界、清理函数、错误处理）在带清单复审时容易被抓出来。
- 关键是检查清单要**具体**：不是「检查一下质量」，而是「① 是否处理了空数组 ② 异步是否清理 ③ 是否符合 TS strict」。
- 成本权衡：自查多一次调用约多 1~2 倍 token，适合高价值产出（公共组件、核心逻辑）；流水线小改动可跳过。
- 追问钩子：进阶做法是换一个模型/角色来审（跨模型交叉检查），减少「自己偏爱自己」的确认偏差。

```javascript
// 两段式：生成 → 自查修订
async function generateWithSelfCheck(requirement, checklist) {
  const draft = await callLLM(`实现以下需求：\n${requirement}`);
  const review = await callLLM(`
你是严格的代码评审员。对照清单逐项检查代码：
${checklist.map((c, i) => `${i + 1}. ${c}`).join('\n')}
对每项输出 PASS/FAIL 及原因，最后输出修订后的完整代码。
<code>${draft}</code>`);
  return { draft, review };
}
```
