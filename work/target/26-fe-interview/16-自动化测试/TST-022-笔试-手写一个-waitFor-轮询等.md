---
title: [TST-022] 笔试：手写一个 waitFor 轮询等待函数
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 笔试题
---

## TST-022：笔试：手写一个 waitFor 轮询等待函数
**答**：
- 需求：实现 `waitFor(cond, { interval, timeout })`，条件函数为真则 resolve，超时则 reject 并带最后错误；条件抛错不应提前终止（下一轮再试），除非超时。
- 核心：setInterval 轮询 + 单独的 setTimeout 计时；清理要同时清 interval 和 timeout（防泄漏）。
- 边界：cond 返回 Promise 时需 await；超时后用最后一次异常作为 reject 原因（比 generic timeout 信息量大）；interval=0 时也应有最小 tick 间隔避免死循环占满 CPU。

```javascript
function waitFor(cond, { interval = 50, timeout = 5000 } = {}) {
  return new Promise((resolve, reject) => {
    let lastErr = null;
    const timer = setTimeout(() => {
      clearInterval(poller); clearTimeout(timer);
      reject(new Error(`waitFor timeout (${timeout}ms)`, { cause: lastErr }));
    }, timeout);

    const poller = setInterval(async () => {
      try {
        const ok = await cond();
        if (ok) {
          clearInterval(poller); clearTimeout(timer);
          resolve(ok);
        }
      } catch (e) {
        lastErr = e;            // 条件内部报错先容忍，等超时再暴露
      }
    }, interval);
  });
}

// ---- 用法 ----
let ready = false;
setTimeout(() => { ready = true; }, 120);
await waitFor(() => ready, { interval: 30, timeout: 1000 });

try {
  await waitFor(() => false, { interval: 10, timeout: 100 });
} catch (e) {
  console.log(e.message);       // waitFor timeout (100ms)
}
```
**评分点**：
- interval 轮询 + timeout 双计时器，超时后两个都要清理。
- 条件抛错被容忍并保存为 lastErr，超时 reject 带上 cause。
- 支持 async 条件（await cond()）。
- 能对比 RTL 的 waitFor：真实实现还监听 DOM MutationObserver 做事件驱动等待，轮询只是兜底。
