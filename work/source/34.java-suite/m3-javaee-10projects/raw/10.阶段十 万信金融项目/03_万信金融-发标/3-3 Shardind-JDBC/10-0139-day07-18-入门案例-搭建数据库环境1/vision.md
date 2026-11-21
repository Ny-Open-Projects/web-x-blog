# 画面线理解：day07-18-入门案例-搭建数据库环境1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day07-18-入门案例-搭建数据库环境1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:08, 02:46, 03:09, 03:47, 04:59, 05:38, 06:22, 07:05, 07:13, 07:35, 08:59, 09:12, 09:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:40:14

1) 这一组画面整体在讲什么（一句话）：
演示如何在单机环境下搭建 MySQL 主从同步环境，包括配置主库和从库的 my.ini 文件、复制数据表结构、安装服务以及验证同步。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“2.3.4 搭建数据库环境”，子标题“2.3.4.1 MySQL主从同步”，并展示数据库分库分表的架构图。
画面2：展示主库配置文件内容，包含 server-id、binlog-do-db、binlog-ignore-db 等配置项。
画面3：主库配置文件内容，与画面2相同，仅鼠标位置不同。
画面4：展示从库配置文件内容，包含 port、datadir、log-bin 等配置项，以及黑马程序员的水印。
画面5：展示 Windows 文件资源管理器，路径为 C:\ProgramData，显示一个名为“MySQL”的文件夹。
画面6：展示数据库分库分表的架构图，包含 STORE_DB 和 PRODUCT_DB_2 两个数据库，以及它们内部的表结构。
画面7：展示从库配置文件内容，包含 port、datadir、log-bin 等配置项，以及黑马程序员的水印。
画面8：展示从库配置文件内容，包含 replicate_wild_do_table 和 replicate_wild_ignore_table 配置项，并给出安装服务的命令。
画面9：展示 Windows 任务管理器，显示 CPU 和内存使用情况，其中 MySQL 服务占用 28.1% 的 CPU。
画面10：展示 Windows 服务管理器，显示 MySQL 服务状态为“已停止”，并高亮显示“MySQL”服务。
画面11：展示多个数据库管理工具窗口，包括 Navicat、SQLyog、MySQL Server、dbsharding 等。
画面12：展示从库配置文件内容，包含 replicate_wild_do_table 和 replicate_wild_ignore_table 配置项，并给出安装服务的命令。
画面13：展示 SQLyog Professional 64 界面，正在执行 DROP TABLE IF EXISTS 'score_info' 命令。
画面14：展示从库配置文件内容，包含 replicate_wild_do_table 和 replicate_wild_ignore_table 配置项，并给出安装服务的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
[mysqld]
#开启日志
log-bin = mysql-bin
#设置服务id，主从不能一样
server-id = 1
#设置需要同步的数据库
binlog-do-db=store_db
binlog-do-db=product_db_1
binlog-do-db=product_db_2
#屏蔽系统表同步
binlog-ignore-db=mysql
binlog-ignore-db=information_schema
binlog-ignore-db=performance_schema
```

画面4：
```
port = 3307
#设置mysql数据库的存放目录(该目录不一定在mysql安装目录下)
datadir=D:\mysql-5.7.25-s1\data
#开启日志
log-bin = mysql-bin
```

画面8：
```
replicate_wild_do_table=store_db.% 
replicate_wild_do_table=product_db_1.% 
replicate_wild_do_table=product_db_2.% 
#屏蔽系统表同步
replicate_wild_ignore_table=mysql.% 
replicate_wild_ignore_table=information_schema.% 
replicate_wild_ignore_table=performance_schema.% 
```

画面12：
```
replicate_wild_do_table=store_db.% 
replicate_wild_do_table=product_db_1.% 
replicate_wild_do_table=product_db_2.% 
#屏蔽系统表同步
replicate_wild_ignore_table=mysql.% 
replicate_wild_ignore_table=information_schema.% 
replicate_wild_ignore_table=performance_schema.% 
```

画面14：
```
replicate_wild_do_table=store_db.% 
replicate_wild_do_table=product_db_1.% 
replicate_wild_do_table=product_db_2.% 
#屏蔽系统表同步
replicate_wild_ignore_table=mysql.% 
replicate_wild_ignore_table=information_schema.% 
replicate_wild_ignore_table=performance_schema.% 
```

画面13：
```
DROP TABLE IF EXISTS 'score_info'
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.3.4 搭建数据库环境”，子标题“2.3.4.1 MySQL主从同步”。
画面6：架构图包含两个数据库“STORE_DB”和“PRODUCT_DB_2”，每个数据库内部包含“商品信息”和“商品描述”表，其中“商品信息”表指向“商品描述”表。
画面11：未展示表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
