---
title: [CSS-395] 笔试：手写 Toast 队列（进出场 + 堆叠管理）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-395：笔试：手写 Toast 队列

**答**：实现 toast：① 右上角堆叠，新消息入场（滑入+淡入），自动 3s 消失（出场动画完成才移除 DOM）；② 同屏最多 5 条，超出最早的立即移除；③ 相同内容 1s 内去重；④ 队列用 flex column-reverse 使新增不推挤旧条目（视觉稳定）；⑤ hover 暂停自动消失。写出核心实现。

```html
<div class="toasts"></div>
```

```css
.toasts {
  position: fixed; top: 16px; right: 16px;
  display: flex; flex-direction: column-reverse;  /* 新增不推挤 */
  gap: 8px; pointer-events: none; z-index: var(--z-toast, 500);
}
.toast {
  pointer-events: auto;
  background: #333; color: #fff; padding: 10px 16px;
  border-radius: 8px;
  animation: in .25s var(--ease-out-quart), out .25s .25s;
  animation-delay: 0s, 2.75s;             /* 3s 总寿命: 入场0.25 + 停留2.5 + 出场0.25 */
  animation-fill-mode: forwards;
}
@keyframes in { from { transform: translateX(20px); opacity: 0; } }
@keyframes out { to { transform: translateX(20px); opacity: 0; } }
.toast:hover { animation-play-state: paused; }   /* hover 暂停整个时间轴 */
```

```javascript
let last = { msg: '', t: 0 };
function toast(msg) {
  const now = Date.now();
  if (msg === last.msg && now - last.t < 1000) return;   // 去重
  last = { msg, t: now };
  const box = document.querySelector('.toasts');
  const el = Object.assign(document.createElement('div'), { className: 'toast', textContent: msg });
  box.append(el);
  while (box.children.length > 5) box.firstElementChild.remove(); // 上限
  setTimeout(() => el.remove(), 3000);
}
```

**评分点**：
- column-reverse 堆叠方向（新增在上不推挤）是关键设计
- 入场/出场动画时间轴编排（fill-mode forwards + 延迟）
- hover 暂停用 animation-play-state（纯 CSS 暂停）
- 同内容去重 + 堆叠上限
