---
title: [FRP-021] Transition 组件是如何实现元素进入/离开动画的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-021：Transition 组件是如何实现元素进入/离开动画的？

**答**：
- Transition 本身**不渲染 DOM**（注释节点），只是包裹单元素/单组件做"进出动画编排"。
- 进入流程：插入元素时依次加 `*-enter-from`（初始态）→ 下一帧移除并加 `*-enter-active` + `*-enter-to`（过渡到终态）→ 过渡结束移除全部，回调 `after-enter`。
- 离开流程：加 `*-leave-*` 系列类 → `whenTransitionEnds` 监听 transitionend 并计算 duration 兜底 → 结束后真正卸载 DOM（`mode="out-in"` 时先等离开完再进入）。
- 关键技术点：强制 reflow（读取 offsetHeight）让 enter-from 的初始样式先生效；若包裹的是组件且子节点是 v-if 切换，则配合 TransitionGroup 处理列表。

```javascript
// 简化实现，帮助理解 Transition 的类名切换时序
function transitionEnter(el, name = 'fade') {
  el.classList.add(`${name}-enter-from`, `${name}-enter-active`); // 1. 初始态 + 过渡

  // 2. 强制 reflow：让 enter-from 的样式先生效（否则浏览器合并样式直接到终态，无动画）
  void el.offsetHeight;

  el.classList.add(`${name}-enter-to`);      // 3. 下一帧：移除 from，过渡到 to
  el.classList.remove(`${name}-enter-from`);

  // 4. 过渡结束：清掉全部类
  const onEnd = (e) => {
    if (e.target !== el) return;
    el.classList.remove(`${name}-enter-active`, `${name}-enter-to`);
    el.removeEventListener('transitionend', onEnd);
  };
  el.addEventListener('transitionend', onEnd);
}

function transitionLeave(el, name = 'fade', done) {
  el.classList.add(`${name}-leave-from`, `${name}-leave-active`);
  void el.offsetHeight;                       // 同样强制 reflow
  el.classList.add(`${name}-leave-to`);
  el.classList.remove(`${name}-leave-from`);

  const onEnd = (e) => {
    if (e.target !== el) return;
    el.classList.remove(`${name}-leave-active`, `${name}-leave-to`);
    el.removeEventListener('transitionend', onEnd);
    done?.(); // mode out-in：离开动画完成后才真正卸载 / 才开始进入
  };
  el.addEventListener('transitionend', onEnd);
}

// CSS 侧（配套）：
// .fade-enter-active, .fade-leave-active { transition: opacity .3s; }
// .fade-enter-from, .fade-leave-to { opacity: 0; }
```

## 四、React Fiber 架构
