---
title: [NODE-514] Node 服务群的 Monorepo 组织（多服务共享代码）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-514：Monorepo 服务群组织
**答**:
- 何时 Monorepo：服务间共享代码多（公共库/协议/工具）、团队协作紧密（跨服务改动一次 MR）——数十个 Node 服务同一团队/域维护时收益大。
- 目录组织：apps/*（服务）、packages/*（共享库：协议客户端/错误码/工具/config——NODE-449 共享层）、protocols/*（契约单源——生成源 NODE-513）。
- 共享纪律：packages 语义化版本（服务锁具体版本——共享库升级可控）或 workspace 协议（源码直引——强一致但耦合发布，按库性质选：协议客户端用版本锁，内部工具可 workspace）、幽灵依赖禁止（NODE-ARC-025 同思想）。
- 构建与 CI：受影响构建（只构建变更服务及其依赖——Turborepo/Nx ARC-023）、跨服务测试（改动 packages → 受影响服务全测——依赖图驱动）。
- 发布：共享库发版流程（changelog/版本一致性检查）、服务发布与共享库发布解耦（服务引用已发布版本）。
- 反模式：Monorepo 里放完全不相关的团队服务（权限/节奏冲突——按团队/域划分仓库边界）。
```yaml
# Turborepo 受影响构建
packages: ["packages/*"]
apps: ["apps/trade-bff", "apps/order-svc"]
# CI: turbo run test build --filter=...[origin/main]  # 只测受影响
```
