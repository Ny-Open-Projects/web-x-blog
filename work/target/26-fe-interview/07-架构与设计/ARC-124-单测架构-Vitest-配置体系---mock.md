---
title: [ARC-124] 单测架构（Vitest 配置体系 / mock 策略 / 覆盖率门禁）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-124：单测架构（Vitest 配置体系 / mock 策略 / 覆盖率门禁）如何设计？
**答**：
- 配置体系分两层：根配置定公共策略（环境、别名、插件、coverage provider），项目级配置只写差异（node 环境 vs jsdom 环境）；monorepo 用 workspace 项目划分避免配置复制。
- mock 策略分层：网络 mock 统一在 msw（handler 即文档、可复用到 storybook/浏览器），时间/随机等非确定性 API 用 vi.useFakeTimers；原则是 mock 边界设施而不是 mock 业务内部实现。
- 覆盖率门禁用"增量门禁"：只要求本次 MR 涉及文件的行覆盖 ≥ 80%，存量不追溯——全量门禁会催生凑数测试。
- 测试文件与源码同目录，命名约定 `*.test.ts`，快照只用于错误信息这类稳定输出。

```typescript
// vitest.workspace.ts + 项目配置
import { defineWorkspace } from 'vitest/config';
export default defineWorkspace([
  { // Node 环境包（工具/服务端逻辑）
    test: { environment: 'node', include: ['packages/*/src/**/*.test.ts'] },
  },
  { // 组件环境包（UI）
    test: {
      environment: 'jsdom',
      setupFiles: ['./test/setup.ts'],        // msw server 启动 + cleanup
      coverage: {
        provider: 'v8',
        thresholds: {
          // 增量门禁：由 CI 脚本计算 diff 文件集，只对这些文件要求阈值
          lines: 80, branches: 70,
        },
      },
    },
  },
]);
// test/setup.ts —— mock 边界设施统一入口
import { server } from './msw/server';
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));   // 未声明接口直接报错
afterEach(() => { server.resetHandlers(); vi.useRealTimers(); });
afterAll(() => server.close());
```
