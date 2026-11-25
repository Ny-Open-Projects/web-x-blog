---
title: [RBL-726] 构建器与增量发布联动：affected 计算与发布队列的构建协同
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-726：构建器与增量发布联动：affected 计算与发布队列的构建协同

**答**:
- 增量发布（changesets/nx release 语义）与构建的协同：PR 合入后「affected 计算」（变更包 + 依赖它的下游闭包 = 需要重新构建/发布/测试的集合）→ 生成发布计划（按拓扑序发布包）。构建器的角色：提供「包输入指纹」（RBL-702 新鲜度）让 affected 判定有据。
- affected 计算的精度层次：1) 文件级（turbo：包内文件 hash 变化 → 包 affected）；2) 语义级（构建器：导出面变化 → 下游需要重构建；仅内部实现变化 → 下游产物不必重发——「语义不变则下游免发布」）；3) 配置级（tsconfig/构建配置变化 → affected）。语义级精度是构建器独有能力。
- 发布队列的顺序约束：依赖包先发布（版本号先落地）再发依赖者（版本引用正确）——拓扑序；同层并发发布（无依赖关系的包并行）；发布失败的回滚（单包撤回，不影响已成功者——发布是逐包原子）。
- 版本号传递：上游 minor 升级，下游的 peerDependencies 是否要同步升？——规则引擎（breaking 需要，minor 不需要）+ codemod 自动更新声明——版本联动是发布工程里最易出错的手工环节。
- 追问钩子：为什么「语义级 affected」能省大量发布？——monorepo 里大多数改动是内部实现（产物语义不变）；下游重发布的成本不只是构建时间，还有 npm 版本膨胀/下游测试矩阵触发——语义判定让「免发布」成为一等决策。

```javascript
// affected 语义计算
function affectedPackages(graph, changed) {
  const affected = new Set(changed);
  for (const pkg of changed) {
    const semanticChange = diffExports(prevOut(pkg), build(pkg));
    if (semanticChange.length === 0)
      continue;                                          // 内部实现变化：语义不变
    for (const [down, spec] of graph.dependents(pkg))
      if (spec.type === 'runtime') affected.add(down);   // 运行时依赖才传播
  }
  return affected;
}
// 发布计划（拓扑序 + 分层并发）
async function releasePlan(affected, graph) {
  const layers = topoLayers(graph, affected);            // 依赖分层
  for (const layer of layers) {
    const results = await Promise.allSettled(layer.map(pkg => publish(pkg)));
    const failed = results.filter(r => r.status === 'rejected');
    if (failed.length) throw new Error(`分层发布失败: ${failed.length} 包——已成功者保留`);
  }
}
```
