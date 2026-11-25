---
title: [ENG-263] 私有 npm 源（registry）的治理怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-263：私有 npm 源治理怎么做的？
**答**：
- 架构：私有源作为上游代理（cache npm 官方）+ 私有包托管——统一出口让「全部依赖过审计代理」成为可能（供应链治理入口）。
- 权限与发布：发布走 CI 令牌（人员账号禁直发）、provenance 签名、dist-tags 管理（next/stable 通道）。
- 可用性设计：私有源是全团队的硬依赖——多副本 + 本地缓存兜底（verdaccio mirror）+ 源故障预案（临时切官方源跑紧急构建，私有包离线包）。
- 治理指标：缓存命中率/源响应 P95/过期包（两年未更新的私有包清单）。
- 追问钩子：为什么「统一出口代理」是供应链治理的地基——所有依赖从代理走，才能实施白名单/审计/镜像锁定；每个团队各自直连官方源时，任何治理规则都形同虚设。

```bash
# .npmrc 统一出口
registry=https://npm.internal.example.com/
@org:registry=https://npm.internal.example.com/
always-auth=true
# 发布权限：CI token only
//npm.internal.example.com/:_authToken=${CI_NPM_TOKEN}
```
```javascript
const registryHealth = { cacheHit: 0.92, p95: 80, stale: privatePackagesNotUpdated2y() };
```
