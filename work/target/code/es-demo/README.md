# es-demo —— Elasticsearch × Go 工程示例

一个**可直接运行**的 Elasticsearch + Go 工程示例，配套 `work/target/es`（1.es-go 课程）全部 ES/Go 知识点。

- **目标 ES 版本**：7.x（本机已装 7.7.1；`docker-compose.yml` 用 7.17.18 单节点）
- **Go 客户端**：`github.com/olivere/elastic/v7`（与课程一致；8.x 选型见文末）
- **验证状态**：`go build` ✅ / `go vet` ✅ / 单元测试 ✅ / **已在本机 ES 7.7.1 上端到端跑通**

---

## 一、5 分钟跑起来

### 方式 A：用你已有的 ES（推荐）

```bash
export ES_URL=http://localhost:9200
make build
./bin/es-demo doctor     # 检查连通性
./bin/es-demo seed       # 建索引 + 写样例数据
./bin/es-demo demo       # 跑全部知识点演示
```

### 方式 B：Docker 起一套（ES + Redis）

```bash
make up          # 起 elasticsearch + redis
make seed        # 建索引写数据
make demo
# 可选：make up-full 额外起 Kafka + Kibana
```

### 方式 C：只跑单元测试（不需要任何集群）

```bash
make test
```

> 单元测试用 `httptest` 模拟 ES，验证请求构造与响应解析；运维诊断逻辑是纯函数，也不需要集群。

---

## 二、目录结构

```
es-demo/
├── cmd/es-demo/main.go        # CLI 入口：doctor / seed / demo / ilm-demo / cache-demo / mq-demo / metrics
├── internal/
│   ├── es/
│   │   ├── client/            # 客户端封装：多集群、关 sniff、读写分离、Perform 原始端点
│   │   ├── index/             # 索引与 Mapping：dynamic 四策略、别名、动态模板
│   │   ├── write/             # 写入：refresh 三值、bulk 三阈值、external 版本、upsert、ByQuery
│   │   ├── search/            # 查询：bool/nested/function_score/sort/search_after/scroll/msearch
│   │   ├── agg/               # 聚合：terms/date_histogram/avg + shard_size + pipeline
│   │   ├── ops/               # 运维：cat/allocation/水位线/forcemerge/reindex/snapshot
│   │   │   └── diagnostics.go # 纯函数诊断器（水位线、未分配分片、滚动重启、线程池）+ 单测
│   │   ├── ilm/               # 生命周期：策略、rollover、codec
│   │   ├── cluster/           # 节点角色、分片规划、分配感知、冷热分层
│   │   └── crosscluster/      # CCS / CCR / 远程集群注册
│   ├── model/                 # 业务文档与 mapping（商品/订单/日志/邮件）
│   ├── cache/                 # Redis 多级缓存 + gzip 压缩
│   ├── mq/                    # Kafka 事件同步（业务写入与索引写入解耦）
│   └── monitor/               # Prometheus 指标
├── docs/
│   ├── ES_API_AUDIT.md        # 知识点审计报告（64 个知识点判定 + 纠正清单）
│   ├── knowledge_graph.json   # 机器可读图谱（nodes/edges）
│   └── knowledge_graph.mmd    # Mermaid 图谱（可直接渲染）
├── docker-compose.yml
├── Dockerfile
└── Makefile
```

---

## 三、知识点 → 代码 映射

| 类别 | 知识点 | 代码位置 |
| --- | --- | --- |
| **客户端** | 多集群 map、关 sniff、多地址、读写分离 | `internal/es/client/` |
| **Mapping** | dynamic 四策略（true/false/strict/runtime） | `internal/es/index/` |
| | 字段选型：text+keyword、`scaled_float`、nested、join | `internal/model/model.go` |
| | dynamic_templates 防字段爆炸 | `internal/es/index/` `PutDynamicTemplate` |
| **写入** | refresh 三值、`BulkProcessor` 三阈值、`external` 版本、upsert | `internal/es/write/` |
| **查询** | bool/nested/has_child/function_score/排序 | `internal/es/search/` |
| | search_after（深翻页推荐）/ scroll（导出用，含 Clear） | `internal/es/search/` |
| | msearch 并发搜索、highlight、`_source` 过滤 | `internal/es/search/` |
| **聚合** | terms/date_histogram/avg + `shard_size` + pipeline | `internal/es/agg/` |
| **运维** | cat APIs、allocation explain、磁盘三档水位线 | `internal/es/ops/` |
| | forcemerge、reindex 幂等、snapshot、只读开关 | `internal/es/ops/` |
| | 滚动重启六步、线程池评估（**纯函数 + 单测**） | `internal/es/ops/diagnostics.go` |
| **ILM** | 四阶段策略、rollover + 写别名、codec | `internal/es/ilm/` |
| **集群** | 节点角色、分片规划、分配感知、冷热分层 | `internal/es/cluster/` |
| **跨集群** | CCS 搜索、CCR 跟随（白金版）、远程注册 | `internal/es/crosscluster/` |
| **集成** | Kafka 事件解耦、Redis 压缩缓存、Prometheus | `internal/mq/`、`internal/cache/`、`internal/monitor/` |

完整 64 个知识点及其**正确性判定**，见 `docs/ES_API_AUDIT.md`；图谱见 `docs/knowledge_graph.json` / `.mmd`。

---

## 四、审计发现的错误与纠正（重点）

审计 **64 个知识点**：`correct 60` / `partial 3` / `error 1`。四条最值得记：

### 1. 【error】8.x 不能继续用 olivere/elastic v7

课程说「8.x 可以继续使用 v7 的包」——**这是错的**。`olivere/elastic` 已停止维护，不官方支持 8.x（8.x 移除 type、默认启用安全层/HTTPS）。

- **ES 7.x** → `github.com/olivere/elastic/v7`（本 demo 采用，与课程一致）
- **ES 8.x** → 官方 `github.com/elastic/go-elasticsearch/v8`（配套 `esapi`/`estransport` + API Key/TLS）

### 2. 【partial】金额字段勿用 `float`

7.x dynamic mapping 确实把浮点数推断为 `float`（课程正确），但金额用 `float` 会**丢精度**。
→ **纠正**：金额用 `scaled_float` + `scaling_factor: 100`（存分）。本 demo 的 `Product.Price`、`Order.PayAmount` 已按此实现。

### 3. 【partial】冷热分层优先用专用 data tier

课程用自定义属性 `node.attr.data_role` —— 能用，但 ILM **不会**自动据此迁移。
→ **纠正**：7.9+ 用 `node.roles: [data_hot]` 专用角色 + ILM `allocate.require.data_tier` 自动驱动。

### 4. 【partial】深翻页优先 search_after，scroll 用于导出

scroll 持有快照上下文、占内存（7.x 默认上限 500）。
→ **纠正**：实时深翻页用 `search_after`（固定排序含唯一键）；全量导出/reindex 才用 scroll，用完 `Clear`。

---

## 五、环境变量

| 变量 | 默认 | 说明 |
| --- | --- | --- |
| `ES_URL` | `http://localhost:9200` | ES 地址 |
| `ES_USER` / `ES_PASSWORD` | 空 | 基础认证 |
| `REDIS_URL` | `redis://localhost:6379` | Redis（`cache-demo` 用） |
| `KAFKA_BROKERS` | `localhost:9092` | Kafka（`mq-demo` 用，逗号分隔） |

---

## 六、Make 目标

```bash
make help       # 查看全部
make build      # 编译到 bin/es-demo
make test       # 单元测试（mock ES，无需集群）
make vet        # 静态检查
make up         # 起 ES + Redis
make up-full    # 额外起 Kafka + Kibana
make seed       # 建索引 + 写样例数据
make demo       # 全部知识点演示
make doctor     # 连通性检查
make down       # 停 compose
```

---

## 七、新手最该记住的 10 条铁律

1. **`refresh` 用 `false`**（或 `wait_for`），`true` 会强制刷新分片、吞吐骤降。
2. **bulk 是异步的**：主进程退出前必须 `Flush`/`Close`，否则数据还在 channel 里就丢了。
3. **`external` 版本必须大于现有版本**，业务自增版本号就是天然乐观锁。
4. **upsert 要么传完整文档，要么 `Doc(partial)+Upsert(full)`**，别拿半截字段覆盖。
5. **`updateByQuery`/`deleteByQuery` 必须 `ProceedOnVersionConflict`**，否则中途冲突整体失败。
6. **带 routing 的文档，get/query 都必须带 routing**，否则路由错分片。
7. **object 数组会扁平化**，要保留元素内关系就用 `nested`（查多写少）或拆索引；`join` 有 global ordinals 重建代价。
8. **red/yellow 根因唯一：存在未分配分片**；red = 主分片未分配。
9. **磁盘水位线百分比与具体空间不能混用**；洪水线只读**必须手动解除**。
10. **滚动重启 `allocation.enable` 只能是 `all`/`null`，绝不能是 `none`**（`none` = 禁止一切分配）。

---

## 八、排障

**集群是 red？**
```bash
curl 'localhost:9200/_cat/shards?h=index,shard,prirep,state,unassigned.reason&s=state'
curl -XPOST 'localhost:9200/_cluster/allocation/explain?pretty' -H 'Content-Type: application/json' -d '{"index":"<idx>","shard":0,"primary":true}'
```
（本机实测时，集群 red 来自你此前遗留的 `t_red` 索引，seed 建的 4 个索引都是 green。）

**`go build` 报 module cache 权限错误？**
默认 `GOPATH` 不可写时，重定向缓存目录即可：
```bash
export GOPATH=/tmp/esdemo-go GOMODCACHE=/tmp/esdemo-go/pkg/mod GOCACHE=/tmp/esdemo-go/cache
export GOSUMDB=off GOPROXY=https://goproxy.cn,direct
```

**Kafka 报 Unknown Topic？**
`mq-demo` 会自动建 topic；若仍失败，确认 broker 可达且允许自动创建。

---

## 九、版本选型速查

| 场景 | 客户端 |
| --- | --- |
| ES 5.x | `gopkg.in/olivere/elastic.v5` |
| ES 6.x | `github.com/olivere/elastic` |
| **ES 7.x（本 demo）** | **`github.com/olivere/elastic/v7`** |
| ES 8.x | `github.com/elastic/go-elasticsearch/v8` |
