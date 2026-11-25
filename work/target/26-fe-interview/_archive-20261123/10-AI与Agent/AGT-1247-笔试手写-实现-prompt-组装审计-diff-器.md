---
title: [1247] 笔试手写：实现 prompt 组装审计 diff 器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, Prompt]
type: 笔试题
---

## 1247：笔试手写：实现 prompt 组装审计 diff 器

**需求**：实现 auditPrompt(template, rendered)：template 含 {var} 占位符，rendered 为实际组装结果。输出审计报告：未替换的残留占位符列表、被注入的未声明变量（rendered 中出现 {xxx} 而 template 没有）、以及模板字面量被意外改动的行（逐行 diff，报告首个不一致行号）。

```js
function auditPrompt(template, rendered) {
  const declared = [...template.matchAll(/\{(\w+)\}/g)].map(m => m[1]);
  const residual = [...rendered.matchAll(/\{(\w+)\}/g)]
    .map(m => m[1]).filter(v => declared.includes(v)); // 模板有但没替换掉
  const injected = [...rendered.matchAll(/\{(\w+)\}/g)]
    .map(m => m[1]).filter(v => !declared.includes(v));
  const tLines = template.split('\n'), rLines = rendered.split('\n');
  let firstDiff = null;
  for (let i = 0; i < Math.max(tLines.length, rLines.length); i++) {
    const t = tLines[i] ?? '', r = rLines[i] ?? '';
    const expect = t.replace(/\{\w+\}/g, '{*}'), actual = r.replace(/\{[^{}]*\}/g, '{*}');
    if (expect !== actual) { firstDiff = i + 1; break; } // 归一化占位后逐行比
  }
  return { residual, injected, firstDiff };
}
```

**评分点**：
- 占位符正则的声明集合与渲染集合分开提取
- 残留（该换没换）与注入（不该有却有）语义相反、不混淆
- 行级 diff 前先做占位符归一化（{*}），避免正常替换误报
- 能讨论：注入检测是安全防线之一，需配合白名单
