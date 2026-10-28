---
disableNunjucks: true
title: "1315 Go 写 ES 的设计要点：routing / ID / json 标签 / painless"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go · Elasticsearch 写入 | 难度：L3 | 题型：应用题 | 频率：中 | 关键词：**routing 同分片** / **业务唯一 ID** / **json 标签** / **painless 脚本** / **seq_no 保序**
> 原文锚点：第 11~42 段「insert/bulkinsert 封装；写入带 routing 让同维度数据同分片提查询效率；更新用业务唯一ID否则ES自动生成；结构体必须 json 标签；withSeqNo+primaryTerm 保 bulk 顺序；painless 脚本更新」

## 一句话总述
用 Go 写 ES 的四个设计要点：**routing**（写入指定路由键，让同维度数据落到同一分片，查询时定向扫一片、避免全集群扫描）、**ID 策略**（需更新用业务唯一键作 ID，否则让 ES 自动生成）、**结构体 json 标签**（字段名与 ES mapping 一一对应）、**painless 脚本**（做部分字段更新等复杂写）。bulk 写入可用 `_seq_no`+`_primary_term` 保顺序。

## 面试官视角
- 意图：是否理解"写入侧 routing 是为了查询侧提速"这一设计闭环。
- P5 知写入要 json 标签、更新用业务 ID；P6 知 routing 让同维度同分片、提查询效率；P7 知 bulk 用 seq_no+primary_term 保顺序、painless 做部分更新。
- 红旗：以为 routing 只为写入快；或不知道 ES 自动生成 ID 与业务 ID 的差异。
- 惊艳点：点出"routing 的本质是控制数据分布，查询侧偏好本地分片才有意义" `[边界]` 见 1314（索引/文档 API）、1312-seqno-primaryterm（seq_no 机制）、1314-bulk-processor（bulk 内存风险）。

## 主问答
**Q（面试官原话）：** 用 Go 写 ES 要注意哪些设计点？
**A：**
1. **routing 控制分布**：写入时带 `routing`（如用户维度），同维度数据落到同一分片；查询时按同 routing 定向扫该分片，避免全集群扫描、提效率。
2. **ID 策略**：文档需后续更新→用业务唯一键作文档 ID（幂等更新）；不更新的数据→让 ES 自动生成 ID 即可。
3. **json 标签**：Go 结构体字段必须加 `json` tag，tag 名才与 ES 字段名对应，否则序列化字段对不上 mapping。
4. **painless 与保序**：部分字段更新可用 painless 脚本；bulk 批量写入用 `_seq_no`+`_primary_term` 保证顺序，避免并发覆盖。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | json 标签 | 基础 | 字段名对应 mapping | 换题 |
| L2 | ID 怎么选 | 设计 | 需更新用业务 ID | 判 P5 |
| L3 | routing 干嘛 | 架构 | 同维度同分片提查询 | 判 P6 |
| L4 | 保序 | 机制 | seq_no+primary_term | 判 P6+ |
| L5 | painless | 进阶 | 部分更新脚本 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ES 全版本 | routing 语义不变 | routing/hash 取模分片；ES7 单类型后 routing 更直接 |

## 关键代码
```go
// 示意：Go 结构体写 ES（routing + json 标签 + 业务 ID），未做端到端验证
type Doc struct {
    Name string `json:"name"` // json tag 对应 ES 字段
    Age  int    `json:"age"`
}
// 需更新 → 业务唯一 ID；写入带 routing 让同用户数据同分片
req := esapi.IndexRequest{
    Index:      "user",
    DocumentID: bizUID,   // 业务唯一键
    Routing:    &userID,  // routing 控分布
    Body:       strings.NewReader(marshal(Doc{Name: "x", Age: 1})),
}
req.Do(ctx, client)
```

## 总结与追问预判
- 写 ES：routing 控分布、ID 看是否更新、json 标签必加、painless 做部分更新、bulk 用 seq_no 保序。
- 预判：seq_no 机制 → 见 1312；文档/索引 API → 见 1314；bulk 风险 → 见 1314。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（英文专有名词被错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：routing 控分布提查询、业务 ID 幂等更新、json 标签对应 mapping、seq_no 保 bulk 顺序、painless 部分更新——均正确，未做更正。
