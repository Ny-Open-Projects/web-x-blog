---
title: [CSS-110] ITCSS 分层架构是什么？如何与 @layer 结合落地？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-110：ITCSS 分层架构是什么？如何与 @layer 结合落地？

**答**：
- ITCSS 按影响力从大到小倒序分层：Settings → Tools → Generic → Elements → Objects → Components → Utilities。
- 后写的层覆盖先写的层，靠"源顺序"而非选择器优先级解决冲突，全项目可告别 !important 军备竞赛。
- Utilities 在最底层，保证工具类永远能覆盖组件样式。
- 原生 `@layer` 让 ITCSS 从"目录约定"升级为"浏览器强制的级联顺序"，第三方样式可显式压到低层。
- 典型落点：reset 归 generic、原子类归 utilities、第三方库样式单独一层且置于 components 之前。

```css
/* @layer 落地 ITCSS：一次声明固定层序 */
@layer generic, vendor, objects, components, utilities;

@layer generic {
  *, *::before, *::after { box-sizing: border-box; }
  body { margin: 0; }
}

@layer components {
  .btn { padding: 8px 16px; background: var(--color-accent); }
}

@layer utilities {
  .mt-0 { margin-top: 0 !important; } /* 即使不用 important 也已高于 components */
}

/* 层外样式（如临时实验代码）优先级高于所有层，注意收敛 */
```
