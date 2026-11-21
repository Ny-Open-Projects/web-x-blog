# 画面线理解：14-Activiti7支持的数据库及准备工作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\14-Activiti7支持的数据库及准备工作_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:14, 00:24, 00:29, 01:06, 02:03, 02:11, 02:26, 02:46, 02:51, 02:54, 03:01, 03:10, 03:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:10:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎中配置并使用 MySQL 数据库，包括数据库连接参数、创建数据库和表的步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Eclipse 中打开 Activiti Designer，展示一个简单的流程图，包含“开始事件”、“用户任务”和“结束事件”。
画面 2: 展示 PPT 页面，标题为“3.3.4 Activiti 支持的数据库”，列出支持的数据库类型、测试版本、JDBC URL 示例和备注。
画面 3: 展示 Windows 资源管理器，显示一个名为“lala.exe”的文件。
画面 4: 展示一张手绘图，解释如何将业务流程图转换为数据库表结构，包括“先将流程图每个节点的数据提取并存入表中”等步骤。
画面 5: 与画面 2 内容相同，展示 PPT 页面“3.3.4 Activiti 支持的数据库”。
画面 6: 展示 PPT 页面“3.3.5 创建 mysql 数据库”，显示创建数据库的 SQL 语句：CREATE DATABASE activiti DEFAULT CHARACTER SET utf8;。
画面 7: 与画面 6 内容相同，展示 PPT 页面“3.3.5 创建 mysql 数据库”。
画面 8: 展示 Windows “运行”对话框，输入“cmd”以打开命令提示符。
画面 9: 与画面 2 内容相同，展示 PPT 页面“3.3.4 Activiti 支持的数据库”。
画面 10: 展示 Windows “服务”管理器，列出各种服务。
画面 11: 展示 Windows “服务”管理器，显示“MySQL”服务正在启动。
画面 12: 展示 MySQL GUI 工具的主界面，提示“Please Connect To A MySQL Server”。
画面 13: 展示 Windows 桌面，显示“传智播客”和“黑马程序员”的联合出品标志。
画面 14: 展示 MySQL GUI 工具的“New Connection”界面，显示已连接的数据库列表，包括“activiti”、“crm”、“crm_hibernate”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
CREATE DATABASE activiti DEFAULT CHARACTER SET utf8;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题: 3.3.4 Activiti 支持的数据库
表格数据:
| Activiti 数据库类型 | 测试版本 | JDBC URL 示例 | 备注 |
|---|---|---|---|
| h2 | 1.3.166 | jdbc:h2:tcp://localhost:9092/activiti | 默认配置的数据库 |
| mysql | 5.1.21 | jdbc:mysql://localhost:3306/activiti?autoReconnect=true | 使用 mysql-connector-java 驱动测试 |
| oracle | 11.2.0.1.0 | jdbc:oracle:thin:@localhost:1521:xe |  |
| postgres | 8.1 | jdbc:postgresql://localhost:5432/activiti |  |
| db2 | DB2 10.1 | jdbc:db2://localhost:50000/activiti |  |
| mssql | 2008 | jdbc:sqlserver://localhost:1433;activiti |  |

画面 6:
标题: 3.3.5 创建 mysql 数据库
内容: 本教程使用 mysql 数据库。
创建 mysql 数据库 activiti (名字任意)。
CREATE DATABASE activiti DEFAULT CHARACTER SET utf8;

画面 7:
标题: 3.3.5 创建 mysql 数据库
内容: 本教程使用 mysql 数据库。
创建 mysql 数据库 activiti (名字任意)。
CREATE DATABASE activiti DEFAULT CHARACTER SET utf8;

画面 9:
标题: 3.3.4 Activiti 支持的数据库
表格数据:
| Activiti 数据库类型 | 测试版本 | JDBC URL 示例 | 备注 |
|---|---|---|---|
| h2 | 1.3.166 | jdbc:h2:tcp://localhost:9092/activiti | 默认配置的数据库 |
| mysql | 5.1.21 | jdbc:mysql://localhost:3306/activiti?autoReconnect=true | 使用 mysql-connector-java 驱动测试 |
| oracle | 11.2.0.1.0 | jdbc:oracle:thin:@localhost:1521:xe |  |
| postgres | 8.1 | jdbc:postgresql://localhost:5432/activiti |  |
| db2 | DB2 10.1 | jdbc:db2://localhost:50000/activiti |  |
| mssql | 2008 | jdbc:sqlserver://localhost:1433;activiti |  |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
