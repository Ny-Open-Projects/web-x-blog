---
title: [WCN-444] 笔试：实现元素样式的 RTL 校验器（物理方向属性扫描）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-444：笔试：实现元素样式的 RTL 校验器（物理方向属性扫描）。
**答**：扫描 CSS：left/right/top/bottom 物理属性（非 inset-logical）→ 违规；transform translateX 无 dir 分支 → 警告；输出建议（margin-inline-start 等）。

```javascript
const RTL_RULES = [
  { re: /(?:margin|padding)-(left|right):/, fix: m => m.replace(/left/, 'inline-start').replace(/right/, 'inline-end') },
  { re: /(?:left|right):/, kind: 'position', fix: () => 'inset-inline-start/end' },
  { re: /translateX\(/, kind: 'warn', fix: () => '检查方向语义（RTL 需镜像）' },
];
function rtlLint(css) {
  return css.split('\n').map((line, i) => ({ line, n: i + 1 }))
    .filter(({ line }) => RTL_RULES.some(r => r.re.test(line)))
    .map(({ line, n }) => ({ line: n, text: line.trim(),
      fix: RTL_RULES.find(r => r.re.test(line)).fix(line.trim()) }));
}

```

**评分点**：
- 物理属性正则（padding-left 等）。
- 逻辑属性白名单（inline-start 等）。
- translateX 警告（方向语义）。
- 建议映射（left → inset-inline-start）。
