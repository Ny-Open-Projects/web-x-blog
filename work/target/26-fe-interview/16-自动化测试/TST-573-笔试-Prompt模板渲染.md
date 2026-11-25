---
title: [TST-573] 笔试：笔试：Prompt 模板渲染与变量注入
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-573：笔试：笔试：Prompt 模板渲染与变量注入

**题目**：实现 renderPrompt(template, vars, opts)。模板用 {{var}} 占位符，支持 {{#if cond}}...{{/if}} 条件块与 {{var}} 转义。opts={ strict:boolean, escape:boolean }。要求：① 简单变量替换 {{name}}；② 条件块 {{#if enabled}}...{{/if}}，enabled 为真才保留块内容；③ escape=true 时对变量值做 HTML 转义（& < > " '）；④ strict=true 时遇到缺失变量抛错，否则替换为空串；⑤ 边界：嵌套条件块可不支持但需说明，模板为空返回空串。

**答**：
- 结论：用正则分步处理——先处理条件块（递归/栈），再替换变量，最后按 opts 转义与严格校验。
- 实现要点：条件块用正则 /{{#if (\w+)}}([\s\S]*?){{\/if}}/g；变量替换用 /{{(\w+)}}/g，replace 回调中按 strict 决定抛错或空串；escape 做字符映射。
- 追问钩子：为什么要转义？——防止注入（用户输入含 {{ 或 HTML 标签时破坏 Prompt 结构或引发 XSS 展示）；Prompt 也是代码，需防注入。

```javascript
function renderPrompt(template = '', vars = {}, opts = {}) {
  const { strict = false, escape = false } = opts;
  const esc = s => escape ? String(s).replace(/[&<>"']/g, c =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])) : String(s);
  // 1) 条件块
  let out = template.replace(/{{#if (\w+)}}([\s\S]*?){{\/if}}/g, (_, k, body) =>
    vars[k] ? body : '');
  // 2) 变量
  out = out.replace(/{{(\w+)}}/g, (_, k) => {
    if (!(k in vars)) { if (strict) throw new Error(`缺失变量: ${k}`); return ''; }
    return esc(vars[k]);
  });
  return out;
}
console.log(renderPrompt('Hi {{name}}{{#if vip}}, VIP{{/if}}', { name: 'A' }));
```

**评分点**：
- 条件块 {{#if}}...{{/if}} 按变量真假保留/移除。
- 变量替换 + escape HTML 转义映射正确。
- strict 缺失变量抛错，非 strict 替换为空串。
- 边界（空模板、嵌套限制说明）处理到位。
