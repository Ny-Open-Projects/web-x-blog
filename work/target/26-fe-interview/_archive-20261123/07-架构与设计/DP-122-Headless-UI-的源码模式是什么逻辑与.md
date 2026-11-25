---
title: [DP-122] Headless UI 的源码模式是什么？"逻辑与 UI 分离"如何精读？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-122：Headless UI 的源码模式是什么？"逻辑与 UI 分离"如何精读？（高频）
**答**：
- Headless 组件 = 无样式组件：内部用 Hook/状态机管理键盘、焦点、ARIA 等行为，通过 render props 或 props getter（`getButtonProps()`）把这些行为"注入"调用方的任意 DOM。
- 核心模式：状态机（开关/多选/弹层转移）+ 状态适配（props getter 把状态映射为 aria-*、事件）+ 组合组件（Menu.Items 等子组件共享 context）。
- 与 styled 组件库的差别：样式层完全外包，逻辑层可被任何设计系统复用。

```jsx
// 精简复刻 Headless useDisclosure + Menu 的模式
function useDisclosure(initial = false) {                       // 行为 Hook：状态机
  const [open, setOpen] = useState(initial);
  return useMemo(() => ({
    open,
    show: () => setOpen(true), hide: () => setOpen(false), toggle: () => setOpen((o) => !o),
  }), [open]);
}
function useMenuProps(state, dispatch) {                        // props getter：状态适配器
  return {
    button: {
      'aria-expanded': state.open,
      onClick: () => dispatch({ type: 'toggle' }),
      onKeyDown: (e) => e.key === 'Escape' && dispatch({ type: 'hide' }),
    },
    list: { role: 'menu', hidden: !state.open },
  };
}
// 无样式组件：只管行为，UI 全由调用方画
function Menu({ children }) {
  const { open, toggle, hide } = useDisclosure();
  const props = useMenuProps({ open }, { type: toggle, hide });   // 简化示意
  return children({ open, buttonProps: props.button, listProps: props.list });
}
<Menu>
  {({ open, buttonProps, listProps }) => (
    <div>
      <button {...buttonProps}>选项 {open ? '▲' : '▼'}</button>
      <ul {...listProps}><li role="menuitem">复制</li><li role="menuitem">删除</li></ul>
    </div>
  )}
</Menu>
```
