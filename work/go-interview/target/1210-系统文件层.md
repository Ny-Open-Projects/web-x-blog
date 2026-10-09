# 1210 系统文件层：日志、数据文件与 PID/socket 全景

> 分类：数据库 / MySQL 架构 | 难度：L4 | 题型：记忆题 | 频率：中 | 关键词：**系统文件层、redo log、binlog、.FRM、.MYD、.MYI、.ibd、ibdata1、PID、socket**

> 原文锚点：第 47~65 段「系统文件层主要负责将数据库的数据和日志文件存储在文件系统上，并且完成与存储引擎的交互…它主要包括日志文件、数据文件、配置文件、PID 文件、socket 文件等等…错误日志默认是开启的，还有通用查询日志以及慢查询日志，还有二进制日志 binlog 以及 redo log 文件…每一张表都有一个 FRM 文件…MYD 格式的文件是 MyISAM 存储引擎专用的文件…MYI 文件是存放 MyISAM 表索引相关信息的文件…IBD 和 IBDATA 文件存放的是 InnoDB 的数据文件」

## 一句话总述
系统文件层是 MySQL 的**物理存储层**，负责把数据与日志落到文件系统并与存储引擎交互；核心包括**日志文件、数据文件、配置文件、PID 文件、socket 文件**五类，其中数据文件按引擎分属不同后缀。

## 面试官视角
P6 知道 binlog 与 redo log；P7 要能**按引擎说清文件后缀的归属**（`.FRM`/`.MYD`/`.MYI` 与 `.ibd`/`.ibdata` 分别属于谁），并知道 **PID 与 socket 文件只在 Unix/Linux 环境**下存在及其用途。

## 主问答
**Q（面试官原话）：** MySQL 在磁盘上到底存了哪些文件？

1. **层的职责**：系统文件层负责**把数据和日志文件存储到文件系统**，并**完成与存储引擎的交互**，是**文件的物理存储层** `[源码]`。
2. **五大类**：主要包括**日志文件、数据文件、配置文件、PID 文件、socket 文件** `[源码]`。
3. **日志文件**：包括**错误日志（默认开启）**、**通用查询日志**、**慢查询日志**、**二进制日志 binlog**，以及 **redo log** 文件 `[源码]`。
4. **配置文件**：用于**存放 MySQL 服务的配置信息** `[源码]`。
5. **.FRM 文件**：存储与表相关的**元数据信息**（表结构定义）；**每张表都有一个 .FRM 文件** `[源码]`。
6. **.MYD 文件**：**MyISAM 专用**，存放 **MyISAM 表的数据**；每张 MyISAM 表对应一个 .MYD `[源码]`。
7. **.MYI 文件**：存放 **MyISAM 表索引**相关信息 `[源码]`。
8. **InnoDB 数据文件**：`.ibd` 与 `.ibdata` 存放 **InnoDB 的数据文件**（也包含索引文件）；InnoDB 有**独立表空间**与**共享表空间**两种方式 `[源码]`。
9. **独立表空间**：**每张 InnoDB 表对应一个 .ibd 文件** `[源码]`。
10. **共享表空间**：所有表**共同使用一个或多个 .ibdata 文件**；哪些表使用可通过配置项配置 `[源码]`。
11. **ibdata1 文件**：记录**系统表空间**的数据，存放**表的元数据、undo 日志**等 `[源码]`。
12. **ib_logfile0 / ib_logfile1**：**redo log** 日志文件 `[源码]`。
13. **PID 文件**：MySQL 的**进程文件**（Unix/Linux 环境），存放**自己的进程 ID** `[源码]`。
14. **socket 文件**：**仅 Unix/Linux 环境**存在；客户端**可不通过 TCP/IP 网络**，而使用 **Unix socket** 连接 MySQL `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 系统文件层包含哪几类文件？ | 答不出日志/数据/配置/PID/socket |
| L2 | .MYD 和 .MYI 属于谁？ | 答不出 MyISAM |
| L3 | InnoDB 的表空间有几种？ | 答不出独立 / 共享 |
| L4 | 独立表空间对应什么文件？ | 答不出每张表一个 .ibd |
| L5 | socket 文件干什么用？ | 答不出本机免 TCP 连接 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 8.0 起 | 取消 .FRM，元数据入数据字典 | 现代版本不再有 .FRM |
| 5.6 起 | 默认独立表空间 | innodb_file_per_table=ON |
| 所有版本 | redo log 文件对数可配 | 通常 ib_logfile0/1 |
| Unix/Linux | 才有 PID 与 socket | Windows 无此类文件 |

## 关键代码
```sql
-- 查看数据目录位置（各类文件的根目录）
SHOW VARIABLES LIKE 'datadir';

-- 查看二进制日志相关配置
SHOW VARIABLES LIKE 'log_bin%';

-- 查看 redo log 与表空间配置
SHOW VARIABLES LIKE 'innodb_log%';
SHOW VARIABLES LIKE 'innodb_file_per_table'; -- ON 表示独立表空间（每张表一个 .ibd）

-- 查看慢查询日志是否开启及其位置
SHOW VARIABLES LIKE 'slow_query_log%';

-- 查看 socket 与 pid 文件路径（Unix/Linux）
SHOW VARIABLES LIKE 'socket';
SHOW VARIABLES LIKE 'pid_file';
```

## 总结与追问预判
**按「引擎 → 文件后缀」配对记忆最牢**：MyISAM 是 .MYD（数据）+ .MYI（索引），InnoDB 是 .ibd（独立）/ .ibdata（共享）。追问常是「8.0 还有 .FRM 吗」——**没有了**，8.0 将元数据统一迁入 InnoDB 数据字典。引擎层职责见同批 1210-storage-engine-layer。

## ⚠️ 原文纠错
1. 事实核校：五类文件、日志种类、.FRM 存表定义的元数据、.MYD 与 .MYI 属 MyISAM、InnoDB 两种表空间、ibdata1 存系统表空间与 undo、ib_logfile 为 redo log、PID 与 socket 限 Unix/Linux——均与 MySQL 一致 `[经验]`。
2. 补充：原文有一处口误——称「独立表空间使用的是 MYD 文件来存放数据」，**正确应为 `.ibd` 文件**，`.MYD` 是 MyISAM 专用；本卡已按正确归属书写 `[经验]`。
3. 崩坏词归一：源码将 InnoDB、MyISAM、索引、元数据、表空间等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
