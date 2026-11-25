---
title: [RBL-846] 场景题：BFF 网关路由与前端产物协同——按路由分流的 chunk 部署
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-846：场景题：BFF 网关路由与前端产物协同——按路由分流的 chunk 部署

**答**:
- 大型应用的路由分流部署（不同路由不同团队/不同发布节奏）：网关按路径把请求分到「不同版本的产物集合」——构建器的配合：1) 路由 → 产物集合映射（每个路由团队的独立构建产出独立 manifest）；2) **跨路由共享资源的版本协调**（路由 A 用的 vendor 1.0 与路由 B 的 2.0——共享缓存的目标要求 vendor URL 一致——共享层单独构建发布）；3) 网关路由表与产物 manifest 的同步（路由表声明 → 网关配置生成——配置即产物）。
- 协同的核心约束：跨路由导航的加载一致性——路由 A 的页面跳到路由 B：B 的 chunk URL 来自 B 的 manifest（运行时查表）——「全局路由 manifest」是协同的枢纽（构建器聚合各团队的 manifest，冲突检测：同一路由两个团队都声明 = 架构违规）。
- 共享层的版本策略：vendor 由「共享层团队」单独发布（semver），业务路由锁定版本（lockfile）——升级走集中流程（RBL-821 升级日）——「共享层是公共品，升级是政治问题，机制解决」。
- 发布顺序：共享层先发（向后兼容窗口）→ 业务路由按节奏发——网关路由表更新是最后一步（RBL-694 发布编排的 manifest switch）。
- 追问钩子：为什么「跨路由导航」是分流部署最难的一致性问题？——导航时的 chunk 加载跨了两个产物集合（A 的 runtime 持有 A 的 manifest，跳 B 要用 B 的 manifest）；实现必须「全局 manifest」或「动态注册」（B 的 manifest 由网关注入 html）——任何一种都要处理「B 正在发布中」的窗口（RBL-694 的顺序契约在跨集合场景放大）。

```javascript
// 路由分流部署的协同配置
const ROUTES = {
  '/shop/**': { team: 'shop', manifest: 'shop.manifest.json' },
  '/admin/**': { team: 'admin', manifest: 'admin.manifest.json' },
  '/shared/vendor-*.js': { team: 'platform', manifest: 'shared.manifest.json' },
};
// 冲突检测
function auditRouteOwnership(manifests, routes) {
  const owners = {};
  for (const [team, m] of Object.entries(manifests))
    for (const route of m.routes ?? [])
      if (owners[route]) fail(`路由冲突: ${route} 被 ${owners[route]} 与 ${team} 同时声明`);
      else owners[route] = team;
  // 路由表覆盖检查：manifest 声明的路由必须有网关条目
  for (const route of Object.keys(owners))
    if (!Object.keys(routes).some(p => matchGlob(p, route)))
      fail(`路由 ${route} 缺网关条目——产物将 404`);
}
// 全局 manifest 聚合
const globalManifest = mergeManifests(manifests);        // chunk → url（跨路由导航查表）
```
