---
title: [DP-369] 组合组件实战：Compound Components 模式
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-369：组合组件（Compound Components）

**答**：
- 模式定义：父组件与子组件「隐式共享状态」（Select + Select.Option——Option 无 props 也知道选中态）——React 的 Context 或 cloneElement 实现
- 价值：API 表达力强（`<Tabs><Tabs.Tab/></Tabs>`——子组件语义化）+ 布局自由（使用者控制子组件排列）
- 实战实现：Context 传递状态（Tab 的 active 状态由 Tabs.Context 提供——子组件无需 props）+ 子组件静态挂载（Tabs.Tab = Tab——命名空间聚合）
- 与 renderless 的组合：compound + headless（逻辑内核 + 组合式 API——Radix/Reka UI 的模式）
- 深水点：隐式耦合的代价——子组件必须在父内使用（单独用崩）——「组合校验」（子组件检测无父 Context → 报错提示）

```jsx
const TabsCtx = createContext(null);
function Tabs({ value, onChange, children }) {
  return <TabsCtx.Provider value={{ value, onChange }}>{children}</TabsCtx.Provider>;
}
Tabs.Tab = function Tab({ value, children }) {
  const ctx = useContext(TabsCtx);
  if (!ctx) throw new Error('Tabs.Tab 必须在 <Tabs> 内使用');   // 组合校验
  const active = ctx.value === value;
  return <button aria-selected={active} onClick={() => ctx.onChange(value)}>{children}</button>;
};
// 用法: <Tabs value="a" onChange={set}><Tabs.Tab value="a">首页</Tabs.Tab></Tabs>
```
