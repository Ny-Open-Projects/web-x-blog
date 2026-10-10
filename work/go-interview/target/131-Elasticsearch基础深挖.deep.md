# 131 Elasticsearch 基础 · 深挖

## 思路与架构
ES 的架构可分层理解：存储层（Lucene 提供单机倒排索引能力）、分布式层（ES 把索引切成主分片+副本分布到节点，自动再平衡与故障转移）、接口层（REST + JSON DSL 屏蔽 Lucene 复杂度）。数据模型上，索引≈表、文档≈行、字段由 mapping 定义；7.x 起 type 固定 _doc，彻底去关系化。写入经主分片、副本异步同步；读取可由副本分担。集群状态、节点角色、分片分配由 master 节点协调。

## 方案取舍
- **Lucene 库 vs ES 服务**：Lucene 灵活但需自写分布式；ES 开箱分布式但黑盒更深，调试靠监控。
- **分片数 vs 副本数**：分片数定写入并行度与上限（后期难改），副本数定读吞吐与可用（可在线调）。
- **多 type vs 单 type**：旧版多 type 像多表但共享结构致冗余冲突，7.x 单 type（_doc）最干净。
- **自建 vs 托管**：小集群 docker-compose 起，生产用 ECK/云托管，省运维。

## 答题技巧
答 ES 概念题先点「ES=Lucene+分布式外壳」，再串：分片（扩展）/副本（可用）/mapping（检索行为）/type 演进（7.x 固定 _doc）。必提 `vm.max_map_count` 运维坑与 Kibana Dev Tools 控制台。追问架构时，用「Lucene 存储层 + ES 分布式层 + REST 接口层」收尾，并指出主分片定并行度、副本可在线调。

## 细节与核心 API

**建索引（7.x 固定 _doc，分片副本可设）：**

```bash
PUT /orders
{ "settings": { "number_of_shards": 3, "number_of_replicas": 1 },
  "mappings": { "properties": { "user_id": { "type": "keyword" }, "content": { "type": "text" } } } }
# 集群/分片核验（面试像做过线上）
GET _cat/nodes?v
GET _cat/shards/orders?v
GET _cluster/health
```

**核心运维坑（ES 起不来的第一关）：**

```bash
sysctl -w vm.max_map_count=262144   # mmapfs 映射数，不够 ES 直接起不来
ulimit -n 65536                     # es 运行用户文件描述符
```

**分布式写入/读取路径：**

```text
写入：客户端 → 协调节点 hash(routing)%主分片数 → 主分片写 → 副本异步同步
读取：可由副本分担；GET by _id 走 doc id 路由，search 走倒排
```
