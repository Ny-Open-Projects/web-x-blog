---
title: [ENG-231] monorepo 的 codegen（GraphQL/OpenAPI 生成）怎么治理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-231：codegen 怎么治理？
**答**：
- 生成物管理：生成代码进产物目录（generated/）不进 Git（构建时生成）还是进 Git？——进 Git 可评审 diff 且新环境零生成成本，代价是提交噪声；schema 变更频繁的团队选「不进 Git + CI 强制生成」。
- 幂等与确定性：codegen 必须确定性输出（稳定排序/无时间戳），否则每次生成 diff 噪声淹没真实变更——codegen 的可复现与构建同级要求。
- 契约校验：schema 变更 PR 自动重新生成 + 类型检查消费方，breaking schema 在 CI 即暴露（SCN-203 影响面联动）。
- 缓存接入：codegen 输出进构建图（schema hash 为输入），未变更 schema 不重跑。
- 追问钩子：为什么生成代码「进 Git」的团队反而更少踩坑——新人 clone 即编译通过（无需懂 codegen 链路）；diff 可见让生成 bug 在评审暴露；只有 schema 日变更上千次的超大团队才值得去掉 Git 化。

```yaml
# codegen 配置：确定性输出
config: { sortProperties: true, useTypeImports: true, omitStaleFields: true }
# CI 契约校验
- run: pnpm codegen
- run: git diff --exit-code src/generated/   # 生成物与 schema 不同步即失败
```
