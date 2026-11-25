---
title: [CSS-348] fixed 定位与滚动：包含块陷阱与合成器滚动
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-348：fixed 定位与滚动：包含块陷阱与合成器滚动

**答**：
- 包含块陷阱：transform/perspective/filter/will-change（非 none）祖先会成为 fixed 元素的包含块——fixed 相对它定位而非视口，「fixed 失效变 absolute」的经典来源（弹窗父级有动画 transform）
- 合成器滚动：普通滚动时 fixed 元素不重绘（合成器直接不移动该层），但祖先链一旦创建上下文/包含块，滚动行为退化为主线程路径
- 移动端键盘联动：visualViewport 缩放/位移时 fixed 元素行为（相对 layout viewport 而非 visual viewport）——底部栏被键盘盖住要用 visualViewport JS 定位或 svh/dvh
- sticky 与 fixed 选择：sticky 保留文档流与父容器约束（吸顶首选），fixed 脱离流全局悬浮——模态遮罩用 fixed，导航吸顶用 sticky
- 调试方法：DevTools 给元素逐级 ancestors 排查 transform；「滚动时 fixed 元素抖动」多半是被包含块限制后的滚动重算

```css
/* 陷阱复现 */
.drawer { transform: translateX(0); }        /* transition 中创建包含块 */
.drawer__close { position: fixed; top: 0; }  /* 相对 drawer 而非视口! */
/* 修复: 把 fixed 元素移出 transform 祖先, 或用 portal 结构 */
```
