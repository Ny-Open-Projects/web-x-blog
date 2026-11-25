---
title: [V3-532] 笔试：手写 useDebounceFn / useThrottleFn（composable 形态）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## V3-532：笔试：手写 useDebounceFn / useThrottleFn

**答**：以 composable 形态实现：① `useDebounceFn(fn, ms, { leading })`：返回包装函数 + 组件卸载自动 cancel（不残留定时器）；② `useThrottleFn(fn, ms, { trailing })`：同上；③ 两者支持手动 cancel/flush；④ 卸载清理用 tryOnScopeDispose（在 scope 内才注册）；⑤ flush 在 pagehide 语义（Vue 环境用 scope dispose 替代）。写出实现。

```javascript
import { getCurrentScope, onScopeDispose } from 'vue';

function tryOnScopeDispose(fn) {
  if (getCurrentScope()) { onScopeDispose(fn); return true; }
  return false;
}

export function useDebounceFn(fn, ms = 200, { leading = false } = {}) {
  let timer = null, firedLeading = false;
  const wrapped = (...args) => {
    if (leading && !firedLeading && !timer) { fn(...args); firedLeading = true; }
    clearTimeout(timer);
    timer = setTimeout(() => { timer = null; firedLeading = false; fn(...args); }, ms);
  };
  wrapped.cancel = () => { clearTimeout(timer); timer = null; };
  wrapped.flush = (...args) => { wrapped.cancel(); fn(...args); };
  tryOnScopeDispose(() => wrapped.cancel());   // 组件卸载自动清理
  return wrapped;
}

export function useThrottleFn(fn, ms = 200, { trailing = true } = {}) {
  let last = 0, timer = null, pendingArgs = null;
  const wrapped = (...args) => {
    const now = Date.now();
    const remain = ms - (now - last);
    pendingArgs = args;
    if (remain <= 0) { last = now; fn(...args); pendingArgs = null; }
    else if (trailing && !timer)
      timer = setTimeout(() => { timer = null; last = Date.now(); fn(...pendingArgs); pendingArgs = null; }, remain);
  };
  wrapped.cancel = () => { clearTimeout(timer); timer = null; pendingArgs = null; };
  tryOnScopeDispose(() => wrapped.cancel());
  return wrapped;
}
```

**评分点**：
- tryOnScopeDispose 的条件注册（非组件环境不崩）
- leading/trailing 选项语义
- cancel/flush API 完整性
- 卸载自动清理防定时器泄漏（composable 特有关注点）
