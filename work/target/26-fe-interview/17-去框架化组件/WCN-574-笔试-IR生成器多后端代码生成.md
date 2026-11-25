---
title: [WCN-574] 笔试：实现「模板 IR 生成器 + 多后端代码生成」（IR 节点 → 两种目标代码）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-574：笔试：实现「模板 IR 生成器 + 多后端代码生成」（IR 节点 → 两种目标代码）。

**答**：
- 结论：先把模板 AST 归一化为平台无关 IR（Element/Text/Bind/Derive），再为两种后端各写 codegen。
- IR 节点类型精简，更新意图用 Bind/Derive 显式表达。
- 后端 A 生成 signal-bind 风格，后端 B 生成直写 DOM 风格，行为等价。
- 追问：如何保证多后端行为一致？（答：同一 IR 跑 golden 测试，断言输出快照一致）

```javascript
function toIR(ast) {
  if (ast.type === 'Text') return { type: 'Text', value: ast.dynamic ? { type: 'Derive', expr: ast.expr } : ast.value };
  if (ast.type === 'Element') return { type: 'Element', tag: ast.tag,
    props: ast.attrs.map(a => ({ name: a.name, value: a.isEvent ? { type: 'Bind', expr: a.expr, kind: 'event' } : a.value })),
    children: (ast.children || []).map(toIR) };
}
function genSignal(ir) {
  if (ir.type === 'Text') return ir.value.type === 'Derive' ? `bindText(() => ${ir.value.expr})` : `text("${ir.value}")`;
  if (ir.type === 'Element') return `el("${ir.tag}", [${ir.children.map(genSignal).join(',')}])`;
}
function genDirect(ir) {
  if (ir.type === 'Text') return ir.value.type === 'Derive' ? `node.textContent=${ir.value.expr}` : `"${ir.value}"`;
  return `createElement(${ir.tag})`;
}
```

**评分点**：
- AST→IR 归一化
- Bind/Derive 显式更新意图
- 两种后端等价 codegen
- golden 测试保证一致
