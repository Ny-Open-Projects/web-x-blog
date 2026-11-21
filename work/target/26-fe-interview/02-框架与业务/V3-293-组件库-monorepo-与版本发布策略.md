---
title: [V3-293] 组件库 monorepo 仓库与版本发布策略怎么设计？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-293：组件库 monorepo 仓库与版本发布策略怎么设计？
**答**：
- 仓库划分：pnpm workspace + packages（ui-core 组件/ui-icons/ui-utils/docs 站点/playground），组件与工具解耦独立发版。
- 版本策略：changesets 管理——PR 提交 changeset（patch/minor/major + changelog），CI 汇总自动发版；固定版本 vs 独立版本按包耦合度选。
- 破坏性变更：major 版本配迁移指南 + codemod 脚本；实验 API 用 `@experimental` 标记并单独文档，正式前可随时移除。
- 发布门禁：CI 跑类型检查/单测/视觉回归（storybook chromatic）/包体积 diff，超阈值阻塞合并。
- 对内策略：内网 npm 源 + 每 alpha 发布到 `next` tag，业务方灰度验证后再 latest。

```yaml
# .changeset/config.json 核心配置
{ "packages": ["packages/*"], "linkWorkspaceDependencies": true,
  "publishConfig": { "registry": "https://npm.internal.example.com" } }
# 流程：feat PR -> `pnpm changeset` 选包与 bump 类型 -> merge main
# CI: changesets/action 自动 version + publish + changelog
# 视觉回归：chromatic --exit-zero-on-changes 只报告不阻塞
# 体积门禁：size-limit --json 比对上次 release，> 5% 阻塞
```
