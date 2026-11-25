---
title: [AIC-526] AI 模型路由：简单任务用便宜模型
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-526：模型路由——简单任务用便宜模型

**答**:
- 模型路由的原理：1) **模型分级**：便宜模型（GPT-3.5/GPT-4o-mini：$0.5/M tokens——快速、便宜）vs 贵模型（GPT-4/Claude Opus：$10/M tokens——高质量、慢）；2) **路由策略**：简单任务（补全/格式化/单行修改）→ 便宜模型；复杂任务（架构设计/多文件重构/逻辑推理）→ 贵模型；3) **路由的实现**：任务分类器（LLM 自评或规则匹配——"单行修改" → cheap，"重构" → expensive）；4) **路由的成本节省**：80% 任务是简单的 → 80% 用便宜模型 → 总成本降 60%（RBL-524 预算管理的成本优化）。
- 模型路由的决策维度：1) **任务复杂度**（代码行数变更/涉及文件数/逻辑复杂度）；2) **质量要求**（安全关键 → 贵模型（RBL-504 T0）；boilerplate → 便宜模型（T2/T3）；3) **延迟要求**（inline 补全 → 便宜快模型；chat → 贵模型；4) **降级策略**（贵模型不可用 → 便宜模型 fallback（性能降级可用性优先 RBL-679）。
- 追问钩子：为什么「模型路由」的 ROI 比「统一用最好的模型」更高？——80% 的任务是简单补全（用贵模型 = 浪费——补全质量差异小）；20% 是复杂任务（用贵模型 = 质量差异大）；成本模型：80% × 便宜 + 20% × 贵 < 100% × 贵（节省 60% 成本）；「路由的复杂度成本」：实现路由器（分类器/规则/fallback）≈ 1 周 vs 节省 60% × $4400/月 = $2600/月 → 回本 2 天——模型路由是 AI 成本优化的第二杠杆（第一是上下文裁剪 RBL-502）。

```typescript
// 模型路由器
interface ModelRoute {
  model: 'cheap' | 'expensive';
  reason: string;
}
function routeModel(task: {
  linesChanged?: number;
  filesInvolved?: number;
  isSecurityCritical?: boolean;
  isInline?: boolean;
  complexityHint?: 'simple'|'medium'|'complex';
}): ModelRoute {
  // 安全关键 → 始终用贵模型（RBL-504 T0）
  if (task.isSecurityCritical)
    return { model: 'expensive', reason: '安全关键——质量优先' };
  // inline 补全 → 便宜模型（快+便宜）
  if (task.isInline)
    return { model: 'cheap', reason: 'inline 补全——延迟优先' };
  // 复杂度判断
  const complexity = task.complexityHint ??
    ((task.linesChanged ?? 0) > 100 || (task.filesInvolved ?? 0) > 3
      ? 'complex' : 'simple');
  if (complexity === 'complex')
    return { model: 'expensive', reason: '复杂任务——质量要求高' };
  return { model: 'cheap', reason: '简单任务——成本优先' };
}
// 路由决策
routeModel({ isInline: true });                         // cheap
routeModel({ linesChanged: 300, filesInvolved: 5 });   // expensive
routeModel({ isSecurityCritical: true });              // expensive
routeModel({ linesChanged: 10 });                      // cheap
```
