---
title: [WCN-703] 多包原子发布时，如何保证发布事务性？出现半发布状态怎么回滚？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-703：多包原子发布时，如何保证发布事务性？出现半发布状态怎么回滚？

**答**：
- 结论：采用「两阶段提交」思路——先 dry-run 校验全部包可发布、版本号无冲突，再统一 publish；任一失败则不进入提交阶段。
- 用 changesets/lerna fixed 模式把强关联包绑为同一版本组，降低半发布概率；发布顺序按依赖拓扑（被依赖方先发）。
- 真出现半发布：立即发布一个 patch 修复版本对齐版本线，并把不一致的包标记 deprecated；配合 lockfile 固定引用。

```javascript
// 发布协调器伪代码
async function atomicPublish(packages) {
  const graph = topoSort(packages);           // 被依赖方在前
  for (const p of graph) {
    const ok = await dryRun(p);                // 阶段1：全量预检
    if (!ok) throw new Error(`预检失败: ${p.name}`);
  }
  const done = [];
  try {
    for (const p of graph) { await publish(p); done.push(p.name); } // 阶段2
  } catch (e) {
    await rollback(done);                      // 半发布回滚
    throw e;
  }
}
async function rollback(done) {
  for (const name of done.reverse()) {
    await deprecate(name, '发布事务失败已回滚');
  }
}
console.log('发布顺序由拓扑排序决定，保证被依赖方先发布');
```
