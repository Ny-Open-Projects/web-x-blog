---
title: [DP-520] 笔试：手写组合组件 Tabs
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-520：笔试：手写组合 Tabs

**答**：实现组合组件 Tabs：① Tabs + Tabs.Tab 组合 API（Context 隐式共享状态——Tab 无 props 拿到选中态）；② Tabs.Tab 的组合校验（脱离 Tabs 使用报错——Context 缺失检测）；③ a11y 完整（role=tablist/tab、aria-selected、键盘左右导航——键盘在 Tabs 层统一处理）；④ 面板联动（Tab 对应 Panel 的显示切换——tabId 关联）；⑤ 受控/非受控双模。写出实现。

```jsx
const Ctx = createContext(null);
export function Tabs({ value: controlled, defaultValue, onChange, children }) {
  const [inner, setInner] = useState(defaultValue);
  const value = controlled ?? inner;
  const setValue = (v) => { controlled === undefined && setInner(v); onChange?.(v); };
  return <Ctx.Provider value={{ value, setValue }}>{children}</Ctx.Provider>;
}
Tabs.Tab = function Tab({ value, children }) {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error('Tabs.Tab 必须在 Tabs 内');   // 组合校验
  return (
    <button role="tab" aria-selected={ctx.value === value}
      onClick={() => ctx.setValue(value)}>{children}</button>
  );
};
Tabs.Panel = function Panel({ value, children }) {
  const ctx = useContext(Ctx);
  return <div role="tabpanel" hidden={ctx.value !== value}>{children}</div>;
};
// 受控: <Tabs value={v} onChange={setV}> / 非受控: <Tabs defaultValue="a">
```

**评分点**：
- Context 隐式共享（Tab 无 props 拿状态——组合模式核心）
- 组合校验（脱离父报错——友好错误）
- 受控/非受控双模（value ?? inner）
- a11y 完整（role/aria-selected/键盘导航）
