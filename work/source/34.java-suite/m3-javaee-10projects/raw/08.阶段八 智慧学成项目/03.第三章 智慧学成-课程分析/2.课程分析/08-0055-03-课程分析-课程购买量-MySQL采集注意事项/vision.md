# 画面线理解：03-课程分析-课程购买量-MySQL采集注意事项

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\03-课程分析-课程购买量-MySQL采集注意事项_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:12, 01:27, 01:41, 02:07, 02:10, 02:14, 02:25, 02:37, 02:39, 02:44, 02:48, 03:10, 03:36, 03:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:00:35

1) 这一组画面整体在讲如何配置Hive以支持MySQL Binlog实时采集，并配置NIFI的MapCacheServer组件。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了Hive配置文件hive-site.xml中关于开启事务支持的配置项，包括hive.support.concurrency、hive.exec.dynamic.partition.mode、hive.txn.manager等。
画面2: 同画面1，鼠标光标在配置项上，强调事务支持配置。
画面3: 展示了Hive表结构的SQL语句，用于创建外部表course_orders_source。
画面4: 展示了Sublime Text编辑器中的hive-site.xml文件，包含Hive连接配置和事务支持配置。
画面5: 展示了Sublime Text编辑器中的hive-site.xml文件，光标在hive.exec.dynamic.partition.mode配置项上。
画面6: 展示了Windows资源管理器中hive-site.xml文件的路径。
画面7: 展示了Hive配置文件中事务支持配置项，包括hive.support.concurrency、hive.txn.manager等。
画面8: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。
画面9: 展示了NIFI流程图中Controller Service的配置界面。
画面10: 展示了NIFI中添加Controller Service的界面，选择DistributedMapCacheServer。
画面11: 展示了NIFI中添加Controller Service的界面，选择DistributedMapCacheServer。
画面12: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。
画面13: 展示了Hive配置文件中事务支持配置项，包括hive.support.concurrency、hive.txn.manager等。
画面14: 展示了NIFI中配置MapCacheServer的界面，以及NIFI处理流程：CaptureChangeMySQL → RouteOnAttribute → MySQLBinLogToHiveProcessor → PutHiveQL。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```xml
<property>
  <name>hive.support.concurrency</name>
  <value>true</value>
</property>
<property>
  <name>hive.exec.dynamic.partition.mode</name>
  <value>nonstrict</value>
</property>
<property>
  <name>hive.txn.manager</name>
  <value>org.apache.hadoop.hive.ql.lockmgr.DbTxnManager</value>
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
  <name>hive.support.concurrency</name>
  <value>true</value>
</property>
<property>
  <name>hive.exec.dynamic.partition.mode</name>
  <value>nonstrict</value>
</property>
<property>
  <name>hive.txn.manager</name>
  <value>org.apache.hadoop.hive.ql.lockmgr.DbTxnManager</value>
</property>
<property>
  <name>hive.compactor.initiator.on</name>
  <value>true</value>
</property>
<property>
  <name>hive.compactor.worker.threads</name>
  <value>1</value>
</property>
<property>
  <name>hive.enforce.bucketing</name>
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
