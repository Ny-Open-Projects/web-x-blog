---
title: [TST-069] 笔试：测试带防抖与清理逻辑的自定义 hook（useDebounce）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-069：笔试：测试带防抖与清理逻辑的自定义 hook（useDebounce）
**答**：
- 需求：`useDebounce(value, delay)` 输入连续变化只在停止变化 delay 后输出最新值；组件卸载时清理定时器（防内存泄漏与卸载后 setState）。
- 要点：fake timers + renderHook 组合——vi.useFakeTimers 后用 act(() => vi.advanceTimersByTime(delay)) 推进；卸载清理用 rerender 到 null 或 unmount + 验证 clearTimeout。
- 边界：值连续变化要「重置」倒计时；卸载后推进时间不应再输出（无 act 警告）。

```jsx
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { useDebounce } from './useDebounce';

afterEach(() => { vi.useRealTimers(); vi.restoreAllMocks(); });

describe('useDebounce', () => {
  it('连续变化只在停止后输出最后值', () => {
    vi.useFakeTimers();
    const { result, rerender } = renderHook(({ v }) => useDebounce(v, 300), { initialProps: { v: 'a' } });

    expect(result.current).toBe('a');                 // 初始直通
    rerender({ v: 'ab' });
    act(() => vi.advanceTimersByTime(100));
    rerender({ v: 'abc' });                            // 途中变化重置计时
    act(() => vi.advanceTimersByTime(299));
    expect(result.current).toBe('a');                  // 还没到 300
    act(() => vi.advanceTimersByTime(1));
    expect(result.current).toBe('abc');                // 300ms 到，输出最后值
  });

  it('卸载时清理定时器', () => {
    vi.useFakeTimers();
    const clearSpy = vi.spyOn(globalThis, 'clearTimeout');
    const { unmount, rerender } = renderHook(({ v }) => useDebounce(v, 300), { initialProps: { v: 'x' } });
    rerender({ v: 'xy' });
    unmount();
    expect(clearSpy).toHaveBeenCalled();               // 卸载清理
    act(() => vi.advanceTimersByTime(500));            // 推进也不应报错/更新
  });
});
```
**评分点**：
- fake timers 与 renderHook 组合、act 包裹 advanceTimersByTime。
- 「途中变化重置倒计时」分支被验证。
- 卸载清理断言（clearTimeout 调用 + 卸载后无更新）。
- 能说出卸载后 setState 会同时引发 React 警告与内存泄漏。
