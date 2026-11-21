---
title: [TST-023] 测试里怎么控制「当前时间」？vi.setSystemTime 用在哪？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-023：测试里怎么控制「当前时间」？vi.setSystemTime 用在哪？
**答**：
- 前提：时间相关 API（Date）受 fake timers 控制，`vi.useFakeTimers({ now: ... })` 或 `vi.setSystemTime(date)` 把系统时间钉住。
- 用途：验证「距今 3 天前」「本月末」这类时间分支（订单超时提示、限时活动、单据编号含日期）——不钉时间，用例会在跨天/时区时随机挂。
- 两种注入方式：fake timers 全量劫持（Date/setTimeout/queueMicrotask）；`vi.useFakeTimers({ toFake: ['Date'] })` 只劫持 Date，保留真实定时器，适合只想控时间不想推时钟的场景。
- 配套：断言用 `expect(Date.now())` 前先 setSystemTime；结束时 restore；注意 UTC vs 本地时区（CI 容器常是 UTC）。
- 追问钩子：更彻底的方案是被测代码依赖注入 `now: () => Date.now()`，单测直接传假函数，不依赖 timer 劫持。

```javascript
import { describe, it, expect, vi, afterEach } from 'vitest';
import { isExpired } from './order';

afterEach(() => vi.useRealTimers());

describe('isExpired', () => {
  it('过去的时间点判定为过期', () => {
    vi.useFakeTimers({ now: new Date('2026-06-01T12:00:00Z'), toFake: ['Date'] });
    expect(isExpired(new Date('2026-05-31T00:00:00Z'))).toBe(true);
    expect(isExpired(new Date('2026-06-02T00:00:00Z'))).toBe(false);
  });
});
// 源码侧更好的做法：
// export const isExpired = (t, now = () => Date.now()) => new Date(t) < now();
// 测试里 isExpired(past, () => fixedTs) 不需要 fake timers。
```
