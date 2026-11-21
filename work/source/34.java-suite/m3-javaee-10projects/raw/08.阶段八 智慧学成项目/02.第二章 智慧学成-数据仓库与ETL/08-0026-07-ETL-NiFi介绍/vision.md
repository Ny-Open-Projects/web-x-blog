# 画面线理解：07-ETL-NiFi介绍

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\07-ETL-NiFi介绍_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 02:39, 06:08, 06:43, 07:10, 07:14, 07:20, 08:14, 08:37, 09:26, 10:03, 10:15, 10:39, 10:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:43:26

1) 这一组画面整体在讲什么（一句话）：
演示 Apache Nifi 的基本概念、架构，并在图形界面中创建并配置一个名为 AttributeRollingWindow 的处理器。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Nifi 使用文档的第1章“Apache Nifi 概念”，重点介绍 1.1 NIFI简介 和 1.2 NIFI核心概念，包括 FlowFile、FlowFile Processor、Connection、Flow Controller 和 Process Group 的定义。
画面2：文档页面滚动，展示 1.3 NIFI构架，包含 OS/Host、JVM、Web Server 的架构图。
画面3：Nifi 图形界面，显示空白的流程图编辑区，左侧为“Navigate”和“Operate”面板。
画面4：在 Nifi 界面中打开“Add Processor”对话框，显示处理器列表，当前选中“ConsumerKafka_1.0”。
画面5：Nifi 界面，空白的流程图编辑区。
画面6：在 Nifi 界面中打开“Add Processor”对话框，当前选中“CompareChangeMySQL”。
画面7：在 Nifi 界面中，添加了一个灰色的处理器组件，右侧显示其运行状态面板。
画面8：在 Nifi 界面中，弹出“Configure Label”对话框，用于设置组件标签。
画面9：Nifi 界面，空白的流程图编辑区。
画面10：在 Nifi 界面中，添加了一个名为“AttributeRollingWindow”的处理器组件，右侧显示其运行状态面板。
画面11：在 Nifi 界面中，鼠标悬停在“AttributeRollingWindow”处理器上，弹出错误提示框，指出多个配置错误，如“Value to track is invalid”、“Time window is invalid”等。
画面12：在 Nifi 界面中，弹出“Create Template”对话框，用于创建模板。
画面13：在 Nifi 界面中，处理器组件被设置为红色，右侧显示其运行状态面板。
画面14：回到 Nifi 使用文档页面，显示 1.1 NIFI简介 和 1.2 NIFI核心概念。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：架构图显示“OS/Host”指向“JVM”，“JVM”指向“Web Server”。
画面1、14：PPT标题为“1, Apache Nifi 概念”，子标题包括“1.1, NIFI简介”和“1.2, NIFI核心概念”，并列出“FlowFile”、“FlowFile Processor”、“Connection”、“Flow Controller”、“Process Group”等概念及其定义。
画面10、13：处理器组件“AttributeRollingWindow”显示其属性，如“Type: AttributeRollingWindow”、“Version: 1.9.2”、“org.apache.nifi.nifi-statful-analysis.nar”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
