---
title: [WCN-670] 笔试：实现多目标编译器的 IR 与后端（HIR → React/Vue/WC 代码生成）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-670：笔试：实现多目标编译器的 IR 与后端（HIR → React/Vue/WC 代码生成）

**答**：
- 需求：定义 HIR 节点（element/component/text/binding），实现 compile(hir, target) 按 target 生成对应框架代码：react 用 {} 表达式、vue 用 {{}} / :prop、wc 用原生标签 + 属性。
- 思路：递归遍历 HIR；每种 target 一个 emit 函数处理节点/属性/绑定；未知类型抛错。
- 边界：动态属性绑定语法按 target 转换；文本插值转义；自闭合标签处理。

```javascript
const emit = {
  react(node) {
    if (node.type === 'text') return node.value;
    const props = (node.props || []).map(p => ` ${p.name}={${p.expr}}`).join('');
    const kids = (node.children || []).map(c => emit.react(c)).join('');
    return `<${node.tag}${props}>${kids}</${node.tag}>`;
  },
  vue(node) {
    if (node.type === 'text') return node.value.replace(/\{\{/g, '&lbrace;');
    const props = (node.props || []).map(p => ` :${p.name}="${p.expr}"`).join('');
    const kids = (node.children || []).map(c => emit.vue(c)).join('');
    return `<${node.tag}${props}>${kids}</${node.tag}>`;
  },
  wc(node) {
    if (node.type === 'text') return node.value;
    const tag = node.tag.startsWith('ds-') ? node.tag : `ds-${node.tag}`;
    const props = (node.props || []).map(p => ` ${p.name}="${p.expr}"`).join('');
    return `<${tag}${props}></${tag}>`;
  },
};
export function compile(hir, target) {
  if (!emit[target]) throw new Error(`未知目标 ${target}`);
  return emit[target](hir);
}
const hir = { type: 'element', tag: 'Button', props: [{ name: 'disabled', expr: 'loading' }],
  children: [{ type: 'text', value: '提交' }] };
console.log(compile(hir, 'react')); // <Button disabled={loading}>提交</Button>
```

**评分点**：
- HIR 结构清晰，递归遍历正确生成子节点。
- 三种 target 的属性绑定语法转换准确（{}/:/）。
- WC 目标自动加 ds- 前缀（平台约定映射）。
- 未知目标抛错，文本插值做基本转义。
