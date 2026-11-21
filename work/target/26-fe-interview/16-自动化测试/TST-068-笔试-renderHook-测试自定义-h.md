---
title: [TST-068] 笔试：用 renderHook 测试自定义 hook（useCounter）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-068：笔试：用 renderHook 测试自定义 hook（useCounter）
**答**：
- 需求：测试 `useCounter(initial)` 返回 { count, inc, dec, reset }：初始值、inc/dec 连续调用、reset 回初始值、边界（dec 不低于 min）。
- 要点：`renderHook(() => useCounter(3))` 返回 result.current——每次取值都是最新渲染快照，断言前必须重新读 current（旧引用比较会误判）；act 包裹触发更新的调用（RTL renderHook 内的 act）。
- 边界：hook 依赖 props 时用 initialProps + rerender 传新 props。

```jsx
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('初始值为传入值', () => {
    const { result } = renderHook(() => useCounter(3));
    expect(result.current.count).toBe(3);
  });

  it('inc/dec 更新计数', () => {
    const { result } = renderHook(() => useCounter(0));
    act(() => result.current.inc());        // act 包裹触发更新
    act(() => result.current.inc());
    act(() => result.current.dec());
    expect(result.current.count).toBe(1);   // 0+1+1-1
  });

  it('reset 回到初始值', () => {
    const { result } = renderHook(() => useCounter(5));
    act(() => result.current.inc());
    act(() => result.current.reset());
    expect(result.current.count).toBe(5);
  });

  it('低于 min 时不再下降', () => {
    const { result } = renderHook(() => useCounter(0, { min: 0 }));
    act(() => result.current.dec());
    expect(result.current.count).toBe(0);   // 边界保护
  });

  it('initialProps 变化时跟随 props', () => {
    const { result, rerender } = renderHook(({ init }) => useCounter(init), { initialProps: { init: 1 } });
    rerender({ init: 9 });
    expect(result.current.count).toBe(9);
  });
});
```
**评分点**：
- renderHook + result.current 快照语义（每次断言读最新值）。
- act 包裹所有触发更新的调用。
- 边界分支（min 保护）与 props 变化（initialProps/rerender）都覆盖。
- 能说出 hook 测试的替代思路：通过消费该 hook 的组件测行为，更贴近真实使用。
