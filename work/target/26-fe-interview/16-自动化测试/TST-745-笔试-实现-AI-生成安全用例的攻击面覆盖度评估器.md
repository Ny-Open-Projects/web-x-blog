---
title: [TST-745] 笔试：实现 AI 生成安全用例的「攻击面覆盖度」评估器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-745：笔试：实现 AI 生成安全用例的「攻击面覆盖度」评估器

**题目**：给定攻击面矩阵 surface（如 ['SQLI','XSS','CSRF','IDOR','SSRF']）与 AI 生成的用例数组 cases [{id, surfaces:[...]}]。计算覆盖度：被至少一个用例覆盖的攻击面占比。返回 {coverage, uncovered:[...], perSurface:{面:用例数}}。要求 uncovered 按 surface 原顺序。

**答**：
- 统计每个攻击面被多少用例覆盖，覆盖度 = 覆盖数/总数。
- uncovered 保持原顺序，便于阅读。
- 空用例数组要兜底 coverage=0。

```javascript
function assessCoverage(surface, cases) {
  const perSurface = Object.fromEntries(surface.map(s => [s, 0]));
  for (const c of cases) for (const s of c.surfaces) {
    if (s in perSurface) perSurface[s] += 1;
  }
  const covered = surface.filter(s => perSurface[s] > 0);
  return {
    coverage: +(covered.length / (surface.length || 1)).toFixed(3),
    uncovered: surface.filter(s => perSurface[s] === 0),
    perSurface,
  };
}
console.log(assessCoverage(
  ['SQLI', 'XSS', 'CSRF', 'IDOR'],
  [{ id: '1', surfaces: ['XSS'] }, { id: '2', surfaces: ['XSS', 'SQLI'] }]
));
```

**评分点**：
- 覆盖度计算正确
- uncovered 保持原顺序
- perSurface 统计正确
- 空数组兜底
