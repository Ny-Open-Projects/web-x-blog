---
title: [AIC-414] 笔试：实现带变量与条件块的提示词模板渲染器。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-414：笔试：实现带变量与条件块的提示词模板渲染器。
**题目**：模板语法：`{{var}}` 变量；`{{#if var}}...{{/if}}` 条件块。实现 `render(tpl, vars)`，未定义变量渲染为空且收集 warning 列表。

```javascript
function render(tpl, vars = {}) {
  const warnings = [];
  const ifRe = /\{\{#if\s+(\w+)\}\}([\s\S]*?)\{\{\/if\}\}/;
  let out = tpl;
  let m;
  while ((m = ifRe.exec(out))) {
    const on = Boolean(vars[m[1]]);
    out = out.replace(m[0], on ? m[2] : '');
  }
  out = out.replace(/\{\{(\w+)\}\}/g, (_, k) => {
    if (!(k in vars)) warnings.push(`missing var: ${k}`);
    return String(vars[k] ?? '');
  });
  return { out, warnings };
}
console.log(render(
  '评审 {{file}}。{{#if strict}}附规范：{{rules}}{{/if}}。',
  { file: 'a.ts', strict: true }));
// 严格模式缺 rules → warning + 空串，不会静默出错

```

**评分点**：
- 条件块支持嵌套或至少正确处理非贪婪匹配。
- 未定义变量：输出空串 + warning（静默输出空是事故来源）。
- 转义：变量值中含模板语法不再二次解析（渲染一遍即止）。
- 测试覆盖：变量、条件开/关、未定义变量警告。
