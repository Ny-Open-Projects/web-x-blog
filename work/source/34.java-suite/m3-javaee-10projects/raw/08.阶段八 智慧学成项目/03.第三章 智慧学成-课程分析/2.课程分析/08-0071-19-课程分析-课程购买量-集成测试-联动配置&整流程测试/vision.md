# 画面线理解：19-课程分析-课程购买量-集成测试-联动配置&整流程测试

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/2.课程分析
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\2.课程分析\19-课程分析-课程购买量-集成测试-联动配置&整流程测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 01:04, 01:35, 02:29, 03:03, 03:42, 04:25, 04:48, 06:11, 07:09, 07:48, 08:17, 09:08, 10:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 23:09:56

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Nifi 流处理平台将 MySQL 数据同步到 Hive，并在前端 Web 页面展示分析结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Hue 的 Table Browser 中查看 Hive 表 course_buy_biz 的数据，包含字段如 course_buy_biz_date_info、course_buy_biz_count 等。
画面 2: 在 Nifi 中配置处理器，从 CourseBuyProcessByBiz 流程组到 WaitForNextGroupProcessor 的连接关系。
画面 3: 配置 WaitForNextGroupProcessor 的属性，包括自动终止关系、成功和等待状态。
画面 4: Nifi 流程图中显示处理器连接错误，提示“Port 'out' is invalid because Output connection for port 'out' is not defined.”。
画面 5: Nifi 流程图中，MySQL To Hive 的处理器配置，显示“Port is invalid”错误。
画面 6: Nifi 流程图中，处理器状态显示为“Queued”，数据处理中。
画面 7: 在 Hue 的 File Browser 中浏览 /user/hive/external/data_course 目录下的文件夹。
画面 8: 在 Hue File Browser 中选中 years=2018 和 years=2019 文件夹，弹出确认删除对话框。
画面 9: Spark Master 界面显示当前运行的应用程序和已完成的应用程序。
画面 10: Nifi 流程图中，处理器状态显示为“Queued”，数据处理中。
画面 11: 在 Navicat Premium 中连接 MySQL 数据库，查看 course_buy_biz 表结构。
画面 12: Spark Master 界面显示已完成的应用程序列表。
画面 13: 智慧学成 Web 页面，显示“访问”和“筛选”按钮，以及“2019 年第 47 周”的时间范围。
画面 14: 技术文档页面，标题为“2.7.5 智慧学成Web展示”，展示数据可视化图表和数据统计。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
