---
title: [RBL-482] 笔试：手写配置 drift 自动修复
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-482：手写配置 drift 自动修复
**答**：实现 `autoFixDrift(repos, baseline)`：1) 检测各仓配置与 baseline 的 drift（字段级 diff）；2) 自动修复分类：safe（版本号对齐——codemod 直接改）/needs-review（语义差异——生成 PR 人工审）/cannot-fix（结构性差异——报告）；3) 修复 PR 生成：带 diff 预览与验证状态；4) 修复幂等：重复执行不产生新变更（修复后与 baseline 一致）；5) 报告 { fixed, needsReview, cannotFix }，修复率追踪。

```javascript
export function autoFixDrift(repos, baseline, codemod) {
  const fixed = [], needsReview = [], cannotFix = []

  for (const repo of repos) {
    const drifts = diffConfig(repo.config, baseline)
    const safeKeys = ['toolVersion', 'browserslist', 'target']      // 结构相同仅值不同
    const allSafe = drifts.every((d) => safeKeys.includes(d.field) && typeof d.expected === typeof d.actual)

    if (!drifts.length) continue
    if (allSafe) {
      const patch = codemod(repo.config, drifts)                    // 生成修复 patch
      const result = codemod.apply(repo, patch)                     // 应用后校验
      if (diffConfig(result, baseline).length === 0) {              // 幂等校验：修复后无 drift
        fixed.push({ repo: repo.name, fields: drifts.map((d) => d.field) })
      } else cannotFix.push({ repo: repo.name, reason: 'fix did not converge' })
    } else if (drifts.some((d) => d.structural)) {
      cannotFix.push({ repo: repo.name, reason: `structural drift at ${drifts.find((d) => d.structural).field}` })
    } else {
      needsReview.push({ repo: repo.name, drifts })                 // 语义差异 → PR 人工审
    }
  }
  return { fixed, needsReview, cannotFix,
    fixRate: repos.length ? fixed.length / (fixed.length + needsReview.length + cannotFix.length) : 0 }
}

function diffConfig(actual, expected, path = '', out = []) {
  if (actual === expected) return out
  if (typeof actual !== 'object' || typeof expected !== 'object' || !actual || !expected)
    return out.concat({ field: path, actual, expected, structural: typeof actual !== typeof expected })
  for (const k of new Set([...Object.keys(expected), ...Object.keys(actual)])) {
    diffConfig(actual[k], expected[k], path ? `${path}.${k}` : k, out)
  }
  return out
}
```
**评分点**：
- 三分类修复策略（safe codemod / needs-review PR / cannot-fix 报告——自动化分级）
- 幂等校验（修复后与 baseline 一致才算 fixed——防修复不收敛）
- structural 差异识别（类型不同不可自动改——诚实边界）
- fixRate 追踪（自动化覆盖率度量）
