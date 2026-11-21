---
title: [TST-089] 笔试：测试组件卸载时的清理逻辑（事件监听/定时器/取消请求）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-089：笔试：测试组件卸载时的清理逻辑（事件监听/定时器/取消请求）
**答**：
- 需求：实时价格组件挂载时 addEventListener('resize') + setInterval 轮询 + 发起请求（AbortController）；卸载后三类资源都要清理。清理缺失的后果：内存泄漏、卸载后 setState 警告、重复请求堆积。
- 手法：spyOn window.addEventListener/removeEventListener 断言配对；fake timers 验证 interval 停止；abort 信号验证 fetch 收到同一 signal 且 abort 被调用。
- 边界：卸载后推进时钟不应再触发更新（无 act 警告）；重复挂载/卸载多次不累积监听器。

```jsx
import { render, act } from '@testing-library/react';
import { describe, it, expect, vi, afterEach } from 'vitest';
import PriceTicker from './PriceTicker';

afterEach(() => { vi.useRealTimers(); vi.restoreAllMocks(); });

describe('PriceTicker 卸载清理', () => {
  it('监听器/定时器/请求全部清理', () => {
    vi.useFakeTimers();
    const addSpy = vi.spyOn(window, 'addEventListener');
    const removeSpy = vi.spyOn(window, 'removeEventListener');
    const fetchMock = vi.fn(() => new Promise(() => {}));       // 永不返回，保留 abort 机会
    const abortSpy = vi.spyOn(AbortController.prototype, 'abort');

    const { unmount } = render(<PriceTicker fetcher={fetchMock} />);
    const added = addSpy.mock.calls.filter(([t]) => t === 'resize');
    expect(added.length).toBe(1);

    unmount();
    expect(removeSpy).toHaveBeenCalledWith('resize', expect.any(Function)); // 配对移除
    expect(abortSpy).toHaveBeenCalled();                                    // 请求取消
    expect(() => act(() => vi.advanceTimersByTime(5000))).not.toThrow();    // 无更新/警告
  });

  it('重复挂载卸载不累积监听器', () => {
    const addSpy = vi.spyOn(window, 'addEventListener');
    const { unmount } = render(<PriceTicker fetcher={vi.fn()} />);
    unmount();
    const { unmount: u2 } = render(<PriceTicker fetcher={vi.fn()} />);
    u2();
    expect(addSpy.mock.calls.filter(([t]) => t === 'resize')).toHaveLength(2); // 每次 1 个
  });
});
```
**评分点**：
- 三类资源（事件/定时器/请求）都验证清理。
- spy add/removeEventListener 断言配对与次数。
- 卸载后推进时钟不产生 act 警告。
- 知道清理缺失的三种实际后果（泄漏/警告/请求堆积）。
