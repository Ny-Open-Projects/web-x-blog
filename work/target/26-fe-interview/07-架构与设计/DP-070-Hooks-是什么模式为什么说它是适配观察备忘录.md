---
title: [DP-070] Hooks 是什么模式？为什么说它是"适配+观察+备忘录"的混合？（高频压轴）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-070：Hooks 是什么模式？为什么说它是"适配+观察+备忘录"的混合？（高频压轴）
**答**：
- Hooks 不是单一 GoF 模式，而是组合体：useState/useRef 提供可隔离的状态存取（备忘录：快照与恢复）；useEffect/useMemo 依赖变化时重执行（观察者：依赖数组即订阅）。
- 适配色彩：Hooks 把类组件的生命周期 API 适配成函数式 API（useEffect 统一了 componentDidMount/Update/Unmount）。
- 实现本质：React 内部用链表按调用顺序存每个 Hook 的状态——调用顺序稳定是契约（不能放 if 里）。
- 面试答法：先给"混合模式"定性，再展开对应关系，最后补 fiber Hook 链表实现。

```javascript
// mini hooks：链表存储（顺序敏感） + 观察者（依赖触发） + 备忘录（状态保存与重置）
function createRenderer() {
  let hookIndex = 0;
  let hooks = [];            // fiber 中的 Hook 链表（此处用数组模拟）
  let rerender = null;

  function render(Component) {
    hookIndex = 0;           // 每次渲染从第 0 个 Hook 开始按序取
    rerender = () => render(Component);
    return Component();
  }
  function useState(initial) {
    const i = hookIndex++;
    if (hooks[i] === undefined) hooks[i] = { value: initial }; // 首次挂载建槽位
    return [
      hooks[i].value,
      (next) => {
        hooks[i].value = next;
        rerender();          // 状态变化 -> 触发重渲染（观察者通知）
      },
    ];
  }
  function useEffect(fn, deps) {
    const i = hookIndex++;
    const old = hooks[i];
    const changed = !old || !deps || deps.some((d, k) => d !== old.deps?.[k]);
    if (changed) {
      old?.cleanup?.();      // 上一次副作用的清理（备忘录式恢复现场）
      const cleanup = fn();
      hooks[i] = { deps, cleanup };
    }
  }
  return { render, useState, useEffect };
}
const { render, useState, useEffect } = createRenderer();
function App() {
  const [count, setCount] = useState(0);
  useEffect(() => { console.log('count 变化', count); }, [count]); // 依赖数组=订阅
  return `count: ${count.value ?? count}`;
}
console.log(render(App));  // count 变化 0 -> count: 0
// setCount(1) 触发 rerender：
// hooks 链表按 index 对齐：第0槽 useState、第1槽 useEffect —— 顺序即身份
```
