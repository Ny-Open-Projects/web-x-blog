---
title: [CSS-122] @container 深入：命名容器、尺寸查询与 style 查询怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-122：@container 深入：命名容器、尺寸查询与 style 查询怎么用？

**答**：
- 命名容器：`container: card / inline-size` 命名 + 类型，`@container card (min-width: 400px)` 精确指向，避免命中错误祖先。
- `container-type: inline-size` 只锁定内联轴（最常用，避免高度循环依赖）；`size` 双轴锁定，要求容器有确定高度。
- style 查询：`@container style(--theme: dark)` 基于容器 CSS 变量值切换样式，"变量即状态机"。
- style 查询暂不支持计算到任意表达式自由度有限，以变量字面值比较为主。
- 与 cqw/cqi 单位、fallback 变量配合，构成完整的组件级响应式体系。

```css
/* 命名容器 */
.dashboard-widget {
  container: widget / inline-size;
}

/* 尺寸查询：指向指定命名容器 */
@container widget (min-width: 480px) {
  .widget-body { grid-template-columns: auto minmax(0, 1fr); }
}

/* style 查询：按容器变量值切换，主题随容器而非页面 */
.card-scope { container-type: inline-size; --theme: light; }
@container style(--theme: dark) {
  .card { --bg-surface: #17181a; --fg-primary: #e8e9ea; }
}
/* JS 只改容器变量：scope.style.setProperty('--theme', 'dark') */
```
