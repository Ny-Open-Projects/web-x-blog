---
title: [SCN-100] 低端机（2GB 内存安卓）用户反馈页面卡顿发热，如何做优雅降级？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-100：低端机（2GB 内存安卓）用户反馈页面卡顿发热，如何做优雅降级？
**答**：
- 静态分档：用 deviceMemory、hardwareConcurrency、UA 识别设备档位（high/mid/low），写入 html data 属性，CSS 按档位关闭模糊、阴影、粒子等昂贵视觉。
- 运行时自适应：FPS 探针发现持续低于 25fps 自动降为低档，比静态判断更可靠（静态判断识别不了后台开一堆 App 的中端机）。
- 降级动作分级：先关动效，再降图片清晰度与轮询频率，最后关虚拟列表动画；高端机体验完全不变。

```typescript
// 低端机自适应降级：静态分档 + 运行时 FPS 自动降档
function deviceTier() {
  const mem = (navigator as any).deviceMemory ?? 4;      // GB
  const cores = navigator.hardwareConcurrency ?? 4;
  if (mem <= 2 || cores <= 4) return 'low';
  if (mem <= 4) return 'mid';
  return 'high';
}
document.documentElement.dataset.tier = deviceTier();
// CSS 按档位关动效：
// html[data-tier="low"] .blur-bg { backdrop-filter: none; background: #333; }
// html[data-tier="low"] * { animation-duration: .01s !important; }

// 运行时自适应：持续低 FPS 自动降档，不依赖静态判断
(function autoDegrade() {
  let last = performance.now(), frames = 0;
  const loop = (now: number) => {
    frames++;
    if (now - last >= 1000) {
      const fps = frames;
      frames = 0; last = now;
      const el = document.documentElement;
      if (fps < 25 && el.dataset.tier !== 'low') {
        el.dataset.tier = 'low';      // 连续卡顿自动降为低档
        report({ type: 'auto-degrade', fps });
      }
    }
    requestAnimationFrame(loop);
  };
  requestAnimationFrame(loop);
})();
```

## 十九、安全场景进阶
