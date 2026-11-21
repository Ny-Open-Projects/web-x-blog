---
title: [TST-081] 笔试：fake timers + userEvent 测试防抖搜索按钮
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-081：笔试：fake timers + userEvent 测试防抖搜索按钮
**答**：
- 需求：搜索框输入后 300ms 防抖触发请求；测试要验证「连续输入只发一次请求、收到最后输入」。难点：userEvent 与 fake timers 共存需要 `userEvent.setup({ advanceTimers })`，否则 userEvent 内部等待会卡死。
- 要点：setup 传 vi.advanceTimersByTime 让 userEvent 的延迟也走虚拟时钟；输入后手动 advanceTimersByTime(300) 触发防抖回调。
- 边界：用例结束 useRealTimers；断言请求参数是最后一次输入值；请求被防抖合并只调 1 次。

```jsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi, afterEach } from 'vitest';
import { api } from './api';
import SearchBox from './SearchBox';

vi.mock('./api', () => ({ api: { search: vi.fn().mockResolvedValue([]) } }));
afterEach(() => { vi.useRealTimers(); vi.mocked(api.search).mockReset(); });

describe('SearchBox 防抖', () => {
  it('连续输入 300ms 后只发一次请求，参数为最后输入', async () => {
    vi.useFakeTimers();
    const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime }); // 关键：桥接
    render(<SearchBox />);

    const input = screen.getByRole('searchbox');
    await user.type(input, 'iphone');            // 逐字符输入（虚拟时钟下快速完成）
    expect(api.search).not.toHaveBeenCalled();   // 300ms 内不触发

    await act(async () => { vi.advanceTimersByTime(300); });  // 推进触发防抖
    await waitFor(() => expect(api.search).toHaveBeenCalledTimes(1));
    expect(api.search).toHaveBeenLastCalledWith('iphone');
  });
});

import { act } from '@testing-library/react';   // act 别忘了引入
```
**评分点**：
- `userEvent.setup({ advanceTimers })` 桥接 fake timers——没这一步测试会挂起，是本题核心考点。
- 断言「未到时间不触发」与「到时间只触发一次、参数为最后值」。
- act 包裹时钟推进、waitFor 等待异步请求落地。
- afterEach 恢复真实时钟。
