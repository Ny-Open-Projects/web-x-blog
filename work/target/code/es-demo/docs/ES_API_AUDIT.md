# ES 课程知识点审计总报告

> 审计对象：`/Users/Wang/Code/github/web-x-blog/work/target/es/`
> 内容来源：es-go 课程转写稿（ASR/机翻），共 97 个已合并篇目（目录内 ~88 个 markdown）
> 知识点总数：**64 个**（correct 60 / partial 3 / error 1）
> 审计角色：资深 Golang + Elasticsearch 专家
> 目标 ES 版本：**7.x**（本机已安装 7.7.1；compose 用 7.17.18）
> Go 客户端：`github.com/olivere/elastic/v7`（与课程一致；8.x 选型见纠正项）
> 审计日期：2026-10-04

---

## 一、审计结论摘要

**总体：课程内容质量很高，技术判断基本正确，可直接作为面试与工程参考。**

| 判定 | 数量 | 说明 |
| --- | --- | --- |
| `correct` | 60 | 与 ES 7.x 官方行为一致，可直接采信 |
| `partial` | 3 | 结论方向正确，但存在版本偏差 / 精度或选型建议需补充 |
| `error` | 1 | 结论有误，会误导工程选型，必须纠正 |

**最需要纠正的 3 处（按风险排序）：**

1. **【error】KP-GO-04「8.x 集群可以继续用 olivere/elastic v7」** —— 这是**错误**的选型建议。`olivere/elastic` 已停止维护，不官方支持 ES 8.x（8.x 移除 type、默认启用安全层与 HTTPS）。**8.x 必须用官方 `github.com/elastic/go-elasticsearch/v8`**，否则会在安全认证、API 兼容性上踩坑。
2. **【partial】KP-MAP-04 浮点数默认推断为 `float`** —— 结论本身正确（7.x 确实推断 `float`），但**金额类字段用 `float` 会丢精度**，应显式用 `scaled_float`（`scaling_factor: 100`）。本 demo 已按纠正方案实现。
3. **【partial】KP-CLUSTER-03 冷热分层用自定义属性 `node.attr.data_role`** —— 能用，但属于 7.9 之前的老做法。7.9+ 有**专用 data tier 节点角色**（`node.roles: [data_hot]`）并由 ILM 的 `allocate.require.data_tier` 自动驱动，自定义属性 ILM 不会自动迁移。

**版本说明（贯穿全文）：**

- 课程整体基于 **7.x**：ILM 可用（6.6+ 正式）、CCS 免费可用、**CCR 需 Platinum 授权**、单节点分片上限 1000（7.0+ 默认）。
- **6.x**：仍有 `type`（`_doc` 之外可自定义），ILM 处于 beta。
- **8.x**：默认开启安全层（HTTPS + 认证）、移除 mapping type、`_all` 移除；客户端应换官方 `go-elasticsearch/v8`。

---

## 二、知识点逐条判定

### Mapping / 索引与字段类型

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-MAP-01 | DynamicMapping 类型推断规则（字符串→text+keyword、整数→long、日期→date） | 3-2 | correct | — | `internal/es/index` |
| KP-MAP-02 | dynamic 四策略 `true`/`false`/`strict`/`runtime` | 3-2 | correct | `runtime` 下字符串映射为 keyword，不支持全文匹配 | `internal/es/index` (`CreateIndexDynamicFalse` 等) |
| KP-MAP-03 | 写入失败仍会创建空 mapping 索引（僵尸索引） | 3-2 | correct | 补充：可用 `action.auto_create_index` 管控 | `internal/es/index` + README |
| KP-MAP-04 | 数字字段类型选型（float/long/scaled_float） | 11-10, 3-2 | **partial** | 见纠正 ②：金额用 `scaled_float`，勿用 `float` | `internal/model`（price/pay_amount 用 scaled_float） |
| KP-MAP-05 | text + keyword 子字段双写（既可分词又可精确匹配/聚合） | 3-4, 7-29 | correct | — | `internal/model` |
| KP-MAP-06 | object 数组被扁平化，元素内字段关系丢失 | 3-8 | correct | 这是嵌套坑的根因 | `internal/model` 注释 + demo 复现 |
| KP-MAP-07 | `nested` 类型 + `nested` query 保留关系 | 3-8 | correct | 更新 nested 字段需整条文档重建 | `internal/es/index`, `internal/es/search` |
| KP-MAP-08 | `join` 父子文档：子文档必须带父 ID 作 routing | 3-8 | correct | — | `internal/model` (OrderMapping), `internal/es/search` |
| KP-MAP-09 | global ordinals 每次 refresh 重建，父 ID 越多越慢 | 3-8 | correct | 这是不推荐 join 的核心原因 | `internal/model` 注释 |
| KP-MAP-10 | `_source` / `doc_values` / `index:false` 开关省空间 | 3-4, 10-7 | correct | 大文本仅建倒排可省 doc_values | `internal/model`（email body doc_values:false） |
| KP-MAP-11 | dynamic_templates 防字段爆炸 | 3-2 | correct | — | `internal/es/index` (`PutDynamicTemplate`) |

### Write / 写入

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-WRITE-01 | refresh 三值 `false`/`true`/`wait_for` | 6-6 | correct | `true` 会刷新主副分片，吞吐骤降 | `internal/es/write`（常量） |
| KP-WRITE-02 | BulkProcessor 三阈值（worker/文档数/字节数） | 6-6 | correct | 任一触发即提交；`After` 回调必须处理错误 | `internal/es/write` (`NewWriter`) |
| KP-WRITE-03 | `external` 版本乐观锁：传入版本须 > 现有版本 | 6-6 | correct | 业务自增版本号天然乐观锁 | `internal/es/write` (`IndexWithVersion`) |
| KP-WRITE-04 | upsert：`Doc(partial)` + `Upsert(full)` | 6-6 | correct | 只改部分字段必须用这套组合 | `internal/es/write` (`Upsert`) |
| KP-WRITE-05 | updateByQuery / deleteByQuery 必须 `ProceedOnVersionConflict` | 6-6 | correct | — | `internal/es/write` |
| KP-WRITE-06 | routing：get/query 必带，否则路由错分片 | 6-6 | correct | — | `internal/es/write` (`Get`), `internal/es/search` |
| KP-WRITE-07 | reindex 幂等：`conflicts:proceed` + `op_type:create` | 11-6, 8.x | correct | 可安全重跑 | `internal/es/ops` (`Reindex`) |
| KP-WRITE-08 | ingest pipeline 预处理 | 10.x | correct | — | `internal/es/write` (`PutPipeline`) |

### Search / 查询

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-SEARCH-01 | term vs match、bool 组合查询 | 6-6, 11-9 | correct | — | `internal/es/search` (`Simple`) |
| KP-SEARCH-02 | nested query（含 path） | 3-8 | correct | 已实测：iPhone+num>1 正确返回 0 命中 | `internal/es/search` (`Nested`) |
| KP-SEARCH-03 | function_score 干预相关性 | 3-6 | correct | — | `internal/es/search` (`FunctionScore`) |
| KP-SEARCH-04 | 排序（字段 / script / geo） | 3-6 | correct | — | `internal/es/search` (`Simple` SortBy) |
| KP-SEARCH-05 | search_after 深翻页（替代 from/size） | 7-19 | correct | 需固定排序（含唯一键） | `internal/es/search` (`SearchAfter`) |
| KP-SEARCH-06 | scroll 滚动查询 + 用完 Clear | 6-6 | **partial** | 见纠正 ④：深翻页优先 search_after，scroll 用于导出 | `internal/es/search` (`Scroll`) |
| KP-SEARCH-07 | track_total_hits / highlight / _source 字段过滤 | 6-6, 7-21 | correct | 少取字段省带宽 | `internal/es/search` (`WithHighlight`) |
| KP-SEARCH-08 | msearch 并发搜索 | 7-16 | correct | — | `internal/es/search` (`MultiSearch`) |
| KP-SEARCH-09 | `preference=_local` 提高缓存命中 | 6-6 | correct | — | `internal/es/search` (`Simple`) |

### Aggregate / 聚合

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-AGG-01 | terms / date_histogram / avg | 7.x | correct | — | `internal/es/agg` |
| KP-AGG-02 | shard_size 提升 terms 精度 | 7.x | correct | 分片级取样不足会漏桶 | `internal/es/agg` (`TermsAgg`) |
| KP-AGG-03 | pipeline 聚合（derivative 环比） | 7.x | correct | — | `internal/es/agg` (`AvgWithPipeline`) |

### Ops / 运维

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-OPS-01 | red/yellow 根因唯一：存在未分配分片 | 11-6 | correct | red=主分片未分配 | `internal/es/ops` |
| KP-OPS-02 | `_cluster/allocation/explain` 问原因 | 11-6 | correct | 看 `assigned` + `decide.explanation` | `internal/es/ops` (`AllocationExplain`) |
| KP-OPS-03 | 磁盘三档水位线 85/90/95%，百分比与空间不能混用 | 11-6 | correct | 已在 demo 中做成硬校验 | `internal/es/ops/diagnostics.go` |
| KP-OPS-04 | 洪水线只读需手动解除 | 11-6 | correct | — | `internal/es/ops` (`SetReadOnly`) |
| KP-OPS-05 | `forcemerge?only_expunge_deletes=true` 回收删除文档 | 11-6, 11-8 | correct | 比合并到指定段数安全 | `internal/es/ops` (`ForcemergeExpunge`) |
| KP-OPS-06 | reroute + `allocate_*_primary` + `accept_data_loss` | 11-6 | correct | 仅磁盘确认损坏才用 | `internal/es/ops/diagnostics.go` (`LossyOps`) |
| KP-OPS-07 | 滚动重启六步；`enable` 不能设 `none` | 11-6 | correct | `none` 与 `null` 语义相反 | `internal/es/ops/diagnostics.go` (`RestartPlan`) |
| KP-OPS-08 | 排查 CPU 三件套：线程池 / hot_threads / pending | 11-6 | correct | rejected>0 即危险 | `internal/es/ops` |
| KP-OPS-09 | 7.x 单节点分片上限 1000 | 11-6 | correct | 临时提额只是止血 | `internal/es/cluster` (`ShardPlan`) |
| KP-OPS-10 | 别名 / ILM / 压缩 / 恢复并发 / 禁通配删 | 11-6 | correct | — | `internal/es/index`, `internal/es/ops` |

### ILM

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-ILM-01 | ILM 四阶段 hot/warm/cold/delete | 9-6 | correct | — | `internal/es/ilm` (`PutPolicy`) |
| KP-ILM-02 | rollover + 写别名 | 9-6 | correct | 已实测：logs-000001→000002 | `internal/es/ilm` (`Rollover`) |
| KP-ILM-03 | `index.codec` 调整需先 close 索引 | 11-6 | correct | — | `internal/es/ilm` (`SetCodec`) |

### Cluster / 集群

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-CLUSTER-01 | 节点角色 master/data/ingest/coordinating | 4-1 | correct | — | `internal/es/cluster` (`NodeRoles`) |
| KP-CLUSTER-02 | 分片/副本规划（10 台 32C128G） | 11-5 | correct | — | `internal/es/cluster` (`ShardPlan`) |
| KP-CLUSTER-03 | 冷热分层 `node.attr.data_role` | 11-6, 4-1 | **partial** | 见纠正 ③：优先专用 data tier | `internal/es/cluster` (`SetTierRouting`) |
| KP-CLUSTER-04 | 分配感知 rack_id / same_shard.host | 11-6 | correct | 避免同机多副本同时不可用 | `internal/es/cluster` (`SetAllocationAwareness`) |

### CrossCluster / 跨集群

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-XC-01 | CCS 跨集群搜索 `<remote>:<index>` | 4-4 | correct | 建议开 `ccs_minimize_roundtrips` | `internal/es/crosscluster` |
| KP-XC-02 | CCR 跨集群复制需 Platinum 授权 | 4-4, 4-7 | correct | 社区版不可用（易被误传为免费） | `internal/es/crosscluster` (`FollowIndex`) |
| KP-XC-03 | 注册 remote cluster seeds | 4-4 | correct | — | `internal/es/crosscluster` (`RegisterRemote`) |

### GoClient / Go 客户端

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-GO-01 | olivere/elastic v7 是 7.x 首选（有 go.mod） | 6-6 | correct | — | `internal/es/client` |
| KP-GO-02 | 显式关 sniff + 配多个地址 | 6-6 | correct | — | `internal/es/client` |
| KP-GO-03 | 读写分离双 client（协调节点读 / ingest 写） | 6-6 | correct | — | `internal/es/client` (`ClientSet`) |
| KP-GO-04 | **8.x 可继续用 v7 包** | 6-6 | **error** | 见纠正 ①：8.x 必须用官方 go-elasticsearch/v8 | README「版本选型」 |
| KP-GO-05 | bulk 异步，退出前必须 flush | 6-6 | correct | — | `internal/es/write` (`Flush`/`Close`) |
| KP-GO-06 | 索引本地缓存慎用 | 6-6 | correct | — | `internal/es/index` 注释 |

### DataModeling / 建模

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-DM-01 | 面向搜索的宽表建模、避免 join | 7-29, 8.x | correct | — | `internal/model` |
| KP-DM-02 | nested vs join 选型（查多写少用 nested） | 3-8 | correct | 最干净是拆索引 | `internal/model` |
| KP-DM-03 | 冷热分离 / 空间换时间 | 10-5, 10-6 | correct | — | `internal/model` + README |

### Integration / 中间件集成

| ID | 知识点 | 来源 | 判定 | 纠正 / 说明 | demo 位置 |
| --- | --- | --- | --- | --- | --- |
| KP-INTEG-01 | Kafka 事件解耦业务写入与索引写入 | 7-14, 6-4 | correct | — | `internal/mq` |
| KP-INTEG-02 | Redis 多级缓存 + 压缩 | 7-18, 6-10 | correct | — | `internal/cache` |
| KP-INTEG-03 | MySQL binlog→ES 同步 | 6-9 | correct | — | README 说明 |
| KP-INTEG-04 | Prometheus 指标上报 | 6-13, 4-8 | correct | — | `internal/monitor` |

---

## 三、纠正清单（error / partial 汇总）

### ① 【error】KP-GO-04：8.x 不应继续使用 olivere/elastic v7

- **课程原表述**：「8.x 可以继续使用 v7 的包，改个集群地址就行，不用为升版本重写业务代码。」
- **问题**：`olivere/elastic` 已进入维护停滞状态，**不官方支持 ES 8.x**。8.x 的破坏性变更包括：完全移除 mapping type、默认启用安全层（HTTPS + 认证/TLS）、部分 REST 响应结构调整。v7 客户端在 8.x 上会出现认证失败、API 语义不一致等问题。
- **纠正方案**：
  - **ES 7.x**（本课程 / 本机 7.7.1）→ 继续用 `github.com/olivere/elastic/v7`，本课程所有用法均正确。
  - **ES 8.x** → 使用官方 `github.com/elastic/go-elasticsearch/v8`（配套 `esapi`/`estransport`），并显式处理 API Key / TLS。
- **对 demo 的影响**：本 demo 目标 ES 7.7.1，故采用 `olivere/elastic/v7`（与课程一致）；README 中已明确写出 8.x 的迁移指引。

### ② 【partial】KP-MAP-04：金额类字段勿用 `float`

- **问题**：7.x dynamic mapping 确实把浮点数推断为 `float`（课程结论正确），但 `float`（32 位）在金额/高精度场景下会**丢精度**。
- **纠正方案**：金额用 `scaled_float` 配 `scaling_factor`（如 100 表示存分），或 `double`；整数统计用 `long`/`integer`。
- **demo 落地**：`internal/model` 中 `Product.Price`、`Order.PayAmount` 均用 `scaled_float` + `scaling_factor: 100`。

### ③ 【partial】KP-CLUSTER-03：冷热分层优先用专用 data tier

- **问题**：课程用自定义节点属性 `node.attr.data_role: data_hot` + `index.routing.allocation.include.data_role`。这在 7.x 可用，但：
  - ILM **不会**自动基于自定义属性做分层迁移，需要手工改 allocation 设置；
  - 7.9+ 已有官方 data tier 角色，配套 ILM 的 `allocate.require.data_tier` 可自动驱动 hot→warm→cold→frozen。
- **纠正方案**：
  ```yaml
  # elasticsearch.yml（7.9+）
  node.roles: [ data_hot ]     # 或 data_warm / data_cold / data_frozen
  ```
  ILM 中用 `"allocate": { "require": { "data_tier": "data_warm" } }`。
- **demo 落地**：`internal/es/cluster.SetTierRouting` 保留了课程做法；`internal/es/ilm` 的 ILM 策略示例已改用官方 tier 语义（`data_role` 仅为兼容示例）。

### ④ 【partial】KP-SEARCH-06：深翻页优先 search_after，scroll 用于导出

- **问题**：课程把 scroll 作为常规滚动/深翻手段讲解。scroll 会**持有快照上下文、占用内存**，且在 7.x 中官方已不推荐用于实时深翻页（`search.max_open_scroll_context` 默认 500 就是限制）。
- **纠正方案**：
  - **实时深翻页** → `search_after`（需固定排序且含唯一键做 tiebreaker）。
  - **全量导出 / reindex** → `scroll`，用完 `Clear`；或 8.x 的 PIT + search_after。
- **demo 落地**：`internal/es/search` 同时实现 `SearchAfter`（推荐）与 `Scroll`（含 `Clear`，用于导出），并在注释中标明适用边界。

---

## 四、与 es-demo 的覆盖关系

审计出的全部知识点均已在 `es-demo` 中有对应代码（详见 `README.md` 的「知识点 → 代码」映射表与 `knowledge_graph.json`）。

- **ES API 知识点**（Mapping/Write/Search/Agg/Ops/ILM/Cluster/CrossCluster）：全部在 `internal/es/*` 下有可运行代码。
- **Go 客户端知识点**：`internal/es/client`（多集群、关 sniff、读写分离）+ `internal/es/write`（bulk 三阈值、refresh、external 版本）。
- **中间件集成知识点**：`internal/mq`（Kafka）、`internal/cache`（Redis 压缩缓存）、`internal/monitor`（Prometheus）。
- **纯逻辑知识点**（水位线、未分配诊断、滚动重启、线程池）：抽成纯函数放在 `internal/es/ops/diagnostics.go`，**配套单元测试，无需真实集群即可验证**。

## 五、验证方式

```bash
make build      # 编译
make test       # 单元测试（mock ES，无需集群）
make up         # 起 ES + Redis（docker compose）
make seed       # 建索引 + 写样例数据
make demo       # 全部知识点演示
make doctor     # 连通性检查
```

本机（ES 7.7.1）已实测通过：`doctor` / `seed` / `demo` / `ilm-demo` / `mq-demo` 全部跑通。
