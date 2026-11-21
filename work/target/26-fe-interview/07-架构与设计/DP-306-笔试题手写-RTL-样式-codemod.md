---
title: [DP-306] 笔试题：手写 RTL 样式 codemod（physical→logical）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-306：笔试题：手写 RTL 样式 codemod（physical→logical）？
**题目**：实现 CSS codemod：1) 替换 physical 属性为 logical（margin-left→margin-inline-start 等 8 组映射）；2) 保留值不变；3) border 复合简写拆分处理（border-left: 1px solid → border-inline-start）；4) 输出变更报告（文件/行/替换对）。
**评分点**：
- 映射表完备（left/right → inline-start/end）。
- 复合简写正确拆分（保留 thickness/style/color）。
- text-align: left → start 特例处理。
- 报告可 review（位置精确）。
```javascript
const MAP = {
  'margin-left': 'margin-inline-start', 'margin-right': 'margin-inline-end',
  'padding-left': 'padding-inline-start', 'padding-right': 'padding-inline-end',
  'border-left': 'border-inline-start', 'border-right': 'border-inline-end',
};
function cssCodemod(css, file) {
  const changes = [];
  let out = css.replace(/^(\s*)([a-z-]+)\s*:\s*([^;]+);/gm, (m, indent, prop, value) => {
    if (prop === 'text-align' && /left|right/.test(value)) {       // 3) 特例
      changes.push({ file, prop, value, to: value === 'left' ? 'start' : 'end' });
      return `${indent}text-align: ${value === 'left' ? 'start' : 'end'};`;
    }
    const target = MAP[prop];
    if (!target) return m;
    changes.push({ file, prop, value, to: target });               // 1)+2)
    return `${indent}${target}: ${value};`;
  });
  return { out, changes };                                          // 4)
}
// border-left 简写示例：'border-left: 1px solid #eee' → 'border-inline-start: 1px solid #eee'
```
