---
title: [MFW-268] 服务端出站调用的限流与重试策略
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-268：出站调用限流重试

**答**:
- 问题：SSR 每请求都调第三方 API（汇率/天气）——流量放大（1 用户请求 → N 出站）+ 第三方 429 连坐页面失败
- 防线四层：缓存（同参数 TTL 内复用——Data Cache 天然位）、单飞合并（并发同 key 单请求 MFW-266）、客户端限流器（令牌桶按第三方配额自限——主动节流不触发 429）、降级默认值（429/超时回最近缓存或常量——页面不死）
- 重试礼貌性：只在幂等 GET 重试 + 尊重 Retry-After 头 + 抖动——不礼貌重试会被第三方封 IP
- 配额感知：响应头剩余配额（x-ratelimit-remaining）回写本地令牌桶——自适应降速

```javascript
// 出站包装：缓存+单飞+令牌桶+降级
async function getRate(date) {
  return withGovernation(`fx:${date}, {
    fetch: () => thirdParty.fx(date),
    ttl: 300_000, scope: 'server',                            // Data Cache 位
    rate: { capacity: 10, per: 's' },                          // 自限流
    onError: () => cache.stale(`fx:${date}`) ?? FX_DEFAULT,    // 降级链
  })
}
```
