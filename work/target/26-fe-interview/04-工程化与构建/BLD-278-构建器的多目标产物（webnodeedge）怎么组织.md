---
title: [BLD-278] 多目标产物（web/node/edge 三目标）怎么组织？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-278：多目标产物怎么组织？
**答**：
- 目标差异：语法目标（es2019 vs node18）、条件解析（browser vs node）、polyfill（web 需要的 node 不需要）、外部化（node external node_modules）——一个源码多套构建配置。
- 组织方式：同仓多构建配置（条件分支集中，SCN-BLD-242）或 meta-package（每目标独立构建产物——exports 条件映射）。
- 一致性验证：多目标产物的「行为一致性」测试（同 fixture 三目标跑同一断言）——目标间行为漂移的防御。
- 追问钩子：为什么「行为一致性测试」要在多目标构建里显式做——三目标的三条转换链（不同 target/polyfill/external）可能产生行为差异（如 edge 目标禁用了某 API 的 polyfill 导致运行路径不同）；统一 fixture 跨目标断言是唯一能抓住「构建器引入的行为漂移」的手段。

```javascript
// 多目标构建
targets: {
  web:  { target: 'es2019', conditions: ['browser'] },
  node: { target: 'node18', conditions: ['node'], external: 'node_modules' },
  edge: { target: 'es2022', conditions: ['edge', 'worker'] },
},
// 行为一致性测试
targets.forEach(t => {
  const out = await build(fixture, t);
  assertBehavior(out);                                 // 同断言跨目标
});
```
