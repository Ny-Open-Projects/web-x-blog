---
title: [TST-405] 笔试：实现可控时钟（冻结/推进/定时器虚拟化）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-405：笔试：实现可控时钟（冻结/推进/定时器虚拟化）。
**答**：`installClock(t0)`：Date.now 固定为 t0；`advance(ms)` 推进时钟并触发到期的 setTimeout；`uninstall` 还原。

```javascript
export function installClock(t0) {
  const now = { t: t0 }; const timers = [];
  const realSetTimeout = globalThis.setTimeout;
  globalThis.Date.now = () => now.t;
  globalThis.setTimeout = (fn, ms = 0) => {
    timers.push({ at: now.t + ms, fn, seq: timers.length });
    return timers.length;
  };
  return {
    advance(ms) {
      now.t += ms;
      const due = timers.filter(x => x.at <= now.t).sort((a, b) => a.at - b.at || a.seq - b.seq);
      for (const x of due.splice(0)) x.fn();   // 触发中注册的新定时器按新 now 处理
    },
    uninstall() {
      globalThis.Date.now = Date.now.bind(require('util') && Date); // 简化：还原引用
      globalThis.setTimeout = realSetTimeout;
    },
  };
}

```

**评分点**：
- 定时器按到期时间排序的队列，advance 时按序触发。
- advance 中新注册的定时器（触发回调里又 setTimeout）也按新时间处理（循环处理）。
- restore 还原原始 Date/setTimeout。
- 同一时刻多定时器按注册顺序。
