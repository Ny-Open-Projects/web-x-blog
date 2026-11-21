# 画面线理解：15-父子报表：父子报表传递数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\15-父子报表：父子报表传递数据_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:15, 01:56, 04:21, 05:29, 07:05, 08:00, 08:37, 09:09, 09:57, 10:26, 11:22, 11:40, 12:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:45:52

1) 这一组画面整体在讲如何在 JasperReports 中创建和配置子报表（Subreport），包括拖拽组件、设置数据源和参数映射。

2) 按时间顺序列出每张画面的要点：
画面1: 讲解制作子报表的步骤，提示点击“Subreport”按钮并拖动到工作区。
画面2: 展示一个手绘的报表结构图，包含“交报表”、“功能1-子报表1”、“功能2-子报表2”和“list”四个部分。
画面3: 在 JasperReports Studio 中，弹出“New Report Wizard”对话框，提示选择父报表文件夹，当前文件名为“main01.jrxml”。
画面4: JasperReports Studio 主界面，显示“main01.jrxml”和“testCharts.jrxml”两个文件，工作区为空。
画面5: 展示一个手绘的报表结构图，与画面2类似，但左侧标注了“java程序”。
画面6: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Parameter1”参数的配置，类型为“java.lang.String”。
画面7: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”。
画面8: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“chart”字样。
画面9: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样。
画面10: 在浏览器中预览报表，显示“用户列表”，包含用户ID、用户名、薪资、部门等字段。
画面11: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Expression”为“testCharts.jasper”。
画面12: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Data Source Expression”为“new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”。
画面13: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样。
画面14: 在 JasperReports Studio 中，打开“testCharts.jrxml”文件，右侧属性面板显示“Subreport: Subreport”的配置，其中“Data Source Expression”为“new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面3: “Report file Please select your reports file name with .jrxml extension.” “Enter or select the parent folder: TestReports/” “The name: main01.jrxml” “Opening file for editing...”

画面6: “Parameter1” “Name: Parameter1” “Class: java.lang.String”

画面9: “new JRBeanCollectionDataSource(userList)”

画面12: “new net.sf.jasperreports.engine.data.JRBeanCollectionDataSource($P{buildList})”

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2: 展示一个手绘的报表结构图，包含“交报表”、“功能1-子报表1”、“功能2-子报表2”和“list”四个部分，其中“交报表”通过三条线分别指向“功能1-子报表1”、“功能2-子报表2”和“list”。

画面7: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”、“功能2-子报表2”和“list”三个框通过线连接。

画面8: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“chart”字样，通过线连接。

画面9: 展示一个手绘的报表结构图，左侧标注“java程序”、“数据”、“map”、“key:sublist”、“value: List<UserCount> list”，右侧“功能1-子报表1”框内有“new JRBeanCollectionDataSource(userList)”字样，通过线连接。

画面10: 展示一个表格，标题为“用户列表”，包含以下列：用户ID、用户名、薪资、部门。数据行包括：
- 用户ID: 1065705989262279, 用户名: a123, 薪资: 1380000002, 部门: 传智播客, 用户名: test1
- 用户ID: 10663704986334863, 用户名: zhe, 薪资: 1380000003, 部门: 传智播客, 用户名: 测试部
- 用户ID: 10716327602228101, 用户名: ll, 薪资: 1380000004, 部门: 传智播客, 用户名: 测试部
- 用户ID: 10742388013307043, 用户名: a01, 薪资: 1340000001, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10742388014020775, 用户名: a02, 薪资: 1340000002, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10753831331064258, 用户名: test001, 薪资: 1350000001, 部门: 传智播客, 用户名: 开发部
- 用户ID: 10753831353713500, 用户名: test002, 薪资: 1350000002, 部门: 传智播客, 用户名: 开发部
- 用户ID: 1075383135494304, 用户名: test003, 薪资: 1350000003, 部门: 传智播客, 用户名: 开发部

5) 无
