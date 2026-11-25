---
title: [DP-372] Headless 组件模式：逻辑与样式彻底分离
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-372：Headless 组件

**答**：
- 模式定义：组件只提供「行为与状态」（无任何样式/DOM 结构约束）——UI 完全由使用者渲染（render props/slot/hook 返回）
- 三种实现形态：render props（`<Counter>{({count, inc}) => ...}</Counter>`）、Hooks（useCounter——最轻）、组合组件 + CSS 变量约定
- 价值：a11y 行为（键盘导航/aria）在逻辑层一次实现，样式无限自由——设计系统「行为标准化、视觉个性化」的正解
- 实战要点：headless 返回的「语义就绪」（aria 状态/事件处理器/id 生成——使用者直接绑定即可）
- 深水点：headless 的「API 设计」——返回粒度（状态+处理器+aria 三件套）与文档（使用者要知道绑什么）——API 设计决定可用性

```jsx
// headless hook: 下拉框
function useDropdown({ items }) {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  return {
    open, active,
    trigger: { 'aria-expanded': open, onClick: () => setOpen(!open),
      onKeyDown: (e) => { if (e.key === 'ArrowDown') setActive((i) => Math.min(i + 1, items.length - 1)); if (e.key === 'Escape') setOpen(false); } },
    menu: { role: 'listbox', hidden: !open },
    option: (i) => ({ role: 'option', 'aria-selected': i === active, id: `opt-${i}` }),
  };
}
// 使用者完全控制 UI, a11y 行为白拿
```
