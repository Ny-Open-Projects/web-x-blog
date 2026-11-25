---
title: [JS-412] 笔试：手写 debounce（带 maxWait 上限）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-412：笔试：手写 debounce（带 maxWait）

**答**：实现 `debounce(fn, wait, { maxWait, leading })`：① 标准 debounce：连续调用只执行最后一次；② maxWait：即使持续触发，最长等待 maxWait 后强制执行一次（防「永远不打字」场景）；③ leading：首次调用立即执行；④ 返回函数带 cancel/flush；⑤ flush 同步执行挂起调用并清定时器。写出实现。

```javascript
function debounce(fn, wait, { maxWait = Infinity, leading = false } = {}) {
  let timer = null, firstAt = 0, pendingArgs = null, invoked = false;
  const invoke = (now) => {
    timer = null;
    if (pendingArgs) { fn(...pendingArgs); pendingArgs = null; }
    invoked = leading ? false : true;      // leading 模式重新武装
    firstAt = 0;
  };
  const wrapped = (...args) => {
    const now = Date.now();
    if (leading && !invoked && !timer) { fn(...args); invoked = true; firstAt = now; return; }
    pendingArgs = args;
    if (!firstAt) firstAt = now;
    clearTimeout(timer);
    const sinceFirst = now - firstAt;
    const delay = Math.min(wait, maxWait - sinceFirst);   // maxWait 约束
    timer = setTimeout(() => invoke(now), Math.max(delay, 0));
  };
  wrapped.cancel = () => { clearTimeout(timer); timer = null; pendingArgs = null; firstAt = 0; };
  wrapped.flush = () => { if (timer) { clearTimeout(timer); invoke(Date.now()); } };
  return wrapped;
}
// 场景: 输入联想 maxWait=1000 → 用户一直打字也不超过 1s 请求一次
```

**评分点**：
- maxWait 与 wait 取 min（自首次调用起算）
- leading 立即执行与重新武装逻辑
- cancel/flush 生命周期方法
- 首次时间戳 firstAt 的重置时机
