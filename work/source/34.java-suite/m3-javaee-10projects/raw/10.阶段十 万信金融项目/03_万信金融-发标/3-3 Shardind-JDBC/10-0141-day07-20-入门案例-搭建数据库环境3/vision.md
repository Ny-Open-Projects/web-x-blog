# 画面线理解：day07-20-入门案例-搭建数据库环境3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-20-入门案例-搭建数据库环境3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:23, 00:55, 01:24, 01:36, 01:50, 02:11, 02:22, 02:28, 02:45, 03:03, 03:28, 03:50, 04:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:41:37

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
