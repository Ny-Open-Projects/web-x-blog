# 画面线理解：08-ETL-快速入门

- 阶段：08.阶段八 智慧学成项目
- 章节：02.第二章 智慧学成-数据仓库与ETL
- 源文件：08.阶段八 智慧学成项目\02.第二章 智慧学成-数据仓库与ETL\08-ETL-快速入门_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:40, 01:06, 01:39, 02:35, 04:10, 04:38, 06:54, 07:25, 08:01, 09:37, 10:43, 10:56, 11:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:43:53

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Apache Nifi 中创建一个执行脚本并将其输出数据写入 HDFS 的数据流。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 Apache Nifi 的核心概念，包括 FlowFile、Processor、Connection、Flow Controller 和 Process Group。
画面2：讲解如何创建 ExecuteScript 处理器，准备将脚本执行结果写入 HDFS。
画面3：展示 Nifi 界面，工作区为空，准备添加处理器。
画面4：在“Add Processor”对话框中选择“PutHDFS”处理器。
画面5：在 Nifi 工作区中，将 ExecuteScript 处理器与 PutHDFS 处理器连接。
画面6：配置 ExecuteScript 处理器的属性，包括 Script Engine、Script File 和 Script Body。
画面7：配置 PutHDFS 处理器时，出现错误提示，指出“Directory”和“Relationship”配置不完整。
画面8：在终端中进入 Hadoop 配置目录，准备修改 core-site.xml。
画面9：在 Sublime Text 编辑器中打开 core-site.xml 文件，准备修改配置。
画面10：在 Nifi 中配置 PutHDFS 处理器，修正了目录和关系配置。
画面11：在 Nifi 中配置 PutHDFS 处理器，修正了目录和关系配置。
画面12：在 HDFS 的网页界面中查看已写入的文件列表。
画面13：在 Typora 文档中，讲解如何配置 Kerberos Principal 和 Keytab 文件。
画面14：在 Nifi 工作区中，ExecuteScript 处理器成功执行并输出数据，PutHDFS 处理器成功写入 HDFS。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8：
```
[root@xc-online-nifi hadoop]# ls
core-site.xml  hadoop-env.sh  hdfs-site.xml  mapred-site.xml  yarn-site.xml
```
画面9：
```
core-site.xml
```
画面13：
```
Kerberos Principal
Kerberos Keytab
Kerberos Principal
Kerberos Keytab
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1, Apache Nifi 概念”，子标题“1.1, NIFI简介”和“1.2, NIFI核心概念”。
画面13：PPT 标题为“4.1.3, 建立连接”，图示中“Kerberos Principal”指向“Kerberos Keytab”，并标注“匹配配置这个两个属性”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
