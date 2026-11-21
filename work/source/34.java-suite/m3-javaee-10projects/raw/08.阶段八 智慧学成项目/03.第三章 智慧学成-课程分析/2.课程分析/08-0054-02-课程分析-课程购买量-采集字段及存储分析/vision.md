# 画面线理解：02-课程分析-课程购买量-采集字段及存储分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\02-课程分析-课程购买量-采集字段及存储分析_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:56, 01:22, 01:31, 01:39, 02:05, 03:17, 03:34, 04:13, 04:43, 04:57, 05:14, 05:40, 06:05, 06:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:00:06

1) 这一组画面整体在讲 ODS 层订单数据的结构定义、数据采集与存储方式，重点展示 MySQL 表结构、JSON 字段结构及 Hive 外部表的创建语句。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 展示了 MySQL 数据库中 `xc_orders` 表的数据查询结果，包含 order_number、initial_price、start_time、status、user_id、details 等字段。
- 右侧编辑器中显示了 `CREATE TABLE xc_orders` 的 SQL 语句，定义了各字段的数据类型和注释。
- 底部 SQL 语句为：`SELECT * FROM xc_orders LIMIT 1000;`

画面 2:
- 展示了 `CREATE TABLE xc_orders` 的 SQL 语句，字段定义包括：order_number (varchar(32)), initial_price (Float(6,2)), price (Float(8,2)), start_time (datetime), end_time (datetime), status (varchar(32)), user_id (varchar(32)), details (varchar(1000))。
- 右侧表格展示了字段的“字段说明”、“数据格式”和“数据样例”，如 order_number 为 uuid，price 为 float，status 为 int。

画面 3:
- 展示了文档目录结构，当前章节为“2.3 数据采集”下的“2.3.1 ODS层数据结构”。
- 右侧表格内容与画面 2 相同，展示了字段的“字段说明”、“数据格式”和“数据样例”。

画面 4:
- 与画面 3 类似，展示文档目录结构和右侧表格内容，但表格中“order_time”字段的“数据格式”显示为“时间戳”，“数据样例”为“1542421759”。

画面 5:
- 展示了文档目录结构和右侧表格内容，表格中“details”字段的“数据格式”为“json”，“数据样例”为 `[{"itemId": "", "itemNum": 1, "orderNumber": "", "itemPrice": ""}]`。

画面 6:
- 展示了 Sublime Text 编辑器，标题为“live stream”，内容为空。

画面 7:
- 展示了 MySQL 数据库中 `xc_orders` 表的数据查询结果，包含 order_number、initial_price、start_time、status、user_id、details 等字段。
- 右侧编辑器中显示了 `CREATE TABLE xc_orders` 的 SQL 语句。

画面 8:
- 展示了 Sublime Text 编辑器，标题为“live stream”，内容为两个 JSON 数组，分别包含 orderNumber、itemId、itemPrice 等字段。

画面 9:
- 展示了文档目录结构和右侧表格内容，表格中“details”字段的“数据格式”为“json”，“数据样例”为 `[{"itemId": "", "itemNum": 1, "orderNumber": "", "itemPrice": ""}]`。

画面 10:
- 展示了文档目录结构和右侧表格内容，表格中“details”字段的“数据格式”为“json”，“数据样例”为 `[{"itemId": "", "itemNum": 1, "orderNumber": "", "itemPrice": ""}]`。
- 下方开始展示“2.3.2 数据存储”章节，标题为“2.3.2.1 NiFi MySQL实时采集存储方式”。

画面 11:
- 展示了浏览器中 Hue 的登录页面，地址为 `xc-online.8888/hue/accounts/login/?next=/`。

画面 12:
- 展示了 Hue 的 Table Browser 界面，左侧显示了数据库和表列表，右侧显示了 `CREATE TABLE xc_orders` 的 SQL 语句。
- 右侧编辑器中显示了 `CREATE TABLE xc_orders` 的 SQL 语句。

画面 13:
- 展示了文档目录结构和右侧表格内容，表格中“details”字段的“数据格式”为“json”，“数据样例”为 `[{"itemId": "", "itemNum": 1, "orderNumber": "", "itemPrice": ""}]`。
- 下方开始展示“2.3.2 数据存储”章节，标题为“2.3.2.1 NiFi MySQL实时采集存储方式”。

画面 14:
- 展示了文档目录结构和右侧表格内容，表格中“details”字段的“数据格式”为“json”，“数据样例”为 `[{"itemId": "", "itemNum": 1, "orderNumber": "", "itemPrice": ""}]`。
- 下方展示“2.3.2.1 NiFi MySQL实时采集存储方式”下的“hive表结构”SQL 语句：
  ```
  CREATE EXTERNAL TABLE
  IF NOT EXISTS data_course.course_orders_source
  (order_number String,
  price Float,
  status String,
  order_time BIGINT,
  user_id String,
  details string)
  clustered by (order_number) into 2 buckets stored as orc
  TBLPROPERTIES ('transactional'='true');
  ```

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：

画面 1:
- SQL 语句：`SELECT * FROM xc_orders LIMIT 1000;`

画面 2:
- SQL 语句：
  ```sql
  CREATE TABLE xc_orders (
  order_number varchar(32) NOT NULL COMMENT '订单号',
  'initial_price' Float(6,2) DEFAULT NULL COMMENT '初始价',
  price Float(8,2) DEFAULT NULL COMMENT '交易价',
  start_time datetime NOT NULL COMMENT '开始时间',
  end_time datetime NOT NULL COMMENT '结束时间',
  status varchar(32) DEFAULT NULL COMMENT '交易状态',
  user_id varchar(32) DEFAULT NULL COMMENT '用户id',
  details varchar(1000) DEFAULT NULL COMMENT '订单明细',
  old_status varchar(32) DEFAULT NULL COMMENT '旧交易状态',
  PRIMARY KEY (order_number) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  ```

画面 3:
- 文档目录结构：
  ```
  2.3 数据采集
  2.3.1 ODS层数据结构
  ```

画面 4:
- 文档目录结构：
  ```
  2.3 数据采集
  2.3.1 ODS层数据结构
  ```

画面 5:
- 文档目录结构：
  ```
  2.3 数据采集
  2.3.1 ODS层数据结构
  ```

画面 6:
- 无代码。

画面 7:
- SQL 语句：
  ```sql
  CREATE TABLE xc_orders (
  order_number varchar(32) NOT NULL COMMENT '订单号',
  'initial_price' Float(6,2) DEFAULT NULL COMMENT '初始价',
  price Float(8,2) DEFAULT NULL COMMENT '交易价',
  start_time datetime NOT NULL COMMENT '开始时间',
  end_time datetime NOT NULL COMMENT '结束时间',
  status varchar(32) DEFAULT NULL COMMENT '交易状态',
  user_id varchar(32) DEFAULT NULL COMMENT '用户id',
  details varchar(1000) DEFAULT NULL COMMENT '订单明细',
  old_status varchar(32) DEFAULT NULL COMMENT '旧交易状态',
  PRIMARY KEY (order_number) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  ```

画面 8:
- 无代码。

画面 9:
- 无代码。

画面 10:
- 无代码。

画面 11:
- 无代码。

画面 12:
- SQL 语句：
  ```sql
  CREATE TABLE xc_orders (
  order_number varchar(32) NOT NULL COMMENT '订单号',
  'initial_price' Float(6,2) DEFAULT NULL COMMENT '初始价',
  price Float(8,2) DEFAULT NULL COMMENT '交易价',
  start_time datetime NOT NULL COMMENT '开始时间',
  end_time datetime NOT NULL COMMENT '结束时间',
  status varchar(32) DEFAULT NULL COMMENT '交易状态',
  user_id varchar(32) DEFAULT NULL COMMENT '用户id',
  details varchar(1000) DEFAULT NULL COMMENT '订单明细',
  old_status varchar(32) DEFAULT NULL COMMENT '旧交易状态',
  PRIMARY KEY (order_number) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
  ```

画面 13:
- 无代码。

画面 14:
- SQL 语句：
  ```sql
  CREATE EXTERNAL TABLE
  IF NOT EXISTS data_course.course_orders_source
  (order_number String,
  price Float,
  status String,
  order_time BIGINT,
  user_id String,
  details string)
  clustered by (order_number) into 2 buckets stored as orc
  TBLPROPERTIES ('transactional'='true');
  ```

4) PPT 标题、架构图/流程图的结构、表格数据：

画面 2:
- PPT 标题：2.3.1 ODS层数据结构
- 表格
