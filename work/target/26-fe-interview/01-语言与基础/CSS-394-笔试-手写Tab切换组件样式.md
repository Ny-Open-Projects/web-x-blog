---
title: [CSS-394] 笔试：手写 Tab 切换组件（滑动指示条）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-394：笔试：手写 Tab 切换组件（滑动指示条）

**答**：实现 Tab：① 指示条随激活项滑动（宽度/位置动画，用 CSS 变量定位）；② 激活项文字颜色过渡；③ 键盘可达（role=tablist + 方向键切换 + roving tabindex）；④ 内容面板切换带淡入；⑤ 指示条位置计算最小 JS。写出核心实现。

```html
<div class="tabs" role="tablist">
  <button role="tab" aria-selected="true" data-i="0">首页</button>
  <button role="tab" aria-selected="false" data-i="1">发现</button>
  <i class="inkbar"></i>
</div>
<div class="panel" role="tabpanel" data-i="0">...</div>
```

```css
.tabs { position: relative; display: flex; gap: 24px; }
.tabs [role='tab'] { background: none; padding: 12px 0; color: #666; transition: color .2s; }
.tabs [aria-selected='true'] { color: var(--primary); }
.inkbar {
  position: absolute; bottom: 0; left: 0;
  height: 2px; width: 0;
  background: var(--primary);
  transform: translateX(var(--x)) scaleX(var(--w));
  transform-origin: 0 50%;
  transition: transform .25s var(--ease-out-quart);
}
.panel { animation: fade-in .2s; }
@keyframes fade-in { from { opacity: 0; transform: translateY(4px); } }
```

```javascript
const ink = document.querySelector('.inkbar');
function activate(tab) {
  document.querySelectorAll('[role=tab]').forEach(t =>
    t.setAttribute('aria-selected', t === tab));
  const r = tab.getBoundingClientRect(), pr = tab.parentElement.getBoundingClientRect();
  ink.style.setProperty('--x', `${r.left - pr.left}px`);   // 位置
  ink.style.setProperty('--w', `${r.width / 100}`);        // scaleX 归一
  ink.style.width = `${r.width}px`;
}
// 键盘: 左右方向键移动 focus 并激活 (roving tabindex)
list.addEventListener('keydown', (e) => {
  const dirs = { ArrowLeft: -1, ArrowRight: 1 };
  if (!dirs[e.key]) return;
  const next = tabs[(tabs.indexOf(document.activeElement) + dirs[e.key] + tabs.length) % tabs.length];
  next.focus(); activate(next);
});
```

**评分点**：
- 指示条用 transform（translate+scaleX）动画而非 left/width
- getBoundingClientRect 相对父容器偏移计算正确
- ARIA tablist/tab/tabpanel + roving tabindex + 方向键
- 面板淡入用 animation 而非 JS class 手动管理
