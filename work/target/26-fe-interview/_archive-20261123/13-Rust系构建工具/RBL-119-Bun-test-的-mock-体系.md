---
title: [RBL-119] bun test 的 mock 能力有哪些？与 jest 的差异？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-119：bun test 的 mock 能力有哪些？与 jest 的差异？
**答**：
- 函数 mock：mock(fn) 创建 spy（记录调用与参数），jest.fn 等价；mocked 模块替换用 mock.module('pkg', () => ({...})) 对应 jest.mock。
- 全局 mock：mock(globalThis, 'fetch', fn) 可直接替换全局 fetch 并用 mock.restore() 还原——比 jest 的 global.fetch = jest.fn() 更整洁。
- 计时器与时间：setSystemTime 控制系统时间（对应 jest 的 fake timers 子集），时间相关测试方便。
- 差异：jest 的自动 mock（automock）、深度模块工厂 hoisting 语义在 bun 里实现方式不同，复杂 mock 场景要验证；snapshot 格式兼容但实现独立。
- 实战建议：mock 范围收敛到"边界"（网络/时间/随机），业务内部尽量真调用，减少 mock 差异风险。
- 追问钩子：mock 的本质是"替换依赖注入点"，过度 mock 会让测试变成实现细节断言——这是测试哲学题不只是 API 题。

```typescript
import { describe, it, expect, mock, setSystemTime } from 'bun:test';

describe('token', () => {
  it('过期判定', () => {
    setSystemTime(new Date('2026-01-01T00:00:00Z'));
    const token = makeToken({ exp: '2026-01-01T01:00:00Z' });
    expect(isExpired(token)).toBe(false);
    setSystemTime(new Date('2026-01-01T02:00:00Z'));
    expect(isExpired(token)).toBe(true);
  });
});
```
