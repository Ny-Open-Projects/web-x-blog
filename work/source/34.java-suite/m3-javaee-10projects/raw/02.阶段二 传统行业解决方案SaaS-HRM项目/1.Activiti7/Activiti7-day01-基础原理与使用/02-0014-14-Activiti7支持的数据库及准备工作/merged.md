# 14-Activiti7支持的数据库及准备工作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\14-Activiti7支持的数据库及准备工作_【海量资源尽在 ubkz.com】.mp4
- 时长 4分9秒（音频 250s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们就开始在安装好了我们的Eclips底下的流程设计器和我们的Ideal底下的流程设计器之后我们就一起来学习一下我们Activity所支持的数据库有哪一些因为我们之前在做Activity内部原理分析的时候我们已经说到其中就有这样的一点是我们的Activity它真正内部运行的核心机制中
[00:29] 其中就需要去将我们的这个BPMN这个流程定义文件对吧或者叫流程流程流程部署文件啊就需要去将这样的一些文件中的节点呢读取到我们的这个MySQL或者是其他数据库的一张表里了去对吧那对呢我们后期又讲过我们Activity7其中支持有25张表对吧那每一张表将来长什么样
[00:57] 以及我们怎么样去得到这25张表对吧这都是我们后续要学习的问题那目前呢我们先来看一看activity所支持的这个数据库包括有很像HRHR是一个内存中的数据库这是它默认支持的这个数据库是这个当然我们将来在实战环节中我们用的比较多的像应该是像我们的MySQL或者Oracle数据库对吧
[01:23] 比如说公司如果搞的这套系统用的是MySQL数据库的话那我们将来就需要就需要说把我们的这个把我们的这个activity去配上相当于让它支持我们的这个MySQL数据库当然也可以是Auric数据库或者是其他的像DB2,MyMS,微软的这个数据库都是可以支持的那我们今天呢主要用的就是用MySQL数据库来给各位做一些测试
[01:53] 那这25张表将来怎么样去得到啊我们的在这个里头我们在这个里头啊可以使用我们这个编写运行我们的加码代码的方式来创建我们的这个MySQL数据库中的表啊那首先我们如果呢要去做这个工作的话我们应该把MySQL环境准备好对吧另外一个呢就是可以再去创建一个MySQL底下的这个数据库
[02:20] 后续我们只要把这25张表生成到指定的库里头去就可以了那么现在就可以把准备工作提前给它做一下好 这时候我开始开始来做一下这个工作那我们做一下这个工作现在我的MySQL服务一般情况是被我已经给它停了现在我把我的MySQL起好起好了然后我就通过这个工具直接连到我们的数据库里头去
[03:03] 那这个时候各位就可以看到我们这边呢就已经准备好了这个环境对不对当我们这个环境准备好了那下一步就开始我们去写一段代码来执行这个代码然后呢生成出我们啊所需要用activity的这25张表我们的这个工作就算做完了对吧那么现在可以再去准备出一个这样的库对不对好比如说我准备一个叫做activity这样的一个库对吧
[03:30] 这时候我就会直接到这边再去create database对吧这样我就会创建一个叫做activity的这样的一个数据库那我们的这些准备工作就应该已经做完了啊我刷新一下这个时候就出来了但是目前这里面肯定是没有任何的表对吧下一个环节我们主要就是去把这个表给它弄出来对吧
[04:01] 让我们的这个activity库里头直接多出25张表我们的这个工作就算完成对吧好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

