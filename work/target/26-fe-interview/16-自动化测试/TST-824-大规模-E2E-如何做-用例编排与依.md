---
title: [TST-824] 大规模 E2E 如何做「用例编排与依赖管理」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-824：大规模 E2E 如何做「用例编排与依赖管理」？
**答**：
- 结论：E2E 编排要「显式声明依赖、支持并行、失败隔离」——避免用例间隐式顺序依赖导致不能并行、一挂全挂。
- 依赖声明：用 DAG 描述 setup->用例->teardown，数据依赖通过 fixtures 显式注入，而非用例 A 污染状态给用例 B。
- 并行策略：无依赖的用例并行跑；有共享状态的用例分片隔离或用独立账号/数据。
- 失败隔离：单用例失败不阻塞其他用例，失败后清理环境（回滚数据/关闭会话），避免脏状态扩散。
- 追问钩子：如果两条用例必须串行（共用同一个测试账号），你如何既保证正确又不牺牲太多并行度？

```javascript
// E2E 编排：用 DAG 描述依赖，无依赖者并行
const dag = {
  'login': [],
  'add-cart': ['login'],
  'checkout': ['add-cart'],
  'browse': ['login'],
};
function topoLevels(dag) {
  const levels = [], done = new Set();
  while (done.size < Object.keys(dag).length) {
    const ready = Object.keys(dag).filter(n =>
      !done.has(n) && dag[n].every(d => done.has(d)));
    if (!ready.length) throw new Error('存在环依赖');
    levels.push(ready); ready.forEach(n => done.add(n));
  }
  return levels;
}
console.log(topoLevels(dag)); // [['login'],['add-cart','browse'],['checkout']] 同层可并行
```
