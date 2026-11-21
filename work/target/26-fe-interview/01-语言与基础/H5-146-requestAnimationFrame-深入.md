---
title: [H5-146] requestAnimationFrame 深入：与 vsync、后台标签页的关系？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-146：requestAnimationFrame 深入：与 vsync、后台标签页的关系？
**答**：
- rAF 回调在"**下一次重绘之前**"执行，与显示器 vsync 对齐（60/120Hz），由浏览器统一调度、天然节流；一帧内多次调用 rAF 只会注册一次回调。
- 回调参数是 `DOMHighResTimeStamp`，与 `performance.now()` 同源——动画逻辑必须用**时间差 delta** 计算，不能假设固定 16.7ms（高刷屏与掉帧都会打破假设）。
- 页面不可见时 rAF 被暂停（省电），恢复时**不补帧**——倒计时/物理模拟要用绝对时间，不能用帧数累加。
- 对比 setTimeout：rAF 与渲染对齐无掉帧堆积；高频 DOM 更新包一层 rAF 可防"一帧多次重排"。

```javascript
// 1) 与 vsync 对齐：60Hz 每 16.7ms 一次，120Hz 每 8.3ms —— 逻辑必须用 delta
let last = performance.now();
function loop(now) {
  const dt = now - last;          // 真实时间差
  last = now;
  physics(dt);                    // 速度按 dt 计算，不同刷新率表现一致
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

// 2) 后台标签页：rAF 暂停且不补帧 —— 倒计时用绝对时间，回来也不会错
const deadline = performance.now() + 60_000;    // 60 秒倒计时
function tick(now) {
  const remain = Math.max(0, deadline - now);    // 用时间差，帧数累加会出错
  render(remain);
  requestAnimationFrame(tick);
}

// 3) rAF 节流器：把高频操作合并到"下一次重绘前"执行一次
const pending = new Set();
let scheduled = false;
function rafThrottle(fn) {
  pending.add(fn);
  if (scheduled) return;
  scheduled = true;
  requestAnimationFrame(() => {
    scheduled = false;
    const fns = [...pending];
    pending.clear();
    for (const f of fns) f(performance.now());
  });
}

// 4) 与 visibilitychange 组合：不可见时主动停掉昂贵逻辑
document.addEventListener('visibilitychange', () => {
  if (document.hidden) pauseSimulation(); else resumeSimulation();
});
```
