---
title: [TST-618] 大型 monorepo 的测试架构治理要点有哪些？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-618：大型 monorepo 的测试架构治理要点有哪些？

**答**：
- 结论：按「包边界」组织测试，构建图决定测试图——只跑受影响包及其下游。
- 统一 workspace 配置但允许包级 override；共享 fixture 必须版本化，避免隐式耦合。
- 跨包集成测试单独分层，放在 CI  nightly，不进 PR 关键路径。
- 追问钩子：包 A 改了类型，包 B 的测试没跑却线上出错，你的影响分析漏了什么？

```javascript
function affected(pkgGraph, changedPkg) {
  const out = new Set([changedPkg]);
  let frontier = [changedPkg];
  while (frontier.length) {
    const next = [];
    pkgGraph.forEach(([from, to]) => {
      if (frontier.includes(from) && !out.has(to)) { out.add(to); next.push(to); }
    });
    frontier = next;
  }
  return [...out];
}
console.log(affected([['a', 'b'], ['b', 'c']], 'a')); // [a,b,c]
```
