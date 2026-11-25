---
title: [CSS-373] 多列布局与破碎盒：跨列/跨页的盒子修饰
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-373：多列布局与破碎盒：跨列/跨页的盒子修饰

**答**：
- 多列布局（columns）：文本流式分栏（报纸式），columns: 2 + column-gap + column-rule——适合长文本，不适合组件卡片（顺序是纵向填列，阅读顺序反直觉）
- 跨列元素：column-span: all 让标题横跨；break-inside: avoid 防卡片被切开——多列的分栏平衡（column-fill: balance）影响最后一列高度
- box-decoration-break：盒子跨行/跨列/跨页被切断时，边框/背景/内边距是否「每段完整」——clone（每段完整圆角内边距，标签高亮场景）vs slice（整体切分）
- 与打印联动：多列在打印时映射为页分割，break-* 属性统一控制分页与分栏
- 实战定位：行内标签多行场景（tag 列表换行保留圆角）是 box-decoration-break: clone 的招牌场景；其余场景被 flex/grid 覆盖

```css
.article { columns: 2 300px; column-gap: 32px; column-rule: 1px solid #eee; }
.article h2 { column-span: all; }
.article figure { break-inside: avoid; }

/* 多行标签每行完整样式 */
.tag {
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
  background: var(--primary-bg);
  padding: 2px 8px; border-radius: 4px;
}
```
