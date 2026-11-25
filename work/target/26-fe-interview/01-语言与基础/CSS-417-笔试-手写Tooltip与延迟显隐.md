---
title: [CSS-417] 笔试：手写 Tooltip（延迟显隐 + 箭头定位）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-417：笔试：手写 Tooltip

**答**：实现 tooltip：① 悬停 300ms 延迟显示（快速滑过不闪），移出立即隐藏（隐藏不延迟）；② 四方向定位（top/bottom 优先，左右溢出翻转）；③ 箭头跟随位置；④ 触摸设备长按显示；⑤ 无障碍（aria-describedby + role=tooltip，焦点触发）。写出核心实现。

```html
<button class="tip-host" aria-describedby="tip1">删除</button>
<div class="tip" id="tip1" role="tooltip" hidden>删除后不可恢复</div>
```

```css
.tip {
  position: absolute;
  background: #333; color: #fff;
  padding: 6px 10px; border-radius: 6px;
  font-size: 12px; white-space: nowrap;
  animation: tip-in .15s;
  transform-origin: bottom center;
  z-index: var(--z-tooltip, 600);
}
.tip::before {                     /* 箭头 */
  content: ''; position: absolute;
  left: var(--ax, 50%); top: 100%;
  margin-left: -5px;
  border: 5px solid transparent; border-top-color: #333;
}
.tip.pos-bottom { transform-origin: top center; }
.tip.pos-bottom::before { top: auto; bottom: 100%; border-top-color: transparent; border-bottom-color: #333; }
.tip.pos-left::before { /* 方向变体 */ }
@keyframes tip-in { from { opacity: 0; transform: translateY(4px); } }
```

```javascript
let showT, hideT;
function place() {
  const r = host.getBoundingClientRect();
  const tw = tip.offsetWidth;
  let x = r.left + r.width / 2 - tw / 2;      // 默认上方居中
  x = Math.max(8, Math.min(x, innerWidth - tw - 8));  // 横向钳制
  tip.style.left = x + 'px';
  tip.style.top = r.top - tip.offsetHeight - 8 + 'px';
  tip.style.setProperty('--ax', `${r.left + r.width / 2 - x}px`); // 箭头跟随
}
host.addEventListener('mouseenter', () => {
  clearTimeout(hideT);
  showT = setTimeout(() => { tip.hidden = false; place(); }, 300);  // 延迟显示
});
host.addEventListener('mouseleave', () => {
  clearTimeout(showT);
  tip.hidden = true;                          // 隐藏立即
});
host.addEventListener('focus', () => { tip.hidden = false; place(); });  // 键盘
```

**评分点**：
- 显示延迟/隐藏立即的非对称时序（快速滑过不闪）
- 位置钳制（不超出视口）+ 箭头 --ax 跟随
- 焦点触发（键盘可达）+ aria-describedby 关联
- mouseleave 清除 pending showT（竞态防御）
