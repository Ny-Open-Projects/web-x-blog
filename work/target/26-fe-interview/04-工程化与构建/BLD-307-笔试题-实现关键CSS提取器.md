---
title: [BLD-307] 笔试题——实现关键 CSS 提取器（首屏样式内联）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-307：手写关键 CSS 提取

**需求与边界**：
- 需求：从全量 CSS 中提取首屏关键样式——① 解析 HTML 首屏 DOM（首屏元素集合）；② CSS 规则匹配（选择器命中首屏元素的规则保留）；③ 关键 CSS 内联 + 全量 CSS 异步加载（SCN-BLD-236 双通道）；④ 体积控制（关键 CSS 上限——超限警告说明首屏过重）。
- 边界：① 选择器匹配简化（类/标签/ID 命中——伪类/后代近似处理保守保留）；② @media/@keyframes 关联保留（命中的动画/media 块跟随）；③ 提取后 HTML 注入位置（head 内联 style）。

**答**：
```javascript
function extractCriticalCSS(html, css, { maxKB = 14 } = {}) {
  const firstPaintEls = parseAboveFold(html);          // 首屏元素集合
  const matched = new Set();
  const rules = parseCssRules(css);
  const out = [];
  for (const rule of rules) {
    if (rule.type === 'keyframes' && referencedBy(rule, matched)) out.push(rule);   // 动画跟随
    if (rule.type !== 'style') continue;
    if (rule.selectors.some(sel => firstPaintEls.some(el => selectorMatches(sel, el)))) {
      out.push(rule); matched.add(rule);
    }
  }
  const critical = stringify(out);
  const kb = Buffer.byteLength(critical) / 1024;
  if (kb > maxKB) warn(`关键 CSS ${kb.toFixed(1)}KB 超限——首屏样式过重`);
  return {
    critical,                                          // 内联进 <head>
    rest: stripRules(css, out),                        // 全量 CSS（异步加载）
  };
}
// HTML 注入
// <style>${critical}</style><link rel="preload" href="full.css" as="style" onload="this.rel='stylesheet'">
```

**评分点**:
- 规则匹配 + 动画/media 跟随保留（关联规则不丢）。
- 双通道输出（内联 + 异步全量——SCN-BLD-236）。
- 体积上限警告（首屏过重的哨兵）。
- 选择器匹配的保守策略（伪类近似保留）。
