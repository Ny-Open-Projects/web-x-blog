---
title: [TST-148] 笔试：为 window resize 响应式 hook 写测试（断点切换 + 监听清理）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-148：笔试：为 window resize 响应式 hook 写测试（断点切换 + 监听清理）
**答**：
- 场景：`useBreakpoint()` 返回当前断点（sm/md/lg），基于 window.innerWidth + resize 监听（或 matchMedia）。测试核心：① 可控地改变 innerWidth 并派发 resize 事件；② 断点边界值判断（767/768/1023/1024）；③ 卸载时移除监听。
- 手段：jsdom 的 innerWidth 是只读属性，用 `Object.defineProperty(window, 'innerWidth', { value, configurable: true })` 赋值后 `window.dispatchEvent(new Event('resize'))`。hook 若用 rAF/防抖节流resize，fake timers 配合。
- 边界：SSR 环境 window 未定义要返回默认断点（hook 健壮性）；初始值直接从当前 innerWidth 计算（不等第一次 resize）。

```jsx
import { renderHook, act } from '@testing-library/react';
import { useBreakpoint } from './useBreakpoint';

function setWidth(w) {
  Object.defineProperty(window, 'innerWidth', { value: w, configurable: true });
  window.dispatchEvent(new Event('resize'));
}

afterEach(() => setWidth(1024)); // 恢复，防串味

test('断点随窗口宽度切换', () => {
  setWidth(400);
  const { result } = renderHook(() => useBreakpoint());
  expect(result.current).toBe('sm');

  act(() => setWidth(768));
  expect(result.current).toBe('md');

  act(() => setWidth(1024));
  expect(result.current).toBe('lg');

  act(() => setWidth(1023));       // 边界：1023 仍是 md
  expect(result.current).toBe('md');
});

test('初始值取自当前宽度，无需先 resize', () => {
  setWidth(1400);
  const { result } = renderHook(() => useBreakpoint());
  expect(result.current).toBe('lg');
});

test('卸载后移除 resize 监听', () => {
  const spy = vi.spyOn(window, 'removeEventListener');
  const { unmount } = renderHook(() => useBreakpoint());
  unmount();
  expect(spy).toHaveBeenCalledWith('resize', expect.any(Function));
  // 或：记录 handleResize 引用，断言窗口变化后 hook 状态不再更新
});
```

**评分点**：
1. defineProperty + dispatchEvent 的 resize 模拟（jsdom 正确姿势）。
2. 边界值覆盖：768/1023/1024 临界判断。
3. 初始值来自当前宽度（不依赖人为先 resize 一次）。
4. 监听移除断言（泄漏检查）+ 用例间宽度恢复。
