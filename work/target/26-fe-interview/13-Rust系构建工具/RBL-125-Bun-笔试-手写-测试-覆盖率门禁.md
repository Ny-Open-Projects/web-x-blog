---
title: [RBL-125] 笔试：手写覆盖率门禁脚本（bun test 覆盖率 + 阈值判定）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-125：笔试：手写覆盖率门禁脚本（bun test 覆盖率 + 阈值判定）
**题目**：写 coverage-gate.ts：1) 运行 bun test --coverage 拿覆盖率数据；2) 对 lines/functions/branches 三个维度设阈值（如 80/70/60）；3) 低于阈值 exit 1 并输出未达标项；4) 支持增量目录白名单（只统计 src/ 下）；5) 输出汇总表。

```typescript
// coverage-gate.ts
import { $ } from 'bun';

const THRESHOLDS = { lines: 80, functions: 70, branches: 60 };

const proc = await $`bun test --coverage`.quiet().nothrow();
const out = proc.stderr.toString() + proc.stdout.toString();

// 解析覆盖率汇总（bun test 输出的 summary 行，示意格式）
// All files | 85.2 | 72.0 | 61.5 | ...
const m = out.match(/All files\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)/);
if (!m) {
  console.error('[gate] 无法解析覆盖率输出:\n', out);
  process.exit(2);
}
const [lines, functions, branches] = [+m[1], +m[2], +m[3]];

const rows = [
  ['lines', lines, THRESHOLDS.lines],
  ['functions', functions, THRESHOLDS.functions],
  ['branches', branches, THRESHOLDS.branches],
];
let fail = false;
console.log('| 维度 | 实际 | 阈值 | 结果 |');
console.log('|---|---|---|---|');
for (const [name, actual, min] of rows) {
  const ok = actual >= min;
  if (!ok) fail = true;
  console.log(`| ${name} | ${actual}% | ${min}% | ${ok ? 'PASS' : 'FAIL'} |`);
}
process.exit(fail ? 1 : 0);
```
**评分点**：
- 覆盖率解析健壮性（无匹配 exit 2 与 exit 1 语义区分）。
- 三维度阈值各自判定。
- 表格输出可读。
- nothrow（不因测试失败中断门禁逻辑）。
- 能说出覆盖率门禁的合理用法：防"新增代码无测试"，而非盲目追求高数字。
