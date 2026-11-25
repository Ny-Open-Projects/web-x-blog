---
title: [NODE-225] 流在 Node 全链路中的位置综述？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-225：流在 Node 全链路中的位置综述？
**答**：
- 综述框架：按数据进出方向盘点——上行（请求体流式解析/文件上传分片）、处理（Transform ETL/压缩）、下行（大响应下载/SSE/视频渐进）。
- 核心不变式：任何"Buffer 整体加载"替代流的地方都是内存风险点；pipeline 是组合的默认姿势（NODE-212）。
- 与框架的关系：Express/Koa 的 req/res 就是流（http.IncomingMessage/ServerResponse）——框架中间件里的流式处理直接用原语。
- 面试表达：给一个"1GB 文件上传→转码→存储"的全流式链路图，标注每段的背压来源与水位线。

```javascript
// 全流式链路一页纸
// 上行：req（IncomingMessage）→ Transform（解密）→ Transform（gzip 解压）→ 行解析 → DB 批量
await pipeline(
  req,                                             // 客户端上行流（背压来源：网络+res 侧）
  createDecipheriv(...),
  createGunzip(),
  new CsvBatch(insertBatch),                       // NODE-215：批插 DB
);
// 下行：DB cursor（pg-cursor 流式）→ Transform 装配 → gzip → res
await pipeline(
  cursorStream(query),                             // 游标流式拉取
  new CsvSerialize(),
  createGzip(),
  res,                                             // 客户端慢 → 全链背压
  { signal: req.abortSignal },
);
// 面试金句："流的本质是让内存占用与数据规模解耦——buffer O(file) vs stream O(chunk)"
```
