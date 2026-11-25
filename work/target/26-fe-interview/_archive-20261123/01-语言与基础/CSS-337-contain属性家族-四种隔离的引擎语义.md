---
title: [CSS-337] contain 属性家族：四种隔离的引擎语义
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-337：contain 属性家族：四种隔离的引擎语义

**答**：
- contain 四类：layout（内部布局与外界隔离，内部变化不影响外部布局）、paint（子树绘制不出边界，创建层叠上下文）、size（宽高不依赖内容，显式声明尺寸）、style（计数器等样式作用域隔离）
- 收益本质：给引擎「优化许可」——知道子树变化不会外溢，失效范围可以收窄、绘制可以裁剪；组件化 UI（卡片/弹窗）都应该 contain: layout paint
- contain: content = layout paint（最常用组合）；strict = size layout paint style——size 要显式给尺寸否则内容被压没，慎用
- 与 content-visibility 关系：auto 隐含 layout paint + 视口外跳过渲染；contain 是底层原语，content-visibility 是高层封装
- 常见误用：给「高度由内容决定」的元素加 size containment → 高度塌陷为 0；paint containment 会裁掉溢出阴影/下拉菜单（要留溢出的组件别加）

```css
.card {
  contain: content;              /* 布局与绘制隔离, 卡片内变化不牵连页面 */
}
.popover {
  /* 不能加 paint containment: 下拉要溢出容器边界 */
  contain: layout;
}
.avatar {
  contain: strict;               /* 尺寸固定(已设 width/height), 全隔离 */
  width: 40px; height: 40px;
}
```
