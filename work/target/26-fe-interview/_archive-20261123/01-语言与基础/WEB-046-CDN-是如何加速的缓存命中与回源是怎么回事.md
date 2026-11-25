---
title: [WEB-046] CDN 是如何加速的？缓存命中与回源是怎么回事？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-046：CDN 是如何加速的？缓存命中与回源是怎么回事？
**答**：
- CDN 把静态资源分发到离用户最近的边缘节点；DNS 智能调度（CNAME 到 CDN 调度系统）把用户解析到最优节点。
- 边缘节点有缓存直接返回（命中率是核心指标）；未命中回源站拉取并缓存（回源），大量并发未命中会造成"缓存击穿"，可用请求合并/预热缓解。
- 缓存更新靠 URL 版本化（hash 文件名）主动刷新，或调 CDN 刷新接口；回源请求一般带 `Via`/`X-Cache` 头可观测。
- 动静分离：HTML/接口不进 CDN 或短 TTL，图片/JS/CSS 长缓存 + hash。

```bash
# 观察 CDN 命中情况：X-Cache 头显示 HIT/MISS，Via 显示经过的节点
curl -sI https://cdn.example.com/static/app.js | grep -Ei 'x-cache|via|age|cache-control'
# X-Cache: HIT          命中边缘缓存
# X-Cache: MISS         未命中，触发回源
# Age: 120              缓存已存活 120 秒

# 查看域名是否 CNAME 到 CDN 调度
dig www.example.com +noall +answer | grep CNAME
```

```javascript
// 回源头与命中率的可观测性：服务端打印命中状态
app.use((req, res, next) => {
  const originalEnd = res.end.bind(res);
  res.end = (...args) => {
    const xCache = res.getHeader('x-cache'); // 经 CDN 转发后可读到 HIT/MISS
    if (xCache === 'MISS') {
      console.warn(`cache miss, origin hit: ${req.url}`); // 监控回源率与击穿
    }
    originalEnd(...args);
  };
  next();
});
```
