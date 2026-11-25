---
title: [AIC-892] 笔试：实现 AI 事故复盘结构化记录器
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-892：笔试：实现 AI 事故复盘结构化记录器
**答**：
- 核心需求：实现 `PostmortemStore`，`add(incident)` 记录事故，`link(incidentId, guardId)` 关联守卫，`stats()` 统计。事故含 `id, severity, modelVersion, promptVersion, missingContext[], evalGap, recurrenceOf?`（复发指向的事故 id）、`guards[]`。
- 规则：`severity` 为 'sev1'|'sev2'|'sev3'；sev1 必须有 modelVersion 与 promptVersion 否则拒绝（高风险事故必须可追溯）；复发（`recurrenceOf` 非空）自动提升严重度一级（sev2→sev1）；`stats()` 返回各级别数量、复发率、有守卫覆盖率。
- 边界：重复 id 抛错；未知关联 id 抛错；空记录返回安全统计（全 0）；severity 非法视为 sev3。
- 追问钩子：追问「为什么 sev1 强制要版本信息」——能答出「严重事故必须能回答'当时用的什么模型/prompt'，否则无法归因和改进，这是 AI 事故复盘区别于传统的基本要求」的候选人理解 AI 可追溯性。

```typescript
type Severity = 'sev1' | 'sev2' | 'sev3';
type Incident = { id: string; severity: Severity; modelVersion?: string;
  promptVersion?: string; missingContext: string[]; evalGap: string;
  recurrenceOf?: string; guards: string[] };

const order: Severity[] = ['sev3','sev2','sev1'];
function bump(s: Severity): Severity { return order[Math.min(2, order.indexOf(s) + 1)]; }

class PostmortemStore {
  private items = new Map<string, Incident>();
  add(i: Incident) {
    if (this.items.has(i.id)) throw new Error('duplicate incident');
    if (i.severity === 'sev1' && (!i.modelVersion || !i.promptVersion))
      throw new Error('sev1 requires modelVersion & promptVersion');
    const severity = i.recurrenceOf ? bump(i.severity ?? 'sev3') : (i.severity ?? 'sev3');
    this.items.set(i.id, { ...i, severity });
  }
  link(incidentId: string, guardId: string) {
    const i = this.items.get(incidentId);
    if (!i) throw new Error('unknown incident');
    i.guards.push(guardId);
  }
  stats() {
    const all = [...this.items.values()];
    return {
      bySeverity: { sev1:all.filter(i=>i.severity==='sev1').length,
        sev2:all.filter(i=>i.severity==='sev2').length,
        sev3:all.filter(i=>i.severity==='sev3').length },
      recurrenceRate: all.length ? +(all.filter(i=>i.recurrenceOf).length/all.length).toFixed(2) : 0,
      guardedRate: all.length ? +(all.filter(i=>i.guards.length>0).length/all.length).toFixed(2) : 0,
    };
  }
}
const store = new PostmortemStore();
store.add({ id:'I-1', severity:'sev2', modelVersion:'v2', promptVersion:'p7',
  missingContext:[], evalGap:'null 边界', guards:[] });
store.add({ id:'I-2', severity:'sev2', recurrenceOf:'I-1',
  modelVersion:'v2', promptVersion:'p7', missingContext:[], evalGap:'同类', guards:[] });
console.log(store.stats().bySeverity.sev1); // 1（I-2 复发被提升为 sev1）
```
**评分点**：
- sev1 强制版本信息校验，缺失则拒绝（可追溯性硬要求）。
- 复发自动提升严重度（bump 函数，sev2→sev1），sev1 封顶不越界。
- 重复 id / 未知关联 id 抛错，空记录返回安全统计。
- severity 非法默认 sev3，边界处理完整。
- stats 含复发率与守卫覆盖率，驱动复盘质量改进。
