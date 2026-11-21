---
title: [FRP-181] 手写 Transition：进入/离开时序与 mode="out-in" 如何控制？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-181：手写 Transition：进入/离开时序与 mode="out-in" 如何控制？

**答**：
- 纯实现层（不依赖 Vue）：给元素加 class 的时序机——enter：`v-enter-from` → 强制 reflow → `v-enter-active v-enter-to` → transitionend 后移除；leave：`v-leave-active v-leave-from` → reflow → `v-leave-to` → 结束后移除并**真正移除 DOM**。
- `mode="out-in"`：新元素必须**等旧元素 leave 完成才 enter**——需要把新元素先"延迟挂载"；`in-out` 相反。
- `transitionend` 不可靠（动画被中断/不触发），生产实现用 `whenTransitionEnds`：读取 computed style 的 duration/delay 取最大值 + 超时兜底。
- 位置移动的动画（v-move）靠 FLIP：先记录旧位置 → 更新 DOM → 计算位移 → 反向 transform → 过渡到 0。

```javascript
// 简化实现，帮助理解 Transition 时序与 out-in
function createTransitionManager() {
  let leavingEl = null;   // out-in 的锁：同一时刻只允许一个离开过程

  function enter(el, done) {
    el.classList.add('v-enter-from', 'v-enter-active');
    void el.offsetHeight;                          // 强制 reflow：让 from 状态生效
    el.classList.remove('v-enter-from');
    el.classList.add('v-enter-to');
    whenTransitionEnds(el, () => {
      el.classList.remove('v-enter-to', 'v-enter-active');
      done?.();
    });
  }

  function leave(el, done) {
    el.classList.add('v-leave-from', 'v-leave-active');
    void el.offsetHeight;
    el.classList.remove('v-leave-from');
    el.classList.add('v-leave-to');
    whenTransitionEnds(el, () => {
      el.classList.remove('v-leave-to', 'v-leave-active');
      el.remove();                                  // 离开结束才真正移除 DOM
      done?.();
    });
  }

  // mode 处理：切换视图的核心逻辑
  function switchView(container, oldEl, newElFactory, mode) {
    if (!oldEl) { const el = newElFactory(); container.appendChild(el); enter(el); return; }
    if (mode === 'out-in') {
      if (leavingEl) return;                        // 锁：正在离开时不挂新元素
      leavingEl = oldEl;
      leave(oldEl, () => {                          // 先离开
        leavingEl = null;
        const el = newElFactory();                  // 离开完成后才创建新元素
        container.appendChild(el);
        enter(el);
      });
      // 关键：旧元素在 leave 期间仍占位（没 remove），新元素不创建 -> 无重叠
    } else if (mode === 'in-out') {
      const el = newElFactory();
      container.appendChild(el);                    // 先进入
      enter(el, () => leave(oldEl));                // 进入完成后再离开旧的
    } else {
      const el = newElFactory();
      container.appendChild(el);                    // 同时进行（默认）：absolute 定位避免跳动
      enter(el);
      leave(oldEl);
    }
  }

  return { switchView, enter, leave };
}

// 结束时机判定（比 transitionend 可靠）
function whenTransitionEnds(el, cb) {
  const { transitionDuration, transitionDelay } = getComputedStyle(el);
  const dur = Math.max(...transitionDuration.split(',').map(parseFloat)) * 1000;
  const del = Math.max(...transitionDelay.split(',').map(parseFloat)) * 1000;
  const total = dur + del;
  if (total === 0) return cb();                    // 无动画：立即结束
  const timer = setTimeout(cb, total + 1);         // 超时兜底
  el.addEventListener('transitionend', function onEnd(e) {
    if (e.target !== el) return;                   // 忽略子元素的事件冒泡！
    clearTimeout(timer);
    el.removeEventListener('transitionend', onEnd);
    cb();
  });
}
```
