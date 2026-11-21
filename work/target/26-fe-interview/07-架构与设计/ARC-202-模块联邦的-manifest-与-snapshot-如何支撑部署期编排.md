---
title: [ARC-202] 模块联邦的 manifest 与 snapshot 如何支撑部署期编排？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-202：模块联邦的 manifest 与 snapshot 如何支撑部署期编排？
**答**：
- manifest = 子应用的"自描述文件"：entry、exposes 清单、shared 依赖与版本、publicPath，运行时据此动态加载，主应用不再写死 remote entry 地址。
- snapshot = 构建期产出的"依赖关系图数据"，是给**平台**消费的：发布平台用它建联邦依赖图谱，回答"谁在引用我、改这个 expose 影响哪些主应用"。
- 部署期编排：主应用发布时不重新构建，而是由发布平台改写主应用消费的 manifest 路由表（指向子应用新版本），实现"主应用不动、子应用独立发布"。
- 配套回滚：manifest 指针回指旧版本 snapshot，CDN 不删旧产物（保留 N 个版本），回滚秒级。
- 追问钩子：manifest 被缓存怎么办？——entry URL 带 hash 或短 TTL + stale-while-revalidate。

```javascript
// 部署平台：把"发布"简化为改 manifest 指针
const registry = { // 每个子应用的版本池（对应 CDN 上的 snapshot 目录）
  shop: { '1.4.2': '/cdn/shop/1.4.2/mf-manifest.json', '1.5.0': '/cdn/shop/1.5.0/mf-manifest.json' },
};
const routes = { host: { shop: '1.4.2' } }; // 主应用 host 当前消费的子应用版本

function publish(app, version)   { routes.host[app] = version; persist(routes); }
function rollback(app, version)  { publish(app, version); }          // 指针回拨即回滚
function dependentsOf(app) {      // snapshot 反查影响面
  return Object.entries(routes).filter(([h, rs]) => app in rs).map(([h]) => h);
}
// host 加载时只请求 routes.host.shop 解析出的 manifest URL，一次网络往返完成版本决策
```
