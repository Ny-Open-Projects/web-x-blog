---
title: [WCN-436] 笔试：实现元素 shadow 样式的「裸值」静态校验器。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-436：笔试：实现元素 shadow 样式的「裸值」静态校验器。
**题目**：输入元素 CSS 文本：颜色（#hex/rgb）、间距（px 除 0）、字体（除 var）出现即违规；var(--ds-*) 合法。输出违规行与建议 token。

```javascript
const RULES = [
  { re: /#[0-9a-fA-F]{3,8}\b|rgba?\(/, kind: 'color',
    suggest: { '#fff': 'var(--ds-surface)', '#000': 'var(--ds-text)' } },
  { re: /\b\d+px\b/, kind: 'spacing', allow: /var\(|0px/ },
  { re: /font(-size)?:\s*(?!var)/, kind: 'font' },
];
function lintTokens(css) {
  return css.split('\n').map((line, i) => ({ line, n: i + 1 }))
    .filter(({ line }) => RULES.some(r => r.re.test(line) && !(r.allow?.test(line))))
    .map(({ line, n }) => ({ line: n, text: line.trim(),
      suggest: RULES.find(r => r.re.test(line))?.kind }));
}

```

**评分点**：
- 正则三类检测（颜色/间距/字体）。
- var(--ds-*) 白名单。
- 建议映射（#fff → --ds-surface 等近似表）。
- 输出行号（修复定位）。
