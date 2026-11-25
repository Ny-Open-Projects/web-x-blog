---
title: [WCN-465] 笔试：实现 token 消费审计（未使用 token / 裸值残留）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-465：笔试：实现 token 消费审计（未使用 token / 裸值残留）。
**答**：输入 token 定义与全仓组件样式。输出：零消费 token 清单（候选删除）、裸值残留（组件内硬编码但存在近似 token）。

```javascript
function tokenAudit(tokens, styles) {
  const used = new Set();
  for (const s of styles) for (const m of s.matchAll(/var\(--ds-([\w-]+)\)/g)) used.add(m[1]);
  const unused = Object.keys(tokens).filter(t => !used.has(t));
  const raw = [];
  for (const s of styles)
    for (const [tk, tv] of Object.entries(tokens))
      if (s.includes(tv) && tv.startsWith('#')) raw.push({ token: tk, value: tv });
  return { unused, rawLeft: raw };
}

```

**评分点**：
- 消费扫描（var(--ds-x) 引用计数）。
- 零消费清单（季度审计删除候选）。
- 裸值近似匹配（颜色值相等 → 建议替换 token）。
- 输出治理报告。
