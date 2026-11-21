---
title: [CSS-120] 动画卡顿的排查流程是什么？layer border 工具怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-120：动画卡顿的排查流程是什么？layer border 工具怎么用？

**答**：
- 三步定位：DevTools Rendering 开启 Paint flashing（绿块=重绘）与 Layout Shift regions（蓝块=重排）看动画期间刷屏范围。
- 开启 Layer borders 看哪些元素被提升为合成层、层尺寸是否异常（超大层=内存与光栅化负担）。
- Performance 录制：动画每帧应只出现 Composite Layers；若出现 Recalculate Style/Layout，说明动了非合成属性。
- 常见元凶：大面积 box-shadow/filter blur 动画、滚动容器内 backdrop-filter、图片尺寸未定导致的反复布局。
- 修复路径：属性迁到 transform/opacity、限制效果面积、加 will-change 到动画元素、大图降分辨率。

```css
/* 排查辅助：devtools 之外的代码级探针（仅调试用） */
* { outline: 1px solid transparent; } /* 需要时改为 red 观察布局范围 */

/* 元凶一：大面积阴影动画 → 改为 opacity 淡入的影子层 */
.hover-card::after {
  content: ""; position: absolute; inset: 0;
  box-shadow: var(--shadow-3);
  opacity: 0; transition: opacity 0.25s; /* 只动 opacity */
}
.hover-card:hover::after { opacity: 1; }

/* 元凶二：blur 动画 → 降级为静态模糊 + 透明度 */
.modal-backdrop {
  backdrop-filter: blur(8px);
  transition: opacity 0.3s; /* 不动画 blur 值本身 */
}
```
