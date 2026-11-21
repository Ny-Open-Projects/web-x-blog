---
title: [TST-050] 笔试：手写可注入的 Stub Clock（替代 fake timers 的轻量方案）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-050：笔试：手写可注入的 Stub Clock（替代 fake timers 的轻量方案）
**答**：
- 需求：实现 `createStubClock(startTs)`，提供 `now()`、`advance(ms)`、`set(ts)`；被测代码通过依赖注入用它替代 Date.now，使时间相关测试无需劫持全局 timer。
- 核心：闭包持有 currentTime；now 返回值恒定直到 advance/set；附带 `sleep(ms)` 实现——真实 setTimeout 但按 stub 时间记账（用于演示），生产代码只依赖 now()。
- 边界：advance 支持连续调用；set 只能前进还是可回拨由约定说明（测试场景常需要回拨，标注）；与 fake timers 的取舍——只控时间点、不控定时器，侵入更小。

```javascript
function createStubClock(startTs = 0) {
  let current = startTs;
  const markers = [];
  return {
    now: () => current,
    advance: (ms) => { markers.push({ from: current, to: current + ms }); current += ms; },
    set: (ts) => { current = ts; },               // 可回拨，测试「时间倒流」分支
    elapsedSince: (ts) => current - ts,           // 常用派生：算间隔
  };
}

// 被测代码：依赖注入 clock
export function isTokenExpired(token, clock = { now: () => Date.now() }) {
  return token.expireAt < clock.now();
}

// ---- 测试：无 fake timers，无全局污染 ----
import { describe, it, expect } from 'vitest';
import { createStubClock } from './stub-clock';
import { isTokenExpired } from './token';

describe('isTokenExpired', () => {
  it('过期返回 true', () => {
    const clock = createStubClock(1_000_000);
    expect(isTokenExpired({ expireAt: 999_999 }, clock)).toBe(true);
    expect(isTokenExpired({ expireAt: 1_000_001 }, clock)).toBe(false);
  });

  it('advance 推进后状态翻转', () => {
    const clock = createStubClock(0);
    const token = { expireAt: 100 };
    expect(isTokenExpired(token, clock)).toBe(false);
    clock.advance(101);
    expect(isTokenExpired(token, clock)).toBe(true);
    expect(clock.elapsedSince(0)).toBe(101);
  });
});
```
**评分点**：
- 注入式 stub 与 fake timers 的取舍说清楚（不劫持全局、无恢复成本）。
- now/advance/set 语义完备，advance/set 有边界说明。
- 被测代码签名展示 `clock = { now: () => Date.now() }` 默认值注入。
- 能延伸到 sinon fake timers / vi.setSystemTime 的对应关系。
