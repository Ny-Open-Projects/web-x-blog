---
title: [TST-043] 笔试：手写用例级超时控制（withTimeout）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-043：笔试：手写用例级超时控制（withTimeout）
**答**：
- 需求：`runWithTimeout(fn, ms)` 超过 ms 抛 TimeoutError 并标记超时；原任务最终失败/成功都不能影响已返回的结果（不能悬挂、不能 unhandled rejection）。
- 核心：Promise.race([task, timeoutPromise])；注意 race 不取消原任务——原任务后到的 rejection 必须被 catch 吞掉，否则进程崩溃（本题的真正考察点）。
- 边界：fn 同步抛错也要走统一路径（用 Promise.resolve().then 包裹）；超时错误要带上用例名与耗时，便于报告归因。

```javascript
class TimeoutError extends Error {
  constructor(name, ms) { super(`${name} timed out after ${ms}ms`); this.name = 'TimeoutError'; this.timedOut = true; }
}

function runWithTimeout(fn, ms, name = 'case') {
  let settled = false;
  const timer = setTimeout(() => { settled = true; }, ms);

  const task = Promise.resolve().then(fn).finally(() => clearTimeout(timer));
  const timeoutP = new Promise((_, reject) => {
    setTimeout(() => reject(new TimeoutError(name, ms)), ms);
  });

  // 原任务后到的失败要静默吞掉（此时超时已 reject，race 已结束）
  task.catch((e) => { if (!settled) throw e; });  // settled 时吞掉，防 unhandled

  return Promise.race([task, timeoutP]);
}

// ---- 用法 ----
// 1) 正常完成
await runWithTimeout(async () => 1 + 1, 1000, 'fast');   // 2

// 2) 超时
try {
  await runWithTimeout(() => new Promise(() => {}), 100, 'stuck');
} catch (e) {
  console.log(e.message); // stuck timed out after 100ms
}

// 3) 超时后原任务又失败 —— 不能产生 unhandled rejection
await runWithTimeout(async () => {
  await new Promise((r) => setTimeout(r, 200));
  throw new Error('late boom');
}, 50, 'late');
console.log('main continues');
await new Promise((r) => setTimeout(r, 300)); // 观察窗口：无 unhandled 报错输出
```
**评分点**：
- Promise.race 实现超时是基础分；「吞掉迟到 rejection」是拉开差距的关键点。
- 同步抛错也被捕获（Promise.resolve().then(fn) 包裹）。
- 超时错误带用例名与时长（可归因）。
- 能说出真正取消需要 AbortSignal（race 只是「不再等待」）。
