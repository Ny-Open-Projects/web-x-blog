---
title: [AIC-882] 一半代码是 AI 写的，出了 bug 算谁的？代码所有权怎么界定？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-882：一半代码是 AI 写的，出了 bug 算谁的？代码所有权怎么界定？
**答**：
- 核心原则：**AI 不承担所有权，提交者承担**。AI 是工具，人和工具的关系里，把代码合并进仓库的人对质量负全责——「AI 写的」不是免责理由。这跟「代码是实习生写的」一个道理：review 并合并的人负责。
- 但工程上要做**贡献归因**：通过 commit trailer / 血缘记录标记「哪些片段由 AI 生成、基于哪个模型和 prompt 版本」——目的不是追责到人，而是**统计与改进**（哪类 AI 产出容易出错、哪个 prompt 模板质量差）。
- 所有权分两层：**责任所有权**（人对合并的代码负责，清晰无争议）和**知识所有权**（谁真正理解这段逻辑——AI 生成的复杂逻辑可能没人真正懂，这是风险）。后者要靠「AI 生成的关键逻辑必须有 owner 能讲清楚」来保证。
- 落地：代码 review 要求「你合并的代码你要能解释」；对 AI 生成的高风险逻辑强制要求补充注释/测试；事故复盘看「为什么人没发现问题」而不是甩锅 AI。
- 追问钩子：能区分「责任所有权（人负责）」和「知识所有权（要有人真懂）」，并指出后者才是 AI 时代真正的风险，候选人思考有深度。

```typescript
type Change = { author: string; aiGenerated: boolean; modelVersion?: string;
  reviewedBy: string; domain: string; ownerCanExplain: boolean };

function ownershipOf(c: Change) {
  return {
    accountable: c.reviewedBy || c.author,  // 责任归属：合并/review 的人
    aiAttribution: c.aiGenerated ? { model:c.modelVersion, tool:'AI' } : null,
    knowledgeRisk: c.aiGenerated && !c.ownerCanExplain,
    action: c.aiGenerated && !c.ownerCanExplain
      ? 'AI 生成的关键逻辑无人能讲清 → 要求补注释/测试或重写' : 'ok',
  };
}
console.log(ownershipOf({ author:'dev1', aiGenerated:true, modelVersion:'v2',
  reviewedBy:'lead', domain:'payment', ownerCanExplain:false }));
// accountable:'lead', knowledgeRisk:true —— 责任清晰，但知识所有权缺失是真风险
```
