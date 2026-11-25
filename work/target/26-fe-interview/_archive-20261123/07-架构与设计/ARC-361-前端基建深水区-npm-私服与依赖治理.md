---
title: [ARC-361] 前端基建：npm 私服与依赖治理架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-361：前端基建：npm 私服与依赖治理架构如何设计？
**答**：
- 私服（Verdaccio/Nexus/云厂商制品库）三价值：内网加速（缓存上游）、私有包托管（业务组件/SDK 不发布公网）、安全卡口（漏洞包/投毒包白名单拦截）。
- 依赖治理分四层：准入（新依赖评审：维护活跃度/体积/许可证/安全扫描）、使用（lockfile 强制 + 幽灵依赖禁令 + 重复依赖合并）、升级（定期自动 PR renovate + 破坏性升级窗口）、退出（无引用依赖自动清理）。
- 安全：CI 集成 audit + lockfile 哈希校验；高危 CVE 自动开单分派到 owner；关键依赖锁大版本。
- 与 Monorepo 配合：内部包统一 workspace 协议引用，私服只承载对外发布的产物。
- 度量：依赖数趋势、重复依赖体积、CVE 修复时长，作为基建健康指标。
```json
// .npmrc 私服配置 + 准入检查脚本（CI 内）
{
  "registry": "https://npm.internal.example.com",
  "//": "CI 阶段运行：node scripts/dep-gate.js && npm audit --audit-level=high"
}
// dep-gate.js：检查 package.json 新增依赖是否在 approved 清单，否则退出码 1
```
