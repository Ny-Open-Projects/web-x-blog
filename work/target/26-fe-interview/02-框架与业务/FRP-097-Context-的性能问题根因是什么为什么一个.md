---
title: [FRP-097] Context 的性能问题根因是什么？为什么"一个 value 变了所有消费者都重渲染"？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-097：Context 的性能问题根因是什么？为什么"一个 value 变了所有消费者都重渲染"？

**答**：
- 根因：Context 的传播机制是**引用比对**——Provider 的 value 引用变化后，React 把所有 `context._currentValue` 标记更新，**每个 useContext 的消费者组件无条件重渲染**，不区分"你用了 value 的哪个字段"（React 19 的 context 依然如此）。
- 与订阅模型对比：Context 是"渲染期读取"（读的是当次 render 的快照，无订阅比对），store 订阅是"独立监听 + 快照比较"，后者能跳过无关组件。
- 加重因素：value 通常是 render 期新对象（`value={{ user, setUser }}`），**每次 Provider 渲染引用都变**，即使内容没变。
- 缓解方案（原理层）：①拆分 Context（把高频变的和低频变的分开）；②value 用 useMemo 包裹稳定引用；③"**State 分离模式**"——Provider 放 state + dispatch，数据本体通过 Zustand 等订阅分发；④children 作为 props 传入（绕过 value 变化）。

```javascript
// 简化实现，帮助理解 Context 的传播面问题
function createContext(defaultValue) {
  const ctx = { _currentValue: defaultValue, consumers: new Set() };
  return ctx;
}
function useContext(ctx) {
  ctx.consumers.add(currentComponent);       // 注册为消费者
  return ctx._currentValue;                  // 渲染期直接读，无任何比较
}
let currentComponent = null;
function renderComponent(name, fn) {
  currentComponent = name;
  fn();
  currentComponent = null;
}

function Provider(ctx, value, children) {
  ctx._currentValue = value;
  children(); // 递归渲染子树：每个 useContext 都无条件拿新值
}

const UserCtx = createContext({ name: 'a', theme: 'light' });
const UserBadge = () => { const u = useContext(UserCtx); console.log(`${currentComponent} 用了 name=${u.name} -> 重渲染`); };
const ThemeBadge = () => { const u = useContext(UserCtx); console.log(`${currentComponent} 用了 theme=${u.theme} -> 重渲染`); };

renderComponent('UserBadge', UserBadge);
renderComponent('ThemeBadge', ThemeBadge);

// 场景 1：只改了 name（Consumer 不关心的字段）
Provider(UserCtx, { name: 'b', theme: 'light' }, () => {
  renderComponent('UserBadge', UserBadge);   // 重渲染（应当）
  renderComponent('ThemeBadge', ThemeBadge); // 也重渲染（浪费！Context 无字段级订阅）
});

// 修复：拆分 Context + useMemo 稳定引用
const NameCtx = createContext('a'), ThemeCtx = createContext('light');
Provider(NameCtx, 'b', () => renderComponent('UserBadge', UserBadge)); // 只有 NameCtx 消费者重渲染
// 对比 Zustand：useStore(s => s.name) 中 theme 变化时 selector 快照不变 -> 直接跳过
```
