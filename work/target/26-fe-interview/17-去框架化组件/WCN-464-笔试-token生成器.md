---
title: [WCN-464] 笔试：实现 token JSON → CSS 变量的生成器（含主题映射）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-464：笔试：实现 token JSON → CSS 变量的生成器（含主题映射）。
**题目**：输入 `tokens: {primitive: {...}, semantic: {...}}` 与主题映射 `{dark: {overrides}}`。输出 light/dark 两份 CSS（语义层引用 primitive；dark 覆盖）。

```javascript
const kebab = s => '--ds-' + s.replace(/[A-Z]/g, c => '-' + c.toLowerCase());
function genCSS(tokens, darkOverrides = {}) {
  const all = { ...tokens.semantic, ...tokens.primitive };
  const light = Object.entries(all).map(([k, v]) => `${kebab(k)}: ${v};`).join('\n');
  const dark = Object.entries({ ...all, ...darkOverrides })
    .map(([k, v]) => `${kebab(k)}: ${v};`).join('\n');
  return { light: `:root { ${light} }`, dark: `.dark { ${dark} }` };
}

```

**评分点**：
- 语义层 → primitive 引用（var() 链）。
- dark overrides 覆盖对应变量。
- 命名转换（camelCase → kebab，加 --ds- 前缀）。
- 输出可直挂 :root/.dark。
