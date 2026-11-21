# 画面线理解：20即时查询-集成测试-配置

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\20即时查询-集成测试-配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:51, 01:21, 01:57, 02:36, 03:19, 04:20, 04:43, 05:00, 05:19, 05:57, 06:23, 06:38, 07:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:06:52

1) 这一组画面整体在讲如何通过编写并上传 Shell 脚本，结合 NIFI 工具链，实现从 Hive 数据源到 HBase 和 ES 的数据实时同步与统计分析流程。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 显示 Hue 文件浏览器界面，位于 /user/hue#/user/hive/external/data_course/learning_course_online_dwm 目录。
- 列出多个名为 data_info2019-12-01 到 data_info2019-12-12 的文件夹，每个文件夹的权限、所有者和修改时间相同。

画面 2:
- 显示 IntelliJ IDEA 中的 Maven 项目构建日志。
- 日志中包含多个 WARNING，提示 org.scala.tools.maven.scala.plugin 缺失，以及多个依赖项需要 Scala 版本 2.11.8。
- 日志底部显示构建顺序：[jar] xc-analysis, [jar] xc-common-utils。

画面 3:
- 显示 PDF 文档页面，标题为“4.2.2 NIFI调度-用户学习”。
- 子标题“4.2.2.1 步骤1统计关联维度脚本”。
- 代码块内容：
  ```
  #!/usr/bin/env bash
  if [[ $1 == "" ]];then
  TO_DATE=$1
  else
  #TO_DATE=`date -d "-1 day" +%Y-%m-%d`
  echo "[===no params input,default data.info is yesterday(STO_DATE)==]"
  exit 1
  fi
  SPARK_SUBMIT \
  $SPARK_SUBMIT \
  --master spark://xc-online-spark:7077 \
  --class ch.itcast.xc.analysis.search.InstantQueryStepToHive \
  /opt/run/jars/xc-service-search.jar with dependencies.jar $(TO_DATE)
  if [[ $? == 0 ]];then
  echo "[===spark-submit process success==]"
  else
  echo "[===spark-submit process failed==]"
  exit 0
  fi
  ```

画面 4:
- 与画面 3 几乎相同，但代码块中注释部分被修改：
  ```
  #TO_DATE=`date -d "-1 day" +%Y-%m-%d`
  ```
  被注释掉。

画面 5:
- 显示 Windows 文件资源管理器和 WinSCP 窗口。
- WinSCP 窗口显示目标路径为 /opt/tmp。
- 文件资源管理器中显示文件 instant_query_step1_to_hive.sh 和 instant_query_step1_to_hbase_and_es.sh。

画面 6:
- 显示 Xshell 终端窗口，连接到 xc-online。
- 终端中显示命令行提示符和部分文件列表。
- 背景为 PDF 文档，标题为“4.2.2.3 步骤1、步骤2 NIFI调度流程”，并包含一个 NIFI 流程图。

画面 7:
- 显示 PDF 文档页面，标题为“4.2.2.3 步骤1、步骤2 NIFI调度流程”。
- 流程图显示“GenerateFlowFile”指向“InstantQueryStepToHive”。
- 文档中提及资料路径：
  ```
  - 源码资料
    - 第3章 即时查询
      - nifi
        - shell
          instant_query_step2_to_hbase_and_es.sh
  ```

画面 8:
- 显示 IntelliJ IDEA 中的 Maven 项目构建日志。
- 日志中包含多个 WARNING，提示依赖项需要 Scala 版本 2.11.8。
- 日志底部显示构建顺序：[jar] xc-analysis, [jar] xc-common-utils。

画面 9:
- 显示 WinSCP 窗口，目标路径为 /opt/tmp。
- 窗口显示文件传输成功，文件名为 xc-service-search.jar with dependencies.jar。

画面 10:
- 显示 PDF 文档页面，标题为“4.3 NIFI流程”。
- 流程图显示“1. 数据生产-用户学习(在线学习)ToHDFS”指向“2. 数据清洗统计-用户学习”。
- 文档中提及资料路径：
  ```
  - 源码资料
    - 第3章 即时查询
      - nifi
        - shell
          instant_query_step2_to_hbase_and_es.sh
  ```

画面 11:
- 显示 Xshell 终端窗口，连接到 xc-online。
- 终端中显示命令行提示符和文件列表，包括 subject_learn_num_by_month.biz.sh 等脚本。

画面 12:
- 显示 NIFI 流程界面，弹出“Upload Template”对话框。
- 对话框包含“Select Template”搜索框和“CANCEL”、“UPLOAD”按钮。

画面 13:
- 显示 NIFI 流程界面，显示“InstantQueryStepToHive”和“InstantQueryStepToHbaseAndES”两个组件。
- “InstantQueryStepToHive”指向“Name output stream”。

画面 14:
- 显示 NIFI 流程界面，显示“1. 数据生产-用户学习(在线学习)ToHDFS”和“2. 数据清洗统计-用户学习”两个组件。
- 两个组件均显示“Opened”、“Read/Write”、“Out”等状态信息。
