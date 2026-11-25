---
title: [ENG-321] 笔试题——实现 AI 上下文预算分配（地图→精读 token 预算）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-321：手写 AI 上下文预算

**需求与边界**：
- 需求：给定任务与 token 预算（如 8k 上下文），分配——① 仓库地图摘要（固定 500）；② 相关文件精读（按相关性排序，预算内尽量多）；③ 任务模板规则（ENG-214 规则集）；超预算时按「相关性×信息密度」裁剪并输出被裁剪清单。
- 边界：① 相关性排序用符号命中 + import 距离；② 文件级裁剪不截半文件（半文件比少文件更误导）；③ 每文件 token 估算（chars/4）。

**答**：
```javascript
function contextBudget(task, budget = 8000) {
  const MAP = 500, RULES = 800;
  let remaining = budget - MAP - RULES;
  const candidates = relevantFiles(task)              // 符号命中 + import 距离排序
    .map(f => ({ ...f, tokens: Math.ceil(f.chars / 4) }));
  const picked = [], dropped = [];
  for (const f of candidates.sort((a, b) => b.relevance - a.relevance)) {
    if (f.tokens > remaining) { dropped.push(f.path); continue; }   // 整文件裁剪不截半
    picked.push(f); remaining -= f.tokens;
  }
  return {
    context: { map: repoMapSummary(), rules: taskRules(task), files: picked },
    dropped,
    note: dropped.length ? `预算不足裁剪 ${dropped.length} 个文件，建议拆任务` : null,
  };
}
```

**评分点**:
- 三层预算分配（地图固定/规则固定/精读弹性）。
- 相关性排序（符号命中 + import 距离——ENG-250）。
- 整文件裁剪不截半（半文件误导 AI）。
- 超预算建议拆任务（上下文工程的边界处理）。
