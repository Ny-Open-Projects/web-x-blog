---
title: [TST-142] 笔试：为轮询 hook 写测试（fake timers + 页签隐藏暂停 + 立即首拉）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-142：笔试：为轮询 hook 写测试（fake timers + 页签隐藏暂停 + 立即首拉）
**答**：
- 场景：`usePolling(fn, interval)`——挂载立即请求一次，之后每 interval 轮询；`document.hidden` 时暂停、恢复时立即补拉；卸载停止。测试难点是「暂停/恢复」要配合 visibilitychange 事件与 fake timers。
- 技巧：fake timers 快进轮询（`advanceTimersByTimeAsync` 而非同步版，要等 promise 链跑完）；visibility 模拟直接 dispatchEvent 一个 `visibilitychange` 事件并改 `document.hidden`（jsdom 里该属性只读，需 Object.defineProperty）。
- 边界：fn 抛错不中断轮询（下次照常）；卸载后不再触发（清 timer）；恢复时「立即补拉」不等下个 interval。

```jsx
import { renderHook, act } from '@testing-library/react';
import { vi } from 'vitest';
import { usePolling } from './usePolling';

function setHidden(hidden) {
  Object.defineProperty(document, 'hidden', { value: hidden, configurable: true });
  document.dispatchEvent(new Event('visibilitychange'));
}

beforeEach(() => vi.useFakeTimers());
afterEach(() => { vi.useRealTimers(); setHidden(false); });

test('挂载立即拉取，按 interval 轮询', async () => {
  const fn = vi.fn().mockResolvedValue({ n: 1 });
  renderHook(() => usePolling(fn, 5000));

  expect(fn).toHaveBeenCalledTimes(1);            // 立即首拉
  await act(() => vi.advanceTimersByTimeAsync(5000));
  expect(fn).toHaveBeenCalledTimes(2);
  await act(() => vi.advanceTimersByTimeAsync(5000));
  expect(fn).toHaveBeenCalledTimes(3);
});

test('页签隐藏暂停，恢复时立即补拉', async () => {
  const fn = vi.fn().mockResolvedValue({});
  renderHook(() => usePolling(fn, 5000));

  act(() => setHidden(true));                     // 隐藏
  await act(() => vi.advanceTimersByTimeAsync(30000));
  expect(fn).toHaveBeenCalledTimes(1);            // 暂停：不轮询

  act(() => setHidden(false));                    // 恢复
  expect(fn).toHaveBeenCalledTimes(2);            // 立即补拉，不等 interval
});

test('fn 报错不影响后续轮询，卸载后停止', async () => {
  const fn = vi.fn()
    .mockRejectedValueOnce(new Error('net'))
    .mockResolvedValue({});
  const { unmount } = renderHook(() => usePolling(fn, 1000));
  await act(() => vi.advanceTimersByTimeAsync(1000));  // 第一次报错
  await act(() => vi.advanceTimersByTimeAsync(1000));  // 仍继续
  expect(fn).toHaveBeenCalledTimes(3);

  unmount();
  await act(() => vi.advanceTimersByTimeAsync(10000));
  expect(fn).toHaveBeenCalledTimes(3);                 // 卸载后不再调用
});
```

**评分点**：
1. advanceTimersByTimeAsync 处理异步轮询（同步版 promise 未决 = 假绿）。
2. document.hidden 只读属性的 defineProperty 处理。
3. 三条核心行为：立即首拉、隐藏暂停 + 恢复补拉、报错不中断。
4. 卸载清理断言（轮询泄漏是线上常见问题）。
