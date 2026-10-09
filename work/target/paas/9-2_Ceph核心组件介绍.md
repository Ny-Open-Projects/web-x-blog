# Go PaaS 平台开发: Ceph 核心组件介绍

## 纲要

- OSD（Object Storage Daemon）：集群数据落地的基本单元，负责数据复制、恢复、回填与再均衡
- MGR（ceph-mgr / Manager）：收集集群状态与运行指标，对外提供 Dashboard 与 Prometheus 等 API，高可用需至少两个实例
- MDS（ceph-mds / Metadata Server）：为 CephFS 文件存储提供元数据计算、缓存与同步
- MON（Monitor）：维护 cluster map 并保证数据一致性，汇总 OSD / MDS / MGR 等全部组件信息
- CRUSH 算法：Ceph 数据分布与寻址的核心，决定 PG 到 OSD 的映射关系

## OSD 对象存储守护进程

OSD（Object Storage Daemon）是 Ceph 分布式存储系统中出现最频繁的组件，也是整个系统最基础的存储单元。

- 集群中所有的数据最终都由 OSD 负责存储
- 负责处理数据的复制（replication）、故障恢复（recovery）、回填（backfill）与再均衡（rebalance）
- 硬盘通过 OSD 进行管理：Ceph 管理 OSD，OSD 再管理其下的物理硬盘

可以说，OSD 是 Ceph 把"对象"真正写到磁盘上的执行者。

## MGR 管理器

MGR（ceph-mgr，通常简称 manager）主要收集 Ceph 集群的状态与运行指标，包括：

- 存储利用率
- 系统负载
- 各类运行监控指标

同时，Manager 还对外提供 Dashboard（可视化界面）与 API（如 Prometheus 指标接口）。我们后续看到的 Ceph UI 以及 Prometheus 相关的 API，都是由 MGR 组件对外提供的。

需要特别注意的是，开启 MGR 高可用时，**至少需要两个实例**才能实现故障切换。

## MDS 元数据服务

MDS（ceph-mds，Metadata Server）是元数据服务，专门处理文件存储（CephFS）相关的事务：

- 为 Ceph 文件系统提供元数据的计算
- 提供元数据缓存
- 提供元数据同步服务

可以将其理解为元数据代理 / 缓存服务器。MDS 仅在需要使用 CephFS（文件存储）时才必须部署，对象存储（RBD）与块存储场景通常不依赖它。

## MON 监控组件

MON（Monitor，简称 MON）是集群中非常重要的组件，作用不止于"监控"：

1. 维护集群的 cluster map（集群地图）——记录集群的拓扑与同步信息，包括元数据信息、pool 相关接口信息等
2. 维护 cluster map 的二进制表，保证集群数据一致性
3. 汇总并维护所有组件信息：Monitor 自身、Manager、OSD、MDS，以及 CRUSH 算法相关的信息

正因为 MON 把所有信息汇总到一起进行维护，它并非单纯意义上的监控进程，而是集群状态一致性的守护者。MON 通常以 3 节点组成小集群，实时同步 OSD 等全部系统信息。

## CRUSH 算法

CRUSH（Controlled Replication Under Scalable Hashing）算法是 Ceph 存储操作系统的核心，决定了对象在集群中的分布方式。它配合 cluster map，实现了集群自动化的数据放置与故障域隔离，是后面讲述"存储过程"时 PG 到 OSD 映射的数学基础。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：否。
