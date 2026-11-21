# day07-14-Sharding-JDBC概览

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-14-Sharding-JDBC概览_【海量资源尽在 666java.com】.mp4
- 时长 5分21秒（音频 322s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们给大家介绍了一下分库分表以及分库分表会带来的一些问题是吧那大家想一想分库分表这个事其实对于我们来说不是多大的难事那不就是拆分吗对吧把库给拆了把表给拆了其实这不是多大的难事那这里边的问题在于呢分库分表之后带来的刚才我们说到那一堆什么呀问题这些问题说实话
[00:30] 能解决吗能但是会比较的麻烦比较的费时费力费劲对不对所以说这里边核心的问题在这那怎么办呢那我们呢就去市面上找了一找对吧去行业里边找了一找我们发现呢这个有一些现成的框架可以分库分表同时还能帮我们解决什么呀对分库分表所带来的这些问题那么这里边呢以sharding
[00:59] GDBC相来说会比较流行一些所以说呢咱接下来就要学习sharding-GDBC这个框架通过它呢进行分库分表当然也要通过它来解决就刚才我们提到的分库分表带来的这一系列问题那咱接下来先整体了解一下这个sharding-GDBC它是国产的对不对国产的
[01:28] 来自于哪来自于当当网当当应该听说过吧电商平台啊虽然比不过这个什么呀电比不过这个京东对吧比不过淘宝天猫但是也是比较有名的啊当当网不知道大家有没有在这个网上买过书啊买过吗那么这个sharding-gdbc呢就是出自于当当网是一个数据库中间件
[01:58] 咱分布分辨指的比如说数据库这一块是不是从3.0呢还是啊3.0这个版本开始sharding gdbc改名改成sharding-sphere而且呢现在已经进入了什么呀apache的复发器420以后呢就是apache的版本了大家看这你看这是吧apache的是不是apache这里边就有sharding-gdbc它现在呢属于sharding-sphere那啥关系呢咱看一看
[02:30] 这个Sharding-Sphere它其实是一个什么生态圈它里边包含三个产品三个产品其中有一个就是咱们要学习的Sharding-GDPC剩下这两个你听一下就行了我们暂时用不着我们目前重点关注的是Sharding-GDPC也就是说Sharding-GDPC现在是属于Sharding-Sphere里边的其中一个什么产品
[02:56] 这三个产品都是相互独立的你可以只用其中的一个就可以那么相应杠GDPC呢它的定位是轻量级的加二框架啊比如说它是一个框架它是在加二GDPC的这个基础上又怎么说呢增强了功能啊提供了额外的一些什么呀服务比如说分股分辨比如说可以解决分股分辨的带来的问题也是加班的形式提供的
[03:24] 我们可以把sharding-gdbc理解为增强版的什么呀gdbc也就是说我们以前的那个gdbc大家还有印象吗咱最早学习这个数据库操作加在一块数据库操作是不是就是gdbc嘛那么原来那个gdbc驱动了呢你可以认为它主要是针对单库单表对不对那我们要想这个去操作这个分库分表的这种情况那用原来的那个gdbc就不想了我们就可以用什么呀sharding-gdbc
[03:54] 它专门可以用来分库分表以及解决分库分表的问题然后呢它还兼容GDPC而且还适应适配各种什么呀对持久层的框架比如说啊看一下比如说我们这个常见的持久层框架GPA啊HB的MyBalance啊等等它全部都支持那数据互联持它常见的也都支持比如说我们项目当中用的是这个德鲁伊对不对它都支持啊包括比较老牌的43P0啊DBCP啊这些它全都支持
[04:24] 而说一括呢他好多也都支持比如说我们用的MesacoOraclePRSoc等等他全都支持所以你看这个Sharding-GDPC他整个生态还是非常不错的你不用担心啊我用了他之后是不是别的框架就不能用了或者说这个什么地方就受影响没有啥影响对不对直接就可以拿来用那这个图里边主要是给你展示这个Sharding
[04:50] -GDPC它在整个这个应用啊或者整个这个结构框架当中它所处的一个位置其实它所处的这个位置就是原来GDPC所处的你可以简单认为就是把原来的GDPC直接给它换成什么呀Sharding-GDPC就OK了那它功能就增强了可以应付什么分库分秒相关的一些操作这是我们整体吧了解了一下这个谁呀Sharding-GDPC

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

