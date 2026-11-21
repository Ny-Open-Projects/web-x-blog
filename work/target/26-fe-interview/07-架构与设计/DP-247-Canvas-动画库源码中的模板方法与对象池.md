---
title: [DP-247] 源码识别：Canvas 动画库源码中的模板方法与对象池？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-247：源码识别：Canvas 动画库源码中的模板方法与对象池？
**答**:
- 模板方法：渲染循环骨架固定（清屏 → 状态保存 → 绘制 → 恢复 → rAF），具体绘制子类/回调注入——PIXI/phaser 的 ticker。
- 对象池：粒子系统大量创建销毁 → 池化复用（GC 压力），死亡粒子 reset 回池。
- 策略：插值策略（linear/easeInOut/弹簧）、碰撞策略按场景注入。
- 识别要点：能说清"rAF 驱动 + delta time（帧率无关动画）+ 暂停时停 ticker"三件套是动画库地基。

```javascript
// 渲染循环模板方法
class Ticker {
  onFrame = [];                            // 每帧回调（策略注入点）
  last = 0;
  start() {
    const loop = (t) => {
      const delta = t - this.last;         // delta time：帧率无关
      this.last = t;
      ctx.clearRect(0, 0, W, H);           // 模板骨架：清屏
      this.onFrame.forEach(f => f(delta));
      if (!this.paused) requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
}
// 对象池：粒子
class ParticlePool {
  pool = [];
  spawn() { return this.pool.pop() ?? new Particle(); }
  recycle(p) { p.reset(); this.pool.push(p); }     // 复用避免 GC
}
// 插值策略：const ease = t => t < 0.5 ? 2*t*t : 1 - (-2*t+2)**2/2;   // easeInOutQuad
```
