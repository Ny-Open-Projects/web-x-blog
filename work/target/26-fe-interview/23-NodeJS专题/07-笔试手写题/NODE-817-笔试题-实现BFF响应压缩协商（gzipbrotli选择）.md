---
title: [NODE-817] 笔试题——实现 BFF 响应压缩协商（Accept-Encoding 分级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-817：手写压缩协商

**需求与边界**：
- 需求：响应压缩协商（SCN-BLD-213）——① Accept-Encoding 解析（brotli > gzip > identity——按质量值 q 协商）；② 压缩阈值（<1KB 不压缩——CPU 收益低于开销）；③ 压缩级别分级（静态资源高压缩/CPU 动态响应中压缩——CPU 权衡）；④ Vary 头（SCN-NODE-692）。
- 边界：① 大响应的流式压缩（不 whole-buffer——内存守恒，SCN-NODE-725）；② brotli 的 CPU 成本（q11 慢——动态响应用 q4~5，静态预压缩 q11）；③ 压缩与 ETag 共存（ETag 强 ETag 在压缩后变化——弱 ETag + Vary，SCN-NODE-807）。

**答**：
```javascript
function compressionMiddleware({ threshold = 1024, dynamicLevel = 5 } = {}) {
  return (req, res, next) => {
    const accepted = parseAcceptEncoding(req.headers['accept-encoding']);   // { brotli: 1, gzip: 0.9 }
    const algo = pickBest(accepted);                   // brotli 优先（体积最优）
    res.setHeader('Vary', 'Accept-Encoding');          // SCN-NODE-692
    if (!algo) return next();
    const size = +res.getHeader('Content-Length') ?? Infinity;
    if (size < threshold) return next();               // 小响应不压缩（CPU 收益低）
    const level = size > 1e6 && isStatic ? 11 : dynamicLevel;   // 静态高压缩/动态中压缩（CPU 权衡）
    const stream = algo === 'br' ? zlib.createBrotliCompress({ params: level })
      : zlib.createGzip({ level });
    res.setHeader('Content-Encoding', algo);
    pipeline(res.locals.bodyStream, stream, res);      // 流式压缩（内存守恒——SCN-NODE-725）
  };
}
```

**评分点**:
- Accept-Encoding 按 q 协商（brotli 优先）。
- 阈值 + 分级压缩（CPU 权衡——静态 11/动态 5）。
- 流式压缩（内存守恒——SCN-NODE-725 背压）。
- Vary + 弱 ETag（SCN-NODE-692/807 联动）。
