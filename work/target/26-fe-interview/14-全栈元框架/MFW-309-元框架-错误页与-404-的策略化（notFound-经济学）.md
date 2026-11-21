---
title: [MFW-309] 404 经济学：notFound 的缓存与成本策略
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-309：404 经济学

**答**:
- 成本结构：爬虫扫参数枚举（/item/1..1000000）→ 每个未知 id 触发 DB 查询 + 渲染 404——404 是被低估的 DDoS 面
- 分层防御：路由级格式校验（非 uuid 直接 410/404 零 DB）、负缓存（确认不存在 → 缓存 404 决策 1h——同 id 不再查）、限流（同 IP 404 频次——MFW-294 IP 维）、软删除页 410 Gone（SEO 正确信号——比 404 好的删档语义）
- 404 页本身要可缓存（静态——高流量页不能每请求渲染）；自定义 404 别做重查询（它是最常被攻击的页面）
- 指标：404 率与来源 IP 分布进日常看板（突增 = 扫描或断链事故）

```javascript
// 三层防
if (!isUUID(params.id)) return notFoundGateway(404, { ttl: 3600})   // 零 DB，负缓存
const item = await itemCache.get(md5) ?? null
if (!item) { await markMissingRecently(id); return notFoundGated() }  // 负缓存 1h
// 410：res.status(410) + gone 页（SEO 删档语义）
```
