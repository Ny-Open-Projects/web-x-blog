---
title: [MFW-764] 笔试：手写 Token 到 CSS 变量生成器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-764：笔试：手写 Token → CSS 变量生成器

**答**：实现 `tokensToCss(tokens, { brands, themes })`。tokens: 嵌套对象 `{ color: { primary: { value: '#3b82f6', brands?: { acme: '#ff0000' } }, bg: { value: '#fff', dark: '#111' } } }`；brands: 品牌数组；themes: 主题数组。规则：1) **扁平化**：嵌套 token → CSS 变量名（`color.primary` → `--color-primary`——点号→连字符）；2) **品牌层**：`[data-brand="acme"] { --color-primary: #ff0000 }`（品牌覆盖 RBL-668）；3) **主题层**：`[data-theme="dark"] { --color-bg: #111 }`（暗色覆盖）；4) **品牌+主题交集**：`[data-brand="acme"][data-theme="dark"]`——品牌在暗色下的覆盖（两级交集——最高优先级）；5) 返回 `{ css, vars: string[] }`（vars = 全部变量名——供 client JS 读 RBL-918）。边界：空 tokens；无 brands/themes（只 :root）；循环引用（RBL-698 校验——引用其他 token 的 value）。

```javascript
function tokensToCss(tokens, { brands = [], themes = [] } = {}) {
  const flat = {};
  function flatten(obj, prefix = '') {
    for (const [k, v] of Object.entries(obj ?? {})) {
      const name = prefix ? `${prefix}-${k}` : k;
      if (v && typeof v === 'object' && ('value' in v || 'brands' in v || 'dark' in v)) {
        flat[name] = v;
      } else if (v && typeof v === 'object') {
        flatten(v, name);                                 // 嵌套继续
      } else flat[name] = { value: v };
    }
  }
  flatten(tokens);
  const varName = (k) => `--${k}`;
  const entries = Object.entries(flat);
  const vars = entries.map(([k]) => varName(k));
  const decl = (vars_) => vars_.map(([k, v]) => `${varName(k)}: ${v};`).join('\n  ');
  // :root 默认层
  let css = `:root {\n  ${decl(entries.map(([k, v]) => [k, v.value ?? v]))}\n}`;
  // 品牌层
  for (const brand of brands) {
    const overrides = entries.filter(([k, v]) => v.brands?.[brand] !== undefined);
    if (overrides.length)
      css += `\n[data-brand="${brand}"] {\n  ${decl(overrides.map(([k, v]) => [k, v.brands[brand]]))}\n}`;
  }
  // 主题层
  for (const theme of themes) {
    const overrides = entries.filter(([k, v]) => v[theme] !== undefined);
    if (overrides.length)
      css += `\n[data-theme="${theme}"] {\n  ${decl(overrides.map(([k, v]) => [k, v[theme]]))}\n}`;
  }
  // 品牌 + 主题交集
  for (const brand of brands)
    for (const theme of themes) {
      const both = entries.filter(([k, v]) =>
        v.brands?.[brand]?.[theme] !== undefined);
      if (both.length)
        css += `\n[data-brand="${brand}"][data-theme="${theme}"] {\n  ${decl(both.map(([k, v]) => [k, v.brands[brand][theme]]))}\n}`;
    }
  return { css, vars };
}

// 自测
const tokens = {
  color: { primary: { value: '#3b82f6', brands: { acme: '#ff0000' } },
    bg: { value: '#fff', dark: '#111111' } },
  radius: { value: '8px' },
};
let r = tokensToCss(tokens, { brands: ['default', 'acme'], themes: ['light', 'dark'] });
console.log(r.css.includes('--color-primary: #3b82f6'));   // :root 默认
console.log(r.css.includes('[data-brand="acme"]'));        // 品牌层
console.log(r.css.includes('--color-primary: #ff0000'));   // acme 覆盖
console.log(r.css.includes('[data-theme="dark"]'));        // 主题层
console.log(r.css.includes('--color-bg: #111111'));
console.log(r.vars.includes('--color-primary'));           // 变量名清单
console.log(r.vars.includes('--radius'));
console.log(!r.css.includes('[data-brand="default"]'));    // default 无覆盖不生成
// 空 tokens
r = tokensToCss({}, { brands: ['a'] });
console.log(r.vars.length === 0 && r.css.includes(':root'));
```

**评分点**：
- 嵌套扁平化（点号→连字符的变量名转换）；三层覆盖（:root/brand/theme）+ 品牌×主题交集
- 变量名清单（vars——供 client JS getPropertyValue RBL-918）；空 tokens 安全
- 边界（无 brands/themes/default 品牌跳过/循环引用由 RBL-698 前置校验）
- 能说清「Token → CSS 变量的三层架构（root/brand/theme）+ 品牌×主题交集——多品牌多主题的完整覆盖」属于加分
