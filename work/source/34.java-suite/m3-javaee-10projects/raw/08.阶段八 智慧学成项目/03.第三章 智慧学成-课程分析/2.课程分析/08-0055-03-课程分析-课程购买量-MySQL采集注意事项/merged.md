# 03-课程分析-课程购买量-MySQL采集注意事项

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\03-课程分析-课程购买量-MySQL采集注意事项_【海量资源尽在 666java.com】.mp4
- 时长 3分48秒（音频 229s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前边呢,咱们已经介绍了采集的字段,是咱们是采集学程在线这个业务数据的哪张表,采集哪张表的哪些字段,以及呢,咱们数据仓库中的一个存储方式。
[00:14] 接下来呢,就是咱们使用NiFi呢,进行一个MySQL的一个实时采集,但是开始之前呢,有两个注意事项需要说一下,第一个呢,就是Hive需要开启事物。
[00:29] 咱们这个地方的一个采集呢是属于一个特殊的采集因为是采集的mycircle的数据监听呢是监听的mycircle的binlog进行的一个采集咱们订单数据呢它可能会有insert的操作也可能会有update的操作这里update的操作呢主要就是对订单状态的一个修改insert的操作呢肯定是有新的订单进来了insert的操作呢它一般情况下只要有补货了之后呢
[01:00] 保证到咱们数据仓库中只有这一个操作的情况下咱们数据仓库是不需要进行一个修改的但是如果订单状态进行了一个修改咱们是不是要对数据仓库中的数据也需要进行修改这里就需要开启Hive的事务支持就是允许Hive进行一个增伤改查这里咱们只针对上面这张表
[01:29] 就是咱们数据存储呢这张表开启了事物这个地方呢可以看到这个地方有一个事物等于处就是开启了这个事物开启事物的配置呢咱们在容器编排的时候呢已经配置好咱们可以来到咱们的数据仓库来看一下这个呢是咱们Hive配置的目录就是OPT下OPT目录内CDH咱们大数据环境的这个目录下的Config目录中Hive这个目录内
[02:02] 有一个Hive Set的XML咱们配置呢就是配置了它这里呢已经将Hive的配置呢Hive开启事物的配置配置好这里再次强调一遍呢就是需要你知道这个地方Hive开启了这个事物的配置而且呢咱们已经配置好好这是咱们第一个注意事项第二个注意事项呢就是Netflix呢配置咱们那个缓存服务全局呢只有一个即可
[02:31] 咱们在前面配置联动的时候就是课程访问量配置联动的时候这里呢已经配置了一个就是咱们这个MAP-KG-SERO配置完成之后呢这里也强调了一遍就是全局只有一个即可这里呢再次强调咱们前面已经将这个配置这个缓存服务呢配置好了咱们下边呢就是后边使用的时候呢直接连接就行就是直接使用那个缓存服务的扣端
[03:02] 直接呢他会直接找得到然后进行一个连接就行咱们这里呢已经配置好就不需要再次配置你需要知道咱们已经配置好直接用即可如果配置多了呢他会造成就是说你服务找不到或者端口冲突的一个问题这里是需要咱们注意的好以上呢咱们讲了两个注意事项第一个呢就是Hive开启了一个事务的一个操作允许呢指定的表
[03:33] 进行增长改查另外一个呢就是咱们NiFi开启了一个缓存服务缓存服务呢全局有一个就行了好注意事项的介绍呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置Hive以支持MySQL Binlog实时采集，并配置NIFI的MapCacheServer组件。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了Hive配置文件Hive-site.xml中关于开启事务支持的配置项，包括Hive.support.concurrency、Hive.exec.dynamic.partition.mode、Hive.txn.manager等。
画面2: 同画面1，鼠标光标在配置项上，强调事务支持配置。
画面3: 展示了Hive表结构的SQL语句，用于创建外部表course_orders_source。
画面4: 展示了Sublime Text编辑器中的Hive-site.xml文件，包含Hive连接配置和事务支持配置。
画面5: 展示了Sublime Text编辑器中的Hive-site.xml文件，光标在Hive.exec.dynamic.partition.mode配置项上。
画面6: 展示了Windows资源管理器中Hive-site.xml文件的路径。
画面7: 展示了Hive配置文件中事务支持配置项，包括Hive.support.concurrency、Hive.txn.manager等。
画面8: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。
画面9: 展示了NIFI流程图中Controller Service的配置界面。
画面10: 展示了NIFI中添加Controller Service的界面，选择DistributedMapCacheServer。
画面11: 展示了NIFI中添加Controller Service的界面，选择DistributedMapCacheServer。
画面12: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。
画面13: 展示了Hive配置文件中事务支持配置项，包括Hive.support.concurrency、Hive.txn.manager等。
画面14: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```xml
<property>
  <name>Hive.support.concurrency</name>
  <value>true</value>
</property>
<property>
  <name>Hive.exec.dynamic.partition.mode</name>
  <value>nonstrict</value>
</property>
<property>
  <name>Hive.txn.manager</name>
  <value>org.apache.Hadoop.Hive.ql.lockmgr.DbTxnManager</value>
</property>
```

画面3:
```sql
CREATE EXTERNAL TABLE
IF NOT EXISTS data_course.course_orders_source
(order_number String,
price Float,
status String,
order_id String,
user_id String,
details String)
CLUSTERED BY (order_number) INTO 2 BUCKETS stored as orc
TBLPROPERTIES ('transactional'='true');
```

画面4:
```xml
<property>
  <name>Hive.support.concurrency</name>
  <value>true</value>
</property>
<property>
  <name>Hive.exec.dynamic.partition.mode</name>
  <value>nonstrict</value>
</property>
<property>
  <name>Hive.txn.manager</name>
  <value>org.apache.Hadoop.Hive.ql.lockmgr.DbTxnManager</value>
</property>
<property>
  <name>Hive.compactor.initiator.on</name>
  <value>true</value>
</property>
<property>
  <name>Hive.compactor.worker.threads</name>
  <value>1</value>
</property>
<property>
  <name>Hive.enforce.bucketing</name>
  <value>true</value>
</property>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面8:
流程图结构：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL

画面12:
表格数据：
| Name | Type | Version | Tags | Status | Scope |
|------|------|---------|------|--------|-------|
| DistributedMapCacheClientService | 1.9.2 | cluster, cache, distributed, ... | 1.9.2 | Enabled | 1.9.2 |
| DistributedMapCacheLookupService | 1.9.2 | cluster, cache, distributed, ... | 1.9.2 | Enabled | 1.9.2 |
| DistributedMapCacheServer | 1.9.2 | cluster, cache, distributed, ... | 1.9.2 | Enabled | 1.9.2 |

5) 无。

