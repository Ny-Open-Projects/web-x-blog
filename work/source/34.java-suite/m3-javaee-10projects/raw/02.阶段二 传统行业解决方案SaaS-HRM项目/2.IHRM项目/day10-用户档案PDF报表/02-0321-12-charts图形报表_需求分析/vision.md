# 画面线理解：12-charts图形报表：需求分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\12-charts图形报表：需求分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:19, 00:23, 00:31, 00:54, 00:58, 01:11, 01:47, 02:03, 02:32, 03:40, 03:46, 03:51, 06:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:44:15

1) 这一组画面整体在讲如何在 JasperReports 中创建分组报表和图表。

2) 按时间顺序列出每张画面的要点：
画面1：展示“设置分组属性”章节，说明可通过选择父表记录ID进行分组，列出“新建模板”和“新建报表群组”两个操作步骤。
画面2：在“Create a new Group”界面，选择“companyName”字段作为分组依据。
画面3：选择创建分组时是否添加分组标题和分组页脚。
画面4：分组设置完成后的空白报表页面。
画面5：切换到“3 Chart图表”章节，介绍“3.1 创建模板”的内容。
画面6：展示创建图表的步骤，包括从工具栏拖拽图表到带区、选择图表类型。
画面7：在图表类型选择界面，鼠标悬停在“Pie Chart”上，显示其属性。
画面8：JasperReports Studio 主界面，显示项目结构和“TestReports2”报表。
画面9：新建报表向导，设置报表文件名为“testCharts.jrxml”，选择父文件夹为“TestReports2”。
画面10：新建报表“testCharts.jrxml”在设计器中打开，显示“Title”和“Summary”带区。
画面11：打开“Chart Wizard”，配置图表数据，选择“Main Dataset”作为数据源。
画面12：在图表编辑器中，对饼图进行样式编辑。
画面13：图表编辑器的空白画布。
画面14：在报表设计器中，从“Palette”中选择“Chart”元素。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“3 Chart图表”，子标题为“3.1 创建模板”，内容为“（1）创建模板，删除不需要的band，保留title和summary。”
画面6：PPT内容为“（3）创建chart图标”，步骤为：
第一步：palette面板找到chart图表，拖拽到band中
第二步：选择需要的图表类型
第三步：设置图表参数
图表类型列表包括：Area Chart, Stacked Area, XY Area, Bar Chart, Bar3D Chart, XY Bar, Stacked Bar, StackBar 3D, Line Chart, XY Line, Pie Chart, Field Chart, Bubble Chart, Candle Chart, TimeChart, HighChart, Scatter Chart, Therm.Chart, Meter Chart, Gantt, MultiChart。
画面11：Chart Wizard 界面，Dataset 选择“Main Dataset”，Series 为下拉框，Value 和 Label 为输入框，Min slice percentage 和 Max slices to show 为数值输入框，Other Section 为按钮。

5) 不要评价画面美观，不要输出与课程无关的内容。
无
