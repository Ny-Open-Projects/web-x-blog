# 画面线理解：14-Hue简介、Hue操作hive及hdfs

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\14-Hue简介、Hue操作hive及hdfs_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:36, 01:58, 02:21, 02:30, 02:59, 05:04, 06:48, 07:17, 07:52, 08:58, 09:42, 10:09, 10:19, 10:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 22:36:02

1) 这一组画面整体在讲如何使用Hue Web界面进行HDFS文件管理、创建数据库以及使用Spark进行词频统计。

2) 按时间顺序列出每张画面的要点：
画面1：终端界面，显示用户登录到远程服务器，当前目录为根目录，提示符为“xc@xc-online:~$”。
画面2：浏览器打开Hue的HDFS浏览页面，URL为“xc-online:8888/hue/”，左侧显示课程PPT目录结构，当前章节为“4.3 Hue组件使用”。
画面3：浏览器显示Hue登录页面，提示用户输入用户名和密码。
画面4：浏览器显示Hue登录页面，提示用户首次登录需设置用户名和密码，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面5：浏览器显示Hue登录页面，提示用户首次登录需设置用户名和密码，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面6：浏览器显示Hue的Query页面，Query History中显示了多个Hive SQL语句，包括“CREATE DATABASE xc_online”、“DROP DATABASE tmp”等。
画面7：浏览器显示Hue的File Browser页面，当前浏览的是“/hbase”目录，列出了多个文件和文件夹。
画面8：浏览器弹出“Create File”对话框，文件名为“Test”。
画面9：浏览器显示Hue的File Browser页面，页面正在加载中，显示一个加载动画。
画面10：浏览器打开一个新标签页，页面为空白。
画面11：浏览器显示Spark Notebook页面，代码内容为Spark的词频统计程序，包括“val input = sc.textFile(...)”、“counts.collect().foreach(println(_))”等。
画面12：浏览器显示课程PPT页面，当前章节为“4.3.1 hive界面介绍”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面13：浏览器显示课程PPT页面，当前章节为“4.3.2.1 hdfs界面介绍”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面14：浏览器显示课程PPT页面，当前章节为“4.3.2.2 使用hue新增文件到hdfs”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：Query History中的SQL语句：
```
CREATE DATABASE xc_online
DROP DATABASE tmp
drop DATABASE tmp
CREATE DATABASE tmp
CREATE DATABASE tmp
```
画面11：Spark Notebook中的代码：
```
val input = sc.textFile("https://xc-online-hadoop:8088/word.txt")
val counts = input.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_, _-2).sortByKey(false, 2)
counts.collect().foreach(println(_))
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“4.3 Hue组件使用”，左侧目录结构显示“4.3.1 hive”、“4.3.2 hdfs”、“4.3.3 使用hue修改hdfs上的文本文件”等。
画面5：PPT标题为“4.3 Hue组件使用”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面12：PPT标题为“4.3.1 hive界面介绍”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面13：PPT标题为“4.3.2.1 hdfs界面介绍”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。
画面14：PPT标题为“4.3.2.2 使用hue新增文件到hdfs”，下方有提示文字“PS: 使用虚拟机中的hue, 用户名: hue, 密码: hue”。

5) 不要评价画面美观，不要输出与课程无关的内容。
