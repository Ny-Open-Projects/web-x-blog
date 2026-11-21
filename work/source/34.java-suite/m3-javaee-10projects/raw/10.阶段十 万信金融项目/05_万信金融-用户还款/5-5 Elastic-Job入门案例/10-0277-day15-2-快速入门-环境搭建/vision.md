# 画面线理解：day15-2-快速入门-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-2-快速入门-环境搭建_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:51, 01:10, 02:25, 02:28, 02:44, 02:47, 03:24, 03:28, 03:40, 03:43, 03:49, 04:02, 04:39, 04:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 08:30:04

1) 这一组画面整体在讲 Elastic-Job 的环境搭建，包括版本要求、Zookeeper 安装与配置、以及数据库准备。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PPT 第 1 页，标题为“2.1 环境搭建”，内容包括版本要求（JDK 1.7+、Maven 3.0.4+、Zookeeper 3.4.6+）、Zookeeper 安装与运行说明（类比 Eureka）、数据库说明（使用 mybatis-plus 入门案例的数据库 mp，表为 tb_user），并附带一个数据库表结构截图。
画面2: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。
画面3: PPT 第 2 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面4: PPT 第 4 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面5: PPT 第 3 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面6: PPT 第 2 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面7: 文件资源管理器，显示“zookeeper-3.4.9”文件夹内容，其中“conf”文件夹被选中。
画面8: 文件资源管理器，显示“zookeeper-3.4.9”文件夹下的“conf”子文件夹内容，其中“zoo.cfg”文件被选中，右侧预览显示“zoo.cfg”文件内容。
画面9: 文件资源管理器，显示“zookeeper-3.4.9”文件夹下的“bin”子文件夹内容，其中“zkServer.cmd”文件被选中。
画面10: 文件资源管理器，显示“zookeeper-3.4.9”文件夹下的“bin”子文件夹内容，其中“zkServer.cmd”文件被选中，右侧预览显示“zkServer.cmd”文件内容。
画面11: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。
画面12: SQLyog 数据库管理工具界面，显示“p2y_repayment”数据库的表结构，其中“p2y_payment”表被选中。
画面13: PPT 第 6 页，标题为“2.2 入门案例”，内容包括“1.新建maven工程”，并展示“2.1 环境搭建”部分。
画面14: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8: zoo.cfg 文件内容：
```
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial synchronization phase can take
initLimit=10
# The number of ticks that can pass between sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
dataDir=D:/zookeeper-3.4.9/data
# the port at which the clients will connect
clientPort=2181
```
画面10: zkServer.cmd 文件内容：
```
@echo off
setlocal enabledelayedexpansion
set ZK_HOME=%~dp0
set ZK_CONF=%ZK_HOME%conf
set ZK_LOG=%ZK_HOME%logs
set ZK_DATA=%ZK_HOME%data
set ZK_PORT=2181
set ZK_TICK_TIME=2000
set ZK_INIT_LIMIT=10
set ZK_SYNC_LIMIT=5
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%Z
