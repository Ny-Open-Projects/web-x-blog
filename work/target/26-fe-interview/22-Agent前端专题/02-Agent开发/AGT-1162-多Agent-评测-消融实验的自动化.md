---
title: [1162] 消融实验（去掉某个组件看影响）怎么自动化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 实验]
type: 面试题
---

## 1162：消融实验（去掉某个组件看影响）怎么自动化

**答**：
- 自动化消融框架：组件注册表（每个组件有开关）+ 实验矩阵（全量 vs 逐个关闭）+ 统一评估跑分，输出「组件贡献表」——每个组件对质量的边际贡献一目了然。
- 用途三处：降级链设计（贡献小的组件先降）、成本优化（贡献低于成本占比的组件砍掉/降档）、新组件验收（新组件的消融增量要显著才保留）。
- 纪律：消融在「其余配置冻结」的前提下跑；结果按意图分层报（组件对不同意图贡献不同）。
- 追问钩子：组件间有依赖怎么消融？——依赖组件被关闭时其下游自动关闭（依赖图传播），报告标注「联合消融」与「独立消融」两种口径，别混着报。

```ts
const registry = { rerank: { on: true, deps: [] }, compress: { on: true, deps: ['rerank'] } };
async function ablation(evalSet) {
  const base = await runEval(evalSet, frozenConfig());
  const rows = [];
  for (const k of Object.keys(registry)) {
    off(k); cascadeOff();                          // 依赖联动关闭
    const r = await runEval(evalSet, frozenConfig());
    rows.push({ component: k, delta: +(r.acc - base.acc).toFixed(3),
      kind: jointOrIndependent(k) });
    on(k);
  }
  return rows.sort((a, b) => a.delta - b.delta);   // 贡献排序
}
```
