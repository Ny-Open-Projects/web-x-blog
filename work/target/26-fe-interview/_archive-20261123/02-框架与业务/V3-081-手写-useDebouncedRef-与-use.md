---
title: [V3-081] 手写 useDebouncedRef 与 useThrottledRef？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-081：手写 useDebouncedRef 与 useThrottledRef？
**答**：
- 都基于 customRef 实现：在 get 里正常收集依赖，在 set 里按策略延迟同步。
- useDebouncedRef：set 后 delay 内没有新写入才真正更新，适合搜索输入。
- useThrottledRef：首次写入立即生效，之后 gap 时间内的写入只保留最后一次，适合滚动/鼠标等高频事件。
- 与 V3-013 的防抖输入不同，这里是通用 ref 工具，可在任何数据源上复用。

```typescript
// composables/useCustomRefs.ts
import { customRef, type Ref } from "vue";

export function useDebouncedRef<T>(initial: T, delay = 300): Ref<T> {
  let value = initial;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let trackFn: () => void;
  let triggerFn: () => void;

  return customRef((track, trigger) => {
    trackFn = track;
    triggerFn = trigger;
    return {
      get() {
        track();
        return value;
      },
      set(newValue: T) {
        clearTimeout(timer);
        timer = setTimeout(() => {
          value = newValue;
          triggerFn(); // 延迟后真正触发更新
        }, delay);
      },
    };
  });
}

export function useThrottledRef<T>(initial: T, gap = 200): Ref<T> {
  let value = initial;
  let pending: T | undefined;
  let lastTime = 0;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let trackFn: () => void;
  let triggerFn: () => void;

  function flush() {
    if (pending === undefined) return;
    value = pending;
    pending = undefined;
    lastTime = Date.now();
    triggerFn();
  }

  return customRef((track, trigger) => {
    trackFn = track;
    triggerFn = trigger;
    return {
      get() {
        track();
        return value;
      },
      set(newValue: T) {
        pending = newValue;
        const rest = gap - (Date.now() - lastTime);
        if (rest <= 0) {
          flush(); // 间隔已到，立即生效
        } else {
          clearTimeout(timer);
          timer = setTimeout(flush, rest); // 间隔内只保留最后一次写入
        }
      },
    };
  });
}
```
