---
title: [HW-049] 手写 Promise 超时取消
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-049：手写 Promise 超时取消

**答**：
- 评分点：与 HW-010 的区别——这里要做**可取消包装器**：cancel 后 Promise 整体 reject 一个「已取消」标记对象，底层结果再回来也**不能 resolve**（状态不可逆天然保证，但要在 cancel 时主动 reject 才能让 await 立刻退出）；被取消时底层任务要能联动中止（AbortController / xhr.abort）；配合 timeout 自动 cancel 组合成「超时即取消」；能说清「取消不是终止已执行的同步逻辑，而是让上层不再关心 + 通知底层中止」。

```javascript
// ===== 5 分钟速写版 =====
function makeCancelable(promise) {
  let canceled = false;
  const wrapped = new Promise((resolve, reject) => {
    promise.then(
      v => canceled ? reject({ isCanceled: true }) : resolve(v),
      e => canceled ? reject({ isCanceled: true, cause: e }) : reject(e)
    );
  });
  return {
    promise: wrapped,
    cancel() { canceled = true; } // 之后落定的结果一律转成「已取消」错误
  };
}
// 用法：const t = makeCancelable(fetchData()); t.cancel();

// ===== 标准完整版（含边界处理：真取消 + 超时自动取消）=====
function makeCancelablePro(task, { signal } = {}) {
  if (typeof task !== 'function') throw new TypeError('task must be a function');
  let canceled = false;
  let abortFn = null;
  const wrapped = new Promise((resolve, reject) => {
    if (signal && signal.aborted) {
      return reject({ isCanceled: true, reason: signal.reason });
    }
    signal && signal.addEventListener('abort', () => {
      canceled = true;
      abortFn && abortFn();              // 联动底层中止
      reject({ isCanceled: true, reason: signal.reason });
    }, { once: true });
    // task 可自行登记中止函数，cancel 时被调用
    const registerAbort = fn => { abortFn = fn; };
    task(registerAbort).then(
      v => canceled ? reject({ isCanceled: true }) : resolve(v),
      e => canceled ? reject({ isCanceled: true, cause: e }) : reject(e)
    );
  });
  return {
    promise: wrapped,
    cancel() { canceled = true; abortFn && abortFn(); }
  };
}
// 超时自动取消组合（推荐写法）：
function fetchWithAutoCancel(url, ms) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(new Error('timeout')), ms);
  const { promise } = makeCancelablePro(
    () => fetch(url, { signal: controller.signal }).then(r => r.json()),
    { signal: controller.signal }
  );
  return promise.finally(() => clearTimeout(timer));
  // 超时路径：abort 触发 → makeCancelablePro 内的 abort 监听把 wrapped reject 成
  // { isCanceled: true, reason }，await 立即退出，无需再手动 cancel。
}
// 追问：cancel 能终止 fetch 吗 —— fetch 传入 signal 后 abort 会真正断开连接；
// 纯 CPU 任务无法取消，只能丢弃结果（协作式取消思想）。
```

---
