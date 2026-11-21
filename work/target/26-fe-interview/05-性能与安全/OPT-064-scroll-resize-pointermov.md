---
title: [OPT-064] scroll/resize/pointermove 的节流参数怎么选？rAF 节流为什么优先？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-064：scroll/resize/pointermove 的节流参数怎么选？rAF 节流为什么优先？

**答**：
- 三类高频事件语义不同，参数不能一概而论：scroll 关心"最新位置"（rAF 节流最合适）、resize 关心"停下来再算"（debounce 200ms）、pointermove 关心"够新即可"（rAF 或 leading throttle 16ms）。
- **rAF 节流**是视觉相关事件的默认答案：一帧一次、与渲染对齐、天然去重；配合 `{ passive: true }` 消除滚动阻塞。
- debounce/troughle 选择依据：值只需"最终态"用 debounce（搜索联想、resize 后重排）；值需要"过程态"用 throttle/rAF（跟随效果、吸顶计算）。
- 移动端 pointermove 触发频率可达 120Hz，超过屏幕刷新率的处理全是浪费，rAF 天然按刷新率收敛。

```javascript
// 一一对应：三类事件的节流选型与 rAF 节流实现
// 通用 rAF 节流：一帧最多执行一次，带 trailing 保证最后一帧不丢
function rafThrottle(fn) {
  let ticking = false, lastArgs = null;
  return (...args) => {
    lastArgs = args;
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      fn(...lastArgs);
      ticking = false;
      lastArgs = null;
    });
  };
}

// ① scroll：rAF 节流 + passive（写法固定，几乎不用改参数）
window.addEventListener('scroll', rafThrottle(() => {
  header.classList.toggle('stuck', window.scrollY > 80);
}), { passive: true });

// ② resize：debounce——布局计算贵，只要最终尺寸
const debounce = (fn, ms) => {
  let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
};
window.addEventListener('resize', debounce(() => chart.resize(), 200));

// ③ pointermove：拖拽跟随用 rAF 节流（过程态）；如需落点记录则 leading throttle
// 120Hz 设备上 rAF 自动收敛到 60/120fps 一次，不会超采样
canvas.addEventListener('pointermove', rafThrottle((e) => drawCursor(e.clientX, e.clientY)));

// 选型速查：
// 输入联想/搜索框        -> debounce 200~300ms
// resize 重排图表        -> debounce 100~200ms
// 吸顶/进度条/跟随       -> rafThrottle + passive
// 埋点上报（scroll 深度） -> throttle leading 1000ms，低频即可
```

## 十二、渲染管线优化
