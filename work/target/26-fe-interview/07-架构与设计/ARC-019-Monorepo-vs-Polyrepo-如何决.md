---
title: [ARC-019] Monorepo vs Polyrepo 如何决策？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-019：Monorepo vs Polyrepo 如何决策？
**答**：
- Monorepo 解决"跨仓改动"成本：原子提交、统一工具链、代码复用零成本；代价是仓库规模、CI 复杂度、权限粒度粗。
- Polyrepo 适合团队边界清晰、发布节奏独立、需要严格权限隔离的场景。
- 决策看三件事：跨仓变更频率、团队规模、共享代码占比；三者都高就选 Monorepo。

```typescript
interface RepoDecision {
  crossRepoChangesPerWeek: number;  // 每周需要跨仓联动的改动数
  teamCount: number;                // 前端团队数
  sharedCodeRatio: number;          // 共享代码占比 0~1
  strictAccessControl: boolean;     // 是否需要仓库级权限隔离（如外包参与）
}

function chooseRepoStrategy(d: RepoDecision): 'monorepo' | 'polyrepo' | 'hybrid' {
  if (d.strictAccessControl) return 'hybrid';          // 核心码 monorepo + 外围 polyrepo
  const score =
    (d.crossRepoChangesPerWeek >= 5 ? 2 : 0) +
    (d.teamCount >= 3 ? 1 : 0) +
    (d.sharedCodeRatio >= 0.3 ? 2 : 0);
  return score >= 3 ? 'monorepo' : 'polyrepo';
}
// 经验值：共享代码 >30% 且每周跨仓联动 ≥5 次，polyrepo 的同步成本会指数上升
```
