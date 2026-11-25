---
title: [CSS-159] 按钮涟漪效果怎么用 JS 坐标 + CSS 动画实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-159：按钮涟漪效果怎么用 JS 坐标 + CSS 动画实现？

**答**：
- JS 负责算坐标：pointerdown 的 `clientX/clientY` 减按钮 `getBoundingClientRect` 得点击点在按钮内的位置。
- CSS 负责动画：一个圆形 span 从 scale(0) 放大到 cover 按钮并淡出，`animationend` 后由 JS 移除节点。
- 半径取 `max(width, height) × 2` 保证任意角度点击都能铺满。
- 按钮要 `overflow: hidden + position: relative`，涟漪 `pointer-events: none` 防劫持点击。

```html
<button class="btn">涟漪按钮</button>
<style>
  .btn {
    position: relative;
    overflow: hidden;          /* 涟漪裁剪在按钮内 */
    padding: 10px 24px;
    border: none;
    border-radius: 6px;
    background: #096;
    color: #fff;
  }
  .btn .ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, .5);
    transform: scale(0);
    animation: ripple .6s ease-out forwards;
    pointer-events: none;      /* 不劫持点击 */
  }
  @keyframes ripple {
    to { transform: scale(4); opacity: 0; }
  }
</style>
<script>
  document.querySelector('.btn').addEventListener('pointerdown', e => {
    const btn = e.currentTarget;
    const rect = btn.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height) * 2;
    const r = document.createElement('span');
    r.className = 'ripple';
    r.style.cssText = `
      width: ${size}px; height: ${size}px;
      left: ${e.clientX - rect.left - size / 2}px;
      top: ${e.clientY - rect.top - size / 2}px;`;
    btn.appendChild(r);
    r.addEventListener('animationend', () => r.remove());
  });
</script>
```

## 二十六、复杂组件样式还原
