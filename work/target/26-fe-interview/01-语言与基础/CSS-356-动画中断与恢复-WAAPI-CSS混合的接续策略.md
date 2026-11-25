---
title: [CSS-356] 动画中断与恢复：WAAPI/CSS 混合的接续策略
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-356：动画中断与恢复：WAAPI/CSS 混合的接续策略

**答**：
- 接续本质：动画中断（用户手势打断 CSS 动画）时，必须「从当前计算值接着动」而不是跳回关键帧起点——读当前值有三条路：getComputedStyle（读值但丢动画上下文）、WAAPI getAnimations()[0].currentTime（时间轴）、element.animate 重启
- WAAPI 方案（推荐）：CSS 动画 + WAAPI 接管同一元素，用 anim.effect.updateTiming 或重建 animate({ ..., currentTime: 保留 }) —— composite: 'accumulate' 可叠加而非覆盖
- CSS 方案：CSS 动画中途改 keyframes/属性会跳变——用 CSS 自定义属性传当前值（@property 注册后可 transition），或切换 class 触发的过渡（transition 从当前值出发天然接续）
- 物理跟手模型：触摸驱动动画用 JS 维护 current 值（唯一真源），CSS 动画只在「无手势」时接管——手势期间暂停 CSS 动画（anim.pause()）避免双驱动打架
- 页面隐藏恢复：切后台 CSS 动画暂停（时间轴停），回来时继续——但依赖 JS 时钟的 JS 动画要按绝对时间补偿

```javascript
// 手势接续 CSS 动画
const anims = el.getAnimations();
anims.forEach(a => a.pause());                 // 手势接管
const cur = getComputedStyle(el).transform;    // 读当前值
// touchmove 中 JS 更新 transform
el.style.transform = `translateX(${newX}px)`;
el.addEventListener('touchend', () => {
  anims.forEach(a => { a.play(); });           // 交还 CSS
  // 或 el.animate([...], { composite: 'accumulate' }) 从当前值续
});
```
