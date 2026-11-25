---
title: [AGT-384] Agent 间协商——自动化谈判（排期/资源）怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-384：让 Agent 代表团队自动协商（排期/资源分配）怎么设计？

**答**:
- 协商框架：各方 Agent 携带"授权边界"（底线/可让步项/目标——由人设定并锁定，AGT-283 权限思想的协商版）→ 多轮提案交换（结构化提案：方案/代价/收益，AGT-425 选项式提案的机器版）→ 共识或升级（超轮次/超授权→转人裁决）。
- 诚实约束：协商 Agent 不得虚报（谎称资源紧张压对方）——提案必须基于可验证数据（排期依据/用量数据），协商记录全留痕可审计——自动化协商的可信度依赖诚实性设计。
- 人监督点：协商起始（授权确认）与结论（共识需人批准才生效——Agent 协商只到"共识草案"为止）；协商过程对双方团队可见（透明防暗箱）。
- 适用边界：结构化清晰的协商（排期/配额/SLA）适合自动化；价值观/战略类协商不适合——自动化协商的价值在把人类从重复拉扯中解放，前提是规则可结构化。

```javascript
async function negotiate(a, b, issue) {
  let round = 0;
  while (round++ < MAX_ROUNDS) {
    const pA = await a.propose(issue, log);     // 授权边界内
    const verdict = await b.evaluate(pA);
    if (verdict.accept) break;
    issue = verdict.counter;
  }
  return round <= MAX_ROUNDS
    ? { draft: issue, pendingHumanApproval: true }  // 共识草案
    : escalate(issue, log);                          // 转人
}
// 提案必附可验证数据；全程留痕审计。
```
