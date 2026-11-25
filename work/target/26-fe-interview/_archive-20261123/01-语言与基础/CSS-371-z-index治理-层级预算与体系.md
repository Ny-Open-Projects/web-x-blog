---
title: [CSS-371] z-index 治理：层级预算与体系
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-371：z-index 治理：层级预算与体系

**答**：
- 病灶：无预算的 z-index 军备竞赛（999→9999→99999）——根因是「层叠上下文边界不清」，大家在一个全局栈里打架
- 治理方案：分层 token（--z-base/--z-dropdown/--z-sticky/--z-overlay/--z-modal/--z-toast/--z-tooltip 固定档位如 0/100/200/.../900）——全局只有 7~8 个值，新增组件必须入档
- 配套规则：每个弹层组件创建独立 stacking context（isolation: isolate），内部相对层级自洽——「模态内 dropdown 被页面元素盖住」的问题由 context 边界解决而不是加 z-index
- z-index: auto 优先：能用文档顺序/上下文嵌套解决的层级不加 z-index；层叠检查进 CR（review 时问一句「这个值属于哪档」）
- 调试手段：DevTools Layers 面板看实际合成层级；「为什么盖不住」先查是否意外创建上下文（opacity/transform 祖先）

```css
:root {
  --z-base: 0; --z-dropdown: 100; --z-sticky: 200;
  --z-overlay: 300; --z-modal: 400; --z-toast: 500; --z-tooltip: 600;
}
.modal { z-index: var(--z-modal); isolation: isolate; }
/* 模态内部 dropdown 用 100 也盖得住页面: context 已隔离 */
```
