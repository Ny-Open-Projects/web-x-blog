---
title: [NODE-370] Node 服务的灰度发布与流量染色如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-370：Node 服务的灰度发布与流量染色
**答**:
- 染色机制：请求按灰度规则打标（header x-gray-tag: canary，网关按用户/百分比/名单染色），路由层按标签路由到对应版本实例（K8s service 按标签选择 + Ingress 按 header 路由）。
- 全链路染色：灰度标签透传（BFF → 下游服务 → MQ 消息带标签，消费端路由到灰度 worker）——避免"前端灰度后端没灰度"的版本错配（ARC-449 双版本兼容的服务端版）。
- 发布策略：金丝雀（1% → 5% → 25% → 全量，每级观察指标）、蓝绿（双版本切换，回滚快但资源翻倍）、滚动（默认）。前端服务用金丝雀 + 自动止损（ARC-475 同构）。
- 灰度期数据兼容：DB 迁移向前兼容（NODE-335），新旧代码可同时读写。
- 观测：灰度桶独立看板（错误率/延迟对比基线），标签进日志与 trace。
```javascript
// 网关染色路由（伪码）
function route(req) {
  const tag = grayRule(req);                                     // 用户/比例/名单 → canary|stable
  if (tag) req.headers['x-gray-tag'] = tag;                      // 全链路透传
  return target(tag ?? 'stable');
}
// MQ：生产消息带 grayTag，消费者按标签消费各自版本
```
