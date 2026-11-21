---
title: [RBL-108] bun test 的能力与 Jest 兼容程度如何？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-108：bun test 的能力与 Jest 兼容程度如何？
**答**：
- 兼容面：describe/it/expect、jest.fn/mock、beforeEach/afterEach、快照、模块 mock（jest.mock 基本语义）API 兼容，存量 Jest 测试大多可平移。
- 内建优势：直接跑 TS/JSX（内置转译）、按文件并行（线程池）、内置 happy-dom 或 DOM 环境切换、watch 快、与 bun.lock 工具链一体。
- 差异面：Jest 的完整插件生态（transform 链、自定义 runner、特定 matcher 扩展）不完全支持；部分 Node 模块 mock 行为有细节差异；jsdom 相关配置项不同。
- 性能量级：同样测试套件 bun test 通常比 jest 快 5~20 倍（无转译进程链 + 原生并行）。
- 使用策略：单测迁 bun test 收益最大；依赖深度 jest 生态（如 @testing-library 的特定 jest 环境）的组件测试要验证或保留 jest 双轨。
- 追问钩子：bun test 的断言失败输出与 jest 兼容，CI 报告解析器（junit）支持情况要按版本核对。

```typescript
// bun test 直接跑 TS，无需配置 transform
import { describe, it, expect, mock } from 'bun:test';
import { fetchUser } from './user';

describe('fetchUser', () => {
  it('缓存命中不重复请求', async () => {
    const fetchMock = mock(globalThis, 'fetch', async () =>
      new Response(JSON.stringify({ id: 1 }), { headers: { 'content-type': 'application/json' } }));
    await fetchUser(1);
    await fetchUser(1);
    expect(fetchMock).toHaveBeenCalledTimes(1); // 或按缓存实现断言
    mock.restore();
  });
});
```
