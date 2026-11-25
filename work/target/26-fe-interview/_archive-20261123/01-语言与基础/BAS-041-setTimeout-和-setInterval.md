---
title: [BAS-041] setTimeout 和 setInterval 有哪些注意点？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-041：setTimeout 和 setInterval 有哪些注意点？
**答**：
- 定时器不精确：delay 只是"最早执行时间"，主线程被占用时顺延；嵌套超过 5 层后最小间隔被强制为 4ms。
- setInterval 若回调执行时间超过间隔，会连续堆积执行，推荐用链式 setTimeout 替代。
- 组件卸载或页面离开时必须 clearTimeout/clearInterval，否则定时器泄漏、回调访问已销毁的组件。

```javascript
// 链式 setTimeout：上一次执行完成后才开始计时，天然防堆积
let timerId;
function poll() {
  fetch('/api/status')
    .then(() => { timerId = setTimeout(poll, 3000); })
    .catch(() => { timerId = setTimeout(poll, 10000); });
}
poll();
// 组件卸载时：clearTimeout(timerId)
```
