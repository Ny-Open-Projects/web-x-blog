---
title: [FRP-086] 自定义 Hook 的闭包陷阱实例有哪些？如何用 useRef 修复？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-086：自定义 Hook 的闭包陷阱实例有哪些？如何用 useRef 修复？

**答**：
- 经典陷阱 1：`useEffect` 内 setInterval 回调读了 state——回调闭包捕获首次渲染的 state，interval 永远读到旧值（每秒打印 0）。修复 A：依赖数组加 `[count]`（但会重建定时器）；修复 B（最优）：用 `useRef` 存最新回调，interval 只调用 ref。
- 经典陷阱 2：事件处理器内读"过期 props/state"（如 setTimeout 延迟 1s 后读 count）；本质同一个问题：**JS 闭包按词法捕获变量，React 每次渲染都是新的作用域**。
- `useRef` 修复模板（useInterval / useEventCallback 模式）：`const savedFn = useRef(); useEffect(() => { savedFn.current = fn; });` 每次 commit 同步更新 ref，稳定的 interval 永远执行 `savedFn.current()`——拿到当次渲染的最新值。
- 原理呼应 FRP-063（Vue 编译器用 `_ctx` 解决同类问题）与 React 官方 useEvent 提案：**可变引用 + 每次同步赋值 = 免闭包过期**。

```javascript
// 简化实现，帮助理解 useInterval 的闭包陷阱与 useRef 修复
function useRef(initial) { return { current: initial }; }
function useEffect(fn, deps) { /* 假设为真实 useEffect */ fn(); }

// 错误版：闭包捕获旧 state
function useIntervalWrong(callback, delay) {
  useEffect(() => {
    const id = setInterval(callback, delay); // callback 永远是首次渲染的闭包
    return () => clearInterval(id);
  }, [delay]); // 漏了 callback 依赖
}
// 使用：count 变化后 interval 里的 count 恒为 0
// useIntervalWrong(() => console.log('wrong:', count), 1000) -> 永远打印 0

// 正确版：useRef 存最新回调
function useInterval(callback, delay) {
  const savedCallback = useRef(callback);
  // 每次渲染后同步更新 ref.current -> 始终指向最新闭包
  useEffect(() => {
    savedCallback.current = callback;
  });
  useEffect(() => {
    const id = setInterval(() => savedCallback.current(), delay); // 解引用取最新
    return () => clearInterval(id);
  }, [delay]); // 依赖只有 delay：定时器稳定，逻辑不落伍
}

// 模拟验证：三次渲染，回调读取的 count 依次为 0/1/2
let renderCount = 0;
const ref = useRef(null);
const simulateRenders = () => {
  [0, 1, 2].forEach((count) => {
    renderCount++;
    const callback = () => console.log('correct:', count); // 每次渲染新闭包
    useEffect(() => { ref.current = callback; });          // 同步进 ref
  });
  ref.current(); // 模拟 interval 触发：读到最后一次渲染的闭包
};
simulateRenders(); // correct: 2
// 若 interval 持有的是第一次的 callback 而非 ref.current()，输出将是 0
```

## 十三、React 渲染机制深入
