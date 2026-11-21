---
title: [TST-132] 笔试：手写组件事件断言库（toHaveEmitted：参数/次数/顺序）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-132：笔试：手写组件事件断言库（toHaveEmitted：参数/次数/顺序）
**答**：
- 需求：实现 `createEventSpy()` 工具——包装任意 emitter（组件 props 回调 / EventEmitter / Vue emit），提供 `toHaveEmitted(event, ...args)`（断言发过某事件及参数）、`toHaveEmittedTimes(event, n)`（次数）、`emittedEvents()`（顺序流，断言「先 loading 后 loaded」这类次序）。
- 核心：拦截器收集 `{ event, args, t }` 时间戳数组；断言基于数组查询；顺序断言比较两个事件首次出现的索引。
- 边界：参数深比较（对象参数用 toEqual 语义）；「从未发出」断言 `not.toHaveEmitted`；同一事件多次发出时 toHaveEmitted 默认「至少一次匹配」并提供 `nth(n)` 精确断言。

```javascript
function createEventSpy(target, events) {
  const log = []; // { event, args, t }
  const unsubs = events.map((ev) => target.on(ev, (...args) => log.push({ event: ev, args, t: Date.now() })));
  const api = {
    log,
    emittedEvents: () => log.map((e) => e.event),
    clear: () => (log.length = 0),
    dispose: () => unsubs.forEach((u) => u()),
    // 断言实现（供 expect 内使用或直接调用）
    toHaveEmitted(event, ...args) {
      const ok = log.some((e) => e.event === event &&
        args.every((a, i) => JSON.stringify(a) === JSON.stringify(e.args[i])));
      if (!ok) throw new Error(`expected event "${event}" with ${JSON.stringify(args)}; got ${JSON.stringify(log)}`);
      return true;
    },
    toHaveEmittedTimes(event, n) {
      const c = log.filter((e) => e.event === event).length;
      if (c !== n) throw new Error(`expected "${event}" x${n}, got x${c}`);
      return true;
    },
    emittedBefore(before, after) { // 顺序断言
      const idx = (e) => log.findIndex((x) => x.event === e);
      const a = idx(before), b = idx(after);
      if (a === -1 || b === -1 || a > b)
        throw new Error(`expected "${before}" before "${after}"; sequence: ${api.emittedEvents()}`);
      return true;
    },
  };
  return api;
}

// ---- 用法 ----
const bus = new (require('events').EventEmitter)();
const spy = createEventSpy(bus, ['loading', 'loaded', 'error']);
bus.emit('loading'); bus.emit('loaded', { count: 3 });

spy.toHaveEmitted('loaded', { count: 3 });
spy.toHaveEmittedTimes('loading', 1);
spy.emittedBefore('loading', 'loaded'); // 次序正确
// React 场景：props 回调包装成 emitter，或直接用 vi.fn + toHaveBeenCalledWith
```

**评分点**：
1. 日志结构含时间序，支持顺序断言（不只是有无）。
2. 参数深比较而非 ===（对象事件参数）。
3. 错误信息带完整事件流（失败可读）。
4. dispose 释放监听（测试泄漏意识）。
