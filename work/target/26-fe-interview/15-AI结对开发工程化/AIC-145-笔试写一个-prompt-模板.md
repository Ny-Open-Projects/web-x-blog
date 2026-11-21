---
title: [AIC-145] 笔试：手写一个 Prompt 模板引擎，支持变量插值、条件段与默认值，并做槽位校验？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-145：笔试：手写一个 Prompt 模板引擎，支持变量插值、条件段与默认值，并做槽位校验？
**需求**：实现 `render(template, vars)`：
- `{{name}}` 插值；`{{name|默认值}}` 支持默认值；
- `{{#if cond}}...{{/if}}` 条件段，cond 为 false/undefined/空字符串/空数组时剔除；
- 缺失且无默认值的槽位必须抛错（防止把 `{{xxx}}` 原样发给模型）；
- 输出前后去多余空行但不破坏代码缩进。
**边界**：模板中可能含 JSON 花括号，不能误伤。

```javascript
function render(template, vars = {}) {
  const slotRe = /\{\{(\w+)(?:\|([^}]*))?\}\}/g;
  // 1. 槽位校验：无默认值且缺失 → 报错
  const missing = [...template.matchAll(/\{\{(\w+)(?:\|[^}]*?)?\}\}/g)]
    .map(m => m[1]).filter(k => !(k in vars) &&
      !new RegExp(`\\{\\{${k}\\|`).test(template));
  if (missing.length) throw new Error(`missing template vars: ${[...new Set(missing)]}`);

  // 2. 条件段处理
  let out = template.replace(/\{\{#if\s+(\w+)\}\}([\s\S]*?)\{\{\/if\}\}/g, (_, key, body) => {
    const v = vars[key];
    const truthy = v && (!Array.isArray(v) || v.length > 0);
    return truthy ? body : '';
  });

  // 3. 插值 + 默认值
  out = out.replace(slotRe, (_, key, def) => {
    const v = vars[key] ?? def ?? '';
    return Array.isArray(v) ? v.join('\n') : String(v);
  });

  // 4. 折叠 >2 个连续空行，去首尾空白
  return out.replace(/\n{3,}/g, '\n\n').trim();
}

// 测试
const tpl = `# 任务\n{{task}}\n{{#if withCode}}参考代码：\n\`\`\`\n{{code}}\n\`\`\`{{/if}}\n{{lang|TypeScript}} 版本`;
console.log(render(tpl, { task: '写 debounce', withCode: true, code: 'a(b)' }));
// 任务段出现，lang 用默认值
console.log(render(tpl, { task: 'x', withCode: false }));
// 条件段整段消失
```

**评分点**：
1. 槽位缺失必须 fail-fast（抛错而非静默输出 `{{xxx}}`），这是发给模型前最关键的一道闸；
2. 条件段的正则要用非贪婪且跨行匹配（`[\s\S]*?`），漏掉会导致条件段吞掉后续内容；
3. 默认值与校验顺序：先校验「真缺失」，再处理默认值，顺序错了合法模板会误报；
4. 是否考虑嵌套条件/转义花括号（追问级，能说出 limitation 加分）；
5. 代码缩进与空行折叠不能破坏代码块内容。
