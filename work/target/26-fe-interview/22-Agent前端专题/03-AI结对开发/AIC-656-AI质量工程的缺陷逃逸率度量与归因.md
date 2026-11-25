---
title: [AIC-656] AI 代码的「缺陷逃逸率」怎么度量和归因？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-656：AI 代码的「缺陷逃逸率」怎么度量和归因？

**答**：
- 结论先行：**缺陷逃逸率 = 上线后发现的缺陷数 / 总缺陷数，它衡量「质量防线漏了多少」，比「缺陷总数」更能反映 AI 质量工程的健康度**。AI 代码若逃逸率高，说明审查与测试防线对 AI 产出失效。
- 度量方法：1) **区分来源**：给缺陷打标「AI 生成代码引入 / 人工代码引入」，分别算逃逸率；2) **区分阶段**：缺陷在哪个阶段被发现（编写/评审/测试/灰度/线上），线上发现 = 逃逸；3) **趋势而非单点**：看 AI 代码逃逸率是否随流程优化下降。
- 归因分析：逃逸的 AI 缺陷集中在哪？1) **需求理解偏差**（意图漂移，AI 没懂业务）→ 改进任务卡与锚点；2) **边界遗漏**（没考虑空/异常）→ 加强属性测试；3) **上下文缺失**（不知道内部框架约束）→ 补 rules/代码地图；4) **审查失效**（review 没看出来）→ 改进审查清单。归因到具体环节才能针对性修复。
- 与「质量对冲看板」配合：提效数据好但逃逸率上升 = 典型「提效幻觉」（AIC-305）——速度提升是以质量下沉为代价。
- 追问钩子：为什么「按来源区分逃逸率」很重要？——因为如果 AI 代码的逃逸率显著高于人工代码，说明现有质量防线是针对人工代码设计的，对 AI 产出的新失效模式（幻觉、意图漂移）不适用；不区分来源就会被平均值掩盖，看不到真正的问题。

```typescript
type Defect = { id: string; source: 'ai'|'human'; foundIn: 'dev'|'review'|'test'|'canary'|'prod'; cause?: string };

function escapeRate(defects: Defect[], source: 'ai'|'human'): { rate: number; escaped: Defect[] } {
  const scoped = defects.filter(d => d.source === source);
  const escaped = scoped.filter(d => d.foundIn === 'prod');
  return { rate: scoped.length ? escaped.length / scoped.length : 0, escaped };
}

function attribute(defects: Defect[]): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const d of defects) if (d.cause) counts[d.cause] = (counts[d.cause] || 0) + 1;
  return counts;
}

const defects: Defect[] = [
  { id: 'd1', source: 'ai', foundIn: 'prod', cause: 'context-missing' },
  { id: 'd2', source: 'ai', foundIn: 'test' },
  { id: 'd3', source: 'human', foundIn: 'prod', cause: 'edge-case' },
  { id: 'd4', source: 'ai', foundIn: 'prod', cause: 'context-missing' },
];
console.log(escapeRate(defects, 'ai').rate === 2 / 3);
console.log(attribute(escapeRate(defects, 'ai').escaped)['context-missing'] === 2);
```
