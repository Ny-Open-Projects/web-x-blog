---
title: [TST-048] 笔试：为节流函数写单测（fake timers 推进时钟）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-048：笔试：为节流函数写单测（fake timers 推进时钟）
**答**：
- 需求：`throttle(fn, wait)` 在 wait 窗口内至多执行一次，且窗口结束后的首次调用要触发（尾沿保证）；测试用 fake timers 推进，不真等。
- 设计要点：throttle 与 debounce 不同——首调立即执行（leading），窗口内合并；测试序列要覆盖「窗口内多次调用只执行 1 次」与「窗口结束后再调执行第 2 次」。
- 边界：afterEach 恢复真实 timers；若实现带 trailing 选项，窗口内最后一次调用参数要在尾沿补发（测试断言收到的是最后参数）。

```javascript
import { describe, it, expect, vi, afterEach } from 'vitest';
import { throttle } from './throttle';

afterEach(() => { vi.useRealTimers(); vi.restoreAllMocks(); });

describe('throttle', () => {
  it('wait 窗口内至多执行一次（首沿立即）', () => {
    vi.useFakeTimers();
    const fn = vi.fn();
    const t = throttle(fn, 200);

    t('a');                       // t=0 立即执行
    expect(fn).toHaveBeenCalledTimes(1);
    t('b'); t('c');               // 窗口内合并
    vi.advanceTimersByTime(199);
    t('d');
    expect(fn).toHaveBeenCalledTimes(1);
    expect(fn).toHaveBeenLastCalledWith('a');
  });

  it('窗口结束后再调用触发第二次，且尾沿补发最后参数', () => {
    vi.useFakeTimers();
    const fn = vi.fn();
    const t = throttle(fn, 200);

    t('a'); t('b'); t('c');       // 窗口内压入
    vi.advanceTimersByTime(200);  // 窗口结束，尾沿触发
    expect(fn).toHaveBeenCalledTimes(2);
    expect(fn).toHaveBeenLastCalledWith('c'); // trailing 补发最后参数
  });
});
```
**评分点**：
- leading 与 trailing 两个语义都被测试覆盖。
- fake timers 推进用 199/200 这类精确边界而不是 sleep。
- 断言「最后收到的参数」验证合并逻辑而不是只数次数。
- afterEach 恢复真实 timers。
