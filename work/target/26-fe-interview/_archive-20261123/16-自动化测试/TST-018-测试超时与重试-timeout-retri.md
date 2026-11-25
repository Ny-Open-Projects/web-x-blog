---
title: [TST-018] 单测里的 timeout 和 retries 怎么配？哪些用例值得重试？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-018：单测里的 timeout 和 retries 怎么配？哪些用例值得重试？
**答**：
- 默认：单条 it 默认 5s 超时，钩子 10s；慢用例（大量 DOM 渲染、真实网络 mock 延迟）单独给 `it('...', fn, 15000)`。
- retries：`test.retries: 2` 让失败用例重试。单测层面应该追求确定性——重试治标，只对「确实存在非确定性外部因素」的用例开启（如依赖真实测试容器的集成测试）。
- 反模式：用长超时掩盖真实卡死（忘了 resolve 的 Promise）；用重试掩盖 flaky——正确路径是修用例（fake timers、显式等待）。
- 诊断：重试开启时报告会标注哪些用例是「重试后通过」，这类用例应进入 flaky 清单专项治理。
- 追问钩子：`vitest run --retry=2` CLI 临时开启，CI 里常配合 flaky 报告使用。

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    testTimeout: 10_000,
    hookTimeout: 15_000,
    // retries: process.env.CI ? 1 : 0,   // CI 允许一次重试并记录 flaky
  },
});

describe('重资源用例', () => {
  it('渲染 1000 行表格', () => { /* ... */ }, 20_000); // 用例级超时覆盖默认值
});
```
