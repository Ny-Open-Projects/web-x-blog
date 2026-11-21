# 画面线理解：05-Jdbc数据源数据填充：构造fields

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\05-Jdbc数据源数据填充：构造fields_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:37, 00:45, 01:04, 01:16, 01:27, 01:32, 01:40, 01:42, 01:49, 02:22, 04:28, 04:34, 05:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:40:36

1) 这一组画面整体在讲如何在 JasperReports Studio 中设计一个包含标题、数据表和字段区域的报表，并配置数据源和查询。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperReports Studio 中打开名为 testConn.jrxml 的报表文件，界面显示设计视图，包含 Title、Detail 1、Summary 三个带状区域，左侧为项目资源管理器，右侧为属性面板。
画面2：在标题带（Band: Title）中拖放一个文本框，文本框内显示“标题”。
画面3：在标题带中选中文本框，属性面板显示其布局为 Free Layout，高度为 79 px，分隔类型为 Stretch。
画面4：切换到画图工具，创建一个包含“id”和“用户名”列的表格。
画面5：切换到画图工具，创建一个包含“fields”文本框的区域。
画面6：在画图工具中，将“fields”文本框复制并排列成一行四个。
画面7：在画图工具中，调整“fields”文本框的大小和位置。
画面8：在 JasperReports Studio 中打开“Dataset and Query Dialog”，选择“java Bean”作为查询语言。
画面9：在“Dataset and Query Dialog”中，选择“mysql”数据库，查询语句为“select * from bs_user”。
画面10：在“Dataset and Query Dialog”中，查看并选择“bs_user”表的字段，包括 id, mobile, username, password, enable_state, create_time, department_id, time_of_entry, form_of_employment。
画面11：在 JasperReports Studio 中，点击“OK”按钮确认数据源和查询配置。
画面12：在 JasperReports Studio 中，点击“Preview”按钮预览报表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8：
Language: java Bean
Query: java Bean
No Metadata. Double click to refresh.

画面9：
Language: sql
Query: java Bean
select * from bs_user

画面10：
Language: sql
Query: java Bean
select * from bs_user
Field Name	Class Type	Description	Time zone	Column na...	Column la...	Column in...	Properties
id	java.lang.String		...	...	...	...
mobile	java.lang.String		...	...	...	...
username	java.lang.String		...	...	...	...
password	java.lang.String		...	...	...	...
enable_state	java.lang.String		...	...	...	...
create_time	java.lang.String		...	...	...	...
department_id	java.lang.String		...	...	...	...
time_of_entry	java.lang.String		...	...	...	...
form_of_employment	java.lang.String		...	...	...	...

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
