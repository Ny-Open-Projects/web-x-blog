---
title: [JS-396] 笔试：手写可中断 sleep 与可暂停序列
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-396：笔试：手写可中断 sleep

**答**：实现：① `sleep(ms, signal)`：可被 AbortSignal 中断，中断时 reject AbortError；② `sleep(ms)` 无信号时正常计时；③ 定时器在提前中断时清理；④ `pauseableInterval(fn, ms, signal)`：可中断的循环间隔（上一轮完成后才开始计时下一轮，避免重入）。写出实现。

```javascript
function sleep(ms, signal) {
  return new Promise((resolve, reject) => {
    if (signal?.aborted) return reject(new DOMException('Aborted', 'AbortError'));
    const t = setTimeout(() => { off(); resolve(); }, ms);
    const onAbort = () => { clearTimeout(t); reject(new DOMException('Aborted', 'AbortError')); };
    const off = () => signal?.removeEventListener('abort', onAbort);
    signal?.addEventListener('abort', onAbort, { once: true });
  });
}

async function pauseableInterval(fn, ms, signal) {
  while (!signal?.aborted) {
    try {
      await fn();                       // 执行完才计时, 防重入
      await sleep(ms, signal);
    } catch (e) {
      if (e.name === 'AbortError') return;
      await sleep(ms, signal);          // 出错也按间隔继续(或按需退出)
    }
  }
}

// 用法
const ctrl = new AbortController();
pauseableInterval(() => syncData(), 5000, ctrl.signal);
// 组件卸载: ctrl.abort() → 循环在下一个 sleep 中断退出
```

**评分点**：
- abort 监听与定时器双向清理（谁先发生都正确收尾）
- 已 aborted 的 signal 快速失败（先检查）
- pauseableInterval「执行完才计时」防重入（与 setInterval 的本质差异）
- AbortError 语义化退出循环
