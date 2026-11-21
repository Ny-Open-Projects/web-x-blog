---
title: [CSS-246] prefers-reduced-motion 怎么落地：动画降级
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 可访问性]
type: 面试题
---

## CSS-246：prefers-reduced-motion 怎么落地：动画降级

**答**：
- 用户系统设置「减少动态效果」时，`prefers-reduced-motion: reduce` 匹配——前庭障碍用户的刚需，也是职业规范要求
- 落地三步：装饰动画直接关（transition-duration: 0.01ms）；功能动画替换为淡入淡出（保语义）；不可替换的轮播/自动播放停掉
- 全局兜底写法：media 块内统一重置 animation/transition/scroll-behavior——一个块覆盖全站
- JS 侧联动：`matchMedia('(prefers-reduced-motion: reduce)')` 决定是否初始化动效库
- 面试话术：不是「把动画全删」，而是降级为安全形式——识别平衡感比喊口号重要

```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
```javascript
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
reduced || initScrollAnimations();
```
