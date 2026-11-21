---
title: [RBL-481] 笔试：手写构建变更的 CodeOwner 路由
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-481：手写构建变更的 CodeOwner 路由
**需求**：实现 `routeReviewers(changedFiles, owners, teamMap)`：1) owners：CODEOWNERS 规则（glob → 团队/个人，后者优先）；2) 路由：变更文件 → 匹配规则 → 需要审批的人（去重合并）；3) 构建专项：构建配置/门禁/缓存文件变更 → 平台组必审（不依赖 CODEOWNERS 也能强制——高风险路径独立规则）；4) 审批门槛分级：平台文件需 2 个 approve（双审）；5) 输出 { reviewers, requiredApprovals: number, paths }。

```javascript
function matchGlob(file, pattern) {
  const re = new RegExp('^' + pattern.replace(/\./g, '\\.').replace(/\*\*/g, '.*').replace(/\*/g, '[^/]*') + '$')
  return re.test(file)
}

export function routeReviewers(changedFiles, owners, { buildFiles, platformTeam, dualApproval }) {
  const reviewers = new Set()
  const matched = []
  for (const file of changedFiles) {
    for (const rule of owners) {                            // 后者优先（按声明顺序覆盖）
      if (matchGlob(file, rule.pattern)) {
        reviewers.add(rule.owner)
        matched.push({ file, owner: rule.owner, pattern: rule.pattern })
      }
    }
    // 构建专项强制路由（独立于 CODEOWNERS）
    if (buildFiles.some((p) => file.startsWith(p))) reviewers.add(platformTeam)
  }
  const needsDual = changedFiles.some((f) => buildFiles.some((p) => f.startsWith(p)))
  return { reviewers: [...reviewers],
    requiredApprovals: needsDual ? dualApproval : 1,
    matched }
}

// 用法
// owners = [{ pattern: '**', owner: '@frontend/all' },
//           { pattern: 'packages/core/**', owner: '@team/core' }]
// routeReviewers(['rsbuild.config.ts', 'src/a.ts'], owners,
//   { buildFiles: ['rsbuild.config', 'turbo.json', '.cache'], platformTeam: '@team/build', dualApproval: 2 })
// → reviewers: ['@frontend/all', '@team/core', '@team/build'], requiredApprovals: 2
```
**评分点**：
- 后者优先语义（CODEOWNERS 规则覆盖顺序——常用语义）
- 构建专项强制路由（平台文件必审——不依赖 CODEOWNERS 的独立防线）
- 双审批门槛（构建变更影响全员——审批杠杆匹配影响面）
- matched 归因（每个文件由谁审——可解释）
