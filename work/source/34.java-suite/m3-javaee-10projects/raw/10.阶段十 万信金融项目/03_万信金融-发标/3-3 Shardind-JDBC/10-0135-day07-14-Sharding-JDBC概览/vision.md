# 画面线理解：day07-14-Sharding-JDBC概览

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-14-Sharding-JDBC概览_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:09, 01:20, 01:21, 02:15, 02:23, 02:28, 02:37, 04:45, 04:46, 05:12, 05:13, 05:15, 05:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:37:22

1) 这一组画面整体在讲什么（一句话）：
介绍分库分表带来的问题，并引出 Sharding-JDBC 作为解决方案，讲解其核心功能与适用场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 内容：讲解分库分表后无法通过常规 SQL 进行关联查询的问题，展示一个 LEFT JOIN 示例。
- 代码：
  SELECT p.*, s.*
  FROM [商品信息] p
  LEFT JOIN [店铺信息] s ON p.id = s.[店铺ID]
  WHERE p.order_by = 'LIMIT ...'

画面 2:
- 内容：展示分库分表后，通过在各节点执行分页查询，再合并结果的流程图。
- 流程图结构：
  - 左侧节点：执行 SELECT p.* FROM [商品信息] p ORDER BY p.id desc limit 0,10
  - 右侧节点：执行 SELECT p.* FROM [商品信息] p ORDER BY p.id desc limit 0,10
  - 合并节点：合并结果后，再执行 SELECT p.* FROM [商品信息] p ORDER BY p.id desc limit 0,10
  - 最终结果：最终结果

画面 3:
- 内容：介绍 Sharding-JDBC，说明其是解决分库分表问题的流行中间件。
- 文本：
  由于分库分表之后，数据被分散在不同的服务器、数据库和表中，因此，对数据的操作也就无法通过常规方式完成，并且它还带来了一系列的问题。我们在开发过程中需要通过一些中间件解决这些问题，市面上有很多中间件可供我们选择，其中Sharding-JDBC较为流行。

画面 4:
- 内容：继续介绍 Sharding-JDBC，说明其从 3.0 开始更名为 Sharding-Sphere，4.0 之后为 Apache 版本。
- 文本：
  Sharding-JDBC 是当当网研发的开源分布式数据库中间件。从 3.0 开始，Sharding-JDBC 更名为 Sharding-Sphere，之后该项目进入 Apache 孵化器，4.0 之后的版本为 Apache 版本。

画面 5:
- 内容：页面切换，显示 Sharding-JDBC 的概览内容。
- 文本：
  Sharding-JDBC 是当当网研发的开源分布式数据库中间件。从 3.0 开始，Sharding-JDBC 更名为 Sharding-Sphere，之后该项目进入 Apache 孵化器，4.0 之后的版本为 Apache 版本。

画面 6:
- 内容：展示 Sharding-JDBC 的 Maven 依赖配置。
- 代码：
  <dependency>
      <groupId>org.apache.shardingsphere</groupId>
      <artifactId>shardingsphere-jdbc-core</artifactId>
      <version>${latest.release.version}</version>
  </dependency>
- 注释：注意，请将 ${latest.release.version} 更改为实际的版本号。

画面 7:
- 内容：与画面 3 内容相同，介绍 Sharding-JDBC 是解决分库分表问题的流行中间件。
- 文本：
  由于分库分表之后，数据被分散在不同的服务器、数据库和表中，因此，对数据的操作也就无法通过常规方式完成，并且它还带来了一系列的问题。我们在开发过程中需要通过一些中间件解决这些问题，市面上有很多中间件可供我们选择，其中Sharding-JDBC较为流行。

画面 8:
- 内容：与画面 4 内容相同，介绍 Sharding-JDBC 的版本演进。
- 文本：
  Sharding-JDBC 是当当网研发的开源分布式数据库中间件。从 3.0 开始，Sharding-JDBC 更名为 Sharding-Sphere，之后该项目进入 Apache 孵化器，4.0 之后的版本为 Apache 版本。

画面 9:
- 内容：与画面 4 内容相同，介绍 Sharding-JDBC 的版本演进。
- 文本：
  Sharding-JDBC 是当当网研发的开源分布式数据库中间件。从 3.0 开始，Sharding-JDBC 更名为 Sharding-Sphere，之后该项目进入 Apache 孵化器，4.0 之后的版本为 Apache 版本。

画面 10:
- 内容：展示 Sharding-JDBC 的架构图，说明其作为中间件连接 Java 应用与数据库。
- 架构图结构：
  - Registry Center（注册中心）
  - Java Application（Java 应用程序）指向 Registry Center
  - Java Application（Java 应用程序）指向 Registry Center

画面 11:
- 内容：展示 Sharding-JDBC 的架构图，说明其连接多个数据库。
- 架构图结构：
  - 两个 Sharding-JDBC 模块
  - 三个 Databases（数据库）
  - Sharding-JDBC 模块指向 Databases

画面 12:
- 内容：介绍 Sharding-JDBC 的核心功能：数据分片和读写分离。
- 文本：
  Sharding-JDBC 可以进行分库分表，同时又可以解决分库分表带来的问题，它的核心功能是：数据分片和读写分离。
  2.2.1 数据分片
  数据分片是 Sharding-JDBC 核心功能，它是指按照某个维度将存放在单数据库中的数据分散存放在多个数据库或表中，以达到提升性能瓶颈以及可用性的效果。数据分片的有效手段是对关系型数据库进行分库和分表。在使用 Sharding-JDBC 进行数据分片前，需要了解以下概念：
  - 逻辑表
  - 水平拆分的数据库（表）的相同逻辑和数据结构的总称。例如：订单数据根据主键尾数拆分为 10 张表，分别是 t_order 0 到 t_order 9，他们的逻辑表名为 t_order。

画面 13:
- 内容：与画面 3 内容相同，介绍 Sharding-JDBC 是解决分库分表问题的流行中间件。
- 文本：
  由于分库分表之后，数据被分散在不同的服务器、数据库和表中，因此，对数据的操作也就无法通过常规方式完成，并且它还带来了一系列的问题。我们在开发过程中需要通过一些中间件解决这些问题，市面上有很多中间件可供我们选择，其中Sharding-JDBC较为流行。

画面 14:
- 内容：与画面 4 内容相同，介绍 Sharding-JDBC 的版本演进。
- 文本：
  Sharding-JDBC 是当当网研发的开源分布式数据库中间件。从 3.0 开始，Sharding-JDBC 更名为 Sharding-Sphere，之后该项目进入 Apache 孵化器，4.0 之后的版本为 Apache 版本。
