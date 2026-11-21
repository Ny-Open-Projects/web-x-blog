---
title: [CSS-227] 组件级响应式设计方法论（container-first）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 容器查询]
type: 面试题
---

## CSS-227：组件级响应式设计方法论（container-first）

**答**：
- 思路转变：从「页面宽度决定布局」（media query）到「容器宽度决定形态」（container query）——组件在任何位置都保持合理形态
- 方法论三步：① 组件声明 container-type: inline-size ② 内部按容器断点（如 300px/500px）切换形态 ③ 页面级只负责给容器分配宽度
- 断点语义变化：断点定义属于组件（卡片 300px 变紧凑），而非全局设备尺寸——设计系统可以内置「自适应组件」
- 配套：cqw/cqi 单位让组件内字号随容器缩放；style() 查询处理主题分支
- 落地路径：设计稿标注从「375/768/1440 断点」转向「组件形态断点」，前端与设计语言对齐

```css
.widget { container-type: inline-size; }
@container (min-width: 480px) {
  .widget { grid-template-columns: 1fr 2fr; } /* 宽容器横排 */
}
@container (max-width: 300px) {
  .widget { font-size: 0.9cqi; } /* 窄容器紧凑 */
}
```
