---
title: [CSS-170] 组件密度调节（compact/comfortable）怎么落地？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-170：组件密度调节（compact/comfortable）怎么落地？

**答**：
- 密度本质是一组尺寸 token：控件高度、内边距、行高、字号，所有组件按 token 布局，不写死 px。
- 切换密度 = 在根节点换一组变量（`data-density="compact"`），全站即时生效，无组件级改动。
- 组件内部需要派生时用 `calc()` 基于密度 token 计算，禁止引入新的魔法数字。
- 交互细节：compact 下触控目标仍需满足最小 44px 触区（用 padding 透明区扩展），无障碍不因密度妥协。

```css
:root {
  --ctrl-h: 40px;      /* 控件高度 */
  --gap: 16px;         /* 常规间距 */
  --fs: 14px;          /* 正文字号 */
  --row-pad: 12px;     /* 表格行内边距 */
}
[data-density="compact"] {
  --ctrl-h: 28px;
  --gap: 8px;
  --fs: 12px;
  --row-pad: 6px;
}
[data-density="comfortable"] { /* 即默认，显式声明便于覆盖 */ }

/* 组件只读 token */
.btn {
  height: var(--ctrl-h);
  padding-inline: calc(var(--gap) / 2);
  font-size: var(--fs);
}
.table-row { padding-block: var(--row-pad); }
.form-item { margin-bottom: var(--gap); }

/* compact 下保证触控区：透明 padding 扩大命中范围 */
[data-density="compact"] .icon-btn {
  min-width: 44px;
  min-height: 44px;
  box-sizing: content-box;
}
/* JS 切换：root.dataset.density = 'compact'，全站即时生效 */
```
