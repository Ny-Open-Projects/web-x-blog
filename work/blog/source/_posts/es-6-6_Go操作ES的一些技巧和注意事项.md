---
title: "Go 项目开发: Go操作ES的一些技巧和注意事项"
date: 2026-10-02 11:05:00
categories: [es, Go, Elasticsearch]
tags: [olivere/elastic, 客户端封装, bulk处理器, 版本冲突, 查询封装, scroll]
disableNunjucks: true

---

# Go 项目开发: Go操作ES的一些技巧和注意事项

Go 操作 ES 的内容看着杂，其实就四块：**客户端怎么初始化、索引怎么建、文档怎么增删改、查询怎么封装**。本节按这四块展开，重点落在**封装里那些"不加就会踩坑"的细节**上：bulk 的三个提交阈值、`refresh` 的三个取值、`external` 版本号怎么比大小、查询为什么必须带 routing、scroll 为什么用完要清上下文。

## 纲要

- ES 版本与 Go SDK 的对应关系，为什么推荐 7.x
- 客户端封装：函数选项模式、client map、bulk 处理器、健康检查与嗅探
- 读写分离：协调节点与 ingest 节点拆成两个 client
- bulk 处理器的三个阈值与失败回调
- 索引操作：是否存在（本地缓存慎用）与创建索引
- 文档写入：`refresh` 的三个取值与 bulk 的两种提交方式
- 版本冲突：`external` 版本号规则、upsert 的两种写法
- 更新与删除：update、updateByQuery、deleteByQuery 与版本冲突处理
- 查询封装：get、mget、query（函数选项模式）、scroll
- 验证演示与注意事项总结

## ES 版本与 SDK 的对应关系

| ES 版本 | Go SDK 包 | 依赖管理 |
| --- | --- | --- |
| 5.x | `gopkg.in/olivere/elastic.v5` | dep / vendor |
| 6.x | `github.com/olivere/elastic` | 无版本号后缀 |
| 7.x | `github.com/olivere/elastic/v7` | **go.mod** |
| 8.x | 兼容，继续用 v7 包 | go.mod |

关键点有三个：

1. **只有 7.x 走了 go.mod**。5.x / 6.x 的仓库没带 go.mod，得靠 `dep`、vendor 或者老式 `go get` + 手工配 GOPATH，搬进 CI 一堆麻烦。
2. **8.x 可以继续使用 v7 的包**，改个集群地址就行，不用为升版本重写业务代码。
3. **新项目优先选 7.x 或 8.x 集群**，被历史包袱拖着是最亏的。

下面所有代码基于 `github.com/olivere/elastic/v7`（v7 分支停在 7.0.32，以下 API 均按该版本核对过）。

## 客户端封装（函数选项模式）

封装目的之一是**支持一个进程连多个集群**，所以用一个 `clientMap`，按 `clientName` 取客户端。参数项很多（是否开日志、慢查询日志、bulk 配置、调试模式……），用**函数选项模式**最干净。

### 客户端、bulk 配置与索引操作

bulk 处理器是 SDK 内置的后台批量提交组件：业务把请求往 channel 里丢，它按阈值攒批后真正发给 ES。三个阈值 —— **刷新时间、提交文档数、提交文档大小** —— 任意一个先到就提交一次。

```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"sync"
	"time"

	"github.com/olivere/elastic/v7"
)

// EsClient ES 客户端封装
type EsClient struct {
	clientName string                 // 客户端标识，多集群靠它区分
	client     *elastic.Client
	username   string
	password   string
	bulk       *elastic.BulkProcessor // 全局 bulk 处理器
	indexCache sync.Map               // 索引是否存在的本地缓存
	lock       sync.Mutex             // 创建索引的并发锁
}

// defaultBulk 默认 bulk：3 个 worker、1 秒刷新、500 条或 5MB 提交
func defaultBulk(client *elastic.Client) *elastic.BulkProcessorService {
	after := func(executionID int64, requests []elastic.BulkableRequest,
		response *elastic.BulkResponse, err error) {
		if err != nil {
			// 生产里按错误码分流：可重试的进重试队列，其余落存储留待补偿
			fmt.Println("bulk submit error, execID:", executionID, "err:", err)
			return
		}
		if response != nil && response.Errors {
			fmt.Println("bulk has failed items:", len(response.Items))
		}
	}
	return elastic.NewBulkProcessorService(client).
		Name("es-bulk").
		Workers(3).
		BulkActions(500).
		BulkSize(5 * 1024 * 1024).
		FlushInterval(time.Second).
		After(after)
}

// options 客户端初始化时的可选项，配合函数选项模式使用
type options struct {
	enableLog     bool
	enableSlowLog bool
	bulkService   *elastic.BulkProcessorService
	debug         bool
}

type option func(*options)

func WithLog() option                   { return func(o *options) { o.enableLog = true } }
func WithSlowLog() option               { return func(o *options) { o.enableSlowLog = true } }
func WithDebug() option                 { return func(o *options) { o.debug = true } }
func WithBulkService(s *elastic.BulkProcessorService) option {
	return func(o *options) { o.bulkService = s }
}

var (
	clientMap     = make(map[string]*EsClient)
	clientMapLock sync.Mutex
)

// InitClient 按名字初始化 ES 客户端，重复调用直接复用
func InitClient(clientName string, urls []string, user, pwd string, opts ...option) (*EsClient, error) {
	clientMapLock.Lock()
	defer clientMapLock.Unlock()

	if c, ok := clientMap[clientName]; ok {
		return c, nil
	}
	o := &options{bulkService: defaultBulk(nil)}
	for _, fn := range opts {
		fn(o)
	}

	// 15 秒一次健康检查；关掉 sniff，请求只打协调节点
	opts2 := []elastic.ClientOptionFunc{
		elastic.SetURL(urls...),
		elastic.SetBasicAuth(user, pwd),
		elastic.SetHealthcheckInterval(15 * time.Second),
		elastic.SetSniff(false),
		elastic.SetHealthcheck(true),
	}
	if o.enableLog {
		opts2 = append(opts2, elastic.SetTraceLog(log.New(os.Stdout, "[es] ", log.LstdFlags)))
	}

	client, err := elastic.NewClient(opts2...)
	if err != nil {
		return nil, err
	}
	// bulk 处理器挂在 client 上，全局复用，业务只管往里 Add
	if o.bulkService == nil {
		o.bulkService = defaultBulk(nil)
	}
	processor, err := o.bulkService.Do(context.Background())
	if err != nil {
		return nil, err
	}

	clientMap[clientName] = &EsClient{
		clientName: clientName,
		client:     client,
		username:   user,
		password:   pwd,
		bulk:       processor,
	}
	return clientMap[clientName], nil
}

// GetClient 按名字取客户端
func GetClient(clientName string) (*EsClient, error) {
	c, ok := clientMap[clientName]
	if !ok {
		return nil, fmt.Errorf("es client not found: " + clientName)
	}
	return c, nil
}

// IndexExists 判断索引是否存在；firstCheck=true 强制查 ES，否则先查本地缓存
func (c *EsClient) IndexExists(ctx context.Context, index string, firstCheck bool) (bool, error) {
	if !firstCheck {
		if _, ok := c.indexCache.Load(index); ok {
			return true, nil
		}
	}
	exist, err := c.client.IndexExists(index).Do(ctx)
	if err != nil {
		return false, err
	}
	if exist {
		c.indexCache.Store(index, struct{}{})
	}
	return exist, nil
}

// CreateIndex 创建索引，body 就是 REST API 里的 mapping + settings 原样 JSON
func (c *EsClient) CreateIndex(ctx context.Context, index string, body string, firstCheck bool) error {
	c.lock.Lock()
	defer c.lock.Unlock()

	exist, err := c.IndexExists(ctx, index, firstCheck)
	if err != nil {
		return err
	}
	if exist {
		return nil
	}
	if _, err := c.client.CreateIndex(index).BodyString(body).Do(ctx); err != nil {
		return err
	}
	c.indexCache.Store(index, struct{}{})
	return nil
}

func main() {
	client, err := InitClient("ESDefaultClient", []string{"http://127.0.0.1:9200"}, "", "")
	if err != nil {
		panic(err)
	}
	body := `{
	  "settings": {"number_of_shards": 3, "number_of_replicas": 1},
	  "mappings": {"properties": {
	    "id": {"type": "keyword"},
	    "name": {"type": "text"},
	    "favorite": {"type": "long"}
	  }}
	}`
	if err := client.CreateIndex(context.Background(), "goods", body, true); err != nil {
		panic(err)
	}
	exist, _ := client.IndexExists(context.Background(), "goods", false)
	fmt.Println("goods exists:", exist)
}
```

四个容易踩的点：

- **`SetSniff(false)` 要显式关**。开了以后 SDK 每隔一段时间嗅探全集群节点、自动把新节点加进连接表；但生产有专门协调节点时请求只想打协调节点，嗅探反而把流量散到数据节点。
- **`SetURL` 支持可变参数，必须给多个地址**。只配一个，恰好这个节点下线，SDK 不会自动切到别的地址，读写直接失败。
- **`After` 回调里必须处理错误**。bulk 是异步的，`Do` 返回 nil 不代表写成功，失败只能在这个回调里捞。
- **索引本地缓存要慎用**：缓存能少发请求，但索引可能被别的实例或工单脚本删掉，本地缓存无从感知，后面写入会一直"以为索引在"。单实例、没人删索引才用缓存，多实例或有删除动作直接传 `firstCheck=true`。

### 读写分离：两套 client

有独立协调节点时，**读请求打协调节点、写请求打 ingest 节点**，两侧分开初始化：

```go
package main

import (
	"context"
	"fmt"

	"github.com/olivere/elastic/v7"
)

// coordURLs 三个读协调节点；ingestURLs 三个 ingest 节点
var (
	coordURLs  = []string{"http://node1.coord:9200", "http://node2.coord:9200", "http://node3.coord:9200"}
	ingestURLs = []string{"http://node1.ingest:9200", "http://node2.ingest:9200", "http://node3.ingest:9200"}
)

// QueryOnCoord 读请求走协调节点
func QueryOnCoord(index string, size int) (int64, error) {
	c, err := elastic.NewClient(elastic.SetURL(coordURLs...), elastic.SetSniff(false))
	if err != nil {
		return 0, err
	}
	result, err := c.Search().Index(index).Size(size).
		Query(elastic.NewMatchAllQuery()).Do(context.Background())
	if err != nil {
		return 0, err
	}
	return result.TotalHits(), nil
}

// IndexOnIngest 写请求走 ingest 节点
func IndexOnIngest(index string, id string) error {
	c, err := elastic.NewClient(elastic.SetURL(ingestURLs...), elastic.SetSniff(false))
	if err != nil {
		return err
	}
	_, err = c.Index().Index(index).Id(id).
		BodyJson(map[string]interface{}{"name": "x"}).Do(context.Background())
	return err
}

func main() {
	fmt.Println(QueryOnCoord("goods", 10))
	fmt.Println(IndexOnIngest("goods", "1"))
}
```

如果只有协调节点、且做了读写分离（6 个协调节点，3 个只收读、3 个只收写），那就初始化两个 client：`coordinatingWithRead` 传 3 个读协调节点，`coordinatingWithWrite` 传 3 个写协调节点，逻辑与上面对齐。

## 文档写入与 refresh 三值

写文档用 `IndexService`，opType 有两个取值：`create`（已存在就报错）、`index`（直接覆盖）。真正要讲清楚的是 `refresh`：

| refresh 取值 | 行为 | 代价 |
| --- | --- | --- |
| `false`（默认） | 不主动刷，写完约 1 秒后可见 | 实时性差，吞吐最高 |
| `true` | **立刻刷新该文档所在的主分片和副本分片** | 实时性高，集群吞吐明显下降 |
| `wait_for` | 等下一次刷新发生（约 1 秒）后才返回 | 折中，能确认写入已完成 |

批量有两种写法，适用不同场景：

- **单条丢进全局 bulk**：业务一次一个文档，`Add` 进去就完事，攒批由 `BulkProcessor` 托管（500 条 / 1 秒 / 5MB）。性能好，但**主进程退出前文档可能还压在 channel 里**，必须留等待时间或主动 flush。
- **一批文档实时提交**：直接 `Bulk().Add(...)` 一次打完，**立刻拿到 `BulkResponse`**，能逐条看成功失败；可用性要求高的场景用这种。

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/olivere/elastic/v7"
)

type Goods struct {
	ID       string `json:"id"`
	Name     string `json:"name"`
	Favorite int64  `json:"favorite"`
}

// DocClient 依赖 elastic.Client 的轻量封装，方便独立演示文档操作
type DocClient struct {
	client *elastic.Client
	bulk   *elastic.BulkProcessor
}

// InitDocClient 初始化文档操作客户端，顺带起一个全局 bulk 处理器
func InitDocClient(urls []string, user, pwd string) (*DocClient, error) {
	client, err := elastic.NewClient(
		elastic.SetURL(urls...),
		elastic.SetBasicAuth(user, pwd),
		elastic.SetSniff(false),
	)
	if err != nil {
		return nil, err
	}
	processor, err := elastic.NewBulkProcessorService(client).
		Name("doc-bulk").
		Workers(3).
		BulkActions(500).
		BulkSize(5 * 1024 * 1024).
		FlushInterval(time.Second).
		After(func(executionID int64, requests []elastic.BulkableRequest,
			response *elastic.BulkResponse, err error) {
			if err != nil {
				fmt.Println("bulk error:", err)
			}
		}).Do(context.Background())
	if err != nil {
		return nil, err
	}
	return &DocClient{client: client, bulk: processor}, nil
}

// CreateDoc 单条写入；refresh 显式传 false，避免误触发强制刷新
func (c *DocClient) CreateDoc(ctx context.Context, index, docID, routing string, doc interface{}) error {
	service := c.client.Index()
	if docID != "" {
		service = service.Id(docID)
	}
	if routing != "" {
		service = service.Routing(routing)
	}
	if _, err := service.Index(index).BodyJson(doc).Refresh("false").Do(ctx); err != nil {
		return err
	}
	return nil
}

// CreateDocWithVersion external 版本：只有传入版本大于 ES 现有版本才写入
func (c *DocClient) CreateDocWithVersion(ctx context.Context, index, docID string,
	doc interface{}, version int64) error {
	if _, err := c.client.Index().Index(index).Id(docID).BodyJson(doc).
		Version(version).VersionType("external").Do(ctx); err != nil {
		return err
	}
	return nil
}

// BulkCreateWithProcessor 单条丢进全局 bulk，攒批由 BulkProcessor 托管
func (c *DocClient) BulkCreateWithProcessor(index string, docs []Goods) {
	for _, d := range docs {
		c.bulk.Add(elastic.NewBulkIndexRequest().Index(index).Id(d.ID).Doc(d))
	}
}

// BulkReplaceNow 一批文档实时提交，立刻拿到每条结果
func (c *DocClient) BulkReplaceNow(ctx context.Context, index string, docs []Goods) error {
	service := c.client.Bulk().Index(index)
	for _, d := range docs {
		service = service.Add(elastic.NewBulkIndexRequest().Index(index).Id(d.ID).Doc(d))
	}
	resp, err := service.Do(ctx)
	if err != nil {
		return err
	}
	if resp.Errors {
		// 逐条看失败原因，version conflict 最常见
		fmt.Println("bulk part failed:", len(resp.Items))
	}
	return nil
}

// BulkDeleteNow 批量删除
func (c *DocClient) BulkDeleteNow(ctx context.Context, index string, ids []string) error {
	service := c.client.Bulk().Index(index)
	for _, id := range ids {
		service = service.Add(elastic.NewBulkDeleteRequest().Index(index).Id(id))
	}
	_, err := service.Do(ctx)
	return err
}

func main() {
	c, err := InitDocClient([]string{"http://127.0.0.1:9200"}, "", "")
	if err != nil {
		panic(err)
	}
	ctx := context.Background()

	if err := c.CreateDoc(ctx, "goods", "1", "", Goods{ID: "1", Name: "name-1", Favorite: 1}); err != nil {
		panic(err)
	}
	// ES 中版本是 1，传 1 会版本冲突，传 2 才成功
	fmt.Println(c.CreateDocWithVersion(ctx, "goods", "1",
		Goods{ID: "1", Name: "name-2", Favorite: 1}, 2))

	docs := []Goods{{ID: "0", Name: "name-0"}, {ID: "1", Name: "name-1"}}
	c.BulkCreateWithProcessor("goods", docs)
	_ = c.BulkReplaceNow(ctx, "goods", docs)
	fmt.Println(c.BulkDeleteNow(ctx, "goods", []string{"0", "1"}))
}
```

注意 `NewBulkCreateRequest` 与 `NewBulkIndexRequest` 的区别：**`index` 不管文档在不在都覆盖写，`create` 文档已存在就报错**。用 `index` 覆盖时，必须保证丢进去的同一 ID 文档是有序的，否则旧文档后到，会把它覆盖成"旧版本"。

## 更新、删除与 upsert

更新必须指定文档 ID；文档设了 routing，**routing 也必须传**，否则更新走不到目标分片。

```go
package main

import (
	"context"
	"fmt"

	"github.com/olivere/elastic/v7"
)

type Goods struct {
	ID       string `json:"id"`
	Name     string `json:"name"`
	Favorite int64  `json:"favorite"`
}

// UpdateDoc 部分字段更新，partial 里只放要改的字段
func UpdateDoc(ctx context.Context, client *elastic.Client, index, docID, routing string,
	partial map[string]interface{}) error {
	service := client.Update().Index(index).Id(docID)
	if routing != "" {
		service = service.Routing(routing)
	}
	if _, err := service.Doc(partial).Do(ctx); err != nil {
		return err
	}
	return nil
}

// UpsertDoc 文档存在就更新、不存在就整体写入；external 版本做乐观锁
func UpsertDoc(ctx context.Context, client *elastic.Client, index, docID string,
	partial map[string]interface{}, full interface{}, version int64) error {
	_, err := client.Update().Index(index).Id(docID).
		Version(version).VersionType("external").
		Doc(partial).
		Upsert(full).
		Do(ctx)
	return err
}

// DeleteByQuery 按条件删除；必须开 ProceedOnVersionConflict 才不会中途失败
func DeleteByQuery(ctx context.Context, client *elastic.Client, index string,
	query elastic.Query) error {
	_, err := client.DeleteByQuery(index).Query(query).
		ProceedOnVersionConflict().Do(ctx)
	return err
}

// UpdateByQuery 按条件批量更新，脚本用 painless
func UpdateByQuery(ctx context.Context, client *elastic.Client, index string,
	query elastic.Query) error {
	_, err := client.UpdateByQuery(index).Query(query).
		Script(elastic.NewScript("ctx._source.favorite += params.inc").
			Params(map[string]interface{}{"inc": 1}).
			Lang("painless")).
		ProceedOnVersionConflict().
		Do(ctx)
	return err
}

// GetDoc 按 ID 取文档
// 文档设了 routing 就必须带 routing，否则 SDK 拿 _id 当 routing 去路由，
// 分片不对就取不到（get 不像 query 那样扫全部分片）
func GetDoc(ctx context.Context, client *elastic.Client, index, docID, routing string) (
	*elastic.GetResult, error) {
	service := client.Get().Index(index).Id(docID)
	if routing != "" {
		service = service.Routing(routing)
	}
	return service.Do(ctx)
}

// MGetDoc 一次取多文档；支持跨索引，所以每个 item 都要带自己的 index 和 routing
func MGetDoc(ctx context.Context, client *elastic.Client, index, routing string,
	ids []string) ([]*elastic.GetResult, error) {
	service := client.Mget().Preference("_local")
	var items []*elastic.MultiGetItem
	for _, id := range ids {
		item := elastic.NewMultiGetItem().Id(id)
		if index != "" {
			item = item.Index(index)
		}
		if routing != "" {
			item = item.Routing(routing)
		}
		items = append(items, item)
	}
	result, err := service.Add(items...).Do(ctx)
	if err != nil {
		return nil, err
	}
	return result.Docs, nil
}

func main() {
	client, err := elastic.NewClient(
		elastic.SetURL("http://127.0.0.1:9200"),
		elastic.SetSniff(false),
	)
	if err != nil {
		panic(err)
	}
	ctx := context.Background()

	_ = UpdateDoc(ctx, client, "goods", "1", "", map[string]interface{}{"name": "name-2"})
	// ES 中版本已是 2，传 2 会冲突，传 3 才能覆盖
	fmt.Println(UpsertDoc(ctx, client, "goods", "1",
		map[string]interface{}{"name": "name-3"},
		Goods{ID: "1", Name: "name-3", Favorite: 1}, 3))

	fmt.Println(DeleteByQuery(ctx, client, "goods", elastic.NewTermQuery("name", "name-9")))
	fmt.Println(UpdateByQuery(ctx, client, "goods", elastic.NewMatchAllQuery()))

	if _, err := GetDoc(ctx, client, "goods", "1", ""); err != nil {
		fmt.Println("get err:", err)
	}
	docs, err := MGetDoc(ctx, client, "goods", "", []string{"0", "1", "2"})
	fmt.Println(len(docs), err)
}
```

`external` 版本的规则要记死：

- **写入/更新**：传入版本号必须**大于** ES 中现有版本才成功；ES 里没有该文档时直接写入（初始版本为 1）。
- **删除**：传入版本号同样必须大于现有版本才删得掉。
- `internal` 几乎不用。业务每次修改生成自增版本号（比如 `updated_at` 时间戳或 DB 乐观锁版本）一起提交，天然挡住"旧数据包后到覆盖新数据"。

一个反直觉的坑：`upsert` 传完整文档时**字段必须完整**，它拿整篇文档去覆盖已有文档；只想改部分字段，就用 `Doc(partial)` + `Upsert(full)` 这套组合 —— 找不到文档时才拿 `full` 补一条。

## 查询封装

查询参数多（排序、高亮、是否打印 DSL、返回字段、慢日志阈值、preference），继续用函数选项模式。

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"time"

	"github.com/olivere/elastic/v7"
)

type Goods struct {
	ID       string `json:"id"`
	Name     string `json:"name"`
	Favorite int64  `json:"favorite"`
}

// queryOptions 查询可选项
type queryOptions struct {
	sorts         []map[string]interface{}
	highlight     *elastic.Highlight
	enableDSL     bool
	include       []string
	exclude       []string
	slowThreshold time.Duration
	preference    string
}

type queryOption func(*queryOptions)

func WithSort(field string, desc bool) queryOption {
	return func(o *queryOptions) {
		dir := "asc"
		if desc {
			dir = "desc"
		}
		o.sorts = append(o.sorts, map[string]interface{}{field: dir})
	}
}
func WithHighlight(field string) queryOption {
	return func(o *queryOptions) { o.highlight = elastic.NewHighlight().Field(field) }
}
func WithDSL() queryOption                    { return func(o *queryOptions) { o.enableDSL = true } }
func WithInclude(fields ...string) queryOption { return func(o *queryOptions) { o.include = fields } }
func WithExclude(fields ...string) queryOption { return func(o *queryOptions) { o.exclude = fields } }
func WithSlowThreshold(d time.Duration) queryOption {
	return func(o *queryOptions) { o.slowThreshold = d }
}

// QueryDoc 单索引 + routing 查询；多索引时 routing 会被套用到每个索引上，
// 导致路由到过多分片，所以封装层面直接限定"单索引查询"
func QueryDoc(ctx context.Context, client *elastic.Client, index string, routing []string,
	from, size int, query elastic.Query, opts ...queryOption) (*elastic.SearchResult, error) {
	o := &queryOptions{preference: "_local", slowThreshold: 500 * time.Millisecond}
	for _, fn := range opts {
		fn(o)
	}

	start := time.Now()
	source := elastic.NewSearchSource().Query(query).From(from).Size(size)
	if len(o.include) > 0 || len(o.exclude) > 0 {
		fc := elastic.NewFetchSourceContext(true)
		if len(o.include) > 0 {
			fc = fc.Include(o.include...)
		}
		if len(o.exclude) > 0 {
			fc = fc.Exclude(o.exclude...)
		}
		source = source.FetchSourceContext(fc)
	}
	for _, s := range o.sorts {
		for field, dir := range s {
			source = source.Sort(field, dir == "asc")
		}
	}
	if o.highlight != nil {
		source = source.Highlight(o.highlight)
	}

	service := client.Search().IgnoreUnavailable(true).
		Preference(o.preference).
		Source(source)
	if len(routing) > 0 {
		service = service.Routing(routing...)
	}
	result, err := service.Do(ctx)

	cost := time.Since(start)
	if o.enableDSL && cost > o.slowThreshold {
		// 慢查把 DSL 打出来；DSL 里不含 routing，单独补一行方便复现
		src, _ := source.Source()
		body, _ := json.Marshal(src)
		fmt.Println("[slow-query]", cost, string(body), "routing:", routing)
	}
	return result, err
}

// ScrollDocs 滚动查询逐批回调；routing 必须带，跑完必须 Clear
func ScrollDocs(ctx context.Context, client *elastic.Client, index, routing string,
	size int, query elastic.Query, cb func(*elastic.SearchHit) error) error {
	source := elastic.NewSearchSource().Size(size).Query(query)
	scroll := client.Scroll().Index(index).Routing(routing).
		Body(source).KeepAlive("1m")

	for {
		result, err := scroll.Do(ctx)
		if err != nil {
			if err == io.EOF {
				break
			}
			return err
		}
		if result.Hits == nil || len(result.Hits.Hits) == 0 {
			break
		}
		for _, hit := range result.Hits.Hits {
			if err := cb(hit); err != nil {
				return err
			}
		}
		if result.ScrollId == "" {
			break
		}
	}
	// 滚动上下文即使会自动过期也要主动清，它长期占内存
	return scroll.Clear(ctx)
}

func main() {
	client, err := elastic.NewClient(
		elastic.SetURL("http://127.0.0.1:9200"),
		elastic.SetSniff(false),
	)
	if err != nil {
		panic(err)
	}
	ctx := context.Background()

	result, err := QueryDoc(ctx, client, "goods", []string{}, 0, 20,
		elastic.NewMatchQuery("name", "name"),
		WithSort("favorite", false),
		WithHighlight("name"),
		WithInclude("id", "name"),
		WithSlowThreshold(500*time.Millisecond),
	)
	if err != nil {
		panic(err)
	}
	var goods []Goods
	for _, hit := range result.Hits.Hits {
		var g Goods
		_ = json.Unmarshal(hit.Source, &g)
		goods = append(goods, g)
	}
	fmt.Println(goods)

	err = ScrollDocs(ctx, client, "goods", "", 100, elastic.NewMatchAllQuery(),
		func(hit *elastic.SearchHit) error { return nil })
	fmt.Println("scroll done:", err)
}
```

几个要点：

- **设了 routing 的查询一定要带 routing**。query 不带 routing 会扫集群全部分片；get 不带 routing 则是路由错了直接取不到 —— 两个都是高频低级故障。
- **少取字段**。大文本字段只做高亮展示时，用 `include/exclude` 排除掉，取字段越少越省。
- **多索引 + routing 是坑**，SDK 会把 routing 套用到传入的每个索引上，所以封装直接限定单索引。
- **`preference` 设 `_local`**：优先从本地分片取数据，能不跨节点就不跨节点，且落在同一分片上缓存命中率更高。

## 验证演示

串一遍完整流程：初始化客户端 → 建索引 → 写文档 → 更新 → 版本冲突 → 批量写 → 查询。

```txt
# 建索引（mapping + settings 与传入的 body 一致）
go run main.go
curl http://127.0.0.1:9200/goods

# ES 里 id=1 的文档：写一次 → version=1，改一次 → version=2
# upsert 传 version=2 → 版本冲突，name 仍是 name-2、version 仍是 2
# upsert 传 version=3 → 成功，name 变成 name-4、version 变成 3

# 批量写 0~9 共十条文档（走全局 bulk 处理器，主进程退出前留 2 秒让它 flush）
go run main.go
curl 'http://127.0.0.1:9200/goods/_search'

# 查询：满足慢查阈值时 DSL 会打印出来（match query、from=0 size=20、按 favorite 正序）
```

注意最后一点：**走全局 bulk 处理器时主进程退出前必须留 flush 时间**，否则提交请求还压在 channel 里，进程一退就没了。

## ES 操作全景

```mermaid
flowchart LR
    A["客户端封装 多集群 map"] --> B["读写分离 双 client"]
    B --> C["bulk 三阈值提交"]
    C --> D["文档写入 refresh 三值"]
    D --> E["external 版本乐观锁"]
    E --> F["查询带 routing + scroll Clear"]
```

```dir
Go 操作 ES 结构/
├── 客户端封装
│   ├── 函数选项模式
│   ├── client map 多集群
│   ├── bulk 处理器 三阈值
│   └── 健康检查 + 关 sniff
├── 读写分离
│   ├── 协调节点 读
│   └── ingest 节点 写
├── 文档操作
│   ├── refresh 三值
│   ├── bulk 两种提交
│   └── external 版本
└── 查询封装
    ├── 单索引 + routing
    ├── mget 跨索引
    └── scroll 必 Clear
```

## 注意事项总结

1. **SDK 选 `olivere/elastic/v7`**，别碰 5.x/6.x 那套没 go.mod 的包。
2. **连接用 `SetURL` 配多个地址、显式关 sniff**：前者防单点故障，后者避免请求散到数据节点。
3. **读写分离拆两个 client**：读走协调节点，写走 ingest 节点。
4. **bulk 三个阈值任一触发就提交**，盯住 `After` 回调里的失败项，别信"没报错就是写成功了"。
5. **bulk 是异步的**：主进程退出前要留 flush 时间。
6. **索引本地缓存慎用**，多实例 + 索引会被删除的场景直接关掉。
7. **`refresh` 用 `false`**：`true` 会强制刷新分片，吞吐掉得厉害。
8. **`external` 版本必须大于现有版本**，业务自增版本号就是天然乐观锁。
9. **`upsert` 要么传完整文档，要么用 `Doc(partial)+Upsert(full)`**，别拿半截字段去覆盖。
10. **`deleteByQuery` / `updateByQuery` 必须开 `ProceedOnVersionConflict`**，否则中途版本冲突就整体失败。
11. **查单个索引、带 routing、少取字段**，这三条是把查询性能拉满的关键。
12. **scroll 跑完主动 `Clear`**，别让滚动上下文长期占内存。

## 总结

Go 操作 ES 的四块内容，每一块都藏着"不加就会踩坑"的细节。**客户端侧**用函数选项模式 + client map 支持多集群，并显式关 sniff、配多地址、盯住 bulk 的 `After` 回调失败项；**读写分离**把协调节点与 ingest 节点拆成两个 client，避免流量相互拖累；**文档操作**里 `refresh` 用 `false`、`external` 版本必须大于现有版本、`upsert` 字段要写全，这三点是版本冲突和性能问题的根源；**查询侧**则卡死三条铁律——查单个索引、带 routing、少取字段，scroll 用完必须 `Clear`。

把这些封装细节做扎实，再配合"主进程退出前留 bulk flush 时间"这类工程习惯，ES 在搜索链路里就能既稳又快地扛住写入与查询两端。

