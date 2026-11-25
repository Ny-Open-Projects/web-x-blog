---
title: [AIC-093] 大型 monorepo 里跑 Agent 有什么特殊问题？「代码地图」怎么帮 agent 不迷路？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-093：大型 monorepo 里跑 Agent 有什么特殊问题？「代码地图」怎么帮 agent 不迷路？
**答**：
- 特殊问题：仓库太大无法全量索引（上下文放不下）、同名概念散落多包（两个 package 都有 utils）、跨包依赖链长（改 lib 影响三个 app）、构建工具链复杂（agent 跑错构建命令）。
- 代码地图（code map）：一份人维护 + 脚本校验的「仓库结构说明」——每个包的职责、owner、依赖关系、构建/测试命令、命名约定。agent 开工前先读地图，避免靠猜。
- 地图要配「导航规则」：任务先定位到包级再深入；禁止跨包直接 import 私有模块；改动 lib 时必须跑受影响 app 的测试。
- 脚本校验地图：CI 里检查地图声明的包列表与实际 workspace 一致、依赖关系与 package.json 一致——地图腐烂比没有更糟。
- 追问钩子：这与 AIC-012（monorepo 规则组织）互补——规则管「怎么写」，地图管「在哪里」。

```markdown
<!-- ai/CODEMAP.md（agent 先读的仓库地图，节选） -->
- packages/ui：通用组件库，owner: fe-core。命令：pnpm --filter ui test
- packages/goods：商品域业务包，依赖 ui 与 api-types
- apps/admin：后台应用。改 packages/lib 后必须跑 admin 的冒烟
规则：跨包引用只允许 import 公共导出；新依赖需 owner 审批
```
