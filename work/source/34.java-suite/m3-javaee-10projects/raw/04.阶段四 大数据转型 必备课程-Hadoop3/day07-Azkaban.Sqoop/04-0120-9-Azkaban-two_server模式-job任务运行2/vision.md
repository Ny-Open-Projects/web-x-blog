# 画面线理解：9-Azkaban-two_server模式-job任务运行2

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\9-Azkaban-two_server模式-job任务运行2【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 02:09, 03:50, 05:36, 06:31, 07:21, 08:26, 09:03, 10:18, 11:17, 12:24, 13:36, 14:41, 16:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:28:01

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Azkaban Web 管理平台创建并上传 Hadoop MapReduce 和 Hive 脚本任务的 zip 包，以及启动和监控这些任务的执行过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了在 Typora 中关于 MapReduce 任务的说明，其中包含创建 job 描述文件的命令示例：
```
type=command
commands=/export/servers/hadoop-3.1.1/bin/hadoop jar hadoop-mapreduce-examples-3.1.1.jar pi 3 5
```
画面 2: 在终端中切换到 Hadoop 的 mapreduce 目录并列出文件，然后切换到 /export/servers/hadoop-3.1.1/share 目录。
画面 3: 在 Azkaban Web 界面中，弹出文件上传对话框，准备上传 zip 包。
画面 4: 在终端中切换到 Azkaban Web Server 目录，并执行激活执行器的 curl 命令。
画面 5: 在 Azkaban Web 界面中，显示名为 "mr" 的任务执行成功，状态为 "SUCCEEDED"。
画面 6: 展示了在 Typora 中关于 Hive 脚本任务的说明，包含创建 Hive 脚本文件和 job 描述文件的步骤。
画面 7: 展示了在 Typora 中关于 Hive 脚本任务的说明，其中 Hive 脚本内容被高亮显示：
```
create database if not exists archive;
use archive;
create table if not exists azttest(id string,name string) row format delimited fields terminated by '\t';
```
画面 8: 在 Notepad++ 中打开名为 "hive.job" 的文件，准备编辑。
画面 9: 在 Azkaban Web 界面中，显示名为 "hive_project" 的项目，包含一个名为 "hive" 的流程。
画面 10: 在终端中切换到 Apache Hive 目录，并列出 bin 目录下的文件。
画面 11: 在 Azkaban Web 界面中，弹出创建项目对话框，用于创建新项目。
画面 12: 在终端中切换到 Apache Hive 的 bin 目录，并列出文件，显示了 SLF4J 的类路径冲突警告。
画面 13: 在 Azkaban Web 界面中，显示名为 "my_command_project" 的项目，包含一个名为 "mycommand" 的流程。
画面 14: 在 Azkaban Web 界面中，显示 "Schedule Flow Options" 页面，用于配置任务的定时执行规则。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
type=command
commands=/export/servers/hadoop-3.1.1/bin/hadoop jar hadoop-mapreduce-examples-3.1.1.jar pi 3 5
```
画面 7:
```
create database if not exists archive;
use archive;
create table if not exists azttest(id string,name string) row format delimited fields terminated by '\t';
```
画面 12:
```
SLF4J: Class path contains multiple SLF4J bindings.
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6: PPT 标题为 "3.5. Hive 脚本任务"，包含三个步骤：
- Step 1: 创建 job 描述文件和 hive 脚本
- Step 2: Job 描述文件: hive.job
- Step 3: 将所有 job 资源文件打到一个 zip 包中

画面 14: PPT 标题为 "Schedule Flow Options"，包含一个表单用于设置定时任务：
- Min: 任意值
- Hours: 任意值
- Day of Month: 任意值
- Month: 任意值
- Day of Week: 任意值
- Special Characters: 任意值、值列表分隔符、值范围、步长值

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
