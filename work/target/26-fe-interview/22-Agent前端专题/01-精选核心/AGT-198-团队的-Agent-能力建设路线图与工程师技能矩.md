---
title: [AGT-198] 团队的 Agent 能力建设路线图与工程师技能矩阵怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-198：团队的 Agent 能力建设路线图与工程师技能矩阵怎么设计？
**答**：
- 技能矩阵三层四维：三层是会调用 → 会编排 → 会治理（与 AGT-120 体系呼应），四维是模型层（prompt/参数/评测）、工具层（function calling/MCP/沙箱）、数据层（RAG/记忆/向量库）、工程层（流式/状态/可观测/成本）——每个人在矩阵上定位，团队缺口一眼可见。
- 路线图分季度推进：Q1 全员到「会调用」（人人能做 demo + 评测意识）；Q2 骨干到「会编排」（2-3 人能交付生产 Agent）；Q3 建治理能力（评测集/成本看板/安全评审常态化）；Q4 平台化沉淀（内部脚手架 + 资产库，新项目起步成本趋零）。
- 前端团队的差异化定位：交互层（流式 UI/生成式 UI/HITL 体验）与工程质量层（状态/可观测/降级）是主场，先建立这两个维度的团队壁垒，再补模型层知识。
- 机制比培训重要：周度 AI 案例 share、每次事故复盘沉淀评测用例、内部「Agent 二十条」设计规约——能力靠practice 积累而非听课。

```typescript
// 工程师技能矩阵与团队缺口分析
type Level = 0 | 1 | 2 | 3;  // 0 未接触 1 会调用 2 会编排 3 会治理
type Dim = 'model' | 'tools' | 'data' | 'engineering';

interface Engineer { name: string; skills: Record<Dim, Level>; }

export function teamGapAnalysis(team: Engineer[], target: Record<Dim, { minLevel: Level; headcount: number }>) {
  const gaps: string[] = [];
  for (const [dim, req] of Object.entries(target) as [Dim, { minLevel: Level; headcount: number }][]) {
    const qualified = team.filter((e) => e.skills[dim] >= req.minLevel).length;
    if (qualified < req.headcount) {
      gaps.push(`${dim} 维度缺口：需 ${req.headcount} 人达到 L${req.minLevel}，当前 ${qualified} 人`);
    }
  }
  const avg = (d: Dim) => team.reduce((s, e) => s + e.skills[d], 0) / team.length;
  const roadmap = (Object.entries(avg) as [Dim, number][])
    .sort((a, b) => a[1] - b[1])                     // 最弱维度优先投入
    .map(([d, v]) => `${d}: 平均 L${v.toFixed(1)}，Q 优先建设`);
  return { gaps, roadmap, barbellRisk: avg.engineering > 1.5 && avg.model < 1 ? '警惕：工程强模型弱，容易做出「好看但不可靠」的 Agent' : null };
}

// 示例：前端团队的典型矩阵快照
const team: Engineer[] = [
  { name: 'A', skills: { model: 1, tools: 2, data: 1, engineering: 3 } },
  { name: 'B', skills: { model: 2, tools: 2, data: 0, engineering: 2 } },
  { name: 'C', skills: { model: 0, tools: 1, data: 0, engineering: 3 } },
];
const target: Record<Dim, { minLevel: Level; headcount: number }> = {
  model: { minLevel: 2, headcount: 2 }, tools: { minLevel: 2, headcount: 2 },
  data: { minLevel: 1, headcount: 1 }, engineering: { minLevel: 2, headcount: 3 },
};
```

## 追问（补充）

**追问**：

1. 十人以内的团队，这套矩阵是不是太重？→ 只留工具层与工程层两维、季度对齐一次，缺口用招聘补，不要求全员铺开。
2. 怎么证明能力真的提升了，而不是培训签到率？→ 看交付物：能独立上线的 Agent 数量、评测集覆盖、复盘沉淀的用例数，三个指标都要有可对比的基线值。
3. 业务压力大时路线图还推得动吗？→ 挂到真实项目上，每个项目强制产出一条评测用例和一次分享，不增加额外投入。
