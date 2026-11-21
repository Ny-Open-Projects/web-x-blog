---
title: [HW-040] 手写 React useState
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-040：手写 React useState

**答**：
- 评分点：hooks 状态存放在**模块级/闭包级数组**中，按调用**顺序**通过递增 index 对齐（这就是「Hooks 不能写在 if/循环里」的原因，必讲）；setState 要做**函数式更新**支持 `setCount(c => c + 1)`；setState 后触发**重新渲染**，渲染开始时 index 重置为 0；每次渲染有独立的 state 快照（闭包捕获，可作追问）；初始化只在第一次赋值（`if (!(i in states))`）。

```javascript
// ===== 5 分钟速写版 =====
let hookIndex = 0;
const hooks = [];
let scheduleRender = null;

function useState(initial) {
  const i = hookIndex++;
  if (!(i in hooks)) hooks[i] = typeof initial === 'function' ? initial() : initial;
  const setState = value => {
    hooks[i] = typeof value === 'function' ? value(hooks[i]) : value; // 函数式更新
    scheduleRender();
  };
  return [hooks[i], setState];
}
function render(App) {
  scheduleRender = () => render(App); // 下一次 setState 的入口
  hookIndex = 0;                      // 每次渲染 index 从 0 重新对齐
  App();                              // 简版：直接函数调用代替真实渲染
}
// 用法：
// function Counter() { const [n, setN] = useState(0); ... }

// ===== 标准完整版（含边界处理）=====
const React = (() => {
  let hookIndex = 0;
  const hooks = [];
  let pendingRenders = [];
  let isBatching = false;
  function useState(initial) {
    const i = hookIndex++;
    // 初始化：惰性初始化支持传入工厂函数（React 同款行为）
    if (!(i in hooks)) hooks[i] = typeof initial === 'function' ? initial() : initial;
    function setState(value) {
      const next = typeof value === 'function' ? value(hooks[i]) : value;
      if (Object.is(next, hooks[i])) return;       // 同值 bail-out，不触发渲染
      hooks[i] = next;
      schedule();
    }
    return [hooks[i], setState];
  }
  // 批处理：一次事件回调里多次 setState 只渲染一次
  function schedule() {
    pendingRenders.push(true);
    if (isBatching) return;
    isBatching = true;
    queueMicrotask(() => {
      pendingRenders = [];
      isBatching = false;
      mount();
    });
  }
  let App = null;
  function mount() {
    hookIndex = 0; // 渲染前重置，按顺序对齐
    App();
  }
  return {
    useState,
    createRoot(app) {
      App = app;
      mount();
      return {
        rerender: mount // 暴露手动渲染用于测试
      };
    }
  };
})();
// 追问考点：
// 1. 为什么不能在条件分支里调 Hook —— index 对齐错位，状态被张冠李戴
// 2. 同一组件多次 useState 依靠调用顺序隔离
// 3. setState 传入相同值 React 会跳过渲染（Object.is）
```

---
