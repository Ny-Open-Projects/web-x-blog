---
title: [RBL-871] 场景题：Monorepo 依赖图可视化——跨包依赖的数据提取与环路诊断
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-871：场景题：Monorepo 依赖图可视化——跨包依赖提取与环路诊断

**答**:
- 依赖图可视化的数据层：1) **包级图**（package.json deps 过滤 workspace 内部包 + 构建器解析验证——声明的图与实际 import 的图可能不一致：声明了没用 = 冗余依赖；用了没声明 = 幽灵 RBL-832）；2) 双图 diff（声明图 vs 实际图）是依赖治理的核心报告；3) 环路诊断（Tarjan SCC RBL-593——包级环是发布拓扑的阻断项）。
- 实际依赖图的提取：从构建器模块图聚合（模块 → 所属包 → 包间边）——比静态扫描 package.json 准（动态 import/子路径导入都能捕获）；提取的「依赖强度」分级（直接 import/类型引用/动态 import）供不同治理决策。
- 可视化的交互语义：包级图几百节点——布局（力导向 or 分层 DAG）+ 焦点模式（点开一个包看它的依赖闭包）；「环高亮」是最重要的交互（发布阻塞的根因可视化）。
- 依赖治理的动作绑定：冗余依赖 → 自动 PR 移除；幽灵依赖 → 加声明 PR；环 → 拆包建议——可视化不是终点，「图 → 问题清单 → 动作」才是。
- 追问钩子：为什么「声明图 vs 实际图」的 diff 比单纯可视化更重要？——可视化回答「长什么样」，diff 回答「哪里错了」；声明与实际的漂移是依赖腐化的早期信号（冗余/幽灵都是漂移的形态）——治理工具的价值在于「把漂移变成 issue」而不是「把图变成图片」。

```javascript
// 双图提取与 diff
function extractActualGraph(modules) {
  const edges = new Map();                               // owner -> Set<depOwner>
  for (const m of modules) {
    for (const imp of m.imports ?? []) {
      const target = ownerOf(imp);                       // import 目标所属包
      if (target && target !== m.owner) {
        edges.get(m.owner) || edges.set(m.owner, new Set()).get(m.owner).add(target);
      }
    }
  }
  return edges;
}
function diffGraphs(declared, actual) {
  const findings = [];
  for (const [pkg, deps] of actual)
    for (const d of deps)
      if (!declared[pkg]?.has(d)) findings.push({ type: 'undeclared', pkg, dep: d });   // 幽灵
  for (const [pkg, deps] of Object.entries(declared))
    for (const d of deps ?? [])
      if (!actual.get(pkg)?.has(d) && isInternal(d))
        findings.push({ type: 'unused', pkg, dep: d });  // 冗余（仅内部包可判定）
  return findings;
}
```
