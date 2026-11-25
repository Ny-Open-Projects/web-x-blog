---
title: [HW-085] 手写 Promise 顺序执行器——串行链 + 失败中断/跳过策略 + 进度回调
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-085：手写 Promise 顺序执行器——串行链 + 失败中断/跳过策略 + 进度回调
**答**：串行执行 N 个异步任务，支持三种失败策略：`fail-fast`（中止返回已完成结果）、`skip`（跳过继续）、`collect`（全部执行返回 errors 数组）。进度回调 onProgress(done, total)。与 HW-028（纯串行）的差异在于策略与进度。

```javascript
function runSequential(tasks, { strategy = 'fail-fast', onProgress } = {}) {
  const results = [], errors = [];
  let done = 0;
  return new Promise((resolve) => {
    const next = (i) => {
      if (i >= tasks.length) {                          // 全部完成
        resolve({ results, errors, completed: done });
        return;
      }
      Promise.resolve()
        .then(() => tasks[i](i))                        // 传索引
        .then((v) => { results[i] = v; })
        .catch((e) => {
          errors.push({ index: i, error: e });
          if (strategy === 'fail-fast') {               // 中止：结果到 i 为止
            resolve({ results, errors, completed: done, abortedAt: i });
            return;
          }
          // skip / collect：继续
        })
        .finally(() => {
          done++;
          onProgress?.(done, tasks.length);
          next(i + 1);
        });
    };
    next(0);
  });
}
// 用法：分 10 片上传，一片失败就中止（fail-fast）
const up = await runSequential(chunks.map((c) => () => upload(c)), {
  strategy: 'fail-fast',
  onProgress: (d, total) => bar.set(d / total),
});
// collect 模式：日志批量上报，失败收集但继续
```

**评分点**：
- 递归链串行正确（不并行）；任务索引传入。
- 三种失败策略语义清晰，fail-fast 返回 abortedAt。
- onProgress 在 finally 里调用（成败都计进度）。
- resolve 唯一性（fail-fast 分支 resolve 后不再递归）。
