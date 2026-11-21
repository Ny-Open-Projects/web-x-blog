---
title: [TST-021] 笔试：用 fake timers 测试一个防抖函数
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-021：笔试：用 fake timers 测试一个防抖函数
**答**：
- 需求：`debounce(fn, 300)` 连续调用只执行最后一次；测试不能真等 300ms，要用 `vi.useFakeTimers()` + `vi.advanceTimersByTime` 推进虚拟时间。
- 要点：useFakeTimers 拦截 setTimeout/clearTimeout；每次调用要重置定时器（clear 旧的）；用 vi.fn 观察执行次数。
- 边界：测试结束后 `vi.useRealTimers()` 恢复（放在 afterEach），否则污染其他用例；连续调用间隔不足/超过 delay 两种序列都要覆盖。

```javascript
// src/debounce.test.ts
import { describe, it, expect, vi, afterEach } from 'vitest';
import { debounce } from './debounce';

afterEach(() => {
  vi.useRealTimers();          // 恢复真实时间，防止污染
  vi.restoreAllMocks();
});

describe('debounce', () => {
  it('连续调用只执行最后一次', () => {
    vi.useFakeTimers();
    const fn = vi.fn();
    const d = debounce(fn, 300);

    d();                       // t=0
    vi.advanceTimersByTime(100);
    d();                       // t=100 重置定时器
    vi.advanceTimersByTime(200); // t=300 尚未到 300（距上次 200）
    expect(fn).not.toHaveBeenCalled();

    vi.advanceTimersByTime(100); // t=400，距上次 300ms，触发
    expect(fn).toHaveBeenCalledTimes(1);
  });

  it('间隔超过 delay 的两次调用各执行一次', () => {
    vi.useFakeTimers();
    const fn = vi.fn();
    const d = debounce(fn, 300);
    d();
    vi.advanceTimersByTime(400);
    d();
    vi.advanceTimersByTime(400);
    expect(fn).toHaveBeenCalledTimes(2);
  });
});
```
**评分点**：
- useFakeTimers / advanceTimersByTime / useRealTimers 三件套齐全，afterEach 恢复。
- 「重置定时器」用推进时间再调用模拟，而不是真等。
- 覆盖「连续调用合并」与「间隔足够各执行」两个序列。
- 能说出 fake timers 下 Date.now/setInterval 也被劫持，相关依赖需用 setSystemTime 对齐。
