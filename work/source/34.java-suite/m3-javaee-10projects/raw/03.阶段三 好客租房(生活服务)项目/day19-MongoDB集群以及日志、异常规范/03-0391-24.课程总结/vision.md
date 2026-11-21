# 画面线理解：24.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\24.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:18, 00:23, 00:30, 00:38, 00:56, 01:01, 01:11, 02:01, 02:09, 02:26, 02:31, 02:52, 03:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:19:03

1) 这一组画面整体在讲什么（一句话）：
本课程视频讲解了 MongoDB 集群的复制集与分片集群架构、搭建方法、故障转移机制，以及 Java 开发中日志规范（特别是 SLF4J 的使用）和异常处理规范。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 讲解 MongoDB 复制集概念，包括目的（保证数据可靠性、提高读写能力）和机制（主从架构、主节点选举）。
画面 2: 展示“三个存储数据的复制集”架构图，包含一个 Primary 和两个 Secondary，通过 Replication 和 Heartbeat 连接。下方有“Election for New Primary”图示。
画面 3: 展示搭建复制集的 Docker 命令，包括创建三个 mongo 容器和启动它们。
画面 4: 讲解故障转移测试和增加 arbiter 节点。展示创建 arbiter 容器的命令和在主节点上执行 rs.addArb() 的命令。
画面 5: 进入“MongoDB集群之分片集群”章节，介绍分片（sharding）概念和两种扩展方式：垂直扩展和水平扩展。
画面 6: 展示分片集群架构图，数据被分片到 Shard A、B、C、D，每个分片存储 Collection1 的一部分。
画面 7: 讲解集群中数据分布，包括 Splitting 和 Balancing 机制。
画面 8: 讲解 chunksize 对分片和迁移的影响，以及默认 chunksize 为 64MB 的建议。
画面 9: 进入“日志规范”章节，从阿里巴巴 Java 开发手册说起，引出 SLF4J 的必要性。
画面 10: 介绍 SLF4J，说明其作为门面框架的作用，以及作者和与 Log4j、Logback 的关系。
画面 11: 展示创建 Maven 项目时的 GroupId 和 ArtifactId，以及导入 SLF4J 依赖的 XML 配置。
画面 12: 展示编写日志代码的示例，以及与 Log4j 整合时需要配置的 log4j.properties 文件。
画面 13: 讲解异常处理规范，包括 try-catch 的使用、finally 块的资源关闭、以及异常处理的强制性要求。
画面 14: 讲解异常处理的其他规范，包括自定义异常、RPC 调用返回方式、DRY 原则，以及推荐的编程规范和 MySQL 数据库规范。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```bash
#创建三个mongo容器
docker create --name mongo01 -p 27017:27017 -v mongo-data-01:/data/db mongo:4.0.3 --replicSet "rs0" --bind_ip_all
docker create --name mongo02 -p 27018:27017 -v mongo-data-02:/data/db mongo:4.0.3 --replicSet "rs0" --bind_ip_all
docker create --name mongo03 -p 27019:27017 -v mongo-data-03:/data/db mongo:4.0.3 --replicSet "rs0" --bind_ip_all

#启动容器
docker start mongo01 mongo02 mongo03

#进入容器操作
docker exec -it mongo01 /bin/bash

#登录到mongo容器
mongo 172.16.55.185:27017

#初始化复制集群
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "172.16.55.185:27017" },
    { _id: 1, host: "172.16.55.185:27018" },
    { _id: 2, host: "172.16.55.185:27019" }
  ]
})
```

画面 4:
```bash
#创建arbitrator节点
docker create --name mongo04 -p 27020:27017 -v mongo-data-04:/data/db mongo:4.0.3 --replicSet "rs0" --bind_ip_all

#启动容器
docker start mongo04

#在主节点执行
rs.addArb("172.16.55.185:27020")
```

画面 5:
```markdown
分片（sharding）是MongoDB用来将大型集合分割到不同服务器（或者设一个集群）上所采用的方法。尽管分片起源于关系型数据库分区，但MongoDB的最 大区别在于它几乎能自动完成所有事情，只要告诉MongoDB要分配数据，它就能自动维护数据在不同服务器之间的均衡。
```

画面 6:
```markdown
使用分片减少了每个分片存储的数据。例如，如果数据集有1TB的数据集，并有4个分片，然后每个分片可能仅有256GB的数据。如果有40个分片，那么每个分片可能只有25GB的数据。
```

画面 7:
```markdown
Splitting：当一个chunk的大小超过配置中的chunk size时，MongoDB的后台进程会把这个chunk切成更小的chunk，从而避免chunk过大的情况。
Balancing：在MongoDB中，balancer是一个后台进程，负责chunk的迁移，从而均衡各个shard server的负载。在MongoDB中，chunk size默认从64M生产，生产上选择适合业务的chunk size是最好的。MongoDB会自动分拆和迁移chunks。
```

画面 8:
```markdown
chunksize
小的chunksize：数据均衡是迅速的，数据分布更均匀，数据分片频繁，路由节点消耗更多资源。
大的chunksize：数据分片少，数据移动时中消耗和IO资源。
适合业务的chunksize是最好的。
chunksize 对分片及迁移的影响
MongoDB 默认的 chunkSize 为 64MB，如果不特殊要求，建议保持默认值；chunksize 会直接影响到 chunk 分片、迁移的行为。
chunksize 越小，chunk 分片及迁移越多，数据分布越均衡；反之，chunksize 越大，chunk 分片及迁移越少，从而可能导致数据分布不均。
chunk 自动分裂只会在数据写入时触发，所以如果将 chunksize 改小，系统需要一定的时间来将 chunk 分裂到指定的大小。
chunk 只会不断分裂，不会合并，所以固将 chunksize 改大，现有的 chunk 数量不会减少，但 chunk 大小会随着数据写入不断增长，直到达到目标大小。
```

画面 11:
```xml
<dependencies>
  <dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>1.7.26</version>
  </dependency>
</dependencies>
```

画面 12:
```xml
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-api</artifactId>
  <version>1.7.26</version>
</dependency>
```

画面 12:
```properties
log4j.rootLogger=DEBUG, A1
log4j.appender.A1=org.apache.log4j.ConsoleAppender
log4j.appender.A1.layout=org.apache.log4j.PatternLayout
log4j.appender.A1.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%c] %p %m%n
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图标题为“三个存储数据的复制集”。结构：一个 Primary 节点，两个 Secondary 节点。Primary 指向两个 Secondary，Secondary 之间有 Heartbeat 连接。下方有“Election for New Primary”图示，表示主节点选举过程。
画面 6: 架构图标题为“分片集群架构图”。结构：Collection1 数据被分片到 Shard A、B、C、D，每个分片存储 Collection1 的一部分。
画面 7: 无图示，但有文字描述 Splitting 和 Balancing 机制。
画面 8: 无图示，但有文字描述 chunksize 对分片及迁移的影响。
画面 12: 无图示，但有文字描述 log4j.properties 文件配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
