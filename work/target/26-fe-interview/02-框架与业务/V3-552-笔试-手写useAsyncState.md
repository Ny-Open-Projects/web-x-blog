---
title: [V3-552] 笔试：手写 useAsyncState（异步状态机 composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 数据流]
type: 笔试题
---

## V3-552：笔试：手写 useAsyncState

**答**：实现 `useAsyncState(fn, initial, { immediate, onError, resetOnExecute })`：① 返回 { state, isReady, isLoading, error, execute }——execute 可重复调用；② 竞态守卫：晚完成的旧调用不覆盖新结果（seq 令牌）；③ resetOnExecute：执行前重置为 initial（防旧数据闪现）；④ isReady 语义：首次成功后为 true 且保持（后续失败不清除）；⑤ immediate 首次自动执行。写出实现。

```javascript
export function useAsyncState(fn, initial, {
  immediate = true, onError, resetOnExecute = true,
} = {}) {
  const state = ref(initial);
  const isReady = ref(false);
  const isLoading = ref(false);
  const error = ref(null);
  let seq = 0;

  async function execute(...args) {
    const mySeq = ++seq;
    isLoading.value = true;
    error.value = null;
    if (resetOnExecute) state.value = initial;
    try {
      const v = await fn(...args);
      if (mySeq !== seq) return v;            // 旧调用: 不覆盖新状态
      state.value = v;
      isReady.value = true;                   // 首次成功后恒 true
      return v;
    } catch (e) {
      if (mySeq !== seq) return;
      error.value = e;
      onError?.(e);
      return;                                 // 失败保持 resetOnExecute 前的值语义
    } finally {
      if (mySeq === seq) isLoading.value = false;
    }
  }
  if (immediate) execute();
  return { state, isReady, isLoading, error, execute };
}
// 用法
const { state: user, isLoading, execute: reload } = useAsyncState(
  () => api.user(), null, { immediate: true, onError: (e) => toast(e) });
```

**评分点**：
- seq 竞态守卫（晚到旧结果丢弃）
- isReady「首次成功恒真」语义（区别于 loading）
- resetOnExecute 防旧数据闪现
- finally 中按 seq 条件复位 loading
