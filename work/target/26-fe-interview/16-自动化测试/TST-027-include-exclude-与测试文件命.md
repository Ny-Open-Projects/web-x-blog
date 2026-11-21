---
title: [TST-027] 测试文件的 include/exclude 配置怎么设计？文件怎么命名？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-027：测试文件的 include/exclude 配置怎么设计？文件怎么命名？
**答**：
- 默认 include 只匹配 `**/*.{test,spec}.?(c|m)[jt]s?(x)`，项目自定义目录（如 `__tests__`、`test/`）要显式加 glob。
- exclude 默认已排除 node_modules/dist；自定义排除要记得 `...configDefaults.exclude` 展开默认值，否则会覆盖丢失 node_modules 排除（高频翻车点）。
- 命名约定：同目录 `foo.test.ts`（就近，好维护）或统一 `__tests__/foo.test.ts`（好批量排除/统计）；类型测试 `foo.test-d.ts`，基准 `foo.bench.ts`。
- 分类过滤：用文件名约定 + `--dir` / 命名 pattern（如 `*.smoke.test.ts`）实现冒烟/全量分层，CI 按阶段跑。
- 追问钩子：monorepo 用 workspace 后，各子包自己 include，根目录不再写大 glob。

```typescript
// vitest.config.ts
import { configDefaults, defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['src/**/*.{test,spec}.{ts,tsx}', '__tests__/**/*.test.ts'],
    exclude: [...configDefaults.exclude, 'packages/legacy/**'], // 别丢默认排除
  },
});
```
