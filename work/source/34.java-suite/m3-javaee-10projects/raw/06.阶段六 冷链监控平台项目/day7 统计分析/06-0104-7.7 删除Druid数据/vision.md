# 画面线理解：7.7 删除Druid数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.7 删除Druid数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:15, 00:17, 00:25, 00:29, 00:32, 00:46, 00:55, 01:11, 01:28, 01:40, 01:44, 01:45, 01:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:42:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Apache Druid 的 Web 管理界面中修改数据源（wikipedia）的保留策略（retention policy），并最终删除该数据源的所有数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Druid 管理界面的“Tasks”页面，列出了多个正在运行和待处理的任务，数据源包括 "all_device_message" 和 "wikipedia"。
画面 2: 切换到“Segments”页面，显示了数据源 "all_device_message" 的多个数据段（Segment），包含起始时间、结束时间、分区号、大小和行数等信息。
画面 3: 切换到“Datasources”页面，显示了两个数据源 "all_device_message" 和 "wikipedia" 的基本信息。
画面 4: 在“Datasources”页面，显示了 "wikipedia" 数据源的详细信息，其保留策略为 "loadByPeriod(P100), dropByPeriod(P300)"，大小为 4.23 GB，行数为 0。
画面 5: 点击 "wikipedia" 数据源的“Retention”列，弹出“Edit retention rules: wikipedia”对话框，当前策略为 "loadForever"，副本数为 2。
画面 6: 在“Edit retention rules: wikipedia”对话框中，将策略从 "loadForever" 改为 "dropForever"，并设置 "Drop" 为 "forever"。
画面 7: 在“Edit retention rules: wikipedia”对话框中，点击“Save”前，弹出“Why are you making this change?”的输入框，要求输入变更描述。
画面 8: 保存并提交了新的保留策略，页面顶部显示绿色提示：“Retention rules submitted successfully”。
画面 9: 页面空白，可能为页面刷新或加载过程。
画面 10: 页面恢复，显示“Datasources”页面，"wikipedia" 数据源的保留策略已更新为 "dropByPeriod(P300)"。
画面 11: 点击 "wikipedia" 数据源的“Actions”列中的“Drop data”按钮，弹出确认对话框：“Are you sure you want to drop all the data for datasource wikipedia?”。
画面 12: 点击确认对话框中的“Drop data”按钮，页面顶部出现绿色提示：“Data drop request acknowledged, next time the coordinator runs data will be dropped”。
画面 13: 绿色提示框中显示“dropped”，表示数据删除请求已确认。
画面 14: 页面恢复，显示“Datasources”页面，"wikipedia" 数据源的行数仍为 0，但保留策略已更新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
