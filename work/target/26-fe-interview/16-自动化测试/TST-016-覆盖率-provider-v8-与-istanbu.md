---
title: [TST-016] Vitest 覆盖率 provider 选 v8 还是 istanbul？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-016：Vitest 覆盖率 provider 选 v8 还是 istanbul？
**答**：
- v8：直接读 V8 引擎自带的覆盖率数据（0 是真实执行结果），几乎零插桩开销，速度快、产物体积不受影响；缺点是分支统计粒度粗、个别行级信息不准。
- istanbul：测试前对源码插桩（每个分支/语句埋计数器），数据最精确（分支覆盖更细），但插桩让执行变慢约 30%~80%，且改写源码可能干扰调试。
- 选型：日常 CI 用 v8（快）；需要严格分支门禁或 istanbul 生态工具（如部分 diff-cover 方案）时用 istanbul。
- 配置：`coverage.provider: 'v8' | 'istanbul'`，报告格式 reporter 支持 text/html/lcov-json（供平台消费）。
- 追问钩子：v8 provider 依赖 V8 的 block coverage，行「部分覆盖」时 v8 可能算成覆盖，导致虚高。

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',                       // 'istanbul' 需另装 @vitest/coverage-istanbul
      reporter: ['text', 'html', 'lcov'],   // lcov 供 CI/平台解析
      include: ['src/**'],
      exclude: ['src/**/*.d.ts', 'src/main.tsx', 'src/__mocks__/**'],
      thresholds: { lines: 80, functions: 80, branches: 70, statements: 80 },
    },
  },
});
// 运行：npx vitest run --coverage
```
