---
disableNunjucks: true
title: "Go 项目开发: ES 集群内与跨集群数据迁移实战"
date: 2026-10-02 08:00:00
categories: [es, Elasticsearch, 运维]
tags: [reindex, reroute, 数据迁移, 下线节点, 双写]
---

# Go 项目开发: ES 集群内与跨集群数据迁移实战

实际业务中**跨集群迁移的场景其实很少**，遇到更多的是集群内迁移（下线节点、调整分片分布）。真正需要跨集群时，方案选择完全取决于具体场景 —— 没有万能解。

## 纲要

- 集群内迁移的三种场景
- 场景一：整个集群搬迁（机器换机房）
- 场景二：只迁移部分索引（reindex 六步法）
- reindex 的关键参数与三条硬限制
- 场景三：新旧集群网络不通（业务数据回放）

## 集群内迁移的三种场景

### 下线节点

支持按 IP、通配符、节点名三种方式：

```txt
# 按 IP 下线（逗号分隔）
PUT /_cluster/settings
{
  "transient": {
    "cluster.routing.allocation.exclude._ip": "192.168.1.60,192.168.1.61"
  }
}

# 按 IP 段下线
PUT /_cluster/settings
{
  "transient": {
    "cluster.routing.allocation.exclude._ip": "192.168.1.*"
  }
}

# 按节点名下线
PUT /_cluster/settings
{
  "transient": {
    "cluster.routing.allocation.exclude._name": "node-1,node-2"
  }
}
```

### 手动调整分片分布

用 `reroute` 把指定分片挪到指定节点：

```txt
POST /_cluster/reroute
{
  "commands": [
    {
      "move": {
        "index": "order",
        "shard": 1,
        "from_node": "node-1",
        "to_node": "node-2"
      }
    }
  ]
}
```

如果分片数据损坏无法修复（比如磁盘坏了），在**允许该分片数据丢失**的前提下，加 `accept_data_loss: true` 强制分配，之后再从上游重建索引数据。

### shrink

`shrink` 需要先把原索引的全部分片迁移到同一个节点上再执行，这个过程本身也涉及分片迁移。

## 场景一：整个集群搬迁

机房调整这类场景，**不需要另搭一套集群**。最简单有效的办法是：把新机器直接加入现有集群，等分片重平衡完成，再下线旧节点。

```txt
1. 确保新增节点与现有集群内网互通（可临时授权，迁移完再取消）
2. 新节点加入集群，等待分片重平衡完成
3. 应用侧把 ES 连接配置改为新节点
4. 通过 API 下线旧节点
5. 把集群 discovery.seed_hosts 改为新节点的 host/IP
```

这种方式**只依赖集群内分片平衡**，运维成本低、速度快，遇到整机房迁移应优先考虑。

## 场景二：只迁移部分索引

可选方案有三种：`reindex`、**业务数据回放**、Logstash。后两者与 reindex 原理相同（都是靠 scroll API 滚动查询），Logstash 还要引入第三方中间件。网络抖动或 ES 负载高都会导致迁移中断，综合下来 **reindex 更简单**。

### reindex 六步法

```txt
# 1）停止原索引写入（写入走 MQ 的话，暂停业务消费，避免数据丢失）

# 2）目标集群关闭副本并调大 refresh 间隔，加快写入
PUT /target_index/_settings
{
  "index": {
    "refresh_interval": "-1",
    "number_of_replicas": 0
  }
}

# 3）执行 reindex
POST /_reindex
{
  "conflicts": "proceed",
  "source": {
    "remote": {
      "host": "http://source-es:9200",
      "username": "xxx",
      "password": "xxx"
    },
    "index": "source_index",
    "size": 1000
  },
  "dest": {
    "index": "target_index",
    "op_type": "create"
  }
}

# 4）查看迁移进度
GET /_tasks?detailed=true&actions=*reindex

# 5）先 refresh 再比对文档数（index buffer 里可能还有数据）
POST /target_index/_refresh
GET /target_index/_count

# 6）恢复目标索引的 refresh_interval 与副本数
```

### 关键参数

| 参数 | 作用 | 注意 |
| --- | --- | --- |
| `slices` | 把 reindex 拆成多个任务并发执行，大幅提升速度 | 建议设为物理 CPU 的一半；**从远程集群执行时不支持设置** |
| `conflicts: proceed` | 遇到版本冲突继续执行而不是中断 | 迁移期间文档被修改会触发版本冲突 |
| `op_type: create` | 目标已存在的文档跳过，只写不存在的 | 发现数量差异大时可重复执行，不用删索引重来 |
| `source.size` | 每次从源集群读取多少条 | **大文本要调小**，一次查太多会导致查询失败 |

### 三条硬限制

- **`_source` 必须开启**，否则不支持 reindex。
- **不能从高主版本 reindex 到低主版本**（如 7.x → 6.x 不支持）。
- **目标集群的所有节点都要把远程主机加入白名单**（`reindex.remote.whitelist`），否则连不上源集群。

## 场景三：新旧集群网络不通

可选方案：业务数据回放、`elasticsearch-dump` 导出导入、快照备份还原。

**后两种对大数据量基本行不通**：

- TB / PB 级索引导出不是一两天能完成的，**成功率无法保证**。
- 导出过程系统负载很高，会**影响线上业务**。
- 导出期间**新增数据无法及时同步**。

而且线上应用通常要求迁移期间继续提供服务，先导出再恢复的方案天然不满足。

```mermaid
graph LR
    A[上游持久化数据] -->|分页读取全量字段| B[搜索服务]
    B --> C[写入新集群 集群二]
    B --> D[同时写入旧集群 集群一]
    E[业务新增/更新数据] --> B
    D --> F[旧集群继续对外服务]
    C --> G[全量导入完成后 下线旧集群]
```

**业务数据回放的做法**：

- 从上游持久化数据分页获取索引需要的全部字段，写入新集群。
- 迁移期间的**新增与更新数据双写**新旧两个集群，保证两边都是最新。
- 旧集群继续对外服务，直到新集群全量导入完成再切换下线。

如果 MQ 队列里本来就保留了全量数据，也可以从头消费；但队列通常有清理策略，过期数据会被删掉，所以一般要依赖上游持久化数据。整个过程可能持续数天甚至数周 —— **但换来的是不停服**，这是其他方案难以满足的。

## 迁移方案速览

```dir
migration/
├── 集群内迁移
│   ├── 下线节点（exclude._ip）
│   ├── reroute 手动挪分片
│   └── shrink 缩分片
├── 整集群搬迁
│   └── 加节点 → 平衡 → 下线旧
├── 部分索引迁移
│   └── reindex 六步法
│       ├── 关副本 / 调 refresh
│       └── conflicts=proceed
└── 网络不通
    └── 业务数据回放双写
```

## 总结

迁移方案的选择逻辑很清晰：**整集群搬迁就加节点进集群再下线旧节点**；**部分索引用 reindex**（记得关副本、调 refresh、设 `conflicts=proceed`）；**网络不通就走业务数据回放双写**。三条硬限制（`_source` 开启、版本不能倒退、远程白名单）在动手前先确认，能省掉大量返工。

