---
title: [DP-222] 源码识别：Vue Transition 源码中的状态模式与钩子？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-222：源码识别：Vue Transition 源码中的状态模式与钩子？
**答**：
- 状态模式：过渡状态机 enter(enter-from → enter-active → enter-to) / leave 同构，源码用类名序列驱动 CSS，JS 钩子（@before-enter 等）是各状态的扩展点。
- 备忘录/快照：过渡期间记录旧 vnode 位置与新位置（FLIP 位移动画：先记 First/Last，再 Invert/Play）。
- 观察者：transitionend/animationend 事件监听驱动状态转移（+ 超时兜底，防事件丢失卡死）。
- 识别要点：FLIP 四步是"First-Last-Invert-Play"——面试能现场推一遍位移动画实现（DP 系列高频）。

```javascript
// Vue Transition enter 状态机（源码级简化）
function enter(el, { appearClass, enterActiveClass, onEnter, onAfterEnter }) {
  el.classList.add(appearClass);                        // enter-from：初始态
  requestAnimationFrame(() => {
    el.classList.remove(appearClass);
    el.classList.add(enterActiveClass);                 // enter-active：过渡中
    const done = e => {
      el.classList.remove(enterActiveClass);
      el.removeEventListener('transitionend', done);    // 观察者驱动转移
      onAfterEnter?.(el);                               // 终态钩子
    };
    el.addEventListener('transitionend', done);
    setTimeout(done, getMaxDuration(el) + 20);          // 超时兜底（事件丢失保险）
    onEnter?.(el);
  });
}
// FLIP：const first = el.getBoundingClientRect(); 变更后 last=…; invert(delta); play(transform→none)
```
