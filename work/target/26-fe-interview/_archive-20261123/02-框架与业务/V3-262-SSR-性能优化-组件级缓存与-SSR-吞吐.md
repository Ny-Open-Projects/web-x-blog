---
title: [V3-262] SSR 性能优化：组件级缓存、内存与吞吐怎么做？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-262：SSR 性能优化：组件级缓存、内存与吞吐怎么做？
**答**：
- 组件级缓存：给"渲染结果稳定"的组件（公告栏/分类树）配 `cache: { max }`/LRU key（含依赖参数），命中时跳过整棵子树渲染，QPS 提升显著。
- 组件级缓存实现要点：SSR 缓存 key 必须包含该组件所有影响输出的输入（props + 请求上下文），否则串数据。
- 渲染外优化：HTML 片段缓存（页面/布局层）、payload 复用、上游接口并行化与超时熔断。
- 内存治理：SSR 是长驻进程——防止"每请求全局变量累积"（模块级 Map、未清理的事件监听），用 heap snapshot 对比定位。
- 吞吐度量：压测 renderToString 单请求耗时 P95 + Node 进程 RSS 曲线；目标"渲染耗时 < 50ms、接口聚合 < 200ms"。

```javascript
// Vue SSR 组件级缓存（getCacheKey 挂在组件上）
export default {
  name: 'CategoryTree',
  ssrCacheKey: (ctx) => `tree-${ctx.props.categoryId}`, // key 含所有输入
  cache: { max: 100, ttl: 60_000 },   // 简化示意：LRU + TTL
  async setup(props) {
    return () => h('ul', await buildTree(props.categoryId));
  },
};
// 压测脚本要点
// autocannon -c 100 -d 30 http://localhost:3000/products/1
// 观察：RPS、P99、RSS 是否持续上涨（泄漏信号）
```
