---
title: [FRP-184] 手写 useDebounceFn：VueUse 风格的防抖 composable 怎么写？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-184：手写 useDebounceFn：VueUse 风格的防抖 composable 怎么写？

**答**：
- 防抖：**重启计时器**——每次调用清除上一次的 timer，wait 内无新调用才真正执行（适合搜索输入、resize）。
- VueUse 风格的完整度：返回的函数带 `cancel()`（取消待执行）与 `flush()`（立即执行待执行）；pending 状态可判断。
- 生命周期集成：`tryOnScopeDispose` —— 在组件 setup 中使用时，组件卸载自动 cancel，防止卸载后回调触发。
- leading 选项：第一次调用立即执行、后续 wait 内忽略（防抖的"立即触发"变体）。

```javascript
// 简化实现，帮助理解 useDebounceFn
import { getCurrentScope, onScopeDispose } from 'vue';

function useDebounceFn(fn, wait = 200, options = {}) {
  let timer = null;
  let pendingArgs = null;
  const { leading = false } = options;   // 首次是否立即执行
  let canLead = true;

  function invoke(args) {
    pendingArgs = null;
    fn(...args);
  }

  function debounced(...args) {
    pendingArgs = args;
    if (leading && canLead) {
      canLead = false;
      invoke(args);                       // leading：第一次立即执行
      return;
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      canLead = true;                     // 冷却结束，允许下次 leading
      invoke(pendingArgs);                // 执行最后一次的参数
    }, wait);
  }

  debounced.cancel = () => {              // 取消待执行
    clearTimeout(timer);
    timer = null;
    pendingArgs = null;
    canLead = true;
  };
  debounced.flush = () => {               // 立即执行待执行
    if (timer && pendingArgs) {
      clearTimeout(timer);
      timer = null;
      invoke(pendingArgs);
    }
  };
  debounced.isPending = () => timer != null;

  // 生命周期集成：组件卸载自动 cancel（VueUse 的 tryOnScopeDispose）
  if (getCurrentScope()) onScopeDispose(debounced.cancel);

  return debounced;
}

// 用法：
// const search = useDebounceFn(async (q) => {
//   results.value = await api(q);
// }, 300);
// <input @input="e => search(e.target.value)" />
// onBeforeUnmount 里不需要手动清理 —— scope 自动 cancel

// 与 useThrottleFn 的核心区别：
// 防抖 = "等你停下来"（重启计时器），节流 = "按固定节奏放行"（时间闸门）
```
