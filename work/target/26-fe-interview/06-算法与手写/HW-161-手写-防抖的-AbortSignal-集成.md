---
title: [HW-161] 手写带 AbortSignal 的防抖——debounce 返回的 Promise 可取消，组件卸载联动
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-161：手写带 AbortSignal 的防抖——debounce 返回的 Promise 可取消，组件卸载联动
**答**：现代防抖形态：debounce(fn, wait, {signal}) 返回 Promise，signal.abort() 取消待执行（Promise reject AbortError）；signal 由组件卸载/请求管理器传入（PER-109 联动）——防抖定时器与外部取消信号统一。

```javascript
function debounceSignal(fn, wait, { signal } = {}) {
  let timer = null;
  return (...args) => new Promise((resolve, reject) => {
    clearTimeout(timer);
    if (signal?.aborted) return reject(new DOMException('aborted', 'AbortError'));
    const onAbort = () => {
      clearTimeout(timer);
      reject(new DOMException('aborted', 'AbortError'));
    };
    signal?.addEventListener('abort', onAbort, { once: true });
    timer = setTimeout(() => {
      signal?.removeEventListener('abort', onAbort);
      try { resolve(fn(...args)); } catch (e) { reject(e); }
    }, wait);
  });
}
// 用法：组件卸载联动（HW-154 的 signal）
// const ctrl = new AbortController(); // unmount: ctrl.abort()
// input.oninput = (e) => debounceSignal(search, 300, { signal: ctrl.signal })(e.target.value)
//   .then(render).catch((err) => { if (err.name !== 'AbortError') throw err; });   // 取消静默
// 语义：防抖等待期间的取消（不只是执行中的取消）—— 输入→卸载的竞态窗口也能精确取消
```

**评分点**：
- 返回 Promise + signal 取消的集成（等待期即可取消，不只执行期）。
- AbortError 与真错误分流（调用方静默取消）。
- once: true 的监听清理（不泄漏）。
- 与卸载防护（HW-154）、请求管理（HW-109）的统一信号语义。
