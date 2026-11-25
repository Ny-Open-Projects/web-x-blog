---
title: [CSS-334] CSS 变量求值与失效：自定义属性的性能面
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-334：CSS 变量求值与失效：自定义属性的性能面

**答**：
- 求值时机：自定义属性在 computed value 阶段解析（继承树传播），var() 引用在属性计算时替换——链式引用（--a 引用 --b）按继承与作用域解析，未定义时 fallback 生效
- 失效特性（关键坑）：改一个根节点变量 → 所有引用它的元素样式失效重算——全局主题变量切换是「全页 style recalc」，比换 class 更贵
- 性能规范：高频动画不要用 CSS 变量做插值载体（每帧改 --x 触发全引用树重算）；动画值直接改 transform；变量适合低频主题切换与设计 token
- 作用域设计：token 分层（primitive → semantic → component），语义层变量挂组件根，避免全改根变量
- 调试：DevTools Computed 面板可看 var 解析结果与来源；`@property` 注册后变量可参与动画/过渡（有类型信息）

```css
/* 高频动画反例 */
.ball { left: var(--x); }        /* JS 每帧 set --x → 大范围失效 */
/* 正解 */
.ball { transform: translateX(0); }  /* JS 直接改 transform, 只合成 */

/* @property: 让变量可动画 */
@property --progress { syntax: '<number>'; inherits: false; initial-value: 0; }
.bar { width: calc(var(--progress) * 100%); transition: --progress .3s; }
```
