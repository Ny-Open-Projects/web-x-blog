---
title: [ENG-293] 笔试题——实现依赖树 diff（迁移后版本漂移检测）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-293：手写依赖树 diff

**需求与边界**：
- 输入：迁移前后依赖树（包名 → 版本 + 依赖来源链）；输出漂移清单：版本变化/新增/消失，版本变化的按「直接影响（顶层声明）vs 传递漂移」分类。
- 边界：① 同包多版本共存（嵌套）要按 resolved 路径比较；② 输出严重度：major 漂移 = 高危（行为可能变化）；③ 去重（同一包多路径漂移聚合）。

**答**：
```javascript
function treeDiff(before, after) {
  const changes = [];
  const keys = new Set([...Object.keys(before), ...Object.keys(after)]);
  for (const pkg of keys) {
    const b = before[pkg] ?? [], a = after[pkg] ?? [];
    const paths = new Set([...b.map(x => x.path), ...a.map(x => x.path)]);
    for (const p of paths) {
      const bv = b.find(x => x.path === p)?.version, av = a.find(x => x.path === p)?.version;
      if (bv === av) continue;
      changes.push({
        pkg, path: p, from: bv ?? 'absent', to: av ?? 'removed',
        kind: !bv ? 'ADDED' : !av ? 'REMOVED' : semverDiffSeverity(bv, av),
      });
    }
  }
  // 聚合同包漂移（多路径）
  const grouped = groupBy(changes, 'pkg');
  return Object.entries(grouped).map(([pkg, list]) => ({
    pkg,
    severity: list.some(c => c.kind === 'MAJOR') ? 'HIGH'
      : list.some(c => c.kind !== 'SAME') ? 'MEDIUM' : 'NONE',
    paths: list,
  })).sort((a, b) => SEV_RANK[b.severity] - SEV_RANK[a.severity]);
}
function semverDiffSeverity(a, b) {
  const da = semver.major(a) !== semver.major(b) ? 'MAJOR'
    : semver.minor(a) !== semver.minor(b) ? 'MINOR' : 'PATCH';
  return da;
}
```

**评分点**:
- 按 resolved 路径比较（多版本共存不误报）。
- 漂移严重度分级（major/minor/patch + 增删）。
- 同包多路径聚合排序（报告可读）。
- absent/removed 语义区分（新增 vs 消失）。
