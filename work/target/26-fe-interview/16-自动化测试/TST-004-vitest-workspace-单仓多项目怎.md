---
title: [TST-004] vitest.workspace.ts 是干什么的？monorepo 多项目怎么组织测试？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-004：vitest.workspace.ts 是干什么的？monorepo 多项目怎么组织测试？
**答**：
- 作用：在一个仓库里同时定义多个「测试项目」，每个项目有独立的 environment/include/coverage 配置，一次 `vitest` 命令全部跑完且并行调度。
- 典型场景：monorepo 里 React 应用（jsdom）、Node 服务（node）、组件库（jsdom + coverage）、CLI 工具（node）测试要求完全不同。
- 定义方式：`vitest.workspace.ts` 导出项目数组，元素可以是 glob 字符串（指向子包配置）或内联 `defineProject` 对象。
- 运行与过滤：`vitest run` 跑全部，`vitest run --project web` 只跑指定项目；子包内 `cd apps/web && vitest` 也能单独跑。
- 追问钩子：workspace 与 Turborepo/Nx 的按需测试并不冲突——前者管「一次跑多套配置」，后者管「哪些包需要跑」。

```typescript
// vitest.workspace.ts（根目录）
import { defineWorkspace } from 'vitest/config';

export default defineWorkspace([
  'apps/*',            // 每个子应用自己的 vitest.config.ts
  'packages/*',
  {                    // 也可内联定义临时项目
    test: {
      name: 'node-scripts',
      environment: 'node',
      include: ['scripts/**/*.test.ts'],
    },
  },
]);

// apps/admin/vitest.config.ts
import { defineProject } from 'vitest/config';
export default defineProject({
  test: { name: 'admin', environment: 'jsdom', include: ['src/**/*.test.tsx'] },
});
// 运行：npx vitest run --project admin
```
