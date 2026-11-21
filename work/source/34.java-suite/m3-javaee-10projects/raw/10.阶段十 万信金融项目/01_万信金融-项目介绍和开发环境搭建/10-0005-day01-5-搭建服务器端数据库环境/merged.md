# day01-5-搭建服务器端数据库环境

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-5-搭建服务器端数据库环境_【海量资源尽在 666java.com】.mp4
- 时长 4分41秒（音频 281s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前的话我们今天的第一个目标已经达到了就是整体了解了一下咱们这个项目啊包括项目的背景啊项目的概述啊里边涉及到功能模块啊核心的业务以及咱们项目涉及到的技术架构技术战啊技术解放等等等等啊整个这一套信息呢我们全部给大家做了一个介绍那咱接下来呢就要搞定第二个目标啊第二个目标呢就是搭建项目的初始开发环境或者技术开发环境这个事情呢你千万不要小瞧它
[00:30] 这样比较小啊不就大环境吗又不是开始开发功能了怎么着怎么着挺简单的是不是其实没那么简单而且你一定要充分重视第一个原因第一个原因就是在企业当中你首先是不是要做这个事这是你逃不掉的对不对第二个我告诉你根据咱以往的经验有不少有不少人在搭建这个项目开发环境的时候这个遇到各种各样的问题所以接下来咱们在搞定第二个目标的时候你还是要充分
[01:01] 重视起来那咱们这个项目环境的搭建呢整体分为两块啊一个是福气的一个是我们的什么呀对前端啊还有一个前端一个是福气的一个是前端我们首先要搭建咱们福气的这个环境福气呢这块首先咱要搞定数据库刚才我们在讲这个基础站的时候大家看到我们是不是用的麦三个数据库对吧那这个数据库呢其实大家之前都已经装过了是不是都已经装了都已经在使用但是这
[01:29] 我们要给大家特别强调一个事就是数据库的版本MySQL数据库的版本你一定要注意了我们P2P项目对于MySQL数据库的版本是有要求的必须是5.6.5以上的版本我建议你直接安装5.7因为我们后边用的一些技术一些框架对于MySQL数据库的版本是有要求的所以你要检查你本级上的MySQL数据库的版本
[01:59] 凡是对于这个版本呢你要卸载掉重新安装我建议直接安装5.7当口就不要改了3306用默认的就行那数据库呢你就自行安装启动就行我就不在故头说了那数据库搞定了之后接下来你要这个执行两个四孔脚本来导入一些数据或者说呢把我们最基本的一些数据库一些数据表给先创建一下
[02:28] 那这两个这个搜索脚本呢我们在资料文件夹里边给大家提供的有大家看一下资料文件夹在这儿在这个地方P2P下回线搜索就这两个你把它俩呢直接拽到我们的什么呀对拽到这个搜索样里边一执行就完事这是我们直接给大家提供好的这个脚本这两个脚本执行的时候呢你最好注意一下这个顺序我们应该先执行谁呢
[02:59] 那你按照讲义来就行先执行这个万信P2P-NIT然后再执行这个万信Depository-NIT已经要注意了这个过程我就不再给大家展示了你在这就直接点击这个按钮整体执行一下就行了这里边就是建库建表它也可能会导入一些什么处理数据包括这边那么这个脚本呢是针对咱P2P平台用到的一些什么呀数据库数据表
[03:27] 而这个脚本万信depository是针对银行那边大家知道我们刚才介绍过是不是银行那边有一个存款系统是不是它也涉及到什么数据库数据表所以说这个脚本是针对银行那边那个系统来建库建表包括导入一些出入数据那你在这里边直接执行就行这个标准执行完之后这是我们产生的一些什么数据库你大概需要了解一下每个库它的作用是啥
[03:56] UA是做认证的对不对Account是存账户信息的这个Consumer是存用户的信息的Transaction是交易的一些数据这个Repayment是还款的一些数据对吧这个Fair是存文件的是不是这个P2P Bank Deposit就是银行存款系统他那边用的数据库对吧这个Deposit Agent就是存款代理这个服务他用的这个数据库最后一个是对账用的一个数据库等等吧
[04:25] 这些你大概先了解一下主要是呢你先执行这两个脚本把这个数据库数据表先造出来至于这些数据库呢在后边反正都要用用的时候再详细跟大家说这是咱先把服务器端的数据库环境先搞定一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

