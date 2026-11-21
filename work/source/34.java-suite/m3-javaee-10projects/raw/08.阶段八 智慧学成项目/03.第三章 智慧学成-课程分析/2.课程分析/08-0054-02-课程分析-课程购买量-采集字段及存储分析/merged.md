# 02-课程分析-课程购买量-采集字段及存储分析

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\02-课程分析-课程购买量-采集字段及存储分析_【海量资源尽在 666java.com】.mp4
- 时长 6分25秒（音频 386s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面呢,咱们已经分析了课程购买量的那个原型根据原型呢,咱们可以看到课程购买量呢和课程访问量在图表展示上形式是一模一样的但是呢,数据来源是不一样的课程购买量的数据来源呢是来于用户的一个订单数据课程访问量的来源呢是来源的用户的一个访问行为数据是通过页面来获取的
[00:28] 这里呢,咱们课程购买量是通过数据库来获取的。
[00:32] 咱们前面已经将学乘在线系统的业务数据库导入到咱们的MySQL中。
[00:39] 这里呢,采集的时候就直接在这个MySQL中数据库中进行一个采集。
[00:46] 以下呢,是咱们就是要采集的一个字段的分析,就是咱们原始数据采集的一个分析。
[00:54] 咱们呢,来看咱们需要采集的。
[00:58] 数据库以及表是哪一个咱们要采集的数据库就是学城的订单库它对应的表就是订单表咱们把它给它打开这里订单表一共是有这么多子弹但是咱们采集的时候并不是需要把所有的都给采集过来咱们来对比来查看来看一下这里进行一个左右窗口的一个切换好
[01:37] 咱们来对着窗口进行一个说明在这里首先咱们要采集的字段呢就是有订单号订单号呢就是每一个订单唯一的一个标识接下来呢是订单的交易价格这个交易价格就是你当前花了多少钱这里呢你可以看到上面还有一个定价这个呢字段是咱们不需要采集的接下来呢是交易状态交易状态呢
[02:14] 包括可能包括你交易成功交易失败或者是一些或者是未付款的付款中啊这些等等接下来呢是起始时间起始时间呢这里对应咱们的一个交易时间就是咱们的一个订单时间咱们这个地方采集过来的资论呢需要把它给这个名字给修改一下接下来呢是用户的一个ID用户ID呢就是你具体的哪一个用户
[02:45] 购买的什么样的一个商品还有订单明细订单明细呢这里咱们订单明细呢它是一个json数据包含了这些就是订单号不是订单不是订单号这个是商品ID然后呢商品数量订单号以及订单的一个价格咱们把它给粘过来看一下这就是咱们需要采集的这个订单详情的一个数据
[03:20] 通过这个可以看到呢它是一个JSON的一个数组数据但是呢这个数组数据呢它这个数据商品是只有一条的也就是每个它虽然是用了一个数组来保存但是每个里边呢商品是只有一条的咱们可以再复制一个来看一下这里呢可以看到它商品是只有一条的它这个地方设计数组它可能的原因是什么呢后期为了系统的一个扩展
[03:51] 但是呢目前这一段它是只保存了一条数据咱们来看咱们的文档回到咱们的文档这里呢它这个订单商品的ID商品ID呢就是你当前商品具体的一个ID是多少商品数量呢这个是1因为咱们刚才说了这里呢它只有一个一条订单的一个数据每一个里边是只存了一条订单数据但是你对这一个订单进行购买的时候比如说你买了一套家务课程
[04:22] 你肯定不会你把这个加号课程同时买了两次这个呢在系统设计上它也是不允许的因为你一个商品购买一次就行了除非你这个商品购买了一个过期了过期之后你再次购买这里呢订单数据还是一接下来是订单编号订单编号呢和咱上面的订单编号是保持一致的商品价格商品价格呢由于商品数量只有一个这里呢和咱们交易价格也是一样的
[04:51] 好,这就是咱们采集的一个字段的一个介绍,接下来咱们来看咱们采集过来的数据是如何存储的,这里呢咱们是使用Hive存储保存到数据仓库中,这里Hive的表结构在咱们数据仓库章节呢已经导入,咱们可以使用HUE来看一下,这里呢咱们需要登录HUE,这里HUE呢登录需要一定的时间,有的时候它就稍微慢一点,有的时候呢会非常快。
[05:26] 这是咱们课程相关的,这里可以看到订单,就是原数据的一个表结构,和咱们的文档中的是一样的,它一共是这么多字段,咱们可以对比一下,这个呢,在咱们保存数据仓库导入Hive表结构的时候呢,已经导入成功,这里的字段呢,和咱们表结构字段肯定是对应上的,但是呢,它这个字段呢,又和咱们采集的字段是对应上的。
[05:57] 也就是说你采集了哪些字段咱们数据仓库中呢就如何进行一个保存这里呢订单详情在咱们数据仓库中呢保存也是它是以字符券进行保存但是它的格式呢也是阶层格式好以上呢就是咱们数据采集这一块采集的字段以及存储方式的一个介绍以及存储字段的一个介绍视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
- 下方展示“2.3.2.1 NiFi MySQL实时采集存储方式”下的“Hive表结构”SQL 语句：
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

