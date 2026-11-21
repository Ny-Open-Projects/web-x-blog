---
title: [JS-301] 笔试：手写可取消的异步任务
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-301：笔试：可取消的异步任务

**题目**：实现 `cancellable(taskFn)`：返回 { promise, cancel }；cancel 后任务尽快终止（协作式：任务内部需检查 signal）；未开始的队列任务直接 reject('cancelled')；取消不视为异常路径（promise 状态区分 resolved/cancelled）。

**答**：
```javascript
function cancellable(taskFn) {
  const ctl = new AbortController();
  let cancelled = false;
  const promise = new Promise((resolve, reject) => {
    taskFn(ctl.signal).then(
      (v) => cancelled ? resolve({ status: 'cancelled' }) : resolve({ status: 'done', value: v }),
      (e) => {
        if (cancelled || e.name === 'AbortError') resolve({ status: 'cancelled' }); // 取消不是 reject
        else reject(e);
      }
    );
  });
  return {
    promise,
    cancel() {
      cancelled = true;
      ctl.abort(); // 通知任务尽快停止（fetch/内部检查点）
    },
  };
}

// 任务内部协作：检查 signal
const job = cancellable(async (signal) => {
  for (let i = 0; i < 5; i++) {
    if (signal.aborted) return 'stopped-at-' + i;
    await sleep(100);
  }
  return 'completed';
});
job.cancel();
const r = await job.promise; // { status: 'cancelled' }
```

**评分点**：
- AbortController 作为取消信号的标准载体
- 取消态与异常态区分（resolve 而非 reject）——语义判分
- 任务内部检查 signal 的协作式取消（不可能强制杀异步任务，需说明）
- AbortError 与自定义 cancelled 的归一处理
