# 画面线理解：5-Hive的架构

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\5-Hive的架构【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:11, 00:36, 00:37, 01:20, 01:36, 01:39, 01:51, 02:18, 03:19, 03:41, 03:42, 04:14, 04:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:31:41

1) 这一组画面整体在讲Hive架构及其与元数据、MapReduce的关系。

2) 按时间顺序列出每张画面的要点：
画面1：
- 展示Hive架构图的上半部分：用户接口（Shell/CLI、JDB客户端、ODB客户端、We接口）指向Thrift服务器。
- 左侧导航栏显示当前章节为“2.2. Hive架构”。
- 画面右上角显示Hive特点：可扩展、易用性、容错性。

画面2：
- 展示Hive架构图的中间部分：Thrift服务器指向解析器、编译器、优化器、执行器。
- 画面右下角显示“元数据库”与执行器双向连接。

画面3：
- 展示Hive元数据概念：Hive的元数据 derby/MySQL，记录表与数据文件之间的映射关系。
- 展示示例SQL语句：
  1. hive可以将一个结构化的数据文件映射成一个数据库表
     create table t_access(id,name,date)
  2. 使用类SQL语句对文件进行查询
     select name,count(*) from t_access group by id;
- 展示access.txt文件内容：
  1.jack:12:30
  2.tom:13:20
  1.jack:15:20
  2.tom:18:40
- 展示“hive MapReduce任务”字样。

画面4：
- 展示Hive架构图的下半部分：执行器指向MapReduce和数据库。
- 画面左下角显示“MapReduce”和“数据库”两个模块。

画面5：
- 展示Hive元数据概念：Hive的元数据 derby/MySQL，记录表与数据文件之间的映射关系。
- 展示示例SQL语句：
  1. hive可以将一个结构化的数据文件映射成一个数据库表
     create table t_access(id,name,date)
  2. 使用类SQL语句对文件进行查询
     select name,count(*) from t_access group by id;
- 展示access.txt文件内容：
  1.jack:12:30
  2.tom:13:20
  1.jack:15:20
  2.tom:18:40
- 展示“hive MapReduce任务”字样。

画面6：
- 展示Hive架构图的完整结构：用户接口（Shell/CLI、JDB客户端、ODB客户端、We接口）指向Thrift服务器，Thrift服务器指向解析器、编译器、优化器、执行器，执行器指向MapReduce和数据库，元数据库与执行器双向连接。

画面7：
- 展示Hive元数据概念：Hive的元数据 derby/MySQL，记录表与数据文件之间的映射关系。
- 展示示例SQL语句：
  1. hive可以将一个结构化的数据文件映射成一个数据库表
     create table t_access(id,name,date)
  2. 使用类SQL语句对文件进行查询
     select name,count(*) from t_access group by id;
- 展示access.txt文件内容：
  1.jack:12:30
  2.tom:13:20
  1.jack:15:20
  2.tom:18:40
- 展示“hive MapReduce任务”字样。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
1. hive可以将一个结构化的数据文件映射成一个数据库表
create table t_access(id,name,date)
2. 使用类SQL语句对文件进行查询
select name,count(*) from t_access group by id;

画面5：
1. hive可以将一个结构化的数据文件映射成一个数据库表
create table t_access(id,name,date)
2. 使用类SQL语句对文件进行查询
select name,count(*) from t_access group by id;

画面7：
1. hive可以将一个结构化的数据文件映射成一个数据库表
create table t_access(id,name,date)
2. 使用类SQL语句对文件进行查询
select name,count(*) from t_access group by id;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- 标题：2.2. Hive架构
- 架构图结构：
  - 用户接口（Shell/CLI、JDB客户端、ODB客户端、We接口）→ Thrift服务器

画面2：
- 架构图结构：
  - Thrift服务器 → 解析器、编译器、优化器、执行器
  - 执行器 ↔ 元数据库

画面3：
- 无PPT标题，无架构图，无表格数据。

画面4：
- 架构图结构：
  - 执行器 → MapReduce、数据库

画面5：
- 无PPT标题，无架构图，无表格数据。

画面6：
- 标题：2.2. Hive架构
- 架构图结构：
  - 用户接口（Shell/CLI、JDB客户端、ODB客户端、We接口）→ Thrift服务器
  - Thrift服务器 → 解析器、编译器、优化器、执行器
  - 执行器 → MapReduce、数据库
  - 元数据库 ↔ 执行器

画面7：
- 无PPT标题，无架构图，无表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
