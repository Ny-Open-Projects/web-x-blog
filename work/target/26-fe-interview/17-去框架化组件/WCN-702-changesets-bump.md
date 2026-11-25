---
title: [WCN-702] 笔试：手写 changesets 风格的语义化版本提升计算器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-702：笔试：手写 changesets 风格的语义化版本提升计算器

**答**：
- 思路：遍历变更集，按每个包的变更类型（patch/minor/major）取最高等级；用有向图传播依赖版本提升（依赖被 minor/major 升级时自身也要 bump）。
- 边界：未知变更类型忽略；循环依赖用 visited 防呆；无变更的包保持原版本。
- 输出每个包的新版本与CHANGELOG 摘要。

```javascript
const RANK = { patch: 1, minor: 2, major: 3 };
function bump(version, level) {
  const [a, b, c] = version.split('.').map(Number);
  if (level === 'major') return `${a + 1}.0.0`;
  if (level === 'minor') return `${a}.${b + 1}.0`;
  return `${a}.${b}.${c + 1}`;
}
function computeVersions(versions, changesets, deps = {}) {
  const bumpLevel = {};                       // 收集每个包的变更等级
  for (const cs of changesets) {
    for (const r of cs.releases) {
      const lv = r.level;
      if (!RANK[lv]) continue;                // 边界：忽略非法等级
      bumpLevel[r.name] = bumpLevel[r.name] || 'patch';
      if (RANK[lv] > RANK[bumpLevel[r.name]]) bumpLevel[r.name] = lv;
    }
  }
  // 依赖传播：A 依赖 B，B 被 major/minor 升级 → A 也至少 patch/minor
  let changed = true;
  while (changed) {
    changed = false;
    for (const [pkg, ds] of Object.entries(deps)) {
      for (const dep of ds) {
        const dl = bumpLevel[dep];
        if (dl && dl !== 'patch') {
          const want = dl === 'major' ? 'minor' : 'patch';
          const cur = bumpLevel[pkg] || 'patch';
          if (RANK[want] > RANK[cur]) { bumpLevel[pkg] = want; changed = true; }
        }
      }
    }
  }
  const out = { ...versions };
  for (const [name, lv] of Object.entries(bumpLevel)) {
    out[name] = bump(versions[name] || '0.0.0', lv);
  }
  return out;
}
console.log(computeVersions(
  { 'ds-core': '1.2.0', 'ds-button': '1.2.0' },
  [{ releases: [{ name: 'ds-core', level: 'minor' }] }],
  { 'ds-button': ['ds-core'] }
));
```

**评分点**：
- 变更等级取最高（RANK 映射比较），而非简单覆盖。
- 依赖传播用 while 迭代到不动点，覆盖多级依赖链。
- 传播时正确降级（被依赖 major → 依赖方 minor），不盲目传递 major。
- 对非法等级与缺失版本有边界防御。
