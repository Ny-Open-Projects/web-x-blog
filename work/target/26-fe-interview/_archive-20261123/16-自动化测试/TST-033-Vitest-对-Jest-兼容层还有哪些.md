---
title: [TST-033] Vitest 有哪些 Jest 兼容设计？哪些 API 不兼容要注意？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-033：Vitest 有哪些 Jest 兼容设计？哪些 API 不兼容要注意？
**答**：
- 兼容面：describe/it/test/expect 全套 matcher（toBe/toEqual/toThrow/toMatchObject…）、生命周期钩子、vi.fn/mock 属性结构（calls/results/instances）、快照机制、test.each——90% 用例机械替换即可。
- 不兼容点 1：fake timers 默认集合不同（Vitest 基于 @sinonjs/fake-timers，需 toFake 指定）。
- 不兼容点 2：jest.requireActual → vi.importActual；jest.mock 的 auto-mock 行为略有差异；jest.setTimeout → it 的 timeout 参数。
- 不兼容点 3：模块系统——Jest CJS 化运行的代码（顶层 this、__dirname）在 ESM 下语义不同，用到这些的测试要改造。
- 判断方法：`npx @vitest/eslint-plugin` + 官方迁移指南逐条过；或先跑 `vitest run` 收集报错再定点修。

```javascript
// 高频 API 对照表（迁移速查）
// jest.fn()                -> vi.fn()
// jest.mock('./x')         -> vi.mock('./x')
// jest.requireActual       -> vi.importActual
// jest.spyOn(obj, 'm')     -> vi.spyOn(obj, 'm')
// jest.useFakeTimers()     -> vi.useFakeTimers({ toFake: [...] })
// jest.clearAllMocks()     -> vi.clearAllMocks()
// expect.assertions(n)     -> 同名支持
// jest.setTimeout(10000)   -> it('..', fn, 10000) 或 config.testTimeout
```
