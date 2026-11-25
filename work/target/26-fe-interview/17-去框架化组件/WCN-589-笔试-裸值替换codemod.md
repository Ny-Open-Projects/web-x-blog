---
title: [WCN-589] 笔试：实现「裸值检测 + 自动替换建议」的 codemod（颜色/间距/圆角字面量 → token）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-589：笔试：实现「裸值检测 + 自动替换建议」的 codemod（颜色/间距/圆角字面量 → token）。

**答**：
- 结论：扫描源码中的裸值，按映射表（字面量 → token）替换为 var(--token)，无法映射的给出人工建议。
- 颜色精确匹配映射表；间距按最接近的 token 档位建议（如 13px → --space-3 12px 或 --space-4 16px）。
- 生成 diff 预览而非直接写回，人工确认后应用。
- 追问：如何避免误替换（如非样式上下文的数字）？（答：只在 CSS 声明值位置替换，解析 CSS AST 而非纯文本）

```javascript
const MAP = { '#fff': '--color-white', '#000': '--color-black', '#ff5000': '--color-brand' };
const SPACE = [4, 8, 12, 16, 24, 32];
function suggest(value) {
  if (MAP[value]) return { token: MAP[value], exact: true };
  const px = parseFloat(value);
  if (!isNaN(px)) { const near = SPACE.reduce((a,b)=>Math.abs(b-px)<Math.abs(a-px)?b:a); return { token: `--space-${near}`, exact: near === px }; }
  return null;
}
function codemod(css) {
  return css.replace(/:\s*(#[0-9a-f]{3,8}|\d+px)\b/gi, (full, val) => {
    const s = suggest(val); return s ? `: var(${s.token})${s.exact ? '' : ' /* 建议值，请确认 */'}` : full;
  });
}
```

**评分点**：
- 字面量→token 映射表
- 间距最近档位建议
- diff 预览人工确认
- CSS AST 上下文避免误替换
