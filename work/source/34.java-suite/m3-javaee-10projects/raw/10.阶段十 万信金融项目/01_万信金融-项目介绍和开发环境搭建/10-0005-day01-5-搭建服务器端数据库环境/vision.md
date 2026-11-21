# 画面线理解：day01-5-搭建服务器端数据库环境

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-5-搭建服务器端数据库环境_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:22, 01:08, 02:31, 02:48, 02:53, 03:11, 03:16, 03:22, 03:43, 03:50, 03:54, 04:27, 04:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:02:25

1) 这一组画面整体在讲什么（一句话）：
讲解万信金融P2P项目开发环境搭建，重点是数据库环境配置和SQL脚本执行。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目介绍PPT，内容包括P2P金融定义、商业模式（P2P个人对个人交易）、风险（资金监管模式）。
画面2：PPT页面切换，显示“1.1 项目背景”章节，内容与画面1相同。
画面3：展示PPT“1 服务端搭建”章节，内容包括“1.1 数据库环境”，说明项目使用MySQL数据库（v5.6.5+），端口号默认3306，需执行SQL脚本导入数据。
画面4：展示文件资源管理器，路径为“wanxinP2P-day01”，包含“万信金融-第1章-开发环境搭建v1.0.pdf”等文件。
画面5：展示SQLyog数据库管理工具界面，连接到localhost，显示数据库列表，当前未打开任何SQL文件。
画面6：SQLyog界面，鼠标点击“wanxingp2p-init.sql”文件，准备执行。
画面7：SQLyog界面，打开并显示“wanxingp2p-init.sql”文件内容，包含创建数据库和表的SQL语句。
画面8：SQLyog界面，显示“wanxingdepository-init.sql”文件内容，包含创建多个数据库的SQL语句。
画面9：SQLyog界面，显示“wanxingdepository-init.sql”文件内容，包含创建“account”表和“role”表的SQL语句。
画面10：SQLyog界面，显示“wanxingdepository-init.sql”文件内容，包含创建“balance_details”表的SQL语句。
画面11：展示PPT“1 服务端搭建”章节，内容包括“1.1 数据库环境”，列出数据库清单。
画面12：PPT页面，内容与画面11相同，展示数据库清单。
画面13：PPT页面，内容与画面3相同，说明安装MySQL数据库和执行SQL脚本。
画面14：PPT页面，内容与画面3相同，说明安装MySQL数据库和执行SQL脚本。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7 SQL内容：
```sql
--!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT;
--!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS;
--!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION;
--!40101 SET NAMES utf8;
--!40101 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, @OLD_SQL_MODE=@@SQL_MODE, @OLD_SQL_NOTES=@@SQL_NOTES;
--!40101 SET @OLD_SQL_MODE=@@SQL_MODE, @OLD_SQL_NOTES=@@SQL_NOTES;

CREATE DATABASE p2p_bank_depository CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE p2p_bank_depository;

DROP TABLE IF EXISTS `balance_details`;

CREATE TABLE `balance_details` (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  USER_ID BIGINT(20) DEFAULT NULL COMMENT '用户ID',
  USER_TYPE VARCHAR(20) DEFAULT NULL COMMENT '用户类型',
  AMOUNT DECIMAL(10,2) DEFAULT NULL COMMENT '交易金额',
  STATUS TINYINT(4) DEFAULT NULL COMMENT '状态',
  BALANCE DECIMAL(10,2) DEFAULT NULL COMMENT '可用金额',
  CREATE_TIME DATETIME DEFAULT NULL COMMENT '创建时间',
  UPDATE_TIME DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='账户余额表';
```

画面8 SQL内容：
```sql
DROP DATABASE IF EXISTS p2p_uaa;
DROP DATABASE IF EXISTS p2p_account;
DROP DATABASE IF EXISTS p2p_consumer;
DROP DATABASE IF EXISTS p2p_repayment;
DROP DATABASE IF EXISTS p2p_transaction_0;
DROP DATABASE IF EXISTS p2p_transaction_1;
DROP DATABASE IF EXISTS p2p_undo_log;
DROP DATABASE IF EXISTS p2p_file;
DROP DATABASE IF EXISTS p2p_bank_depository;
DROP DATABASE IF EXISTS p2p_depository_agent;
DROP DATABASE IF EXISTS p2p_reconciliation;
```

画面9 SQL内容：
```sql
USE p2p_account;

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  USERNAME VARCHAR(50) DEFAULT NULL COMMENT '用户名',
  PASSWORD VARCHAR(50) DEFAULT NULL COMMENT '密码',
  EMAIL VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
  STATUS TINYINT(4) DEFAULT NULL COMMENT '状态',
  CREATE_TIME DATETIME DEFAULT NULL COMMENT '创建时间',
  UPDATE_TIME DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='账户表';

-- Create syntax for TABLE 'role'
CREATE TABLE `role` (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  NAME VARCHAR(50) DEFAULT NULL COMMENT '角色名',
  CODE VARCHAR(50) DEFAULT NULL COMMENT '角色编码',
  STATUS TINYINT(4) DEFAULT NULL COMMENT '状态',
  CREATE_TIME DATETIME DEFAULT NULL COMMENT '创建时间',
  UPDATE_TIME DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='角色表';
```

画面10 SQL内容：
```sql
USE p2p_bank_depository;

DROP TABLE IF EXISTS `balance_details`;

CREATE TABLE `balance_details` (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  USER_ID BIGINT(20) DEFAULT NULL COMMENT '用户ID',
  USER_TYPE VARCHAR(20) DEFAULT NULL COMMENT '用户类型',
  AMOUNT DECIMAL(10,2) DEFAULT NULL COMMENT '交易金额',
  STATUS TINYINT(4) DEFAULT NULL COMMENT '状态',
  BALANCE DECIMAL(10,2) DEFAULT NULL COMMENT '可用金额',
  CREATE_TIME DATETIME DEFAULT NULL COMMENT '创建时间',
  UPDATE_TIME DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='账户余额表';
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3、11、12、13、14 PPT内容：
标题：“1 服务端搭建”
子标题：“1.1 数据库环境”
内容：
“本项目使用MySQL数据库(v5.6.5+)”
“端口号默认使用3306，请自行安装并启动MySQL数据库”
“2）执行下列SQL脚本导入数据”
“执行wanxingp2p-init.sql 创建P2P平台数据库并导入初始数据”
“执行wanxingdepository-init.sql 创建银行存管系统数据库并导入初始数据”
表格数据：
| 数据库名称 | 数据内容 |
| --- | --- |
| p2p_uaa | 统一认证数据 |
| p2p_account | 统一账户数据 |
| p2p_consumer | 用户中心数据 |
| p2p_transaction_0 | 交易中心数据库1 |
| p2p_transaction_1 | 交易中心数据库2 |
| p2p_undo_log | 分布式事务框架Hmily数据库 |
| p2p_repayment | 还款中心数据 |
| p2p_file | 文件存储服务 |
| p2p_bank_depository | 银行存管系统 |
| p2p_depository_agent | 银行存管代理服务数据 |
| p2p_reconciliation | 对账数据 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
