---
title: [TST-007] 笔试：用 vi.mock 测试一个 axios 请求封装模块
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-007：笔试：用 vi.mock 测试一个 axios 请求封装模块
**答**：
- 需求：`getUser(id)` 内部调用 axios.get 并做数据剥壳（res.data.data）；测试要验证 URL、参数与返回值，且不真实发请求。
- 要点：`vi.mock('axios')` 整体 mock default 导出；工厂里用 `vi.fn()` 创建 get；用 `vi.mocked()` 收回类型；在 beforeEach 里统一 reset 并注入返回值。
- 边界：请求失败分支也要测（reject 时封装层抛出业务错误）；afterEach `verify`/`restoreAllMocks` 防止用例间污染。

```typescript
// src/api/user.test.ts
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import axios from 'axios';
import { getUser, User } from './user';

vi.mock('axios', () => ({
  default: { get: vi.fn() },   // 工厂返回 mock 的 default 导出
}));
const mockedGet = vi.mocked(axios.get);

beforeEach(() => {
  mockedGet.mockReset();
});
afterEach(() => {
  vi.restoreAllMocks();
});

describe('getUser', () => {
  it('请求正确的 URL 并剥壳返回 data', async () => {
    mockedGet.mockResolvedValue({ data: { data: { id: 1, name: '张三' } } } as any);
    const user: User = await getUser(1);
    expect(mockedGet).toHaveBeenCalledWith('/api/users/1');
    expect(user.name).toBe('张三');
  });

  it('接口失败时抛出业务错误', async () => {
    mockedGet.mockRejectedValue(new Error('network down'));
    await expect(getUser(2)).rejects.toThrow('network down');
    expect(mockedGet).toHaveBeenCalledTimes(1);
  });
});

// 被测源码 src/api/user.ts：export const getUser = (id:number) =>
//   axios.get(`/api/users/${id}`).then(r => r.data.data);
```
**评分点**：
- mock 工厂写成 `() => ({ default: { get: vi.fn() } })`，漏 default 会拿到 undefined。
- beforeEach reset：避免上一条用例的调用记录串场。
- 成功 + 失败两条分支都覆盖。
- 用 `vi.mocked` 保持 TS 类型而不是 any 硬转。
