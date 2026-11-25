---
title: [NODE-278] SSR 内存泄漏的定位与防护？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-278：SSR 内存泄漏的定位与防护？
**答**:
- SSR 泄漏三大源：模块级缓存无上限（每请求写 Map）、事件监听未清理（请求级订阅）、闭包持有请求上下文（长生命周期对象引用请求对象）。
- 定位：heap snapshot diff（NODE-083）按 constructor 分组找增长点；async_hooks 追踪请求级资源是否释放。
- 防护：请求级缓存用 ALS（NODE-256）自动随请求结束释放；模块级缓存全部带上限/TTL；监控 RSS 增长率 + max_memory_restart 兜底。
- 压测验证：持续压 1 万请求后 RSS 稳定（增长 < 5%）才算过。

```javascript
// 泄漏源示例与修复
// 反模式：模块级缓存
// const pageCache = new Map(); pageCache.set(url, html)   // 无上限 → 泄漏
// 修复：LRU + 上限
const pageCache = new LRUCache(500, 60_000);      // NODE-283
// 请求级上下文：ALS 自动释放
const als = new AsyncLocalStorage();
app.use((ctx, next) => als.run({ reqId: ctx.id }, next));   // 请求结束 GC 自动回收
// 压测回归：
// autocannon -c 100 -d 300 → 观察 rss 曲线；两次 heap snapshot diff by constructor
```
