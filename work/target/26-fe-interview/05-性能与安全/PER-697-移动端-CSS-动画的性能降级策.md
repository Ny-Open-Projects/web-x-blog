---
title: [PER-697] 移动端 CSS 动画的性能降级策略：哪些动画必须降、按什么信号降、降级后的替代方案
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-697：移动端 CSS 动画的性能降级策略：哪些动画必须降、按什么信号降、降级后的替代方案

**答**：
- 必须降的动画：大面积 blur/shadow 动画（光栅化开销大）、非 transform/opacity 的属性动画（触发重排重绘）、大量并行动画（合成层爆炸）、视差滚动中的多层 transform（低端机 GPU 跟不上）。
- 降级信号：设备档（689）+ `prefers-reduced-motion` 用户偏好 + 实测帧率（679 探针发现持续掉帧自动降）——三层信号，静态档位 + 动态实测。
- 替代方案：blur 动画 -> 透明度渐变；位移动画 -> transform 合成层动画；粒子特效 -> 静态图/简化版；重过渡 -> 直接切换 + 短淡入。
- 落地机制：动画组件统一走 `motionLevel()` 决策（full/reduced/minimal），CSS 用 `@media (prefers-reduced-motion)` + JS 档位 class 双通道，埋点记录降级触发率验证策略。

```javascript

const motionPolicy = {
  mustDowngrade: ['大面积 blur/shadow 动画', '非 transform/opacity 属性动画',
    '>20 个并行动画', '多层视差 transform'],
  signals: { static: 'deviceTier 档位 + prefers-reduced-motion',
    dynamic: 'FPS 探针持续掉帧 -> 运行时自动降档' },
  alternatives: { blur: 'opacity 渐变', layoutAnim: 'transform 合成动画',
    particles: '静态图/简化版', transition: '直接切换+短淡入' },
  essence: '动画组件统一走 motionLevel() 决策，CSS 媒体查询与 JS 档位 class 双通道落地',
};
console.log(motionPolicy.essence);
```
