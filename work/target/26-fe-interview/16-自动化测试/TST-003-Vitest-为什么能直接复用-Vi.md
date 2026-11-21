---
title: [TST-003] Vitest 为什么能直接复用 Vite 的配置？机制是什么？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-003：Vitest 为什么能直接复用 Vite 的配置？机制是什么？
**答**：
- Vitest 本质是「挂在 Vite dev server 之上的测试运行器」：测试文件也走 Vite 的 transform 管线（插件、alias、define、环境变量解析全部生效）。
- resolve.alias、plugins、define、css 等字段与 vite.config.ts 完全同一套，不存在 Jest 那种「测试配置与构建配置两份真相」的漂移问题。
- test 字段是 Vitest 扩展的命名空间，Vite 会忽略；通过 `defineConfig from 'vitest/config'` 获得类型提示，或用 `mergeConfig` 合并两份配置。
- 按需拆分：vite.config.ts 与 vitest.config.ts 同目录时 Vitest 优先后者；不写则直接读 vite.config.ts。插件里 `apply: 'serve'` 的插件不参与测试转换，可用 `test: { pluginsMode }` 控制。
- 追问钩子：测试时想要不同的 alias/define（如 mock 重的三方库），就在 vitest.config.ts 里 override。

```typescript
// vitest.config.ts —— 以 vite.config 为底，只叠加测试差异项
import { defineConfig, mergeConfig } from 'vitest/config';
import viteConfig from './vite.config';

export default mergeConfig(
  defineConfig(viteConfig), // 复用 plugins/alias/define
  defineConfig({
    test: {
      environment: 'jsdom',
      globals: true,
      setupFiles: ['./vitest.setup.ts'],
      coverage: { provider: 'v8', thresholds: { lines: 80 } },
    },
    resolve: { alias: { 'heavy-chart-lib': '/src/__mocks__/chart.ts' } }, // 测试专用 override
  }),
);
```
