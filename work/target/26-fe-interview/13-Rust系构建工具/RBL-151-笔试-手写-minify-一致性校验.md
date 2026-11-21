---
title: [RBL-151] 笔试：手写压缩一致性校验工具（minify 前后 diff）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-151：笔试：手写压缩一致性校验工具（minify 前后行为等价抽查）

**题目**：写 verify-minify.mjs：1) 输入原始 chunk 与压缩后 chunk 两个文件路径；2) 用 @swc/core 分别 parse 两份代码得到导出符号集与字符串字面量集；3) 校验：压缩后导出名集合 ⊆ 原导出名集合（mangle 允许局部重命名但 export 名应保留）、字符串字面量集合一致（防止压缩吞掉关键串）；4) 体积对比输出 gzip 前后压缩率；5) 任一校验失败 exit 1 并打印首个差异。

```javascript
// verify-minify.mjs
import { parseSync } from '@swc/core';
import { readFileSync } from 'node:fs';
import { gzipSync } from 'node:zlib';

function analyze(file) {
  const src = readFileSync(file, 'utf8');
  const ast = parseSync(src, { syntax: 'ecmascript' }).body;
  const exportsSet = new Set(), strings = new Set();
  walk(ast, {
    ExportNamedDeclaration(n) {
      for (const s of n.specifiers ?? []) exportsSet.add(s.exported?.value ?? s.local?.value);
      if (n.declaration?.id?.name) exportsSet.add(n.declaration.id.name);
    },
    StringLiteral(n) { strings.add(n.value); },
  });
  return { exportsSet, strings, size: Buffer.byteLength(src) };
}

const [origPath, minPath] = process.argv.slice(2);
const a = analyze(origPath), b = analyze(minPath);

let failed = false;
for (const e of b.exportsSet) {
  if (!a.exportsSet.has(e)) { console.error(`导出凭空出现: ${e}`); failed = true; }
}
for (const e of a.exportsSet) {
  if (e && !b.exportsSet.has(e)) { console.error(`导出丢失: ${e}`); failed = true; }
}
const missingStr = [...a.strings].filter(s => !b.strings.has(s));
if (missingStr.length) { console.error('字符串字面量缺失:', missingStr.slice(0, 3)); failed = true; }

const gz = (n, f) => gzipSync(readFileSync(f)).length;
console.log(`raw ${a.size}→${b.size} (${(b.size / a.size * 100).toFixed(1)}%) | gzip ${gz(0, origPath)}→${gz(0, minPath)}`);
process.exit(failed ? 1 : 0);
```
**评分点**：
- 校验维度明确：导出集合双向对比（丢失/凭空）+ 字符串集合。
- gzip 压缩率用 zlib 真实计算而非估算。
- 首个差异即报 + exit code 语义。
- 知道局限：mangle 顶层与内联字符串拼接等会让静态对比有噪声，需白名单机制。
- 能对接 CI：作为产物回归门禁步骤。
