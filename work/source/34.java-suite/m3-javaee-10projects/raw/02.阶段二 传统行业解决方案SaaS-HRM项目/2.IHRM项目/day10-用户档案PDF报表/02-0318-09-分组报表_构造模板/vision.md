# 画面线理解：09-分组报表：构造模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\09-分组报表：构造模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:30, 02:01, 02:40, 03:06, 03:35, 04:32, 04:59, 05:31, 05:53, 06:50, 07:01, 07:38, 08:22
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:42:52

1) 这一组画面整体在讲什么（一句话）：
演示如何在 JasperReports Studio 中创建和配置一个包含分组的报表，涉及参数传递、字段绑定和分组设置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，标题为“1.1 参数Map填充数据”，子标题“1.1.1 模板制作”，要点为“（1）创建新模板，删除不需要的Band”。
画面2：打开“画图”程序，准备绘制图形。
画面3：在画图程序中绘制第一个矩形框，标注“传智播客：”。
画面4：在画图程序中绘制第二个矩形框，标注“黑马程序员：”。
画面5：在 JasperReports Studio 中，弹出“New Report Wizard”对话框，提示选择报表文件夹和文件名，文件名设置为“Blank_Ad.jrxml”。
画面6：在 JasperReports Studio 中，打开“testGroup.jrxml”报表文件，显示报表设计界面，包含“Title”、“Page Header”、“Column Header”、“Detail 1”、“Column Footer”、“Page Footer”等带。
画面7：在 JasperReports Studio 中，选中“Detail 1”带，显示其属性面板，布局为“Free Layout”，高度为“125 px”，分页方式为“Stretch”。
画面8：在 JasperReports Studio 中，设计界面显示“$F{username}”、“$F{dept}”、“$F{company}”等字段表达式。
画面9：在画图程序中，绘制一个三列的表格和一个下方的矩形框。
画面10：在 JasperReports Studio 中，选中“Fields”节点，显示“testGroup”报表的属性，语言为“java”，格式工厂类为“<NULL>”。
画面11：在 JasperReports Studio 中，选中“Group1 Group Header 1”带，显示其属性面板，组名为“Group1”，表达式为“$F{company}”，最小高度为“50px”。
画面12：在画图程序中，绘制一个三列的表格和一个下方的矩形框。
画面13：在 JasperReports Studio 中，选中“Group1 Group Header 1”带，显示其属性面板，组名为“Group1”，表达式为“$F{company}”，最小高度为“50px”。
画面14：在 JasperReports Studio 中，选中“Text Field...”组件，显示其属性面板，位置类型为“Position Type: Px Relative To Top”，宽度为“100 px”，高度为“30 px”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“1.1 参数Map填充数据”，子标题为“1.1.1 模板制作”，要点为“（1）创建新模板，删除不需要的Band”。
画面5：弹出“New Report Wizard”对话框，提示选择报表文件夹和文件名，文件名设置为“Blank_Ad.jrxml”。
画面10：报表属性面板显示“Report Name: testGroup”，“Language: java”，“Format Factory Class: <NULL>”。
画面11：组属性面板显示“Group Properties: Name: Group1, Expression: $F{company}”，“Group Band Properties: Min Height To Start New Page: 0 px, Minimum Details To Start From Top: 0”。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
