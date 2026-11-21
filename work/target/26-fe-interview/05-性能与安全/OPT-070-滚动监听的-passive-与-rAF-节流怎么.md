---
title: [OPT-070] 滚动监听的 passive 与 rAF 节流怎么组合才完整？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-070：滚动监听的 passive 与 rAF 节流怎么组合才完整？

**答**：
- passive 告诉浏览器"回调不会 preventDefault"，滚动本身不再等 JS 回调，消除**输入延迟**；rAF 节流保证回调一帧一次，消除**重复计算**。两者解决的是不同问题，必须组合。
- 不组合的两种半吊子：只 passive 不节流——每秒几百次回调照样烧 CPU；只节流不 passive——每次滚动仍被回调同步阻塞。
- passive 有自动场景：window/document/body 上的 wheel/touch 监听 Chrome 默认 passive；但绑定在子元素上不自动，必须显式传。
- 需要 `preventDefault` 的场景（下拉刷新、自定滚动）不能 passive，此时把"阻止默认"与"计算"拆开：先同步阻止，再 rAF 里计算。

```javascript
// 一一对应：passive + rAF 组合的三种典型写法
const onScrollCalc = () => {
  progress.style.transform = `scaleX(${window.scrollY / docHeight})`; // 只动 transform
};

// ① 标准组合：passive 消除滚动阻塞，rAF 收敛到一帧一次
window.addEventListener('scroll', rafThrottle(onScrollCalc), { passive: true });

// ② touch 系列绑定在子元素上不会自动 passive，必须显式声明
document.querySelector('.drawer').addEventListener('touchmove', rafThrottle((e) => {
  dragHandle(e.touches[0].clientY);
}), { passive: true });

// ③ 必须 preventDefault 时：拆分"阻止"与"计算"
const gestureEl = document.querySelector('.pull-refresh');
gestureEl.addEventListener('touchmove', (e) => {
  if (pullingDown) e.preventDefault();       // 同步阻止默认滚动（不能 passive）
  pendingY = e.touches[0].clientY;           // 只记录，不计算
  requestAnimationFrame(() => updatePullUI(pendingY)); // 计算放到 rAF
}, { passive: false }); // 显式声明非 passive，浏览器也无需猜测

// 自检：Performance 面板录制滚动，Main 线程上不应出现连续的小 Script 块；
// 若有，说明 passive 或 rAF 节流没生效
```
