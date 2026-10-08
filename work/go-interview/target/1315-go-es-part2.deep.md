# 1315 Go 操作 Elasticsearch（二）深挖

> 分类：Go · Elasticsearch | 难度：L3 | 题型：深挖 | 频率：中 | 关键词：**官方 SDK** / **HTTPS** / **routing** / **preference** / **scroll 内存**
> 原文锚点：第 1~47 段「官方 SDK 两级封装+HTTPS；写入 routing/ID/json/painless/seq_no；查询 preference/scroll clearScroll」

## 思路与架构
Go 操作 ES（二）把"客户端封装 → 写入设计 → 查询优化"串成一条线，且与（一）互补：（一）偏连接管理与基础 API，（二）偏官方 SDK 视角与工程优化细节。

## 方案取舍
```text
Go 操作 ES 两讲的职责切分：
──────────────────────────────────────────────────────
(一) 1314-*          连接池封装 / 两种 SDK 取舍 / bulk 处理器 / 索引文档 API / 查询 API
(二) 1315-*（本波）   官方 SDK 两级封装 + HTTPS/TLS / 写入 routing·ID·json·painless / 查询 preference·scroll 内存

写入设计取舍：
routing   → 控数据分布，查询侧定向扫一片（非为写快）
ID        → 需更新用业务唯一键（幂等）/ 否则 ES 自动生成
json 标签 → 字段名与 mapping 对应，缺则串行错
painless  → 部分字段更新等复杂写
查询优化取舍：
preference → 本地分片优先，命中缓存、减跨节点
scroll     → 用完 clearScroll；scrollID 变化才清旧，防误清在用游标
```

## 答题技巧
```text
面试话术（按"初始化→写入→查询"顺序）：
1. 初始化：官方 SDK 两级封装(newclient 原始 DSL / newtype 高层)；HTTPS 配 transport+TLSConfig
2. 写入：routing 控分布提查询 / 业务 ID 幂等更新 / json 标签对应 / painless 部分更新 / bulk 用 seq_no 保序
3. 查询：preference 本地分片提缓存命中 / scroll 用完 clearScroll 且 scrollID 变化才清旧
4. 收尾：新版深翻页用 PIT+search_after 替代 scroll；生产 HTTPS 应校验证书
```

> 边界：连接池封装见 1314-client-init；两种 SDK 取舍见 1314-go-es-sdk-choice；索引/文档 API 见 1314-doc-index-api；查询 API 见 1314-query-api；bulk 风险见 1314-bulk-processor；seq_no 机制见 1312-seqno-primaryterm；深翻页替代见 1311-search-after。本卡只深挖"Go 操作 ES（二）"不重述（一）各机制。
