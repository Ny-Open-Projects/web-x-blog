---
title: [HW-160] 手写真进度条——可估算总量任务（上传/多步）的确定性进度 + 不确定任务的伪进度收敛
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-160：手写真进度条——可估算总量任务（上传/多步）的确定性进度 + 不确定任务的伪进度收敛
**答**：进度条两种语义：① 确定任务（分片上传 N 片）——真实进度 = 已完成片/总片（加权：大分片权重高）；② 不确定任务（单请求无进度）——伪进度：先快后慢逼近 90%（100ms 步进 × 衰减），真实完成跳 100%——伪进度绝不骗到 100%（完成以真实事件为准）。渲染走 rAF + transform（合成器）。

```javascript
function createProgress(el) {
  let value = 0, target = 0, mode = 'determinate', rafId = null;
  function tick() {
    const delta = (target - value) * 0.15;                // 缓动逼近
    value = Math.min(value + Math.max(delta, 0.05), target);
    el.style.transform = `scaleX(${value / 100})`;        // transform：合成器（PER-347）
    if (Math.abs(target - value) > 0.1 || (mode === 'indeterminate' && target < 90)) {
      rafId = requestAnimationFrame(tick);
      if (mode === 'indeterminate') {                     // 伪进度：先快后慢逼近 90%
        target = Math.min(target + (90 - target) * 0.02, 90);
      }
    } else rafId = null;
  }
  return {
    determinate(pct) { mode = 'determinate'; target = Math.min(pct, 100); tick(); },
    indeterminate() { mode = 'indeterminate'; target = 5; tick(); },    // 从 5% 起步
    done() { mode = 'determinate'; target = 100; tick(); },           // 真实完成才 100%
    destroy() { cancelAnimationFrame(rafId); },
  };
}
// 上传（确定）：progress.determinate(uploadedChunks / total * 100)
// 单接口（不确定）：progress.indeterminate() → 响应回来 done()
// 语义铁律：伪进度上限 90% —— 到 100% 只能由真实完成事件触发（骗用户 = 失去信任）
```

**评分点**：
- 两种模式语义（确定/伪进度上限 90%）与铁律（100% 只由真实事件触发）——本题核心。
- scaleX transform 合成器渲染（无 layout）。
- 缓动逼近（rAF 平滑）与 destroy 清理。
- 分片上传的真实进度加权意识。
