---
title: [HW-205] 手写性能单测——行为断言（防抖可取消/缓存有上限/切片耗时上限）的测试基建？
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：性能行为的单测锁（PER-459 ②）：① 接口断言（debounce 有 cancel/flush；缓存有 max 参数且超限淘汰）；② 行为断言（mock 计时器下防抖只执行一次；LRU 满后访问最少项被淘汰）；③ 耗时断言（纯函数单次调用 < 1ms，用 performance.now 计时、跑 1000 次取均值——阈值宽松防 CI 抖动）。

```javascript
// vitest 示例
import { describe, it, expect, vi } from 'vitest';

describe('debounce 行为锁', () => {
  it('必须提供 cancel/flush', () => {
    const d = debounce(() => {}, 100);
    expect(d.cancel).toBeTypeOf('function');              // 接口锁：防止"简版"实现混入
    expect(d.flush).toBeTypeOf('function');
  });
  it('连续触发只执行一次', () => {
    vi.useFakeTimers();
    const fn = vi.fn();
    const d = debounce(fn, 100);
    d(); d(); d();
    vi.advanceTimersByTime(150);
    expect(fn).toHaveBeenCalledTimes(1);                  // 行为锁：核心语义
  });
});

describe('LRU 容量锁', () => {
  it('超限淘汰最旧', () => {
    const c = new TTLCache({ max: 2 });
    c.set('a', 1); c.set('b', 2); c.set('c', 3);
    expect(c.get('a')).toBeUndefined();                   // 行为锁：容量约束生效
  });
});

describe('纯函数耗时锁', () => {
  it('formatPrice 单次 < 1ms（1000 次均值）', () => {
    const t0 = performance.now();
    for (let i = 0; i < 1000; i++) formatPrice(Math.random() * 1000, 'CNY');
    expect((performance.now() - t0) / 1000).toBeLessThan(1);   // 耗时锁：均值防 CI 抖动
  });
});
// 三层锁的层级：接口锁（防退化实现）> 行为锁（防语义回归）> 耗时锁（防性能回归，CI 需稳定环境）
// 耗时锁阈值要宽松（均值 + 倍数余量）—— CI 机器抖动会让精确阈值变成 flaky test
```

**评分点**：
- 三层锁（接口/行为/耗时）的设计分层——本题核心。
- vi.useFakeTimers 的确定性测试（真实定时器会 flaky）。
- 耗时锁用均值 + 宽松阈值（防 CI 抖动 flaky）。
- 行为锁直接对应 PER-459 防线清单的"单测锁"。
