---
title: [DP-155] 为什么防抖节流是状态模式的变体？leading/trailing 如何实现？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-155：为什么防抖节流是状态模式的变体？leading/trailing 如何实现？（高频）
**答**：
- 防抖/节流内部维护"当前处于什么相位"（空闲/等待中/已触发），不同相位对"再来一次调用"响应不同——这正是状态模式的行为分派（DP-052 的函数式微缩版）。
- 两个策略轴：leading（首次立即执行）与 trailing（最后一次补执行），组合出四象限（lodash 的 leading/trailing 选项）。
- 加分实现：cancel（取消等待中的相位）、flush（立即结算）、返回值透传 leading 首次结果。

```javascript
// 状态模式视角的防抖：相位 = idle / waiting
function debounce(fn, wait, { leading = false } = {}) {
  let timer = null, phase = 'idle', lastArgs, lastThis;
  function invoke() {                                          // 结算动作：两相位共用
    fn.apply(lastThis, lastArgs);
    phase = 'idle'; timer = null;
  }
  function debounced(...args) {
    lastArgs = args; lastThis = this;
    const isFirst = phase === 'idle';
    if (isFirst && leading) { phase = 'leading'; fn.apply(this, args); phase = 'waiting'; }  // leading 立即发
    clearTimeout(timer);
    timer = setTimeout(invoke, wait);                          // waiting 相位：不断重置倒计时
    if (isFirst && !leading) phase = 'waiting';
  }
  debounced.cancel = () => { clearTimeout(timer); timer = null; phase = 'idle'; };   // 状态清理
  debounced.flush = () => { if (phase === 'waiting') { clearTimeout(timer); invoke(); } };
  return debounced;
}
// 节流：相位 = idle / cooling，冷却结束按 trailing 补一次
function throttle(fn, wait, { leading = true, trailing = true } = {}) {
  let timer = null, last = 0, pendingArgs = null;
  return function (...args) {
    const now = Date.now(), remaining = wait - (now - last);
    pendingArgs = args;
    if (remaining <= 0 && !timer) {                            // idle 相位：可执行
      if (leading) { last = now; fn.apply(this, args); pendingArgs = null; }
      else last = now;
    } else if (trailing && !timer) {                           // cooling 相位：预约补发
      timer = setTimeout(() => {
        last = Date.now(); timer = null;
        if (pendingArgs) { fn.apply(this, pendingArgs); pendingArgs = null; }
      }, remaining);
    }
  };
}
const search = debounce((kw) => api.search(kw), 300, { leading: false });
const reportScroll = throttle(() => sendBeacon(), 1000, { leading: true, trailing: true });
```
