---
title: [ARC-103] 从前端视角看 CDN→边缘→网关→服务端的缓存分层架构如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-103：从前端视角看 CDN→边缘→网关→服务端的缓存分层架构如何设计？
**答**：
- 每层职责清晰：CDN 缓存全量静态资源与可缓存的 API 响应；边缘计算（Edge Function）做个性化剥离（把 Cookie 里的个性化部分剥离后才能命中 CDN）；网关做接口级缓存与合并；服务端做应用缓存与本地内存缓存。
- Cache-Key 设计是核心：个性化内容必须从 key 中剥离（登录态用"是否登录"这种粗粒度而不是 userId），否则命中率趋近于 0。
- 失效广播要贯通：内容变更→网关 purge→CDN purge，用统一失效中心管理，禁止各层私自设置互相矛盾的 TTL。
- 指标：分层命中率（每层独立统计），总回源率是最终北极星。

```yaml
# 缓存分层配置示例（前端可维护的部分）
cache_layers:
  cdn:
    static_assets:      { ttl: 31536000, key: "url + content-hash" }   # 带 hash 永久缓存
    api_cache:
      paths: ["/api/home/feed", "/api/product/detail"]
      ttl: 60
      key_rule: "path + query-white-list(version,channel) "   # 剥离个性化 query
      vary_on: ["X-Login-State"]     # 只区分 登录/游客 两种粒度
  edge:
    personalization:                  # 边缘把个性化小块拼接进缓存的大块
      strategy: "esi-like"            # 大块缓存 + 小块边缘动态拼装
  gateway:
    merge: ["/api/home/batch"]        # 聚合接口内部合并下游请求
    dedup_window: 100ms               # 同 key 并发请求合并回源
  server:
    stale_while_revalidate: true      # 过期先返回旧值后台刷新
metrics:
  - 每层独立命中率
  - 总回源率 < 5% 为健康线
```
