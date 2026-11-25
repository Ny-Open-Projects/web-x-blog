---
title: [TST-175] monorepo 里的测试架构怎么搭？vitest workspace 怎么组织？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-175：monorepo 里的测试架构怎么搭？vitest workspace 怎么组织？
**答**：
- 组织原则：每个 package 独立 test 配置（依赖、环境不同），workspace 层做「统一命令 + 共享 setup + 聚合覆盖率」。业务 app 用 jsdom + RTL；工具库用 node 环境；SSR 包用 node + MSW node adapter——环境差异就是拆项目的第一理由。
- 共享测试基建收进 `@org/test-utils` 包：renderWithProviders、fixture 工厂、axe 断言、seated random——测试工具库化，避免每个包复制粘贴 helper（与业务代码复用同理）。
- 覆盖率聚合：各包跑完输出 lcov，`nyc merge` / 自研聚合脚本合并成整仓报告，门禁在根级别跑（分层阈值见 TST-115）；受影响测试选择器在 monorepo 里尤其有价值（依赖图跨包，改 utils 只跑依赖它的包的用例）。
- CI 编排：changed-based 触发——turbo/nx 只跑受影响 package 的 test（`turbo run test --filter=...[origin/main]`）；E2E 只有一个入口（部署后的整合环境），不按包拆。
- 缓存：turbo 的 test 任务按输入哈希缓存（源码没变测试不重跑），加上 node_modules/pnpm store 缓存，PR 时长可控。

```json
// vitest.workspace.ts
export default [
  { test: { name: 'web', root: 'apps/web', environment: 'jsdom',
      setupFiles: ['apps/web/vitest.setup.ts'] } },
  { test: { name: 'utils', root: 'packages/utils', environment: 'node' } },
  { test: { name: 'ui-kit', root: 'packages/ui', environment: 'jsdom',
      setupFiles: ['packages/test-utils/src/setup.ts'] } },
];

// turbo.json：受影响包才跑测试
// turbo run test --filter=...[origin/main]
// 共享测试工具包 packages/test-utils：
// renderWithProviders / createOrderFixture / expectNoA11yViolations / seededRandom
```
