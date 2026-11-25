---
title: [AGT-181] 自研 Agent 框架 vs 采用开源框架，团队怎么决策？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-181：自研 Agent 框架 vs 采用开源框架，团队怎么决策？
**答**：
- 决策变量五项：场景复杂度（线性 RAG 用库、复杂状态机可考虑图框架或自研）、团队规模与运维能力（框架省的开发人力 vs 自研多的运维负担）、可控性要求（金融/强合规倾向自研薄层）、迭代速度压力（POC 阶段必用框架快速验证）、人才市场（框架经验好招人）。
- 推荐路径：「POC 用框架 → 生产评估：若 80% 逻辑是框架胶水且复杂度在状态管理，迁移到自研薄 Runtime；若复杂度在检索/数据管线，留在框架只自研外围」。
- 自研的合理边界：自研「Runtime 内核」（消息循环/状态/checkpoint/trace，约 1-2k 行可控代码）+ 复用「生态件」（向量库客户端/评测工具/网关），而不是从零造 RAG 库。
- 反面信号：团队为「少一个依赖」自研了 5000 行没人敢改的编排器；或为「多一个能力」把 LangChain 私有 monkey-patch——两个方向都是失衡。

```typescript
// 决策评分器：把框架 vs 自研的权衡做成可计算
interface TeamContext {
  scenarioComplexity: 'linear_rag' | 'multi_step' | 'complex_state';
  teamSize: number; platformTeam: boolean;      // 是否有平台组承接运维
  complianceCritical: boolean;
  timeToMarketWeeks: number;
  existingFrameworkExp: number;                 // 团队框架经验 0-5
}

export function decideBuildVsFramework(ctx: TeamContext): { choice: 'framework' | 'hybrid' | 'build'; rationale: string } {
  const frameworkScore =
    (ctx.scenarioComplexity === 'linear_rag' ? 3 : ctx.scenarioComplexity === 'multi_step' ? 2 : 1) +
    (ctx.platformTeam ? 1 : 0) +
    (ctx.timeToMarketWeeks <= 8 ? 2 : 0) +
    ctx.existingFrameworkExp * 0.4 +
    (ctx.complianceCritical ? -2 : 0);

  if (frameworkScore >= 5) return { choice: 'framework', rationale: '复杂度可控、有平台运维与时间压力：直接用框架，把人力花在评测与数据上' };
  if (frameworkScore >= 3) return { choice: 'hybrid', rationale: '自研薄 Runtime 内核（循环/状态/trace）+ 生态件（向量库/评测/网关），框架留在 POC 层' };
  return { choice: 'build', rationale: '强合规或复杂状态机：自研内核保证可控性，但必须配上 checkpoint/trace/评测三件套，否则自研即裸奔' };
}
```

---

## 三十一、综合与前瞻
