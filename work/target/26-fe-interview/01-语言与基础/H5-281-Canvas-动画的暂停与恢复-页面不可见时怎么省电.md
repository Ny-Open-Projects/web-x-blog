---
title: [H5-281] Canvas 动画的暂停与恢复：页面不可见时怎么省电
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-281：Canvas 动画的暂停与恢复：页面不可见时怎么省电

**答**：
- rAF 自动暂停：页面隐藏时 rAF 回调停止——天然省电，但恢复时 dt 会突然巨大，动画逻辑要 clamp 时间差
- 策略分层：可见时全帧率；隐藏超过阈值（如 5s）彻底停止定时器/Worker 任务；前台恢复时快速重建
- 动画时间用「累计动画时间」而非真实时间：暂停期间不累计，恢复后从暂停点继续（倒计时、进度类动画必须如此）
- setTimeout/setInterval 在后台会被浏览器节流到最低 1Hz，依赖它的动画在后台会失真
- 检测入口：visibilitychange + document.hidden；配合 Page Lifecycle API（freeze/resume）处理极端休眠

```javascript
let animTime = 0, last = 0, running = true;
function frame(t) {
  if (!running) return;
  animTime += Math.min(t - last, 100); // clamp 防跳帧
  last = t;
  render(animTime);
  requestAnimationFrame(frame);
}
document.addEventListener('visibilitychange', () => {
  if (document.hidden) { running = false; }
  else if (!running) { running = true; last = performance.now(); requestAnimationFrame(frame); }
});
```
