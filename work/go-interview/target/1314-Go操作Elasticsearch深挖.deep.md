# 1314 Go 操作 Elasticsearch（深挖）

> 分类：Go · Elasticsearch 客户端 | 难度：L4 | 题型：设计题 | 频率：中 | 关键词：**客户端架构**/**写入管线**/**查询封装**
> 原文锚点：第 1~111 段「使用 Go 操作 Elasticsearch 全貌」

## 思路与架构
整体分三层：
1. **连接层**：client 池（多实例 map）+ ClientConfig + sync.Map 索引缓存 + 函数选项模式初始化；production 关 sniff。
2. **写入层**：单条 Index（OpType/refresh/routing）与 bulk 处理器（workers goroutine + 三触发条件 + afterFunction 回调）双通道。
3. **查询层**：Get/MGet/Query/Scroll 四类封装，结果统一 hits 遍历 + json 反序列化；深翻页用 scroll 回调。

## 方案取舍
- **olivere/elastic vs 官方 SDK**：第三方易用但 ES7 停维护，官方 API 全但繁琐——新项目选官方。
- **单条写 vs bulk**：单条简单但慢、且默认不 refresh 不可立即查；bulk 吞吐高但占内存缓冲，须调三参数。
- **refresh=true vs false**：true 实时可见但刷分片开销大；false 性能优先，靠 refresh_interval 周期可见——写入默认 false。
- **scroll vs from/size**：深翻页用 scroll（游标+回调）避免内存爆；ES 新版本推荐 PIT+search_after。

## 答题技巧
- 答「Go 怎么操作 ES」用**分层法**：连接→写入→查询，每层点一个「坑」（嗅探、内存、深翻页）。
- 必提 bulk 的**三触发条件**与**内存风险**，这是最容易体现实战经验的点。
- 被追问版本时，直接用「官方 SDK /v8 对应 ES8」对齐，展示你知道版本耦合。
- 主动补一句「scroll 已被 PIT+search_after 替代」，体现你跟进了新版最佳实践。

## 细节与核心 API

**官方 SDK 初始化（v8，生产关 sniff）：**

```go
es, err := elasticsearch.NewClient(elasticsearch.Config{
    Addresses: []string{"https://es:9200"},
    Username:  "elastic",
    Password:  "***",
    // 生产关闭 sniff（容器/云托管拓扑下嗅探反而错）
})
```

**写入双通道：单条 Index + bulk 处理器：**

```go
// 单条写：OpType/index、refresh、routing
_, err := es.Index("orders",
    bytes.NewReader(doc),
    es.Index.WithRouting("uid123"),
    es.Index.WithRefresh("false")) // 写入默认不 refresh，不可立即查

// bulk 处理器：workers goroutine + 三触发（flush bytes / actions / interval）+ afterFunction 回调
bulk := esutil.NewBulkIndexer(esutil.BulkIndexerConfig{
    Index:         "orders",
    NumWorkers:    4,
    FlushBytes:    5 << 20,
    FlushInterval: 10 * time.Second,
})
_ = bulk.Add(ctx, esutil.BulkIndexerItem{
    Action: "index", Routing: "uid123",
    Body: bytes.NewReader(doc),
    OnSuccess: func(ctx, it, res) {},
})
_ = bulk.Close(ctx)
```

**查询封装（Get/MGet/Query/Scroll 四类）：**

```go
// 深翻页用 scroll 回调，用完 clearScroll；新版优先 PIT + search_after（见 1311）
```
1. 事实核校： [经验] 三层架构、SDK 选型、bulk 三条件、refresh 默认 false、scroll 深翻页——均正确，本卡为架构性归纳。
2. 崩坏词归一：源码将 Elasticsearch 音译为崩坏词，本卡统一为 Elasticsearch；源码将 bulk 音译为 bug（本卡统一为 bulk）；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
