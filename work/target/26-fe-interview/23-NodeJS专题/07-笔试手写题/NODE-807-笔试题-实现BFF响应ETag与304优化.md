---
title: [NODE-807] 笔试题——实现 BFF 响应 ETag 与 304 优化（大响应）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-807：手写 ETag 优化

**需求与边界**：
- 需求：ETag 协商缓存（SCN-NODE-692）——① ETag 生成（数据版本驱动——SCN-NODE-803 数据版本键，不 hash body——大响应 hash 贵）；② If-None-Match 校验 → 304（省传输）；③ 弱 ETag（动态内容微变容忍）；④ Vary 一致（SCN-NODE-777 校验联动）。
- 边界：① ETag 计算成本（数据版本 hash 比 body hash 便宜——缓存友好）；② 304 的收益判断（大响应才值得——SCN-NODE-692 成本评估）；③ ETag 与压缩共存（gzip 后的 ETag——Vary: Accept-Encoding）。

**答**：
```javascript
function etagMiddleware() {
  return async (req, res, next) => {
    const dataVer = await dataVersion(req.url);        // 数据版本（SCN-NODE-803——不 hash body）
    const etag = `W/"${sha256([dataVer, req.profile, req.grayBucket]).slice(0, 16)}"`;   // 弱 ETag + 维度
    res.setHeader('ETag', etag);
    res.setHeader('Vary', 'Accept-Encoding, X-Gray-Bucket');   // SCN-NODE-777 Vary
    if (req.headers['if-none-match'] === etag) {
      res.status(304).end();                           // 304 省传输
      telemetry.count('etag-304');
      return;
    }
    next();
  };
}
// 大响应才启用（SCN-NODE-692 成本评估）
if (route.expectSize > 50_000) router.use(etagMiddleware());
```

**评分点**:
- 数据版本驱动 ETag（不 hash body——大响应省计算，SCN-NODE-803 联动）。
- 弱 ETag + 维度组合（profile/gray 进 ETag——Vary 一致）。
- 304 短路 + 计数（可观测）。
- 大响应才启用（成本评估——SCN-NODE-692）。
