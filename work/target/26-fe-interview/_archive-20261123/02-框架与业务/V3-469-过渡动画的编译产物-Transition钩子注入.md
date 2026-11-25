---
title: [V3-469] Transition 编译产物：enter/leave 钩子如何注入 vnode
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-469：Transition 编译产物：enter/leave 钩子如何注入 vnode

**答**：
- Transition 是渲染函数级组件：无模板，直接在 render 里读 child vnode 并注入 transition hooks（vnode.transition 属性）——patch 的 mount/patch/unmount 分支检查该属性执行动画
- CSS 模式：runtime 根据类名约定（v-enter-from 等，name 定制）自动 add/remove class + transitionend 监听——编译器不参与，约定在 runtime
- JS 钩子：@enter/@leave/@before-enter 编译为普通 props，Transition 组件读 props 拼装 hooks——JS 模式下 CSS 自动检测关闭
- appear：初次渲染也触发——transition 属性注入时根据 appear prop 决定 mount 时是否走 enter 流程
- 深水点：leave 期间元素「保留在 DOM 但脱离 patch 流」（延迟卸载）——leaveActive 的 whenTransitionEnds 等待最后一个过渡结束才真正 remove；打断（leave 未完重新进入）走 cancel 逻辑

```javascript
// Transition render 核心
child.transition = { // 注入到 vnode
  name, appear,
  onBeforeEnter, onEnter, onAfterEnter,
  onBeforeLeave, onLeave, onAfterLeave,
};
// patch unmount 分支: vnode.transition ? performLeave(el) : remove(el)
```
