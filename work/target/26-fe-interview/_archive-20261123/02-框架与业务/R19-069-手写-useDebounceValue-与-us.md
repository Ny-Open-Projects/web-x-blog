---
title: [R19-069] 手写 useDebounceValue 与 useThrottleValue？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-069：手写 useDebounceValue 与 useThrottleValue？
**答**：
- 值版防抖：value 变化时重置计时器，只输出"静止 delay 后"的值，适合搜索框驱动请求。
- 值版节流：固定窗口内最多更新一次，注意兜底——窗口结束后要补发最后一次值，否则末尾状态丢失。
- 两者都是"在 hook 里订阅输入、定时输出"的模式，副作用全部在 effect 中清理。
- 选型：输入联想用防抖；滚动位置、resize 这类连续值用节流。

```jsx
// useDebounceValue / useThrottleValue —— 值版防抖与节流
import { useEffect, useRef, useState } from 'react';

export function useDebounceValue(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);              // 值变化时重置计时器
  }, [value, delay]);
  return debounced;
}

export function useThrottleValue(value, interval = 300) {
  const [throttled, setThrottled] = useState(value);
  const lastRef = useRef(0);
  const timerRef = useRef(null);
  useEffect(() => {
    const now = Date.now();
    if (now - lastRef.current >= interval) {
      lastRef.current = now;
      setThrottled(value);
    } else if (!timerRef.current) {
      timerRef.current = setTimeout(() => {        // 兜底：窗口结束后补发最后一次
        lastRef.current = Date.now();
        setThrottled(value);
        timerRef.current = null;
      }, interval - (now - lastRef.current));
    }
    return () => clearTimeout(timerRef.current);
  }, [value, interval]);
  return throttled;
}

// const debouncedKeyword = useDebounceValue(keyword, 400);
// useEffect(() => { fetchSuggestions(debouncedKeyword); }, [debouncedKeyword]);
```
