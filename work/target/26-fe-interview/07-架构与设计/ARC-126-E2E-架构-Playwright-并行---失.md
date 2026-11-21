---
title: [ARC-126] E2E 架构（Playwright 并行 / 失败重试 / tracing）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-126：E2E 架构（Playwright 并行 / 失败重试 / tracing）如何设计？
**答**：
- 并行体系：用例内自治（不共享状态）→ 浏览器上下文级隔离 → CI 按文件分片（--shard）横向扩展；登录态用 storageState 复用（登录一次，全组用例共享），把每条用例的 setup 开销降到零。
- 稳定性设计：选择器只认 data-testid（约定进 lint）、等待策略认网络/idle 断言而不是 sleep、每条用例自建数据（API 造数）不依赖前序用例。
- 失败处理：retries 在 CI 开 2（本地 0 便于暴露问题）、失败自动留 trace + 截图 + video，trace viewer 定位失败比看录像快一个量级。
- 用例准入：E2E 用例数量受控（只保关键路径），新增 E2E 需要说明"为什么组件测试覆盖不了"。

```typescript
// playwright.config.ts 核心设计
import { defineConfig, devices } from '@playwright/test';
export default defineConfig({
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,             // CI 重试吸收偶发，本地不掩盖
  workers: process.env.CI ? 4 : undefined,
  use: {
    trace: 'retain-on-failure',                // 失败保留 trace（可回放每一步）
    screenshot: 'only-on-failure',
    baseURL: 'http://localhost:3000',
  },
  projects: [
    { name: 'setup', testMatch: /auth\.setup\.ts/ },        // 登录一次生成 storageState
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'], storageState: 'e2e/.auth/user.json' },
      dependencies: ['setup'],                              // 先跑 setup
    },
  ],
  // CI 分片由流水线控制：
  // npx playwright test --shard=${SHARD_INDEX}/${SHARD_TOTAL}
  reporter: [['html'], ['github']],            // 失败行内标注到 PR
});
```
