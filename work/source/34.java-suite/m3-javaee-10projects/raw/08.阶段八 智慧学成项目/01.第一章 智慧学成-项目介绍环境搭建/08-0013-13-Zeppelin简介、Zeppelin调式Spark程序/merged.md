# 13-Zeppelin简介、Zeppelin调式Spark程序

- 阶段：08.阶段八 智慧学成项目
- 章节：01.第一章 智慧学成-项目介绍环境搭建
- 源文件：08.阶段八 智慧学成项目\01.第一章 智慧学成-项目介绍环境搭建\13-Zeppelin简介、Zeppelin调式Spark程序_【海量资源尽在 666java.com】.mp4
- 时长 12分16秒（音频 737s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来学习ZipLin调试Spark程序通过学习也是需要掌握能够使用ZipLin调试Spark程序首先来看一下什么是ZipLinZipLin是一个基于网页的交互式数据分析开源框架ZipLin提供了数据分析数据可视化等功能支持的图表如下这里它的图表就是
[00:30] 数据框数据可视化的功能有表格柱状图饼状图轴线图去势图以及散点图默认的查询结果是以表格的形式展示ZPLA也是支持多元的包括ScalarPython以及G3方的框架像SparkSparkCore和SparkCircleHiveHBaseAleskaSource以及
[01:01] 兼容GDPC协议的数据库像Oracle, MySQL等等介绍完什么是ZipLin呢接下来咱们就是对它进行使用了使用之前呢需要先进行配置这里ZipLin的配置咱们只配置和Spark相关的因为呢咱们在学习中也是只使用ZipLin调试Spark在配置之前需要确认ZipLin的容器是否已启动
[01:32] 咱们在容器编排的时候ZPlane是和咱们的系统一起启动的不管是你的服务器还是你的虚拟机只要系统开机了它就启动了这里咱们可以验证一下使用Docker命令Docker PS这里可以找得到ZPlane已经启动端口映射是18080咱们进行一个访问
[02:01] 按着Ctrl键点击它就会打开浏览器这里已经打开了ZPling的外部界面接下来就是对它进行配置这里就直接操作了在右上角点击Ending Mouse弹出的菜单第二个选项就是它所有支持的一些应该是叫做处理器吧所有支持的第三方的
[02:32] 开源框架也好第三方的组件也好都是在这里这里输入Spark输入Spark之后呢就出现了咱们Spark的配置界面它是一个自动筛选的一个功能这里咱们只用关心Spark master的配置是咱们容器的地址集合这里呢在编排的时候其实也已经配置好了只是呢在这个地方还需要再确认一下它是
[03:03] 配置正确了咱们在使用Spark的时候呢只使用了Spark以及Spark Circle它的引用方式就是以百分号Spark加百分号Circle的方式进行一个使用后面呢DP Python Spark还有iPython Spark这些呢咱们是不做使用的感兴趣的话可以去了解咱们只掌握前两个即可接下来呢就是创建
[03:34] 点击notebook弹出菜单第一个curricle按钮note这里呢它默认已经选中了Spark你可以在下面看往下拉可以看到它支持其他的一些第三方的组件Spark这是有sh脚本来支持也支持fair文件pythonhive 啊不是这是hbase这是pig以及gdbc
[04:04] 只要兼容GDPC协议的这个地方都可以进行连接进行操作Hive也是兼容GDPC的Hive也在这个GDPC里边进行配置咱们这里边选择Spark给它起个名字也是Spark点击Create即可这个时候已经创建成功了咱们来回到文档看咱们走到哪一步了配置Spark已经完成这个地方接下来就是要运行
[04:32] Spark程序创建DataPook也已经完成接下来就是使用Spark Circle来查看有多少数据库这里咱们直接进行查看咱们使用Spark Circle的时候引用的命令是百分号Circle这里直接使用ShowDatabase进行一个查看多了一个分号这个地方是不需要分号的
[05:02] 编写完成之后,点击小三角进行运行。
[05:06] 这个地方正在Rain,正在执行中,等它响应一下。
[05:12] 这个Spark Circle是访问的咱们的Hive数据库,这个地方已经查看出来了,只有一个数据库,咱们来验证一下。
[05:27] 咱们使用Dock命令登录咱们的Hive容器,这里是XC-LineHive,终端是Base。
[05:38] 直接登录Hive的脚本咱们同样的是执行查看数据库的命令BASES这个地方已经查看了因为这个地方已经查看出结果可以发现它们是一样的但是你说我对Hive进行了一个修改这个地方创建一个temp创建一个新的数据库起名tmpOK已经创建成功
[06:16] 接下来呢,咱们再次执行结果,执行咱们这个脚本,可以看得到已经查询出来,说明咱们这个Spark Circle已经OK。
[06:28] 接下来呢,咱们下一步看是该做什么了。
[06:32] 接下来是使用Spark Code执行WordCount,这里呢,还是读取了咱们Hadoop上面的文件,然后呢,编写一个统计单词个数的一个程序,咱们来。
[06:48] 进行Spark call的一个编写这里呢在下面上面是一个编辑器你编写完了之后呢只要运行成功运行正确这个地方就不要再管它了咱们在下面写因为每一个功能你这个地方的话对应一个对应一块区域就可以对应一个工作区就行了这里咱们引用的是Spark引用完Spark之后这里的sc命令是可以直接使用了
[07:20] 咱们直接读取Hadoop上的文件这里给它一个import咱们是使用sc命令进行一个读取这里读取的是文件是直接使用text file进行一个读取读取完成之后咱们再做后续的操作这里填写咱们HDFS的文件协议路径咱们的路径是学程online
[07:51] Hadoop然后咱们的端口是9000文件呢就是word.txt这个时候呢文件已经读取完成了由于这个地方经之前的测试它是不能输入中文的不能输入中文咱们注释就没有办法加这个地方呢我就直接写了接下来呢进行一个统计给它一个电量吧contest
[08:19] 保持和咱们脚本里边和咱们开发工具里边是一致的这里使用input进行数据的处理input这个变量首先呢先对文件进行切分这个地方的话使用Feldt MapM大写首先呢咱们是按行读取的按行读取呢再对这个每行进行一个切分使用split
[08:48] 咱们切分的方式呢是table切分这就拿到了咱们每行的每行的切分后的每个单词拿到每个单词之后呢咱们需要对它进行一个计数这里呢写用map算子给它一个值给它一个变量叫word这个时候呢咱们把这个word进行一个计数就是每个单词计数为1word的计数完成之后呢咱们接下来就是合并单词的个数了
[09:19] 就是如果重复了就把1后面的1全部给累加起来这里使用reduce by kreduce by ky是小型这个时候因为它那个k咱们是直接加就行了咱们不管其他的值直接把它给相加相加完成之后咱们就得到了咱们这个结果这个时候就可以对结果进行一个办便利
[09:51] 这里便利直接使用for each的方式首先还是需要把它给转成一个集合不转成集合for each是没有办法编写的没有办法执行的for each用clicson转换然后for each进行打印print line这里直接输出即可这就是咱们执行word counter的一个小案例然后看一下
[10:24] 执行一下看代码有没有编写错误好这里统计出来了但是是不是少了一个排序这个地方的话它是按照单词按照单词的出现的顺序进行一个乱序的输出咱们接着对它进行一个排序使用star y还是和咱们代码里边idea代码里边保持一致这里使用降序排列这里是
[10:56] 降息的话就是files咱们再运行一遍看是否得到正确的结果OK这个结果呢就得到了咱们最终的一个正确的结果是排序后的结果咱们来回到文档好执行完word count之后呢咱们就是以一个入门案例拿这个word count当做咱们的入门案例就是来调试咱们这个Spark程序这里咱们结果已经输出
[11:28] 调试呢也就到这里就结束了咱们再来看一下咱们最终的一个达能达到了一个需要达到一个目的就是使用Zip令调试Spark程序这里呢咱们首先介绍了Zip令接着呢对Zip令进行了一个配置但是配置之前呢需要是把容器给启动起来了容器启动起来呢之前之后呢咱们创建了Spark的Netbook
[11:55] 接着呢就是在这个notebook上面Spark的notebook上面执行了Spark Circle以及呢执行了Spark Card World Counter通过这两个小案例呢咱们来简单的入门咱们的Zip令调试Spark程序以上呢就是本节课的所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 启动 Zeppelin 并使用 Spark SQL 和 Spark Core 进行数据操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：介绍 Zeppelin 是一个基于网页的交互式数据分析开源框架，支持数据查询、可视化等功能，并展示其界面元素（表格、柱状图、折线图等）。
画面2：继续介绍 Zeppelin，强调其支持多种语言（Scala、Python、SparkSQL、Hive、HBase、Elasticsearch、JDBC等），并展示配置 Spark 属性的界面。
画面3：展示 Zeppelin Notebook 页面，准备创建新 Notebook。
画面4：在 Zeppelin 中创建新 Notebook，选择默认解释器为 Spark。
画面5：在 Zeppelin 文档中说明创建 Spark notebook 的操作步骤。
画面6：展示 Zeppelin Notebook 界面，准备执行 Spark sql 查询数据库。
画面7：在终端中执行 Docker-compose up 命令启动服务。
画面8：在终端中执行 bash 命令进入容器环境。
画面9：展示 Zeppelin Notebook 界面，准备执行 Spark sql 查询数据库。
画面10：在 Zeppelin Notebook 中输入 Spark 代码读取文件。
画面11：在 Zeppelin Notebook 中执行 Spark 代码，显示结果。
画面12：在 Zeppelin 文档中说明使用 SparkSQL 查看数据库。
画面13：展示 Zeppelin Notebook 页面，准备创建新 Notebook。
画面14：展示 Zeppelin Notebook 界面，准备执行 Spark sql 查询数据库。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
a. Apache Zeppelin 是一个基于网页的交互式数据分析开源框架。Zeppelin提供了数据
分析，数据可视化功能支持的界面如下所示：
```
画面2：
```
启动zeppelin 如果已启动，此步可跳过，继续下一步
在Docker-compose.yml文件中执行bash命令，这里的路径是：/opt/cdh5.14.0
Docker-compose up -d xc-online-zeppelin
```
画面7：
```
xc-online-s$ Docker-compose up -d xc-online-zeppelin
```
画面8：
```
xc-online-s$ xc-online-Hive bash
```
画面10：
```
val input = sc.textFile("/hdfs://xc-online-Hadoop:9000/word.txt")
```
画面11：
```
val counts = input.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _).sortBy(_._2, false)
counts.collect().foreach(println(_))
```
画面14：
```
show databases
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题“3.1 什么是Zeppelin”，内容包括 Zeppelin 的功能介绍和界面元素。
画面2：PPT标题“3.2 Zeppelin配置Spark”，内容包括启动命令和配置界面。
画面5：PPT标题“3.3 Zeppelin运行Spark程序”，内容包括创建 notebook 的操作步骤。
画面6：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 Spark sql 查询数据库的界面。
画面12：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 Spark sql 查询数据库的界面。
画面13：PPT标题“3.3.1 创建Spark notebook”，内容包括创建 notebook 的操作步骤。
画面14：PPT标题“3.3.2 使用SparkSQL查看有多少数据库”，内容包括 Spark sql 查询数据库的界面。

5) 不要评价画面美观，不要输出与课程无关的内容。

