---
title: [CSS-426] 笔试：手写筛选器 Chips（多选 + 全部清空）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-426：笔试：手写筛选器 Chips

**答**：实现筛选 chips：① 多选互斥组合（多值 chips + 单值段选择器 Segmented 并存）；② 选中态样式（填充/描边切换）；③ 已选条件回显区（可单独移除 + 一键清空）；④ 横向溢出滚动 + 展开更多；⑤ 无障碍（aria-pressed 标记选中态）。写出核心实现。

```html
<div class="filters">
  <div class="chips" role="group" aria-label="品类">
    <button class="chip" aria-pressed="false" data-v="phone">手机</button>
    <button class="chip" aria-pressed="false" data-v="pad">平板</button>
    <button class="chip" aria-pressed="false" data-v="watch">手表</button>
  </div>
  <div class="seg" role="radiogroup" aria-label="排序">
    <button role="radio" aria-checked="true" data-v="hot">热门</button>
    <button role="radio" aria-checked="false" data-v="new">最新</button>
  </div>
  <div class="applied"></div>
</div>
```

```css
.chips { display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; }
.chip {
  padding: 6px 14px; border-radius: 16px;
  border: 1px solid #ddd; background: #fff;
  white-space: nowrap;
  transition: all .15s;
}
.chip[aria-pressed='true'] {
  background: var(--primary); color: #fff;
  border-color: var(--primary);
}
.seg { display: inline-flex; border-radius: 8px; overflow: hidden; border: 1px solid #ddd; }
.seg [role='radio'] { padding: 6px 16px; background: #fff; border: none; }
.seg [aria-checked='true'] { background: var(--primary-bg); color: var(--primary); font-weight: 600; }

.applied { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; }
.applied .tag {
  display: inline-flex; align-items: center; gap: 4px;
  background: var(--primary-bg); color: var(--primary);
  border-radius: 4px; padding: 2px 8px; font-size: 12px;
}
.applied .tag button { border: none; background: none; cursor: pointer; }
.applied .clear { color: #999; background: none; border: none; }
```

```javascript
function syncApplied() {
  const sel = [...document.querySelectorAll('.chip[aria-pressed=true]')].map(c => c.textContent);
  applied.innerHTML = sel.map(s =>
    `<span class="tag">${s}<button data-v="${s}">×</button></span>`).join('')
    + (sel.length ? '<button class="clear">清空</button>' : '');
}
chips.addEventListener('click', (e) => {
  const chip = e.target.closest('.chip');
  if (!chip) return;
  chip.setAttribute('aria-pressed', chip.getAttribute('aria-pressed') !== 'true');
  syncApplied(); filter();   // 触发查询
});
```

**评分点**：
- aria-pressed（多选）与 aria-checked（单选）语义区分
- 选中态填充/描边切换 + 回显区与 chips 状态同步
- 横向溢出滚动 + flex 不换行
- 状态单一来源（DOM 属性）驱动回显渲染
