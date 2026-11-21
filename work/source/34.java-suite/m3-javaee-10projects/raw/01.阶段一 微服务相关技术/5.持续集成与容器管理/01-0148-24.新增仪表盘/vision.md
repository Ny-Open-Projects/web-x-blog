# 画面线理解：24.新增仪表盘

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\24.新增仪表盘_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:34, 01:01, 01:06, 01:16, 01:26, 01:55, 02:18, 02:30, 02:54, 03:29, 03:33, 03:40, 03:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:27:26

1) 这一组画面整体在讲什么（一句话）：
在 Grafana 中创建并配置一个用于监控基础微服务内存使用情况的图表面板。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 选择 Grafana 的 Dashboards 管理页面，点击“+ Dashboard”按钮开始创建新面板。
画面 2: 在“New dashboard”页面，点击“Graph”组件，进入图表面板编辑界面。
画面 3: 在图表面板的“Info”区域，输入标题“基础微服务-内存”。
画面 4: 在“Title”输入框中，将标题修改为“基础微服务-内存监控”。
画面 5: 在“Description”字段中，输入描述“Panel description, supports markdown & links”。
画面 6: 切换到“Metrics”选项卡，开始配置数据查询。
画面 7: 在“Metrics”配置中，将测量值（measurement）设置为“memory_usage”。
画面 8: 在“WHERE”条件中，输入容器名称过滤条件“container_name = 'fenqiang-base-services-1-a432bf7'”。
画面 9: 确认并应用查询条件，图表开始显示数据。
画面 10: 切换到“Axes”选项卡，配置坐标轴显示参数。
画面 11: 弹出“Save As...”对话框，准备保存面板。
画面 12: 在“Save As...”对话框中，将面板名称设置为“基础微服务”，保存到“General”文件夹。
画面 13: 保存后，图表面板成功显示，标题为“基础微服务-内存监控”。
画面 14: 图表面板最终显示效果，数据点在时间轴上呈现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6-9 中的 SQL 查询配置：
FROM default memory_usage
SELECT field (value) mean () 
GROUP BY time (30s) fill (null)
FORMAT AS Time series
ALIAS BY Naming pattern

画面 8 中的 WHERE 条件：
container_name = 'fenqiang-base-services-1-a432bf7'

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
