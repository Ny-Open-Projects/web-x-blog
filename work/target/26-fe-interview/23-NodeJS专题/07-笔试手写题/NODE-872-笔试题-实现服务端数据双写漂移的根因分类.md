---
title: [NODE-872] 笔试题——实现双写漂移根因分类（自动归因）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-872：手写漂移归因

**需求与边界**：
- 需求：双写漂移归因（SCN-NODE-793）——① 漂移样本分析（新旧值差异模式——SCN-OPS-331）；② 根因分类（双写 bug/并发覆盖/转换错误——SCN-NODE-793）；③ 自动修复的可行性判定（可修——SCN-OPS-259）；④ 根因报告（SCN-OPS-331）。
- 边界：① 并发覆盖的检测（写入时间戳对比——SCN-OPS-331）；② 转换函数的验证（transform 幂等测试——SCN-联想-764 迁移）；③ 修复建议映射（每类根因——SCN-OPS-331）。

**答**：
```javascript
function classifyDrift(drifts) {
  const causes = {};
  for (const d of drifts) {
    if (d.newTs > d.oldTs) causes['concurrent-overwrite'] ??= [];   // 并发覆盖（新写覆盖旧写）
    else if (transform(d.oldVal) !== d.newVal) causes['transform-bug'] ??= [];   // 转换错误
    else causes['dual-write-bug'] ??= [];               // 双写遗漏（SCN-OPS-331）
    const key = d.newTs > d.oldTs ? 'concurrent-overwrite' : 'transform-bug';
    causes[key].push(d);
  }
  const FIX = {
    'concurrent-overwrite': '接受新值（旧列重算）',
    'transform-bug': '修复 transform 函数 + 补偿（SCN-联想-764）',
    'dual-write-bug': '补写新列（幂等补偿——SCN-NODE-868）',
  };
  return { causes, fix: Object.keys(causes).map(k => FIX[k]),
    autoFixable: !causes['dual-write-bug']?.length };   // 双写 bug 不可自动修（代码问题）
}
```

**评分点**:
- 三类根因（并发覆盖/转换错误/双写遗漏——SCN-OPS-331）。
- 时间戳判别法（并发覆盖——newTs > oldTs）。
- 自动修复可行性判定（双写 bug 不可自动修——代码问题走人工）。
- 修复建议映射（每类根因）。
