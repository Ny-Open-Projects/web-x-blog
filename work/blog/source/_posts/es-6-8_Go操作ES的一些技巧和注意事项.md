---
disableNunjucks: true
title: "Go操作ES的一些技巧和注意事项"
date: 2026-10-04 03:05:00
categories: [Elasticsearch, Go]
tags: [es-go, 函数选项模式, routing, Scroll, Bulk, 版本控制]
---

# Go操作ES的一些技巧和注意事项

本篇继续讲 Go SDK 对 ES 的封装，聚焦**查询链路**：`Get / MGet / Query / Scroll` 四个接口，以及它们共同的几个「保命细节」——`routing`、`preference`、`_source` 字段裁剪、Scroll 上下文释放、批量写入的 `bulkProcessor` 提交时序、基于版本的并发控制。演示基于 **ES 8.2.2**。

## 纲要

- 函数选项模式封装查询参数（排序/高亮/_source/慢查阈值/preference）
- `Get`/`MGet` 必须带 `routing`，否则按 `_id` 路由可能取不到文档
- `preference` 优先本地分片，提升缓存命中、避免跨节点
- 单索引 + 指定 routing 比多索引查询高效；多索引 + routing 会把 routing 作用到所有索引
- `Scroll` 滚动查询要手动释放上下文，否则吃内存
- 批量 `bulkProcessor` 需 sleep 等提交；`updateWithVersion` 做乐观锁

## 查询封装与 routing / preference

封装查询时参数多，用**函数选项模式**（Functional Options）很合适：定义 `QueryOption` 结构体，再提供一组函数把选项注入，调用侧按需选用。

```mermaid
flowchart LR
    A["调用方 query"] --> B["构造 SearchSource"]
    B --> C["设置 _source 字段"]
    B --> D["设置 sort/highlight/profile"]
    C --> E["SearchService.do"]
    D --> E
    E --> F{"带 routing?"}
    F -- 是 --> G["显式传入 routing"]
    F -- 否 --> H["按 _id 路由全分片扫"]
```

```go
// Get 必须带 routing：文档写时指定了 routing，
// 读时不带会按 _id 路由，分片不一致就取不到
getSvc := client.Get().Index(idx).Id(id).Routing(routing)
```

```dir
ES Go SDK 查询封装/
├── Get/                # 按 ID 取，须带 routing
├── MGet/               # 多文档，逐项指定 index+id+routing
├── Query/              # match 查询
│   ├── _source 裁剪
│   ├── sort/highlight
│   └── preference
└── Scroll/             # 滚动查询 + 释放上下文
```

`preference` 默认从本地分片取数：副本也能提供查询，本地命中既能避免跨节点转发，又提高缓存命中率。`MGet` 支持从不同索引取文档，所以每个 item 都要带自己的 `index/id/routing`。

## _source 裁剪与 DSL 打印

查询不是字段越多越好——大文本字段拉全对 ES 压力很大。用 `_source` 只取需要的字段：

```go
src := elastic.NewFetchSource()
src.Include("name", "price")   // 只取这些
src.Exclude("bigContent")      // 或排除某些
```

开启 debug / `enableDSL` 时打印 DSL 便于排查；注意 **DSL 里不带 routing，需单独把 routing 打印出来**：

```go
if debug || opt.EnableDSL {
    log.Printf("DSL: %s | routing: %s", src.Source(), routing)
}
```

> 多索引查询 + routing 的坑：routing 会被依次作用到传入的所有索引上，路由到过多分片。建议**查单索引 + 指定 routing**，最高效。

## Scroll 滚动查询与资源释放

`Scroll` 适合深度遍历，但会占用大量上下文内存，**结束务必释放**：

```go
scrollSvc := client.Scroll(idx).Size(1000).Routing(routing)
for {
    res, err := scrollSvc.Do(ctx)
    if err == io.EOF { // 滚完
        break
    }
    // 回调通知调用方每批结果
    callback(res)
}
// 手动清上下文，别等自动过期
client.ClearScroll(idx).Do(ctx)
```

慢查阈值命中时把 DSL 打印出来定位问题。不要在回调里做耗时操作，否则游标超时断开、后续数据丢失——先把结果攒到本地 slice 再统一处理。

## 批量写入与版本控制

批量写用 `bulkProcessor` 异步提交到 channel，**主进程退出前必须 sleep 等它刷完**，否则文档没提交就丢了：

```go
// BulkReplace：routing 和 id 都设为 docID
processor.Add(bulkBulkReplaceReq)
time.Sleep(time.Second * 2) // 等 processor 提交
```

基于版本的乐观锁控制并发更新：

```go
// 版本号必须 > 当前已写入版本才成功，否则报版本冲突
_, err := svc.UpdateWithVersion(ctx, idx, id, doc, 3)
// 版本冲突时不更新，name 保持原值 —— 符合预期
```

| 细节 | 正确做法 | 错误后果 |
| --- | --- | --- |
| `Get`/`MGet` routing | 写时带则读必带 | 按 `_id` 路由取不到 |
| `preference` | 默认本地分片 | 跨节点 + 缓存命中低 |
| 多索引 + routing | 改查单索引 + routing | 路由过多分片 |
| `Scroll` 上下文 | 结束 `ClearScroll` | 长期占内存 |
| `bulkProcessor` | 退出前 sleep 等提交 | channel 未提交文档丢失 |
| 版本控制 | `version` 须大于当前 | 版本冲突不更新 |

## 总结

Go 操作 ES 的查询封装，难点不在 API 调用，而在那些「不报错但会出事」的细节：**routing 读写必须对称**（写时带 routing，Get/MGet/Query 读时也要带，否则按 `_id` 路由取不到）；**多索引查询别带 routing**（会被作用到所有索引）；**Scroll 一定手动 ClearScroll**；**bulkProcessor 退出前 sleep 等提交**；**并发更新用 `updateWithVersion` 做乐观锁**。把这些细节固化进 SDK 封装层，业务代码才不会反复踩坑。
