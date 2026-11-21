---
title: [ENG-050] Vitest 的常用 mock 能力有哪些？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-050：Vitest 的常用 mock 能力有哪些？
**答**：
- vi.mock 模拟整个模块；vi.fn 创建 spy 并可用 mockResolvedValue 设定返回值。
- vi.useFakeTimers + setSystemTime 控制时间，测试定时器与时间相关逻辑。
- vi.spyOn 监听对象方法调用而不替换实现；beforeEach 中重置，避免用例间污染。
- mock 的粒度越靠近边界（网络、时间、随机）越好，业务逻辑保持真实。

```javascript
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { getGreeting } from './utils';
import { fetchUser } from './api';

// 模拟网络边界
vi.mock('./api', () => ({
  fetchUser: vi.fn(),
}));

describe('getGreeting', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.restoreAllMocks();
  });

  it('早上 8 点返回早上好', () => {
    vi.setSystemTime(new Date('2026-01-01T08:00:00'));
    expect(getGreeting()).toBe('早上好');
  });

  it('fetchUser 被调用时返回 mock 数据', async () => {
    vi.mocked(fetchUser).mockResolvedValue({ name: 'Wang' });
    const user = await fetchUser();
    expect(user.name).toBe('Wang');
  });
});
```

---

## 第十二章 发布与环境变量（ENG-051 ~ ENG-053）
