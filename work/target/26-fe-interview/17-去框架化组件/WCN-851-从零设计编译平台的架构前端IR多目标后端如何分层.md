---
title: [WCN-851] 从零设计一个「编译平台」的架构：前端 → IR → 多目标后端，如何分层？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-851：从零设计一个「编译平台」的架构：前端 → IR → 多目标后端，如何分层？

**答**：
- 结论先行：编译平台的标准分层是「前端（解析+语义分析）→ 中间表示 IR（与语言/目标无关）→ 优化 Pass → 多后端代码生成」——引入 IR 是为了让「M 种前端 × N 种目标」从 M×N 变成 M+N。
- 前端层：词法/语法分析生成 AST，做作用域、类型、响应式依赖分析（哪些是响应式插值、哪些是静态），输出统一的 IR。
- IR 层：用一种与源语言、目标平台都无关的表示（如带「响应式标记」的指令树、三地址码）——这是平台的核心资产，所有优化都作用在 IR 上。
- 优化 Pass：静态提升、死代码消除、常量折叠、依赖标记、副作用分析——以可插拔 Pass 形式串联，便于按需开关。
- 多后端：从 IR 生成不同目标代码——DOM 更新指令（浏览器）、SSR 字符串拼接、Native 模板指令、SourceMap；共享同一 IR 保证跨端语义一致。
- 追问钩子：面试官会问「为什么不直接 AST→目标代码」——答：那样每加一个目标都要为每个前端重写一遍，IR 是解耦枢纽；且优化只需在 IR 上做一次，所有后端受益。

```javascript
// 编译平台骨架：前端 → IR → Pass → 多后端
function compile(source, { front, passes, backend }) {
  const ast = front.parse(source);          // 前端：源码 → AST
  const ir = front.lower(ast);              // AST → 统一 IR（带响应式标记）
  let optimized = ir;
  for (const pass of passes) optimized = pass(optimized);  // 可插拔优化
  return backend.emit(optimized);           // 后端：IR → 目标代码
}
const ir = { kind: 'Template', children: [
  { kind: 'Text', value: '静态' },
  { kind: 'Expr', dep: 'count', raw: '{{count}}' },
] };
const hoist = (node) => ({ ...node, children: node.children.map(c =>
  c.kind === 'Text' ? { ...c, hoisted: true } : c) });
const domBackend = { emit: (n) => n.children.map(c => c.hoisted
  ? `setText(static_${c.value})` : `bindText(() => ${c.dep})`).join('\n') };
console.log(compile('tpl', { front: { parse: s => s, lower: () => ir }, passes: [hoist], backend: domBackend }));
```
