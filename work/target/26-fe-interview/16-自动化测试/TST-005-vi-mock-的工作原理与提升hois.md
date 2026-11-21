---
title: [TST-005] vi.mock 的工作原理是什么？为什么它会被提升到文件顶部？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-005：vi.mock 的工作原理是什么？为什么它会被提升到文件顶部？
**答**：
- 原理：Vitest 在转换测试文件时（Vite 管线）做模块拦截——被 `vi.mock(path)` 声明的导入在模块加载阶段被替换为 mock 工厂产物，之后所有引用该模块的代码拿到的都是同一份 mock。
- hoisting：`vi.mock` 调用会被编译提升到文件所有 import 之前，因为 import 是静态提升的，mock 必须更早注册才拦得住。
- 推论：工厂函数里不能引用外部普通变量（此时它们还没初始化），会抛「Cannot access before initialization」；需要外部变量要用 `vi.hoisted`。
- 与 Jest 同构：Jest 的 babel-plugin-jest-hoist 也是同样套路，所以迁移时心智模型一致。
- 追问钩子：`vi.doMock` 不提升、对后续动态 import 生效，适合按测试用例切换 mock 行为。

```javascript
import { describe, it, expect, vi } from 'vitest';

// ❌ 错误：vi.mock 被提升到 const 之前，工厂执行时 config 还是 TDZ
// const config = { host: 'api.test' };
// vi.mock('./api', () => ({ fetchUser: () => fetch(config.host) }));

// ✅ 正确：vi.hoisted 同样被提升，且先于 mock 工厂执行
const { fakeHost } = vi.hoisted(() => ({ fakeHost: 'mock.example.com' }));
vi.mock('./api', () => ({
  fetchUser: (id) => fetch(`${fakeHost}/users/${id}`),
}));

import { fetchUser } from './api'; // 拿到的已是 mock 版

describe('fetchUser', () => {
  it('走 mock 实现', async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(new Response('{}'));
    await fetchUser(1);
    expect(globalThis.fetch).toHaveBeenCalledWith('mock.example.com/users/1');
  });
});
```
