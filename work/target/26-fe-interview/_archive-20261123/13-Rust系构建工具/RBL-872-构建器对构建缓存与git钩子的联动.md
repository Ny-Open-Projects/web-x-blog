---
title: [RBL-872] 场景题：Git 钩子与构建的联动——pre-commit 检查的范围裁剪与失败策略
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-872：场景题：Git 钩子与构建的联动——pre-commit 检查的范围裁剪

**答**:
- pre-commit 钩子的性能约束：开发者等待容忍 < 10s（RBL-855 的上下文切换成本）——检查范围必须裁剪到「staged 文件闭包」：1) lint-staged 模式（只 lint staged 文件）；2) 受影响测试选择（staged 文件 → 依赖它的测试子集——RBL-635 失效传播的反向应用）；3) 类型检查的裁剪难题（tsc 是全局闭包——项目级 incremental tsc 只查关联文件，或挪到 pre-push）。
- 钩子的失败策略：可自动修复的（格式化）自动修并 re-stage——「钩子帮你修好」优于「钩子报错让你修」；不可自动修复的（lint 错误）给出精确修复提示——钩子的价值是「快速反馈」不是「拦截」。
- 职责分层：pre-commit（快检查：lint/format/受影响单测）→ pre-push（中检查：全量单测/类型检查）→ CI（全量：构建/语义 diff/e2e）——「同质检查在不同层重复」是浪费，分层让每层的成本与时机匹配。
- 钩子的逃逸治理：`--no-verify` 绕过是常态（CI 兜底）——但高频绕过 = 钩子太慢或误报（信号：绕过率 > 30% 时钩子设计有问题）；钩子的耗时与误报率要作为指标监控（RBL-705）。
- 追问钩子：为什么类型检查不该放 pre-commit？——tsc 的正确性要求全量闭包（增量 tsc 有边界漏报风险 RBL-646）；全量 tsc 在大仓库 > 30s 违反钩子时延预算；放 pre-push/CI 让「提交快、推送稍慢、CI 全查」的节奏匹配注意力曲线——检查的放置位置是「反馈速度 vs 覆盖完备」的工程权衡。

```javascript
// pre-commit 受影响测试选择
function affectedTests(staged, graph, tests) {
  const affected = new Set();
  for (const f of staged) {
    affected.add(f);
    for (const importer of reverseClosure(graph, f))     // 反向闭包：谁依赖它
      if (tests.includes(importer)) affected.add(importer);
  }
  return [...affected].filter(t => tests.includes(t));
}
// lint-staged 配置语义
const lintStaged = {
  '*.{ts,tsx}': ['eslint --fix', 'prettier --write'],   // 自动修复 + re-stage
  '*.css': ['stylelint --fix'],
};
// 钩子健康度
function hookHealth({ runs, avgMs, bypassRate, falsePositives }) {
  if (avgMs > 10000) warn('钩子超 10s——检查范围需裁剪（绕过率将上升）');
  if (bypassRate > 0.3) fail('绕过率 >30%——钩子设计有问题，重新评估检查项');
  return { avgMs, bypassRate, falsePositives };
}
```
