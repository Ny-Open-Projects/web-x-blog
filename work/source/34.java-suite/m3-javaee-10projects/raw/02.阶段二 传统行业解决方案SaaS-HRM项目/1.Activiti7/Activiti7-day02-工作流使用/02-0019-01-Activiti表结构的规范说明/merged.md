# 01-Activiti表结构的规范说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\01-Activiti表结构的规范说明_【海量资源尽在 ubkz.com】.mp4
- 时长 4分32秒（音频 272s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 各位同学,我们现在就一起对于我们刚刚所生成出来的这25张表来做一个分类汇总那分为哪些具体的种类,我们一起来看你看,比如说都是以ACT开头的,对吧这是它的一个特点那将来如果我们的业务系统比如说我们自己做了一个人力资源的这个系统那这个系统里头还有,比如说还有50张表那50张表和我们这些表的将来就不会被混在一起,对吧
[00:28] 因为它这里头都是以ACT开头做前缀然后你会发现这些前缀中又会有包括有GE的有HI的还有我们的RE的还有像我们的RU的这样的一些表的特征我们这些前缀都代表什么意思我们一起来看一下比如说我们先来看一下我们的RERE指的是Repository
[00:53] 那这个代表着我们的流程定义流程的静态资源包括像我们的图片等啊那我们再回头来看一下R1在这里头你看看这就是我们的这个流程部署对吧这是我们的model这是我们的这个流程定义文件啊流程定义的文件那这些这些呢就是我们的一些资源的信息将来都会被放到这里头来进行存储对吧这是这个部分啊然后呢我们再还有一个部分
[01:22] 是我们的RURU指的是Runtime代表的是我们运行时的这样的一些表那我们的一个流程一旦启动之后它所产生的一些任务也好变量也好那最终的都会被存储到我们的这个RU一系列的这些表里头就是这些表里头就会存储我们的相关的内容比如说如果我们在这里头有一些什么到期的job或者是我们的execution真正的一些执行者
[01:52] 或者是我们的这个身份验证的对吧或者是我们的job或者是说是挂起的job或者是task的任务啊以及我们的timer job出发的任务以及我们的这个流程变量啊对应的在流程实力真正跑的时候比如说真正这个流程从开始到它还没有结束之前那这一段数据都会被存在于RU开头的这一堆表里头当我们的这个流程一旦结束了
[02:20] 说我这个流程正常比如说张三请假都已经请完了那请完了我们的RU中对于张三请假的这些过程的数据就会被再次删除这是我们之前讲我们的内部核心的时候也给各位讲过这是RU还有一个就是HI指的是Historic它会把我们在运行RU产生的运行过程中的这一堆数据最终当它跑完结束之后
[02:49] 在我们的这个HI开头的这一堆表中它都会把它记录下来这就是啊这一堆表它的主要作用是充当我们的这个历史数据的记录啊好这是一段然后我们还有一个就是GE开头的叫做general这个代表的是一些通用数据啊我们也可以一起来看一下什么样的一些数据是通用数据呢比如说我们来看一下啊这里头就有一个叫做batterybattery呢
[03:17] 比如说我们真正部署的这个pmb bpm文件以及我们的png文件将来在这里边其实也是有一个具体的备份这个部分它是用byte用的是字节给它存在这里头然后以及我们的property这是我们activity所产生出来的这个库的一些特点比如说我们可以看到它的历史版本对吧这样的一些信息
[03:45] 那这样我们整体上就把这25张表里头的最主要的这几个分类给各位说完了当然我们也还有其他的一些分类没有加入进来比如说EVT,Event,Log这其实就是一个日志记录的一张表对吧完了我们也还有像我们这里头还有一个叫Positive叫做流程叫做Positive Definition Inform这是我们流程定义信息的一个具体的内容放在这里头
[04:15] 这是这两张表其他的我们基本上全都已经给它添加到这里头来了这是我们关于我们的这个产生出来的25张表来给各位把这个具体的规范给各位大致介绍了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Activiti 工作流引擎的数据库表结构及其命名规则，通过 SQLyog 客户端查看表数据并结合 PPT 讲解表名含义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: SQLyog 客户端显示数据库连接，左侧树形结构选中表 act_ge_bytearray，右侧数据表显示 ID、REV、NAME、DEPLOYMENT_ID、BYTES、CREATED 等字段。
画面 2: PPT 页面标题为“3.3.7 数据库表的命名规则”，内容解释 ACT_RE_*、ACT_RU_*、ACT_HI_*、ACT_GE_* 的含义。
画面 3: SQLyog 客户端选中表 act_ge_bytearray，数据表显示字段包括 ID、REV、NAME、DEPLOYMENT_ID、BYTES、CREATED。
画面 4: SQLyog 客户端选中表 act_re_model，数据表显示字段包括 ID、NAME、CATEGORY、KEY、TENANT_ID、DEPLOYMENT_ID、REVISION_VERSION。
画面 5: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。
画面 6: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。
画面 7: SQLyog 客户端选中表 act_re_model，数据表显示字段包括 ID、NAME、CATEGORY、KEY、TENANT_ID、DEPLOYMENT_ID、REVISION_VERSION。
画面 8: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 9: SQLyog 客户端选中表 act_ru_task，数据表显示字段包括 ID、REV、TYPE、NAME、CREATION_TIME、ASSIGNEE_ID、PARENT_ID、RETRY_COUNT、EXCLUSIVE、TEXT。
画面 10: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 11: SQLyog 客户端选中表 act_ru_task，数据表显示字段包括 ID、REV、TYPE、NAME、CREATION_TIME、ASSIGNEE_ID、PARENT_ID、RETRY_COUNT、EXCLUSIVE、TEXT。
画面 12: SQLyog 客户端选中表 act_ge_property，数据表显示字段包括 NAME 和 VALUE，内容为：
- act_execution-related-artifacts-count: 1
- next-dbid: 1
- process-history: 7.0.0.0
- activiti-version: [NULL]
画面 13: PPT 页面标题为“第4章 Activiti 服务架构图”，内容为“3.3.7 数据库表的命名规则”。
画面 14: PPT 页面内容与画面 2 相同，鼠标光标在“ACT_GE_*”条目上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：
- 画面 2: “3.3.7 数据库表的命名规则”
- 画面 8: “第4章 Activiti 服务架构图”
- 画面 10: “第4章 Activiti 服务架构图”
- 画面 13: “第4章 Activiti 服务架构图”
表格数据：
- 画面 2: 无表格数据。
- 画面 12: 表格数据为：
  - NAME: act_execution-related-artifacts-count, VALUE: 1
  - NAME: next-dbid, VALUE: 1
  - NAME: process-history, VALUE: 7.0.0.0
  - NAME: activiti-version, VALUE: [NULL]

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

