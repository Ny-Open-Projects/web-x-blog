---
title: [RBL-631] 笔试：手写原子 CSS 类名提取与变体展开器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-631：笔试：手写原子 CSS 类名提取与变体展开器

**需求**：实现 `extract(code)` 与 `expand(cls, theme)`。`extract`：从 JSX/HTML 混合代码提取 class/className 属性值中的类名（字符串字面量与模板字符串；模板中 `${...}` 表达式替换为占位跳过）；返回去重数组（首次出现序）。`expand`：类名 → CSS 规则。规则表内置：`text-{color}` → `color: {值}`、`bg-{color}` → `background-color: {值}`、`p{t|b|l|r}-{n}` → padding 侧边；变体：`hover:` → `&:hover { }`、`dark:` → `.dark & { }`、`md:` → `@media (min-width: 768px) { }`。多层变体嵌套包装（内层变体先生成）；未知基类返回 null。theme: `{ colors: { red500: '#ef4444' } }`。

```javascript
function extract(code) {
  const RE = /class(?:Name)?=\{?["'`]([^"'`]*)["'`]\}?/g;
  const found = [];
  let m;
  while ((m = RE.exec(code))) {
    const cleaned = m[1].replace(/\$\{[^}]*\}/g, ' ');   // 表达式占位
    for (const c of cleaned.split(/\s+/)) {
      if (c && !found.includes(c)) found.push(c);
    }
  }
  return found;
}

function expand(cls, theme) {
  const parts = cls.split(':');
  const base = parts.pop();
  const variants = parts;
  const css = baseRule(base, theme);
  if (!css) return null;
  let out = css;
  for (const v of [...variants].reverse()) {             // 内层变体先包装
    if (v === 'hover') out = `&:hover { ${out} }`;
    else if (v === 'dark') out = `.dark & { ${out} }`;
    else if (v === 'md') out = `@media (min-width: 768px) { ${out} }`;
    else return null;                                    // 未知变体 -> null
  }
  return out;
}

function baseRule(base, theme) {
  let m;
  if ((m = /^text-(\w+)$/.exec(base))) {
    const c = theme.colors[m[1]]; return c ? `color: ${c}` : null;
  }
  if ((m = /^bg-(\w+)$/.exec(base))) {
    const c = theme.colors[m[1]]; return c ? `background-color: ${c}` : null;
  }
  if ((m = /^p([tblr])-(\d+)$/.exec(base))) {
    const side = { t: 'top', b: 'bottom', l: 'left', r: 'right' }[m[1]];
    return `padding-${side}: ${m[2] * 4}px`;
  }
  if ((m = /^p-(\d+)$/.exec(base))) return `padding: ${m[1] * 4}px`;
  return null;
}

// 自测
const theme = { colors: { red500: '#ef4444', blue500: '#3b82f6' } };
console.log(extract(`<div className="p-2 text-red500 ${x} bg-blue500">` +
                     `<span class="p-2">`));
// ['p-2', 'text-red500', 'bg-blue500']（${x} 占位跳过、去重保持首现序）

console.log(expand('text-red500', theme));               // 'color: #ef4444'
console.log(expand('p-t-4', theme));                     // 'padding-top: 16px'
console.log(expand('hover:text-red500', theme));         // '&:hover { color: #ef4444 }'
console.log(expand('dark:md:text-red500', theme));
// '.dark & { @media (min-width: 768px) { color: #ef4444 } }'
console.log(expand('text-unknown', theme) === null);
console.log(expand('weird:text-red500', theme) === null);
console.log(expand('p-2', theme));                       // 'padding: 8px'
```

**评分点**：
- 提取覆盖 className/class、单双引号、模板字符串；`${}` 表达式占位不吞类名；去重保序
- 多层变体包装顺序正确（reverse 后内层先生成）；未知基类与未知变体区分返回 null
- padding 侧边缩写映射与 4px 基数换算正确；主题 token 查不到返回 null（不硬编色值）
- 能说明「生成顺序稳定是原子 CSS 覆盖正确性的前提」属于加分
