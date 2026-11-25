---
title: [RBL-152] 笔试：手写语法降级缺口检测（target vs 源码语法）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-152：笔试：手写语法降级缺口检测（target vs 源码语法）

**答**：写 check-syntax-gap.mjs：1) 输入目标 target（es2015/es2018/es2020）与源文件列表；2) 对每个文件用 parser 检测是否使用了"高于 target 才有的语法"：es2020 独有（?? 空值合并、?. 可选链）、es2022（class fields、顶层 await、#private）；3) 输出报告 {file: [features]}，标注"构建器需降级"或"target 已覆盖无需处理"；4) 检测基于 token/AST 节点类型映射表实现；5) 顶层 await 检测只看模块顶层（函数内 await 不算）。

```javascript
// check-syntax-gap.mjs
import { parseSync } from 'oxc-parser';
import { readFileSync } from 'node:fs';

// 节点类型 → 引入版本映射
const FEATURE = {
  ChainExpression: 'optional-chaining',          // ES2020
  AwaitExpression: 'await',
  PropertyDefinition: 'class-fields',            // ES2022
  PrivateIdentifier: 'private-fields',           // ES2022
  LogicalExpression: 'nullish-or-logical',
};
const SINCE = { 'optional-chaining': 2020, 'await': 2017, 'class-fields': 2022,
                'private-fields': 2022, 'nullish-or-logical': 2020 };

function detect(file, targetYear) {
  const src = readFileSync(file, 'utf8');
  const ast = parseSync(file, src, { sourceType: 'module', lang: 'ts' });
  const found = new Set();
  let topAwait = false;

  walk(ast.program, {
    ChainExpression(n) { found.add('optional-chaining'); },
    PropertyDefinition() { found.add('class-fields'); },
    PrivateIdentifier() { found.add('private-fields'); },
    LogicalExpression(n) {
      if (n.operator === '??') found.add('nullish-or-logical');
    },
    AwaitExpression(n) {
      // 粗化：span 覆盖判断是否顶层——嵌套层级记录由 walker 栈决定，这里简化为模块体直系
      if (isTopLevel(ast.program, n)) topAwait = true;
      else found.add('await');
    },
  });
  const report = [];
  for (const f of found) {
    const year = SINCE[f];
    report.push({ feature: f, need: year > targetYear ? '降级' : '已覆盖' });
  }
  if (topAwait) report.push({ feature: 'top-level-await', need: targetYear >= 2022 ? '已覆盖' : '需打包器支持（模块级转换）' });
  return report;
}

function isTopLevel(program, node) {
  return program.body.some(s => s.span.start <= node.span.start && node.span.end <= s.span.end)
    && program.body.some(s => s === node || (s.expression === node));
}
console.log(detect(process.argv[2] ?? 'a.ts', Number(process.argv[3] ?? 2018)));
```
**评分点**：
- 版本映射表驱动（可扩展），不是硬编码 if/else 链。
- ?? 与 ?. 区分（不同版本引入）。
- 顶层 await 与函数内 await 区分。
- 报告语义清晰：需降级 / 已覆盖 / 需打包器支持。
- 能说出真实场景：锁定 target 后预判产物兼容性，避免灰度才炸老机型。
