# 20即时查询-集成测试-配置

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\20即时查询-集成测试-配置_【海量资源尽在 666java.com】.mp4
- 时长 7分13秒（音频 433s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来咱们进行集成测试的学习集成测试就是把所有的任务调度都交给NiFi进行处理这里咱们数据采集是采用NiFi上进行生产数据的方式这个已经在NiFi上面了接下来就是数据的一个统计分析的一个NiFi调度这里数据统计分析咱们还是在代码中进行的一个统计分析
[00:28] 在开发工具中进行一个统计分析接下来呢就是要打成大包然后呢交给NiFi进行统计分析咱们呢先进行一个打包打包之前呢咱们一定要把咱们这个集群模式给打开这里呢集群模式打开就是把这个注视给去掉就行这里呢由于打包需要一定的时间咱们呢先让他打包好打包已经开始这里呢打包过程中呢咱们来介绍一下咱们这个
[00:59] 集成测试中咱们需要做的事这里集成测试刚才已经说了数据采集咱们集成测试的时候是使用NetFi生产数据的方式这个已经配置好统计分析咱们一共是代码是分为两步第一步是统计维度关联维度还有相关的一个统计第二步就是保存到ES和HBase这两个咱们NetFi调度是采用一个流程
[01:27] 步骤一就是先进行一个关联维度关联维度完成之后进行统计统计完成之后咱们保存到数据仓库中然后进行步骤二步骤二就是把数据仓库中的数据拿过来然后再索引到Lasik测试保存到eSpace中然后这个流程就结束了这里使用到了两个脚板就是NiFi调度的两个脚板
[01:56] 是分别是调度步骤一和步骤二的咱们先把脚本上传到咱们的服务器上这里咱们还是使用tmp的目录这是之前咱们上传的内容把之前的内容可以删掉好已经删除完成咱们来切到资料目录这里NiFi调度里边有serial脚本还有咱们NiFi的调度的一些原码还有咱们Python的脚本
[02:30] 咱们这里就使用NetFi调度把这两个脚本先上传到咱们的服务器上好上传服务器完成之后咱们等待咱们这个代码打包完成这里打包还没有完成咱们可以先把这两个脚本上传到咱们NetFi的容器中咱们切到opt的time模组下这里使用Dock的cp命令把这两个给上传上去
[03:05] 咱们首先是步骤一咱们需要上传的目录是在NiFi的opt run目录下的secretreferent目录内这里直接上传到目标目录好已经上传完成了接下来上传第二个就是staff2好上传完成之后咱们切到NiFi容器中使用钢IT三数
[03:38] 然后呢是中端是BSH这个时候呢咱们直接切到这个门路就是咱们这个脚本门路咱们这个脚本上传完成之后呢是需要添加可执行权限的不添加可执行权限的调度的时候就没法正常的运行咱们呢使用CHMOD两个脚本这里呢使用星星点SH的方式把所有的都给添加可以看到这里呢已经添加完成咱们来
[04:08] 查看这个打包完成没这里呢打包还没有完成咱们再继续等待一下基层测试这里呢介绍已经完成那一块的流程呢等会儿咱们由于它这个生产呢咱们是没有它这个依赖关系的生产和数据清洗是独立的它这个依赖关系呢有的已经在这个地方已经配置了就是不周一和不周二的这个配置所以说这个地方呢是不需要联动的好这里呢已经打包完成
[04:45] 打包完成之后呢,咱们把这个给上传上来还是使用带依赖这个加包好,等data上传完成好,已经上传完成了咱们这里呢,新开一个终端新开一个终端进行一个上传操作这个呢,是上传到G2的目录下是在OPT的G2目录内咱们把这个复制一下,修改修改这里呢,切换到咱们的temp目录下
[05:42] Doccp把这个severs-search上传进来咱们的容器是9-5容器这个是GALS目录好已经上传完成咱们来切换到GALS目录可以看到search已经进来好咱们切回文档到此咱们9-5上的流程已经OK
[06:17] 这个地方还少一个步骤就是内发调度的流程还没有上传进来把内发调度的流程上传进来刚才咱们只是将咱们清洗脚本清洗的调度脚本还有代码给打包上传了这个地方差点忘了数据统计分析清洗用户学习调度这个上传上传之后咱们内发流程就算完成了即时查询的流程就算完成了好这个视频就到这里
[06:50] 通过这个视频的学习,咱们需要将NetFi需要的配置,就是两个SAC脚本以及大包上传到NetFi容器中,以NetFi中的调度给上传进来。
[07:04] 这里由于它用的是web的依赖,这里不需要其他的配置,直接上传即可。
[07:11] 好,视频就到这里。

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过编写并上传 Shell 脚本，结合 NIFI 工具链，实现从 Hive 数据源到 HBase 和 ES 的数据实时同步与统计分析流程。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 显示 Hue 文件浏览器界面，位于 /user/hue#/user/Hive/external/data_course/learning_course_online_dwm 目录。
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
  --master Spark://xc-online-Spark:7077 \
  --class ch.itcast.xc.analysis.search.InstantQueryStepToHive \
  /opt/run/jars/xc-Service-search.jar with dependencies.jar $(TO_DATE)
  if [[ $? == 0 ]];then
  echo "[===Spark-submit process success==]"
  else
  echo "[===Spark-submit process failed==]"
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
- 窗口显示文件传输成功，文件名为 xc-Service-search.jar with dependencies.jar。

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

