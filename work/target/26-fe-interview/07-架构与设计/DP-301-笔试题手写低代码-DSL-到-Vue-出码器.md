---
title: [DP-301] 笔试题：手写低代码 DSL→Vue 出码器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-301：笔试题：手写低代码 DSL→Vue 出码器？
**题目**：实现 `generate(dsl) → vue SFC 字符串`：1) 组件树递归生成 template（缩进）；2) props 中表达式 `{{expr}}` 转为 :prop 绑定；3) 事件 onClick 字符串表达式转 @click 方法引用；4) 生成 script setup（数据源/方法声明）。
**评分点**：
- 递归生成正确（children 嵌套 + 缩进）。
- 表达式 vs 字面量区分正确（type: 'expression' → :bind）。
- 事件方法去重声明（同名方法只生成一次）。
- 产物可读（语义命名、空行）。
```javascript
function generate(dsl) {
  const methods = new Set();
  const template = (node, indent = '  ') => {
    const tag = kebabCase(node.componentName);
    const attrs = Object.entries(node.props ?? {}).map(([k, v]) => {
      if (v && v.type === 'expression') return `:${k}="${v.value}"`;   // 2) 表达式绑定
      if (k === 'onClick') { const fn = exprFnName(v); methods.add(fn); return `@click="${fn}"`; }  // 3)
      return typeof v === 'string' ? `${k}="${v}"` : `:${k}="${JSON.stringify(v)}"`;
    }).join(' ');
    const kids = (node.children ?? []).map(c => template(c, indent + '  ')).join('\n');
    return kids ? `${indent}<${tag} ${attrs}>\n${kids}\n${indent}</${tag}>`
                : `${indent}<${tag} ${attrs}/>`;
  };
  const body = (dsl.components ?? []).map(c => template(c)).join('\n');
  const script = `<script setup>\n${[...methods].map(m => `const ${m} = () => { /* TODO */ };`).join('\n')}\n</script>`;  // 4)
  return `<template>\n${body}\n</template>\n\n${script}`;
}
const kebabCase = s => s.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
const exprFnName = (v) => `on_${v.replace(/\W+/g, '_').slice(0, 20)}`;
```
