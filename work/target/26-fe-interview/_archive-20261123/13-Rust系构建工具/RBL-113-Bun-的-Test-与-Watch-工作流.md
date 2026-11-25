---
title: [RBL-113] 用 Bun 打造前端脚手架的 CI 流水线有什么优势？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-113：用 Bun 打造前端脚手架的 CI 流水线有什么优势？
**答**：
- 安装提速：bun install 替换 npm install，CI 中安装时间通常下降 3~20 倍，是流水线里收益最大且风险最低的一步。
- 测试提速：bun test 替换 jest，无需 tsc-js 双转译链路；测试越多的仓库收益越明显。
- 脚本统一：bun run 替代 node scripts，TS 脚本免编译直接跑，省去 ts-node/tsx 依赖。
- 缓存策略：CI 缓存 bun 的全局缓存目录 + node_modules，二次构建只增量。
- 一体化减少安装面：jest/ts-jest/babel 及其 preset 链可以直接从 devDependencies 移除，依赖树变小。
- 风险控制：保留 npm 双轨命令一段时间（npm run test 兼容），对比产物/测试结果一致后再切换默认。
- 追问钩子：CI 提速要给数据——迁移前后各跑 5 次取 P50，用数据说服团队。

```yaml
# GitHub Actions（bun）
- uses: oven-sh/setup-bun@v2
  with: { bun-version: latest }
- run: bun install --frozen-lockfile
- run: bun run typecheck
- run: bun test --coverage
- run: bun run build
# 缓存
# path: ~/.bun/install/cache
```
