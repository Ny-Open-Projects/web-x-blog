# 1314 Go ES 查询 API（get/mget/query/scroll）

> 分类：Go · Elasticsearch 查询 | 难度：L3 | 题型：应用题 | 频率：高 | 关键词：**Get by ID+routing**/**MGet**/**Query DSL**/**ScrollQuery 回调**/**结果反序列化**
> 原文锚点：第 98~111 段「查询方法的封装与结果处理」

## 一句话总述
查询封装在 query.go：GetAPI 按 ID+routing 取单文档、MGet 批量取、Query 传 DSL（enableDSL 可打印）、ScrollQuery 滚游标并用回调函数逐批把文档回给业务方；结果集遍历 hits 数组、json 反序列化得具体文档。

## 面试官视角
- 考察意图：知不知道「深翻页用 scroll 而非 from/size」，以及结果集怎么解析。
- 分档：P5 知 Get 按 ID 取；P6 知 MGet 批量、enableDSL 调试；P7 知 ScrollQuery 游标+回调、结果反序列化。
- 红旗答案：深翻页用 from/size 一直翻；或不知道 MGet 批量取。
- 惊艳点：点出「scroll 用游标+回调避免一次性加载全量，适合海量导出」。

## 主问答
**Q（面试官原话）：** 查询结果怎么取、深翻页怎么做？
**A：**
1. **单文档**：GetAPI 按 doc ID + routing 取指定文档（routing 错会取不到）。
2. **批量文档**：MGet 依次获取多个文档，减少往返。
3. **条件查询**：Query 传 DSL，enableDSL=true 可打印发出的查询语句便于调试。
4. **结果解析**：返回结果集，遍历 hits 数组，对每篇文档 json 反序列化得实体。
5. **深翻页**：ScrollQuery 滚动游标，在循环里不断滚动，用回调函数把每批文档返回业务方，避免一次性加载全量。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 按 ID 取文档？ | 基础 | Get + routing | P5 |
| L2 | 批量取？ | 优化 | MGet | P6 |
| L3 | DSL 怎么调试？ | 工具 | enableDSL 打印 | P6 |
| L4 | 深翻页怎么做？ | 原理 | scroll 游标 | P7 |
| L5 | scroll 代价？ | 进阶 | 占 search context，需主动清 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 7.0+ | scroll 在新版被 search_after/PIT 取代建议 | 新项目用 PIT + search_after 替代 scroll |

## 关键代码
```go
// 按 ID + routing 取
res, _ := cli.Get().Index("netdisk").Id("doc-1").Routing("u123").Do(ctx)
// scroll 深翻页（回调返回每批）
_ = ScrollQuery(ctx, dsl, func(hit Hit) { process(hit) })
```

## 总结与追问预判
查询 API 分层：单条 Get、批量 MGet、条件 Query、深翻页 Scroll；结果统一反序列化。下一步可谈「scroll 已被 PIT+search_after 替代」的新实践。

## ⚠️ 原文纠错
1. 事实核校： [经验] Get 带 routing、MGet 批量、Query 传 DSL+enableDSL、结果遍历 hits 反序列化、ScrollQuery 游标+回调——均正确。
2. 崩坏词归一：源码将 init 音译为 NITES、MarshalJSON 音译为 martialjason、MGet 音译为 m的gate、ScrollQuery 音译为 scorequery；源码将 Elasticsearch 音译为崩坏词，本卡统一为 Elasticsearch；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
