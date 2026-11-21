---
title: [WCN-312] 复杂元素（combobox/grid）的 a11y 实现深水？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-312：复杂元素（combobox/grid）的 a11y 实现深水？
**答**：
- WAI-ARIA APG 模式逐条实现：combobox 的 aria-expanded/activedescendant/键盘流（上下/回车/esc）。
- 焦点管理：activedescendant vs 焦点移动两种模式（列表项可聚焦性决定）。
- live region：结果数变化 aria-live=polite 播报。
- 测试：APG 逐条用例化（键盘流表格驱动），SR 真机走查（NVDA/VoiceOver 双平台）。

```javascript
test.each([
  ['ArrowDown', 'actives second option'],
  ['Enter', 'selects active'],
  ['Escape', 'closes without select'],
])('combobox %s', async (key, expectDesc) => { /* APG 流 */ });
r
```
