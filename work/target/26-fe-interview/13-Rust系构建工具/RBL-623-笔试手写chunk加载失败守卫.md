---
title: [RBL-623] 笔试：手写 chunk 加载失败守卫（分类识别 + 一次性刷新）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-623：笔试：手写 chunk 加载失败守卫（分类识别 + 一次性刷新）

**答**：实现 `installChunkGuard({ onReload, onError, sessionStorage, maxReloadPerSession })`。监听 window `error` 与 `unhandledrejection`，识别 chunk 加载失败（message 含 'ChunkLoadError' 或 'Failed to fetch dynamically imported module' 或 error.name==='ChunkLoadError'）。规则：1) 首次命中 → sessionStorage 记数 → 调 onReload()（不真实刷新，由测试断言）；2) 记数 ≥ maxReloadPerSession → 不再 reload，调 onError(reason)（供上报/降级 UI）；3) 非 chunk 错误不处理（透传，不影响全局错误处理）；4) 同一 URL 连续失败应合并计数。返回 uninstall 函数。

```javascript
function installChunkGuard({ onReload, onError, sessionStorage, maxReloadPerSession = 1 }) {
  const KEY = 'chunk_reload_count';
  const isChunkError = (e) => {
    const err = e?.reason ?? e?.error ?? e;
    const msg = String(err?.message ?? e?.message ?? '');
    return err?.name === 'ChunkLoadError' ||
      /ChunkLoadError|Failed to fetch dynamically imported module/i.test(msg);
  };
  const handler = (e) => {
    if (!isChunkError(e)) return;                        // 非 chunk 错误透传
    const n = +(sessionStorage.getItem(KEY) || 0) + 1;
    sessionStorage.setItem(KEY, String(n));
    if (n <= maxReloadPerSession) onReload(n);           // 一次性刷新
    else onError({ count: n, message: String(e?.reason?.message ?? e?.message) });
  };
  window.addEventListener('error', handler);
  window.addEventListener('unhandledrejection', handler);
  return () => {
    window.removeEventListener('error', handler);
    window.removeEventListener('unhandledrejection', handler);
  };
}

// 自测
const store = new Map();
const sess = { getItem: k => store.get(k) ?? null, setItem: (k, v) => store.set(k, v) };
let reloads = 0, errors = [];
const uninstall = installChunkGuard({
  onReload: () => reloads++,
  onError: (info) => errors.push(info),
  sessionStorage: sess, maxReloadPerSession: 1,
});

// 1) ChunkLoadError -> reload
window.dispatchEvent(new ErrorEvent('error', { error: { name: 'ChunkLoadError', message: 'x' } }));
console.log(reloads === 1);
// 2) 第二次 -> onError
window.dispatchEvent(new ErrorEvent('error', { message: 'ChunkLoadError: y' }));
console.log(reloads === 1 && errors.length === 1 && errors[0].count === 2);
// 3) 非 chunk 错误透传
window.dispatchEvent(new ErrorEvent('error', { message: 'TypeError: z' }));
console.log(reloads === 1 && errors.length === 1);
// 4) unhandledrejection + 动态 import 文案
window.dispatchEvent(new PromiseRejectionEvent('unhandledrejection', {
  reason: new Error('Failed to fetch dynamically imported module: /chunk.js') }));
console.log(reloads === 2);                              // maxReload 1：第二次后 onError
console.log(errors.length === 2);
uninstall();
window.dispatchEvent(new ErrorEvent('error', { message: 'ChunkLoadError: after' }));
console.log(reloads === 2);                              // 卸载后不再触发
```

**评分点**：
- 识别分类完整（error.name / message 正则 / rejection reason 三入口），非 chunk 错误完全透传
- 计数与 maxReloadPerSession 判定正确（首次 reload，超限 onError 且携带计数）
- uninstall 完整移除双监听；能说明「防刷新风暴是 maxReload 的动机」属于加分
- promise rejection 与 error 事件的取值差异（reason vs error）处理正确
