---
title: [CSS-286] Element.animate 与 WAAPI 的编排能力
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-286：Element.animate 与 WAAPI 的编排能力

**答**：
- 编排三件套：Animation 对象（控制单个动画）→ currentTime/playbackRate（时间轴操作）→ document.getAnimations()（收集全页动画统一调度）
- 组合场景：入场动画完成后再播强调动画（await finished 链）；暂停全部动画（调试/省电）；全局倍速（playbackRate 统一调节）
- offset 关键帧：数组中位置对应时间比例（0~1），多段缓动精确编排
- 与 CSS 动画的互操作：getAnimations 能拿到 CSS 动画的 Animation 对象——统一控制入口
- commitStyles()：把动画结束态写入元素样式（fill: forwards 的持久化替代）

```javascript
// 串行编排
const a1 = el.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 200, fill: 'forwards' });
await a1.finished;
const a2 = el.animate([{ transform: 'translateY(0)' }, { transform: 'translateY(20px)' }], { duration: 300, easing: 'ease-in' });
// 全局暂停/倍速
document.getAnimations().forEach(a => a.pause());
document.getAnimations().forEach(a => (a.playbackRate = 2));
```
