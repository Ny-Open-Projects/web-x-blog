---
title: [CSS-240] 跨文档 View Transitions：MPA 的页面切换动画
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-240：跨文档 View Transitions：MPA 的页面切换动画

**答**：
- 同文档（SPA）之外的另一半：跨文档过渡让「整页跳转」也有过渡动画——浏览器拦截导航、截图、加载新页、交叉渐变
- 启用：新旧两个页面都声明 `@view-transition { navigation: auto; }`
- 限制：同源导航、无 redirect、GET 请求；form POST/跨域不触发
- 元素级共享：同 view-transition-name 的元素跨页配对（列表页 → 详情页头图）——MPA 里做共享元素动画
- 事件钩子：pageswap（离开前）/ pagereveal（进入后）可调整命名与时机

```css
/* 两个页面都写 */
@view-transition { navigation: auto; }
.product-img { view-transition-name: product; }
```
