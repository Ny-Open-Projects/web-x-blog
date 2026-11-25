---
title: [RBL-148] 笔试：手写 import 依赖扫描器（基于 parser 的 AST 统计）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-148：笔试：手写 import 依赖扫描器（基于 parser 的 AST 统计）

**答**：写 scan-deps.mjs：1) 输入一个文件，解析 AST（可用 oxc-parser 或任意 parser）；2) 统计四类依赖：静态 import、动态 import()、require() 调用、export ... from；3) 区分外部包（非相对路径，取 bare specifier 的包名，支持 @scope/name）与内部文件；4) 输出 { external: [...], internal: [...], dynamic: [...], reexport: [...] }，各自去重排序；5) parse 失败输出 errors 并继续（返回空结构 + 错误信息）。

```javascript
// scan-deps.mjs
import { parseSync } from 'oxc-parser';
import { readFileSync } from 'node:fs';

function pkgName(spec) { // bare specifier → @scope/name 或 name
  const parts = spec.split('/');
  return spec.startsWith('@') ? parts.slice(0, 2).join('/') : parts[0];
}
const isInternal = (s) => s.startsWith('.') || s.startsWith('/');

export function scanDeps(file) {
  const out = { external: [], internal: [], dynamic: [], reexport: [], errors: [] };
  let ast;
  try {
    ast = parseSync(file, readFileSync(file, 'utf8'), { sourceType: 'module', lang: 'tsx' }).program;
  } catch (e) { out.errors.push(e.message); return out; }

  walk(ast, {
    ImportDeclaration(n) {
      if (n.importKind === 'type') return; // TS type-only import 不算运行时依赖
      (isInternal(n.source.value) ? out.internal : out.external).push(n.source.value);
    },
    ExportAllDeclaration(n) { out.reexport.push(n.source.value); },
    ExportNamedDeclaration(n) {
      if (n.source) out.reexport.push(n.source.value);
    },
    CallExpression(n) {
      const arg = n.arguments?.[0];
      if (n.callee?.name === 'require' && arg?.value) {
        (isInternal(arg.value) ? out.internal : out.external).push(arg.value);
      }
      if (n.callee?.type === 'Import' && arg?.value) out.dynamic.push(arg.value);
    },
    ImportExpression(n) { // oxc/ESTree 变体：import() 单独节点
      if (n.source?.value) out.dynamic.push(n.source.value);
    },
  });

  const dedup = (a) => [...new Set(a)].sort();
  return { external: dedup(out.external), internal: dedup(out.internal),
           dynamic: dedup(out.dynamic), reexport: dedup(out.reexport), errors: out.errors };
}

// 输出示例：{ external: ['react'], internal: ['./utils'], dynamic: [], reexport: [] }
console.log(scanDeps(process.argv[2] ?? 'a.tsx'));
```
**评分点**：
- 四类依赖覆盖：静态 import / 动态 import / require / re-export。
- type-only import 剔除（运行时依赖语义）。
- bare specifier 的 @scope/name 包名提取正确。
- 去重 + 排序保证输出稳定。
- parse 失败不抛、收集 errors。
- 能说出适用场景：依赖审计、构建缓存 key、affected 检测。
