// Command es-demo —— Elasticsearch × Go 工程示例入口。
//
// 用法（环境变量：ES_URL / REDIS_URL / KAFKA_BROKERS）：
//
//	es-demo doctor      检查 ES / Redis 连通性
//	es-demo seed        建索引 + 写样例数据
//	es-demo demo        运行全部 ES 知识点演示（需 ES）
//	es-demo ilm-demo    ILM 策略 + rollover 演示（需 ES）
//	es-demo cache-demo  Redis 多级缓存演示（需 Redis）
//	es-demo mq-demo     Kafka 事件同步演示（需 Kafka）
//	es-demo metrics     暴露 /metrics（Prometheus 抓取）
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/cache"
	"es-demo/internal/es/agg"
	"es-demo/internal/es/client"
	"es-demo/internal/es/cluster"
	"es-demo/internal/es/crosscluster"
	"es-demo/internal/es/ilm"
	"es-demo/internal/es/index"
	"es-demo/internal/es/ops"
	"es-demo/internal/es/search"
	"es-demo/internal/es/write"
	"es-demo/internal/model"
	"es-demo/internal/monitor"
	"es-demo/internal/mq"
)

func main() {
	if len(os.Args) < 2 {
		usage()
		os.Exit(1)
	}
	ctx := context.Background()
	switch os.Args[1] {
	case "doctor":
		cmdDoctor(ctx)
	case "seed":
		cmdSeed(ctx)
	case "demo":
		cmdDemo(ctx)
	case "ilm-demo":
		cmdILMDemo(ctx)
	case "cache-demo":
		cmdCacheDemo(ctx)
	case "mq-demo":
		cmdMQDemo(ctx)
	case "metrics":
		cmdMetrics(ctx)
	default:
		usage()
		os.Exit(1)
	}
}

func usage() {
	fmt.Println(`es-demo: Elasticsearch × Go 工程示例

  doctor      检查 ES / Redis 连通性
  seed        建索引 + 写样例数据
  demo        运行全部 ES 知识点演示（需 ES）
  ilm-demo    ILM 策略 + rollover（需 ES）
  cache-demo  Redis 多级缓存（需 Redis）
  mq-demo     Kafka 事件同步（需 Kafka）
  metrics     暴露 /metrics（Prometheus）`)
}

func envOr(key, def string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return def
}

// banner 打印章节分隔，便于在 demo 输出里对照知识点。
func banner(title string) {
	fmt.Println("\n" + strings.Repeat("=", 60))
	fmt.Println("  " + title)
	fmt.Println(strings.Repeat("=", 60))
}

// ---------------------------------------------------------------- doctor

func cmdDoctor(ctx context.Context) {
	esURL := envOr("ES_URL", "http://localhost:9200")
	c, err := client.New(client.WithURLs(esURL))
	if err != nil {
		fatal(err)
	}
	ver, err := c.Ping(ctx)
	if err != nil {
		fmt.Printf("[ES] 不可达 %s: %v\n", esURL, err)
	} else {
		st, _ := c.Health(ctx)
		fmt.Printf("[ES] 可达 版本=%s 健康=%s\n", ver, st)
	}

	redisURL := envOr("REDIS_URL", "redis://localhost:6379")
	sc, err := cache.New(redisURL, time.Minute)
	if err != nil {
		fmt.Printf("[Redis] 连接失败: %v\n", err)
		return
	}
	defer sc.Close()
	if _, _, err := sc.Get(ctx, "__ping__"); err != nil {
		fmt.Printf("[Redis] 不可达: %v\n", err)
	} else {
		fmt.Printf("[Redis] 可达 %s\n", redisURL)
	}
}

// ---------------------------------------------------------------- seed

func cmdSeed(ctx context.Context) {
	c := mustClient()
	w, err := write.NewWriter(ctx, c)
	if err != nil {
		fatal(err)
	}
	defer w.Close()

	must(index.CreateIndex(ctx, c, "product", model.ProductMapping))
	must(index.CreateIndex(ctx, c, "order", model.OrderMapping))
	must(index.CreateIndex(ctx, c, "app_log", model.LogMapping))
	must(index.CreateIndex(ctx, c, "email", model.EmailMapping))

	// 商品：含 nested 规格，演示保留数组元素关系
	products := []model.Product{
		{ID: "p1", Title: "iPhone 15", CategoryID: 1, Price: 799900, Tags: []string{"phone", "apple"}, OnSale: true, Sales: 1000, CreatedAt: time.Now().UnixMilli(),
			Specs: []model.Spec{{Name: "color", Value: "black"}, {Name: "storage", Value: "256g"}}},
		{ID: "p2", Title: "华为 Mate 60", CategoryID: 1, Price: 699900, Tags: []string{"phone", "huawei"}, OnSale: true, Sales: 800, CreatedAt: time.Now().UnixMilli(),
			Specs: []model.Spec{{Name: "color", Value: "white"}, {Name: "storage", Value: "512g"}}},
	}
	for _, p := range products {
		must(w.Index(ctx, "product", p.ID, "", p, write.RefreshWaitFor))
	}

	// 订单：含 nested 订单项
	orders := []model.Order{
		{ID: "o1", UserID: "u1", Status: 1, PayAmount: 999900, CreatedAt: time.Now().UnixMilli(),
			Items: []model.OrderItem{{SKU: "sku-iphone", Name: "iPhone", Num: 1}, {SKU: "sku-huawei", Name: "华为", Num: 2}}},
	}
	for _, o := range orders {
		must(w.Index(ctx, "order", o.ID, "", o, write.RefreshWaitFor))
	}

	// 日志
	logs := []model.LogDoc{
		{Timestamp: time.Now().UnixMilli(), Level: "INFO", Service: "search", Message: "query ok", TraceID: "t1"},
		{Timestamp: time.Now().UnixMilli(), Level: "ERROR", Service: "search", Message: "query timeout", TraceID: "t2"},
	}
	for i, l := range logs {
		must(w.Index(ctx, "app_log", fmt.Sprintf("l%d", i), "", l, write.RefreshWaitFor))
	}

	// 邮件
	emails := []model.EmailDoc{
		{ID: "e1", From: "a@x.com", To: "b@x.com", Subject: "开会通知", Body: "本周五下午三点开会讨论搜索架构", HasAtt: false, Date: time.Now().UnixMilli()},
	}
	for _, e := range emails {
		must(w.Index(ctx, "email", e.ID, "", e, write.RefreshWaitFor))
	}
	fmt.Println("seed 完成：product / order / app_log / email 已建索引并写入样例数据")
}

// ---------------------------------------------------------------- demo

func cmdDemo(ctx context.Context) {
	c := mustClient()
	w, err := write.NewWriter(ctx, c)
	if err != nil {
		fatal(err)
	}
	defer w.Close()
	searcher := search.New(c)
	aggr := agg.New(c)
	o := ops.New(c)
	metrics := monitor.New()

	banner("KP-MAP-02 / KP-WRITE-01 写入与 refresh 三值")
	p := model.Product{ID: "p-demo", Title: "演示商品", CategoryID: 1, Price: 10000, Sales: 10, CreatedAt: time.Now().UnixMilli()}
	must(w.Index(ctx, "product", p.ID, "", p, write.RefreshWaitFor))
	fmt.Println("已写入 product/p-demo，refresh=wait_for（写后即可查）")

	banner("KP-SEARCH-01 bool 组合查询 + track_total_hits")
	t0 := time.Now()
	res, err := searcher.Simple(ctx, "product", "",
		[]elastic.Query{elastic.NewMatchQuery("title", "iPhone")},
		nil,
		[]elastic.Query{elastic.NewTermQuery("on_sale", true)},
		0, 10, elastic.NewFieldSort("sales").Desc())
	metrics.Observe("product", time.Since(t0), err == nil)
	if err != nil {
		fatal(err)
	}
	search.PrintResult("bool(match title=iPhone AND on_sale=true)", res)

	banner("KP-MAP-05 / KP-SEARCH-02 nested 查询（保留数组元素关系）")
	inner := elastic.NewBoolQuery().
		Must(elastic.NewMatchQuery("items.name", "iPhone")).
		Must(elastic.NewRangeQuery("items.num").Gt(1))
	r, err := searcher.Nested(ctx, "order", "items", inner)
	if err != nil {
		fatal(err)
	}
	search.PrintResult("nested: 订单项 name=iPhone AND num>1（命中 o1：华为2件不匹配，iPhone仅1件也不匹配 → 应为空）", r)

	banner("KP-SEARCH-04 function_score 相关性干预（按销量加权）")
	fs, err := searcher.FunctionScore(ctx, "product", elastic.NewMatchAllQuery(), "sales")
	if err != nil {
		fatal(err)
	}
	search.PrintResult("function_score(按 sales 加权)", fs)

	banner("KP-SEARCH-06 search_after 深翻页")
	sort := elastic.NewFieldSort("sales").Desc()
	page, err := searcher.SearchAfter(ctx, "product", elastic.NewMatchAllQuery(), sort, nil)
	if err != nil {
		fatal(err)
	}
	search.PrintResult("search_after 第一页", page)

	banner("KP-SEARCH-07 scroll 滚动查询（用完 Clear）")
	err = searcher.Scroll(ctx, "app_log", "", elastic.NewMatchAllQuery(), 10, func(src []byte) error {
		fmt.Printf("  scroll hit: %s\n", string(src))
		return nil
	})
	if err != nil {
		fatal(err)
	}
	fmt.Println("scroll 完成并 Clear")

	banner("KP-AGG-01 / KP-AGG-02 terms 聚合 + shard_size 精度")
	terms, err := aggr.TermsAgg(ctx, "product", "category_id", 10, 100)
	if err != nil {
		fatal(err)
	}
	fmt.Printf("category_id 分布: %v\n", terms)

	banner("KP-OPS 运维诊断（纯函数，无需集群）")
	wm := ops.Defaults()
	fmt.Printf("水位线校验(默认85/90/95): %v\n", wm.Validate())
	for _, st := range []struct{ t, u float64 }{{1000, 500}, {1000, 970}} {
		s := wm.Evaluate(st.t, st.u)
		fmt.Printf("  磁盘 %d/%d → %s：%s\n", int(st.u), int(st.t), s.Name, s.Effect)
	}
	ex := ops.Explain{Index: "order", Shard: 0, Primary: true, Reason: "the node containing this shard copy recently left the cluster (node_left)"}
	for _, op := range ops.Diagnose(ex) {
		fmt.Printf("  诊断 → %s | %s\n", op.Action, op.Command)
	}

	banner("KP-OPS-04 / KP-OPS-07 forcemerge + reindex（需真实集群）")
	if err := o.ForcemergeExpunge(ctx, "app_log"); err != nil {
		fmt.Println("  forcemerge 失败（可能无权限/索引只读）:", err)
	} else {
		fmt.Println("  forcemerge?only_expunge_deletes 完成")
	}
	if err := o.Reindex(ctx, "product", "product_bak"); err != nil {
		fmt.Println("  reindex 失败:", err)
	} else {
		fmt.Println("  reindex product→product_bak 完成")
	}

	banner("KP-CLUSTER-01 节点角色（_cat/nodes）")
	cl := cluster.New(c)
	roles, err := cl.NodeRoles(ctx)
	if err != nil {
		fmt.Println("  _cat/nodes 失败:", err)
	} else {
		fmt.Println("  节点列表:", roles)
	}
	fmt.Printf("  分片规划建议（10 节点/每节点 1000 分片/目标 2000 片）→ %d\n",
		cluster.ShardPlan(10, 1000, 2000))

	banner("KP-XC-01 跨集群搜索（需先注册 remote cluster）")
	cc := crosscluster.New(c)
	if _, err := cc.CrossClusterSearch(ctx, "remote_demo", "product", elastic.NewMatchAllQuery()); err != nil {
		fmt.Println("  跨集群搜索失败（预期：本机未注册远程集群）——", err)
	} else {
		fmt.Println("  跨集群搜索命中")
	}
	fmt.Println(`  语法：<remote>:<index>；生产建议开启 ccs_minimize_roundtrips 减少往返。`)
	fmt.Println(`  注意：CCR（跨集群复制）需要 Platinum 授权，社区版不可用。`)

	banner("KP-ILM-01 ILM 策略（读取当前策略）")
	il := ilm.New(c)
	if p, err := il.GetPolicy(ctx, "demo_policy"); err != nil {
		fmt.Println("  读取 ILM 策略失败（可能尚未创建）:", err)
	} else {
		fmt.Println("  当前 demo_policy:", p)
	}

	fmt.Println("\n✅ demo 完成。如需指标，另开终端运行：es-demo metrics")
}

// ---------------------------------------------------------------- ilm-demo

func cmdILMDemo(ctx context.Context) {
	c := mustClient()
	i := ilm.New(c)
	policy := `{
      "policy": {
        "phases": {
          "hot":   { "actions": { "rollover": { "max_size": "1gb", "max_age": "1d" } } },
          "warm":  { "actions": { "allocate": { "require": { "data_role": "data_warm" } } } },
          "delete":{ "min_age": "30d", "actions": { "delete": {} } }
        }
      }
    }`
	must(i.PutPolicy(ctx, "demo_policy", policy))
	fmt.Println("ILM 策略 demo_policy 已创建（hot→warm→delete）")

	// 用写别名 + rollover 模式建索引
	must(index.CreateIndex(ctx, c, "logs-000001", model.LogMapping))
	must(index.AliasAdd(ctx, c, "logs-000001", "logs-write"))
	must(i.BindPolicy(ctx, "logs-write", "demo_policy"))
	out, err := i.Rollover(ctx, "logs-write")
	if err != nil {
		fmt.Println("rollover 失败:", err)
	} else {
		fmt.Printf("rollover 结果: %s\n", out)
	}
}

// ---------------------------------------------------------------- cache-demo

func cmdCacheDemo(ctx context.Context) {
	redisURL := envOr("REDIS_URL", "redis://localhost:6379")
	sc, err := cache.New(redisURL, time.Minute)
	if err != nil {
		fatal(err)
	}
	defer sc.Close()
	val := []byte(`{"hits":[{"id":"p1","title":"iPhone 15"}]}`)
	if err := sc.Set(ctx, "search:product:iPhone", val); err != nil {
		fatal(err)
	}
	got, hit, err := sc.Get(ctx, "search:product:iPhone")
	if err != nil {
		fatal(err)
	}
	fmt.Printf("缓存命中=%v 解压后=%s\n", hit, string(got))
}

// ---------------------------------------------------------------- mq-demo

func cmdMQDemo(ctx context.Context) {
	brokers := strings.Split(envOr("KAFKA_BROKERS", "localhost:9092"), ",")
	topic := "product-events"
	// broker 关闭 auto-create 时先建 topic，保证 demo 开箱即跑
	if err := mq.EnsureTopic(brokers, topic, 1); err != nil {
		fmt.Printf("  topic 创建失败（将尝试直接发送）: %v\n", err)
	}
	p := mq.NewProducer(brokers, topic)
	defer p.Close()
	e := mq.Event{Op: "insert", Index: "product", ID: "p1", Doc: []byte(`{"title":"iPhone 15"}`)}
	if err := p.Publish(ctx, e); err != nil {
		fatal(fmt.Errorf("publish 失败（Kafka 是否可用？）: %w", err))
	}
	b, _ := json.Marshal(e)
	fmt.Printf("已发送 Kafka 事件: %s\n", string(b))
	fmt.Println("提示：另起消费者用 mq.NewConsumer(...).Run 即可异步写 ES，实现业务与索引写入解耦。")
}

// ---------------------------------------------------------------- metrics

func cmdMetrics(ctx context.Context) {
	m := monitor.New()
	// 后台跑几轮示例搜索以产生指标
	go func() {
		c := mustClient()
		searcher := search.New(c)
		ticker := time.NewTicker(2 * time.Second)
		defer ticker.Stop()
		for range ticker.C {
			_, _ = searcher.Simple(context.Background(), "product", "",
				[]elastic.Query{elastic.NewMatchAllQuery()}, nil, nil, 0, 10)
			m.Observe("product", 5*time.Millisecond, true)
		}
	}()
	fmt.Println("Prometheus 指标已暴露在 :2112/metrics，按 Ctrl+C 退出")
	if err := m.Serve(":2112"); err != nil {
		fatal(err)
	}
}

// ---------------------------------------------------------------- helpers

func mustClient() *client.Client {
	esURL := envOr("ES_URL", "http://localhost:9200")
	c, err := client.New(client.WithURLs(esURL))
	if err != nil {
		fatal(err)
	}
	return c
}

func must(err error) {
	if err != nil {
		fatal(err)
	}
}

func fatal(err error) {
	fmt.Fprintf(os.Stderr, "❌ %v\n", err)
	os.Exit(1)
}
