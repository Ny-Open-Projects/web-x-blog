---
title: [SCN-840] 笔试题——实现 combobox 键盘导航（循环 + aria 同步 + ghost 预览）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-840：手写 combobox 键盘导航

**需求与边界**：
- 需求：↑↓ 循环移动（含分组头跳过）、Enter 采纳、Esc 关闭；aria-activedescendant 同步；ghost 预览（键盘选中时输入框灰色补全）。
- 边界：① 分组头（history/hot 标题行）不可选中自动跳过；② items 变化时 active 重置到 -1 或保持语义位置；③ hover 与键盘共写 activeIndex（最后操作者胜）。

**答**：
```javascript
function comboboxNav(items, { onAdopt, onClose }) {
  let active = -1;
  const selectable = items.map((it, i) => it.selectable ? i : -1).filter(i => i >= 0);
  function move(dir) {
    if (!selectable.length) return;
    const pos = selectable.indexOf(active);
    const next = pos === -1
      ? (dir > 0 ? 0 : selectable.length - 1)
      : (pos + dir + selectable.length) % selectable.length;
    active = selectable[next];                         // 分组头自动跳过
    syncAria(active);
    ghost(active);                                     // 输入框灰色补全预览
  }
  function onKey(e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); onAdopt(items[active]); }
    else if (e.key === 'Escape') onClose();
  }
  function onItemsChange(newItems) { active = -1; }    // 数据变化重置（语义位置难保持，安全重置）
  return { onKey, get active() { return active; }, setActive: (i) => (active = i) };  // hover 复用
}
```

**评分点**:
- selectable 过滤分组头（不可选行跳过）。
- 循环移动含「未选中→首/尾」初始跳转。
- aria-activedescendant 同步（读屏跟随）。
- hover/键盘共用 activeIndex（单一状态源）+ 数据变化重置。
