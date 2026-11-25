---
title: [WCN-524] 企业前端中台：WCN 元素作为「UI 中台资产」的版本目录与资产市场如何设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-524：企业前端中台：WCN 元素作为「UI 中台资产」的版本目录与资产市场如何设计？

**答**：
- 结论：资产市场 = 版本目录（可发现）+ 质量分（可信任）+ 采用数据（可决策）三件套。
- 版本目录：每元素多版本共存，标注 semver、兼容宿主、breaking 说明。
- 质量分由 a11y/测试覆盖/文档完整度/线上健康度加权得出，低于阈值不给「推荐」标。
- 追问：如何防止市场变成「僵尸组件坟场」？（答：deprecation 机制 + 长期无引用自动归档）

```javascript
function assetScore(a) {
  const w = { a11y: 0.3, coverage: 0.3, docs: 0.2, health: 0.2 };
  return Math.round(100 * Object.keys(w).reduce((s, k) => s + w[k] * a[k], 0));
}
function catalog(assets) {
  return assets.map(a => ({
    ...a, score: assetScore(a),
    recommended: assetScore(a) >= 80 && !a.deprecated,
    status: a.lastUsedMonths > 12 ? 'archived' : 'active',
  }));
}
```
