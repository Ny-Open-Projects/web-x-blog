---
title: [CSS-354] 预渲染与 CSS 状态一致性：prefetch/prerender 的样式陷阱
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-354：预渲染与 CSS 状态一致性：prefetch/prerender 的样式陷阱

**答**：
- 预渲染链路：Speculation Rules 预渲染在后台完整执行渲染管线（CSS 解析/布局/绘制），激活时快照直接上屏——CSS 解析成本被提前支付
- 状态一致性坑：预渲染期间 JS 执行的「相对时间」（Date.now 相关）、动画时钟、轮播进度在激活时要重校准（prerenderingchange 事件里重置）——CSS 动画时间轴在后台照常走，激活瞬间动画可能已跑到中途
- 媒体查询与视口：预渲染按当前视口条件渲染，激活后视口变化（移动旋转）正常走响应式重算，无需特殊处理
- 主题/AB 分组：预渲染期间注入的 AB 分组/主题可能与激活时策略变化——在 prerenderingchange 里重读策略，不要信预渲染时注入的值
- 资源消耗权衡：预渲染一个页面 = 完整渲染管线成本（内存+CPU），命中率高才划算——对确定性导航（列表第一项/按钮主 CTA）启用

```javascript
if (document.prerendering) {
  document.addEventListener('prerenderingchange', () => {
    resetCarouselClock();        // 动画时钟重置
    reReadAbGroup();             // 分组重读
    startVideoOnlyOnActive();    // 视频等激活后动作
  }, { once: true });
}
```
