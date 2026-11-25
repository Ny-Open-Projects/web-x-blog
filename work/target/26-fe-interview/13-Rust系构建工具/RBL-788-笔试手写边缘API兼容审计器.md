---
title: [RBL-788] 笔试：手写边缘 API 兼容审计器（支持表比对 + 初始化瘦身检测）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-788：笔试：手写边缘 API 兼容审计器（支持表 + 初始化检测）

**答**：实现 `auditEdge(modules, supportTable)`。modules: `Record<id, { code, isEntry }>`；supportTable: `Record<api, boolean>`（node:xxx API 是否被 workerd 支持）。规则：1) 扫描 import/require 语句的 API 名：不支持 → problem `{ mod, api }`（全部命中处聚合）；2) 初始化瘦身：entry 模块顶层（非函数内）出现「重调用模式」（`new Map(` 大字面量/`loadXxx()`/`readFileSync` 等函数调用赋值给顶层 const）→ warning 'heavy-init'；3) 返回 `{ problems: Array<{ mod, api }>, heavyInit: string[] }`。API 提取正则：`from ['"]node:(\w+[\w/-]*)['"]` 与 `require\(['"]node:...['"]\)`。边界：模块无 node API；supportTable 未列出的 API 视为不支持（保守）。

```javascript
function auditEdge(modules, supportTable = {}) {
  const problems = [];
  const heavyInit = [];
  const API_RE = /(?:from\s*|require\()\s*['"]node:([\w/-]+)['"]/g;

  for (const [id, m] of Object.entries(modules)) {
    for (const match of m.code.matchAll(API_RE)) {
      const api = 'node:' + match[1];
      if (supportTable[api] !== true)                     // 未列出 = 不支持（保守）
        problems.push({ mod: id, api });
    }
    if (m.isEntry) {
      // 顶层重调用检测：去掉函数体后仍含调用赋值
      const topLevel = m.code
        .replace(/function[\s\S]*?\n\}/g, '')             // 粗略剔除函数块
        .replace(/=>\s*\{[\s\S]*?\}/g, '');
      if (/(?:^|\n)\s*(?:const|let|var)\s+\w+\s*=\s*(?:load\w*\(|readFileSync\(|new\s+Map\(\[)/.test(topLevel))
        heavyInit.push(id);
    }
  }
  problems.sort((a, b) => a.mod.localeCompare(b.mod) || a.api.localeCompare(b.api));
  return { problems, heavyInit: [...new Set(heavyInit)] };
}

// 自测
const support = { 'node:crypto': true, 'node:path': true };
const modules = {
  'entry.ts': { isEntry: true, code: [
    "const big = new Map([['a',1],['b',2]]);",            // heavy-init
    "import { hash } from 'node:crypto';",
    "export function h(x) { return hash(x); }",
  ].join('\n') },
  'file.ts': { isEntry: false, code: "import fs from 'node:fs';" },   // 不支持
  'ok.ts': { isEntry: false, code: "import path from 'node:path';\nexport const f = () => loadX();" },
};
let r = auditEdge(modules, support);
console.log(r.problems[0].mod === 'file.ts' && r.problems[0].api === 'node:fs');
console.log(r.heavyInit.join(',') === 'entry.ts');
console.log(r.problems.length === 1);

// 未知 API 保守判定
r = auditEdge({ x: { isEntry: false, code: "import 'node:zlib';" } }, support);
console.log(r.problems[0].api === 'node:zlib');

// 无 node API
r = auditEdge({ y: { isEntry: true, code: 'export const a = 1;' } }, support);
console.log(r.problems.length === 0 && r.heavyInit.length === 0);
```

**评分点**：
- API 提取双形态（import from / require）；支持表未列出按不支持（保守判定）
- heavy-init 的顶层检测（剔除函数体后判定）与 entry 限定；去重排序输出
- 边界：无 API/无 entry 安全
- 能说清「顶层执行在每次冷启动付费，初始化瘦身比体积更优先」属于加分
