---
title: [WEB-396] 后台标签页里定时器和 rAF 会被怎么节流？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-396：后台标签页里定时器和 rAF 会被怎么节流？
**答**：
- rAF 在不可见 tab 完全暂停（没有渲染就没有帧）；setTimeout 被限到最低 1 次/秒（Chrome 对普通 tab）。
- 更狠的节流：后台 5 分钟后 intensive throttling 1 次/分钟（链式定时器）；省电模式下更严。
- 影响：轮询/倒计时/心跳全部失真——倒计时用"绝对时间差"算，心跳靠服务端重连兜底，配合 visibilitychange 恢复。

```javascript
// 后台 tab: setInterval(…, 1000) 实际 ~60000ms
let endTime = Date.now() + 60 * 1000;
setInterval(() => {
  const left = Math.max(0, endTime - Date.now()); // 绝对差而非递减计数
  render(left);
}, 1000);
document.addEventListener('visibilitychange', () => {
  if (!document.hidden) sync();   // 回前台立即校正
});
console.log('倒计时永远算绝对时间差');
```
