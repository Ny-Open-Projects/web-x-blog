---
title: [HW-156] 手写 Pointer Events 通用拖拽——统一鼠标触摸、点按阈值区分点击/拖拽、touch-action 协调
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-156：手写 Pointer Events 通用拖拽——统一鼠标触摸、点按阈值区分点击/拖拽、touch-action 协调
**答**：通用拖拽三层决策：① Pointer Events 统一鼠标/触摸/笔（setPointerCapture 持续跟踪）；② 点按阈值（move < 5px 判定为点击，> 阈值才进入拖拽——防止触摸设备上"想点击却拖走"）；③ touch-action: none 声明（告诉浏览器该区域手势归应用管，防拖拽时页面滚动打架）。

```javascript
function draggable(el, { onMove, onStart, onEnd, threshold = 5 } = {}) {
  el.style.touchAction = 'none';                          // 手势归应用（否则触摸拖拽时页面滚动）
  let start = null, dragging = false, pid = null;
  el.addEventListener('pointerdown', (e) => {
    pid = e.pointerId;
    start = { x: e.clientX, y: e.clientY };
    el.setPointerCapture(pid);                            // 移出元素也持续跟踪
  });
  el.addEventListener('pointermove', (e) => {
    if (pid !== e.pointerId || !start) return;
    const dx = e.clientX - start.x, dy = e.clientY - start.y;
    if (!dragging && Math.hypot(dx, dy) > threshold) {
      dragging = true;
      onStart?.({ x: start.x, y: start.y });              // 超阈值：进入拖拽
    }
    if (dragging) onMove?.({ dx, dy, x: e.clientX, y: e.clientY });
  });
  const finish = (e) => {
    if (pid !== e.pointerId) return;
    if (!dragging) el.dispatchEvent(new CustomEvent('tap', { detail: e }));   // 未超阈值：当点击
    else onEnd?.();
    dragging = false; start = null; pid = null;
  };
  el.addEventListener('pointerup', finish);
  el.addEventListener('pointercancel', finish);           // 系统中断（来电/手势抢占）也要清理
}
// 关键点：
// pointercancel 必须处理（电话进来/浏览器手势抢占，漏了 = 拖拽状态残留卡死）
// 阈值 5px 区分点击与拖拽（触摸屏上手指微小抖动不该触发拖拽）
// touch-action: none 只加在拖拽元素上（整页 none 会禁掉页面滚动）
```

**评分点**：
- Pointer Events 统一 + setPointerCapture 跟踪。
- 点按阈值区分点击/拖拽（触摸抖动防护）——本题核心。
- pointercancel 清理（漏了状态残留是高频 bug）。
- touch-action: none 的作用域（元素级非全局）。
