---
title: [RBL-149] 笔试：手写未使用 import 清理器（AST 收集 + 重写）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-149：笔试：手写未使用 import 清理器（AST 收集 + 重写）

**答**：写 remove-unused-imports.ts：1) 解析源码收集所有 import 声明的导入标识符；2) 扫描 AST 其余部分统计标识符实际使用（含 JSX 中使用的组件）；3) 删除整个未使用的 import 语句；部分使用的 ImportSpecifier 只保留用到的子句；4) 使用位置偏移列表从后往前做文本重写（避免位移）；5) 输出清理后代码与删除清单。

```typescript
// remove-unused-imports.ts
import { parseSync } from 'oxc-parser';

export function clean(source: string) {
  const ast = parseSync('a.tsx', source, { sourceType: 'module', lang: 'tsx' }).program;
  const imported: { name: string; start: number; end: number; fullStart: number; specEnd: number }[] = [];
  const used = new Set<string>();

  walk(ast, {
    ImportDeclaration(n: any) {
      for (const s of n.specifiers) {
        const local = s.local.name; // default/named/namespace
        imported.push({ name: local, start: s.span.start, end: s.span.end,
          fullStart: n.span.start, specEnd: n.span.end });
      }
    },
    Identifier(n: any) { if (!n.span.__inImport) used.add(n.name); },
    JSXIdentifier(n: any) { used.add(n.name); }, // <Button/> 属于 JSXIdentifier
  });

  const spans: Array<[number, number]> = [];
  const removed: string[] = [];
  for (const imp of imported) {
    if (used.has(imp.name)) continue;
    // 简化策略：整条 import 的 specifier 段删除；单个 specifier 直接删 span
    spans.push([imp.start, imp.end]); // 从后往前删可保偏移不变
    removed.push(imp.name);
  }
  let result = source;
  for (const [s, e] of [...spans].sort((a, b) => b[0] - a[0])) {
    result = result.slice(0, s) + result.slice(e); // 倒序删除避免位移
  }
  return { code: result, removed };
}
// 注意边界：类型使用（type 位置）、字符串内同名不算使用、side-effect import 保留。
```
**评分点**：
- 收集与使用统计分离，JSX 标识符单独处理（JSXIdentifier）。
- 从后往前重写避免 span 位移（或改为生成 AST 输出）。
- 部分 specifier 保留逻辑（只删未用子句）有考虑。
- side-effect import（`import './x'`）与 type import 边界处理。
- 能指出生产直接用 ESLint no-unused-vars --fix 或 oxlint autofix。
