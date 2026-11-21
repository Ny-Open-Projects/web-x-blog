---
title: [PER-215] 笔试题：手写 scheduler.yield 的降级 polyfill 与 yieldToMain（含优先级说明）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-215：手写 scheduler.yield 的降级 polyfill 与 yieldToMain（含优先级说明）

**题目**：实现 `yieldToMain()`：① 原生 `scheduler.yield` 优先（ continuation 保持用户可见优先级）；② 降级用 `scheduler.postTask('user-visible')` + MessageChannel；③ 最后兜底 `setTimeout(0)`；④ 返回 Promise；⑤ 支持传入 signal 取消等待。

**答**：核心是优先级阶梯——原生 yield 让出后任务仍以 user-visible 优先级续排，不会被渲染任务饿死；postTask 可显式声明优先级；MessageChannel 宏任务比 setTimeout 更早且不受 4ms 下限钳制，是常见的让出手段。

```javascript
const yieldToMain = (signal) => {
  if ('scheduler' in window && 'yield' in scheduler) {
    return scheduler.yield({ signal });            // 原生：continuation 保优先级
  }
  if ('scheduler' in window && 'postTask' in scheduler) {
    return scheduler.postTask(() => {}, { priority: 'user-visible', signal });
  }
  return new Promise((resolve, reject) => {        // MessageChannel 宏任务让出
    const ch = new MessageChannel();
    const onAbort = () => { ch.port1.close(); reject(new DOMException('aborted', 'AbortError')); };
    ch.port1.onmessage = () => { signal?.removeEventListener('abort', onAbort); resolve(); };
    ch.port2.postMessage(null);
    signal?.addEventListener('abort', onAbort, { once: true });
  });
};

// 用法：把 500ms 的重活切成 5 段，每段间让出
async function heavyWork(signal) {
  for (let i = 0; i < 5; i++) {
    doChunk(i);                 // 每段约 100ms 内
    await yieldToMain(signal);  // 让出给渲染与输入事件
  }
}
// 注意：setTimeout(0) 是最低优先级且被 4ms 钳制，仅作最后兜底；
// 过密切片（每片 < 5ms）会让调度成本超过收益。
```

**评分点**：
- 优先级阶梯完整且顺序正确：原生 yield > postTask > MessageChannel/setTimeout。
- 说明"原生 yield 保持 continuation 优先级、防止被饿死"这一关键差异。
- MessageChannel 实现无 4ms 钳制、比 setTimeout 及时。
- 支持 AbortSignal 取消，切片循环可被中断。
