---
title: [H5-107] tabindex 的 -1、0、正整数各自语义是什么？roving tabindex 怎么实现？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-107：tabindex 的 -1、0、正整数各自语义是什么？roving tabindex 怎么实现？
**答**：
- `tabindex="0"`：加入 Tab 序（按 DOM 顺序），用于"本身不可聚焦但需要可达"的组件容器；`tabindex="-1"`：**仅可编程聚焦**（`focus()` 可达、Tab 跳过），用于"点击后聚焦但不进 Tab 序"的元素。
- 正整数：按数值手动排序 Tab 序——**反模式**，值一大 Tab 顺序与视觉顺序脱节，应通过调整 DOM 顺序解决；只允许在极特殊场景（如多列表交叉）谨慎使用。
- 全局规则：Tab 序 = 正整数（按值）→ tabindex=0 与原生可聚焦元素（按 DOM）。
- roving tabindex 模式（工具栏/表格/单选组标配）：组内多子项中**只有一个 tabindex=0**，方向键移动时把 0 挪给下一项、旧项改 -1，保证"一次 Tab 进组、方向键在组内移动、一次 Tab 出组"。
- 焦点丢失检测：`document.activeElement` 与 `:focus-visible` 配合做样式；组件卸载记得把焦点还回合理位置（aria 焦点管理红线）。

```html
<div class="toolbar" role="toolbar" aria-label="格式工具">
  <button tabindex="0" data-idx="0">B</button>
  <button tabindex="-1" data-idx="1">I</button>
  <button tabindex="-1" data-idx="2">U</button>
</div>

<script>
  // roving tabindex：一次 Tab 进入组，方向键移动，一次 Tab 离开
  const toolbar = document.querySelector('.toolbar');
  const buttons = [...toolbar.querySelectorAll('button')];

  toolbar.addEventListener('keydown', (e) => {
    const dirs = { ArrowRight: 1, ArrowLeft: -1, ArrowUp: -1, ArrowDown: 1 };
    if (!(e.key in dirs)) return;
    e.preventDefault();

    const cur = buttons.indexOf(document.activeElement);
    const next = (cur + dirs[e.key] + buttons.length) % buttons.length;

    buttons.forEach((b, i) => b.tabIndex = i === next ? 0 : -1); // 焦点令牌转移
    buttons[next].focus();                            // -1 的价值：可编程聚焦
  });

  // tabindex=-1 的另一用途：模态框关闭后焦点归还触发按钮
  let lastTrigger = null;
  dialog.addEventListener('close', () => {
    (lastTrigger ?? document.body).focus();           // Tab 序外的元素也能 focus
  });
  openBtn.addEventListener('click', () => { lastTrigger = openBtn; dialog.showModal(); });
</script>

<style>
  /* 焦点可见性：鼠标点击不出圈，键盘导航出圈 */
  button:focus:not(:focus-visible) { outline: none; }
  button:focus-visible { outline: 2px solid #1677ff; outline-offset: 2px; }
</style>
```
