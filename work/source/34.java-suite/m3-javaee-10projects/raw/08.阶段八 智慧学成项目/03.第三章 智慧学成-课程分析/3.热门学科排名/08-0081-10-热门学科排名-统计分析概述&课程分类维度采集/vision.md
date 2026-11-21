# 画面线理解：10-热门学科排名-统计分析概述&课程分类维度采集

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\10-热门学科排名-统计分析概述&课程分类维度采集_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:57, 02:16, 02:30, 02:43, 03:02, 04:01, 04:43, 04:55, 06:00, 06:07, 06:22, 06:32, 06:48, 07:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:16:33

1) 这一组画面整体在讲什么（一句话）：
演示如何在Nifi中配置数据流，将Hive数据转换为JSON并写入Hive，同时展示Hue中数据表的结构和内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：Nifi界面，显示两个处理器的运行状态，分别是“课程分类-维度”和“课程分类-维度”。
画面2：文件资源管理器，显示多个XML文件，其中“热门学科排名-用户-因数.xml”被选中，弹出“Upload Template”对话框。
画面3：Nifi界面，显示三个处理器的运行状态，分别是“课程分类-维度”、“课程分类-维度”和“用户-维度”。
画面4：Nifi的“课程分类-维度 Configuration”页面，显示“CONTROLLER SERVICES”标签页，其中“hive连接池”状态为“Enabled”，“数据源”状态为“Disabled”。
画面5：Nifi的“课程分类-维度 Configuration”页面，显示“CONTROLLER SERVICES”标签页，其中“hive连接池”状态为“Enabled”，“数据源”状态为“Enabled”。
画面6：Hue的“Table Browser”页面，显示“course_category_dim”表的数据，包含“course_category_dim.course_category_dim_id”、“course_category_dim.name”、“course_category_dim.label”等字段。
画面7：Nifi界面，显示数据流，包括“课程分类-维度”、“ConvertAvroToJSON”和“WriteToHiveProcessor”三个处理器，数据流向从“课程分类-维度”到“ConvertAvroToJSON”，再到“WriteToHiveProcessor”。
画面8：终端界面，显示SSH连接到“xc-online”服务器，提示信息包括“SSH compression: ✓”、“X11-forwarding: ✓”、“DISPLAY: ✓”。
画面9：终端界面，显示Nifi启动日志，包括“Successfully recovered 934 records in 4 milliseconds”、“Successfully enabled DBCPConnectionPool”等信息。
画面10：终端界面，显示Nifi启动日志，包括“Successfully recovered 71056 records in 711 milliseconds”、“Successfully enabled DBCPConnectionPool”等信息。
画面11：Hue的“Table Browser”页面，显示“course_category_dim”表的数据，包含“course_category_dim.course_category_dim_id”、“course_category_dim.name”、“course_category_dim.label”等字段。
画面12：Hue的“Table Browser”页面，显示“course_category_dim”表的数据，包含“course_category_dim.course_category_dim_id”、“course_category_dim.name”、“course_category_dim.label”等字段。
画面13：Hue的“Table Browser”页面，显示“course_category_dim”表的数据，包含“course_category_dim.course_category_dim_id”、“course_category_dim.name”、“course_category_dim.label”等字段。
画面14：文档页面，显示“3.5 统计分析”章节，其中“3.5.1 销售量”部分提到“课程购买数据已经沉淀在DWM层数据中”，并列出“统计分析步骤”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
