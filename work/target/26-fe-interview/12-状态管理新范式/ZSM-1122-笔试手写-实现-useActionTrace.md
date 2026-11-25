---
title: [1122] 笔试手写：实现 useActionTrace
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 调试]
type: 笔试题
---

## 1122：笔试手写：实现 useActionTrace

**答**：实现 traceActions(store) 返回包装 store：wrapAction(name, fn) 执行时记录 { name, start, end, duration, ok, error }；trace() 返回记录列表；slowThan(ms) 过滤慢 action；由 action 触发的嵌套 action 用栈结构记 parent（形成调用树）。

```js
function traceActions() {
  const log = [];
  const stack = [];
  return {
    async wrapAction(name, fn) {
      const parent = stack.at(-1)?.name ?? null; // 嵌套归因
      const start = Date.now();
      stack.push({ name, start });
      try {
        const r = await fn();
        log.push({ name, parent, start, end: Date.now(), duration: Date.now() - start, ok: true });
        return r;
      } catch (e) {
        log.push({ name, parent, start, end: Date.now(), duration: Date.now() - start,
          ok: false, error: String(e) });
        throw e;
      } finally {
        stack.pop();
      }
    },
    trace: () => [...log],
    slowThan: ms => log.filter(e => e.duration > ms),
  };
}
```

**评分点**：
- 执行栈记录 parent（嵌套 action 的调用树归因）
- finally 保证栈回退（异常路径不破栈）
- ok/error 双路径记录
- 能讨论：trace 与 devtools 的分工——自建 trace 可进上报管道做线上归因
