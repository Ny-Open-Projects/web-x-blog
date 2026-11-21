---
title: [WCN-074] 笔试：手写防抖 signal 与节流 signal（debouncedSignal / throttledSignal）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-074：笔试：手写防抖 signal 与节流 signal

**题目**：实现派生信号：① `debouncedSignal(src, wait)` — 源停止变化 wait 毫秒后才更新；② `throttledSignal(src, interval)` — 源高频变化时按 interval 节流更新（首尾都要有值）；③ 返回只读 getter，可被 computed/effect 正常追踪；④ dispose 后清理定时器。

**答**：

```javascript
import { createSignal, effect } from './mini.js';

export function debouncedSignal(src, wait) {
  const [get, set] = createSignal(src());
  let timer;
  effect(() => {
    const v = src();
    clearTimeout(timer);
    timer = setTimeout(() => set(v), wait);
  });
  const read = () => get();
  read.dispose = () => { clearTimeout(timer); };
  return read;
}

export function throttledSignal(src, interval) {
  const [get, set] = createSignal(src());
  let last = 0, timer;
  effect(() => {
    const v = src();
    const now = Date.now();
    const remain = interval - (now - last);
    if (remain <= 0) {           // 首次/超间隔：立即更新
      last = now; set(v);
    } else if (!timer) {         // 尾随：保证最后一次值最终生效
      timer = setTimeout(() => { last = Date.now(); set(src()); timer = null; }, remain);
    }
  });
  const read = () => get();
  read.dispose = () => { clearTimeout(timer); };
  return read;
}

// 口径：
// const [q, setQ] = createSignal('');
// const dq = debouncedSignal(q, 300);   // 输入停 300ms 后 dq() 更新
// effect(() => fetchSearch(dq()));      // 搜索请求防抖
```

**评分点**：
- 用 effect 追踪源 signal（派生信号复用依赖追踪，而非手动订阅）。
- 防抖：每次变化重置 timer；节流：首值立即 + 尾值 setTimeout 保证最终一致。
- 可追踪性：返回 getter 与普通 signal 同构，可进 computed 链。
- dispose 清理定时器（生命周期意识）。
