---
title: [RBL-902] 综合深水：跨包变更的完整生命周期——从一次 commit 到 10 个包发布
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-902：综合深水：跨包变更的完整生命周期——从 commit 到发布

**答**:
- 一次跨包变更（改 utils 包）的完整生命周期：1) PR 触发 affected 计算（RBL-726 语义判定：utils 内部实现变化 vs 导出变化）；2) CI 只跑 affected（构建/测试/检查——RBL-815 关键路径）；3) 合入后 changesets 生成版本计划（拓扑分层 RBL-727）；4) 逐层发布（幂等恢复 RBL-824）；5) 文档站/API 参考同步（RBL-817）；6) 下游 app 的产物重建（跨包失效 RBL-702）与发布；7) 发布后的指标回流（RBL-851）。
- 生命周期的关键分叉：导出变化 vs 内部变化——内部变化下游免发布（语义不变），导出变化才传播——语义判定的精度直接决定发布范围（RBL-726 的核心价值）。
- 时间维度的预算：整个生命周期目标 < 30 分钟（PR CI 10 分钟 + 发布 10 分钟 + 下游重建 10 分钟）——每段的优化手段都已在本目录展开（affected 裁剪/缓存/并行）。
- 故障面：生命周期 7 步各有失败模式（affected 漏算→下游没更新；发布失败→半发布 RBL-823；文档漂移→RBL-818）——「生命周期的预案卡」按步组织。
- 追问钩子：为什么「affected 的语义精度」是整条链路的杠杆？——精度差（内部变化也传播）→ 每次变更发布全部下游（版本膨胀/CI 分钟暴涨）；精度高 → 发布范围 = 语义变化范围——一次判定影响全链路的成本结构，与缓存键的最小完备（RBL-582）同理：判定范围的最小完备性是增量系统的第一性原理。

```javascript
// 生命周期编排
async function crossPackageRelease(changedPkg, { semanticChanged }) {
  const affected = semanticChanged
    ? affectedPackages(pkgGraph, [changedPkg])           // RBL-726
    : [changedPkg];                                      // 内部变化只发自己
  const ci = await runAffectedCI(affected, { criticalPath: true });   // RBL-815
  if (!ci.ok) return { blocked: ci.failures };
  const plan = releasePlan(affected, pkgGraph);          // RBL-727 分层
  const release = await resumeRelease(plan, { registry, notify });   // RBL-824
  if (release.failed.length) return { half: release };   // 半发布预案
  await rebuildDownstream(affected);                     // 跨包失效 RBL-702
  await syncDocs(plan.version);                          // RBL-817
  scheduleWatch(affected);                               // RBL-851
  return release;
}
```
