# day07-20-入门案例-搭建数据库环境3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-20-入门案例-搭建数据库环境3_【海量资源尽在 666java.com】.mp4
- 时长 4分26秒（音频 263s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们在本地把主从架构以及主从数据同步功能全部搞定搞定完之后呢咱接下来开始造库造表就是初始化我们的数据库都需要造哪一库哪一表还有印象吗那没有印象的话咱往这看啊往这看咱们前面在讲数据库设计的时候是不是已经把库和表给确定下来是不是怎么拆分嘛最终我们确定一共有三个库StoreDB
[00:30] product db1还有product db2是不是store db这里边就一张表存储店铺的信息product db这两个库里边呢都是四张表我们进行了水平拆分吧商品信息一商品描述一商品信息二商品描述二咱接下来就是把这几个库几张表给造一下怎么造呢我们这给大家提供的有现成的脚本三个搜口就是三个库码在这
[01:03] 这两个还有这这三个分别执行刚才我们说的那三个库以及库里边的那几张表就全部造出来那按照顺序我们最好是先造这个库就是店铺然后再造这两个商品信息这个库那你直接把它打开就行了用速回啊直接在这运行就行了另外呢提醒大家注意这几个脚本我在执行的时候都是放到主库里边运行
[01:34] 大家看我的搜索项这里边有几个链接对两个链接这个链接就是大家现在看到当前这个链接lookhost的它是链接的主库就是3306而这个带有-SE的这个链接连的是从库就是3307那我这几个脚本全是在主库里边运行了我们先执行第一个脚本我直接运行了好大家看一下这已经全部成功了是不是然后我们这边刷新一下库已经出来了
[02:09] 里边的表也出来了而且这个表里边我们还给了两行测试数据然后呢咱顺便把这两个脚本也都给他拽进来执行一下这个也拽进来我们分别执行一下先执行这个product db1执行这是创建product的db1这个数据库以及里边的四张表我们稍等片刻这边你看全部都成功了是不是我们这边再刷新一下
[02:50] 你看这个数据库也就出来了里边四张表表里边都是空的然后我们再执行这个脚本这个脚本呢是用来创建product db2这个数据库而且里边也有几张表四张表稍等一下好全部执行成功我们这呢再刷新一下然后你看db2是吧然后我们展开里边四张表对吧然后提醒大家注意啊我这三个脚本都是在主库这边运行了从库这边我运行了没有
[03:23] 从库那边我没有执行这三个脚本但是咱接下来切换到从库这边咱看一下看啥呢你看我刷新一下好我们再刷新一下再刷新一下大家看到这三个库是不是全部都有然后你再看这里边表是不是也都有数据是不是也有对吧这这些都有这四张表
[03:46] 还有这四张表是不是都有对不对那这顺便是不是把我们前面这个主从库的数据同步功能也测出来是不是没有问题吧因为我再次给大家强调一下我们刚才是不是只是在主库这边是不是执行了这些脚本从库里边可没执行但是我们切换到从库这边之后你得注意要刷新一下要刷新然后你会发现这边库也有了表也有了那不就是说我们的这个主从这个数据同步功能也是没问题
[04:16] 那到目前为止吧咱们把数据库整个这套环境就全部搭建完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何搭建 MySQL 主从同步环境并初始化分库分表数据。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录结构，当前章节为“2.3.4.1 MySQL主从同步”，并列出主库配置文件（my.ini）中需修改的配置项，包括 server-id、log-bin、binlog-do-db、binlog-ignore-db 等。
画面2：展示数据库分库分表的架构图，包含 STORE_DB、PRODUCT_DB_1、PRODUCT_DB_2 三个数据库，以及它们内部的表结构和关联关系。
画面3：展示课程目录结构，当前章节为“2.3.4.2 初始化数据库”，并说明需执行 store_db.sql 和 product_db_2.sql 脚本。
画面4：SQLyog 连接本地 MySQL 服务，显示数据库列表，但尚未选择任何数据库。
画面5：SQLyog 连接本地 MySQL 服务，已选择数据库为 store_db。
画面6：SQLyog 中打开并显示 store_db.sql 脚本内容，包含创建数据库和表的 SQL 语句。
画面7：SQLyog 中执行 store_db.sql 脚本，成功创建 store_db 数据库和 store_info 表。
画面8：SQLyog 中打开并显示 product_db_1.sql 脚本内容，包含创建数据库和表的 SQL 语句。
画面9：SQLyog 中执行 product_db_1.sql 脚本，成功创建 product_db_1 数据库和相关表。
画面10：SQLyog 中执行 product_db_1.sql 脚本后，显示执行结果，包含执行时间、警告信息和表结构。
画面11：SQLyog 中打开并显示 product_db_2.sql 脚本内容，包含创建数据库和表的 SQL 语句。
画面12：SQLyog 中连接到本地 MySQL 服务，但未选择任何数据库。
画面13：SQLyog 中连接到本地 MySQL 服务，选择数据库为 product_db_2，显示表结构。
画面14：SQLyog 中连接到本地 MySQL 服务，选择数据库为 product_db_2，显示表数据，包含 store_name、region_code 字段。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
[mysqld]
#设置日志
log-bin = mysql-bin
#设置服务id，主从不一致
server-id = 1
#设置需要同步的数据库
binlog-do-db=store_db
binlog-do-db=product_db_1
binlog-do-db=product_db_2
#屏蔽系统同步
binlog-ignore-db=mysql
binlog-ignore-db=information_schema
binlog-ignore-db=performance_schema

画面6：
CREATE DATABASE `store_db` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE `store_db`;
DROP TABLE IF EXISTS `store_info`;
CREATE TABLE `store_info` (
`id` INT(11) NOT NULL COMMENT 'ID',
`store_name` VARCHAR(100) NOT NULL COMMENT '店铺名称',
`region_code` INT(11) NOT NULL COMMENT '区域编码',
`PRIMARY KEY (`id`) USING BTREE
) ENGINE = INNODB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;
INSERT INTO `store_info` VALUES (1, '南京德才', 4, '110109');
INSERT INTO `store_info` VALUES (2, '南京德才', 3, '110109');

画面8：
DROP TABLE IF EXISTS `product_descript_1`;
CREATE TABLE `product_descript_1` (
`id` INT(11) NOT NULL COMMENT 'ID',
`product_info_id` INT(20) NOT NULL COMMENT '商品描述ID',
`store_info_id` INT(20) NOT NULL COMMENT '店铺ID',
`description` VARCHAR(255) NOT NULL COMMENT '商品描述',
`PRIMARY KEY (`id`) USING BTREE
) ENGINE = INNODB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;
DROP TABLE IF EXISTS `product_descript_2`;
CREATE TABLE `product_descript_2` (
`id` INT(11) NOT NULL COMMENT 'ID',
`product_info_id` INT(20) NOT NULL COMMENT '商品描述ID',
`description` VARCHAR(255) NOT NULL COMMENT '商品描述',
`PRIMARY KEY (`id`) USING BTREE
) ENGINE = INNODB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

画面11：
DROP TABLE IF EXISTS `product_info_1`;
CREATE TABLE `product_info_1` (
`id` INT(11) NOT NULL COMMENT 'ID',
`product_info_id` INT(20) NOT NULL COMMENT '商品ID',
`description` VARCHAR(255) NOT NULL COMMENT '商品描述',
`PRIMARY KEY (`id`) USING BTREE
) ENGINE = INNODB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：架构图包含三个数据库：STORE_DB、PRODUCT_DB_1、PRODUCT_DB_2。STORE_DB 中的 store_info 表指向 PRODUCT_DB_1 中的 product_descript_1 表，PRODUCT_DB_1 中的 product_descript_1 表指向 PRODUCT_DB_2 中的 product_descript_2 表。

5) 无。

