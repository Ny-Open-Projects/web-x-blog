# 8.7 Superset简介

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day8 数据可视化
- 源文件：06.阶段六 冷链监控平台项目\day8 数据可视化\8.7 Superset简介_【海量资源尽在 666java.com】.mp4
- 时长 10分59秒（音频 659s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来看一看Apache SupersetSuperset是由Airbnb也就是Airbnb开源的一个数据分析和一个可视化的一个平台它是用Python语言来构建的那么我们来简单的介绍一下我们为什么需要这种BI平台或者BI平台它到底做什么用呢我们知道在我们的业务系统里边其实有很多的业务需求这业务需求就是说我需要开发一个报表系统
[00:27] 而这个报表系统呢它包含几部分第一部分来讲的话是说我们有一个叫做数据的一个展示对吧数据展示而这种展示方式可以通过列表形式可以通过图表形式那么有很多的需求其实是需要经通过这种图表方式来进行展示的那对它展示的时候我们可以使用e-chart啊或者说其他的啊各种各样的这种前端的框架来开发图表
[01:01] 那开发图表它就需要有一个部分来提供数据的一个叫什么呢数据API接口对吧我根据接口我能够把我们的数据提供给前端展示出来而要有接口的话它其实就要查询我们的数据库我需要存储了一些数据而由这些数据呢我对它进行一个查询而这些数据从哪来呢
[01:36] 这些数据其实是从我们的各种各样的数据库的来各种各样的类型的这种数据库过来的比如说观星数据库MySQL Oracle等等或者是我们的大数据平台的数据库JadeApacheJade然后呢那个Clickhouse或者说是Hadoop Hive等等各种各样的数据库数据语言对吧它的数据语言有非常多种的多样它甚至还包括我们的文本文件
[02:08] 所以在这个过程中我们可以看一看如果一个报表它需要开发多少东西那第一部分来讲的话是我们的这个前端的页面的开发对吧前端前端的报表开发那第二部分来讲的话是后台的接口开发那第三部分来讲的话是属于我们的叫做什么呢我们的这个数据收取而在这样的一个情况下
[02:49] 开发一个报表那有可能会需要啊三天五天甚至于十天八天的这样的一个过程而对于前端的业务需求它其实变化非常多那有的时候是说哎我需要加上一个这个字段有的时候我需要新开一个数据库的一个报表我需要从多个数据源里面查取数据那在这种情况下我们的数据的开发其实是变得
[03:18] 相对来讲是时间可能是满足不了前满足不了业务的一个需要那另外一个另外一个需要是什么呢另外一个需要是说那针对于后台开发人员他其实不太他是不太懂业务的那前端的话对业务的敏感度比较强那前端说我需要自己来定义我们的开发定义自己来定义我的图表长成什么样我自己想用
[03:47] 柱状图,饼状图或者直线图来展示数据那能不能我自己来操作呢所以这两个这个关键点结合在一起就出现了一个叫做BI的工具我们可以看一下刚才看的这个逻辑图那么在这个逻辑图里边如果有一个BI系统那么这个BI系统的话它是需要提供几方面的内容第一
[04:21] 业务人员可以定义报表而这种报表来讲的话包括它的长的形式就是样式对吧无论是柱状图饼状图或者各种各样的这种形式然后它还可以自己定义数据语言对不对业务人员自己能定义数据语言业务人员自己能定义样式那这种数据语言的话包括我从哪一个数据库里面取哪一些字段
[05:04] 这些都是属于业务人员自己定义的一个范畴那第三部分来讲的话业务人员他希望这个时间周期比较快对吧他自己定义完了之后是所见即所得对吧我自己能够把它展现出来我自己就能看到了我必须要等待很长时间这是业务人员的心声那开发人员说那我无论怎么样我的前端开发后端开发数据抽取都是需要时间的
[05:34] 那如果按照原来的那种模式它其实是做不到的所以才有了这种BI系统OK那么我们看一看我们如果要开发BI系统它包含了几部分内容刚才看到的是一个是传统的业务逻辑开发一个是BI系统它想要达到的一个结果那么我们来我们来再看一下我们的这个BI系统那首先第一部分来讲的话肯定是数据出取对不对对
[06:13] 第一部分是我们的数据定义我们能够定义我们的数据在数据管理阶段那边第一部分定义数据语言第二部分定义展现形式是吧那在这的时候我们就是定义数据语言了那在这一部分的话我们就是需要有一个数据展示或者换句话说在这个地方如果不叫定义数据语言那其实可以把它叫做这种
[07:06] 数据抽取或者说数据的一个映射这是我们不同的数据源我们可以做的是如果把数据进行了一个抽取过来但是抽取过来有一个坏处是我的数据库可能会非常非常的多对不对我无论是mycircle也好或者说是大数据平台的数据库那它的无论是Hive或者其他的那相应的数据的数据量非常大如果我把它抽取过来其实是
[07:45] 也很难实现我们的一个效果我只能可能是说我只能是抽取一部分数据对吧那一种做法是数据抽取另外一种做法是数据映射能理解吧本身我的原始数据库里边有ABCABC三个字的那我在映射过程中我可能就映射成A片或者说叫小A小B小C这三个字的
[08:35] 那我在展示的时候我只要展示a小ab加c然后我用我们的图表或者桌上图来展示这也ok了对不对所以在这个过程中当然了在这个里边其实还有一个数据的一个接口提供在这个过程中我们的用户就能够看到了我们的我们的这种各种各样的图表了
[09:28] 我们接口提供给我们数据展示然后我们的映射执行的时候我们做了当它查询A的时候我们就直接就查询到了我们的我们的这个映射关系由此我们就能找到我们在这张表里面的这个字段这是我们的这个BI平台它所具有的一些功能我们回过头来看一看SuperSight
[09:57] SuperSight它是有一个映射的框架这个映射框架是Pathin因为本身SuperSight是用Pathin开发的所以说它的一个使用的OM框架也是属于Pathin的叫Circle ArchamCircle Archam它支持十多种的数据包括MyCircleOracleMSCircle等等这种关于数据库还包括我们的这种Hive或者说ClickHouseBigQuery
[10:25] 等等这些都属于大数据平台的数据库也就是说我们在我们的这种映射关系中它是通过在这种数据映射这个层面上它是就是用Circle Alt M来实现这种映射的那么通过这种方式它实现了我们对于数据从数据的展示到数据的数据源的定义然后对它数据的一个映射等等各种各样的一个
[10:54] 功能实现了我们这种BI的平台的一个功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲数据可视化工具 Superset 的架构、数据管理流程以及如何通过 Docker 安装部署。

2) 按时间顺序列出每张画面的要点：
画面 1: 新建空白演示文稿，准备绘制架构图。
画面 2: 绘制第一个架构图，包含三个矩形框，从上到下依次为“数据展示：列表、图表”、“接口”、“数据库”。
画面 3: 在“数据库”框下方添加三个新矩形框，并用箭头连接，表示“数据库”指向“数据源”。
画面 4: 在架构图右侧添加一个“BI系统”框，并用箭头连接“接口”框。
画面 5: 画面切换，显示空白屏幕。
画面 6: 在新页面中绘制两个矩形框，左侧框内有“1. 0.0”字样，右侧框内有“数据管理：1. 定义数据源 2. 定义展现形式”。
画面 7: 在左侧框内添加文字“定义数据源”，并用虚线箭头连接右侧框。
画面 8: 在左侧添加三个空矩形框，并用箭头连接中间的“数据映射”框。
画面 9: 在左侧三个矩形框上方添加文字“A.B.C字段”。
画面 10: 在“数据映射”框内添加文字“a.b.c”。
画面 11: 在“数据展示”框下方添加“接口”框，并用箭头连接“数据展示”框。
画面 12: 切换到文档，显示“数据可视化工具 - Superset”文档的“7.1 简介”和“7.2 安装”章节，其中包含数据库连接配置表。
画面 13: 显示“7.2 安装”章节内容，包含使用 Docker 安装 Superset 的命令。
画面 14: 显示“7.1 简介”章节内容，包含 Superset 支持的数据库及其对应的 SQLAlchemy 路径前缀。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 12:
```
数据库 安装命令 SQLAlchemy 路径前缀
MySQL pip install mysqlclient mysql://
Postgres pip install psycopg2 postgresql+psycopg2://
Presto pip install pyhive presto://
Hive pip install pyhive Hive://
Oracle pip install cx_Oracle oracle://
sqlite pip install sqlite3 sqlite://
Snowflake pip install snowflake-sqlalchemy snowflake://
Redshift pip install sqlalchmey-redshift snowflake://
MSSQL pip install pymssql mssql://
Impala pip install impyla impala://
SparkSQL pip install pyhive jdbc:Spark:psycopg2://
Greenplum pip install psycopg2 postgresql+psycopg2://
Athena pip install "PyAthena300c1.0.9" athena://
Athena pip install "PyAthena300c1.0.9" athena://
Vertica pip install sqlalchemy-vertica-python vertica://
ClickHouse pip install sqlalchemy-clickhouse clickhouse://
```
画面 13:
```
本例中我们使用superset展示mysql数据库和druid数据库。
7.2 安装
使用Docker方式安装superset，Docker镜像地址为：https://hub.Docker.com/r/amancevice/superset
# 更改现有superset镜像
[root@node2 ~]# Docker search superset
# 下载superset镜像
Docker pull amancevice/superset
# 查看本地镜像
Docker images | grep superset
amancevice/superset latest 2650648081308 3 months ago 1.40B
```
画面 14:
```
数据库 安装命令 SQLAlchemy 路径前缀
MySQL pip install mysqlclient mysql://
Postgres pip install psycopg2 postgresql+psycopg2://
Presto pip install pyhive presto://
Hive pip install pyhive Hive://
Oracle pip install cx_Oracle oracle://
sqlite pip install sqlite3 sqlite://
Snowflake pip install snowflake-sqlalchemy snowflake://
Redshift pip install sqlalchmey-redshift snowflake://
MSSQL pip install pymssql mssql://
Impala pip install impyla impala://
SparkSQL pip install pyhive jdbc:Spark:psycopg2://
Greenplum pip install psycopg2 postgresql+psycopg2://
Athena pip install "PyAthena300c1.0.9" athena://
Athena pip install "PyAthena300c1.0.9" athena://
Vertica pip install sqlalchemy-vertica-python vertica://
ClickHouse pip install sqlalchemy-clickhouse clickhouse://
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 架构图结构：从上到下，“数据展示：列表、图表”指向“接口”，“接口”指向“数据库”。
画面 3: 架构图结构：从上到下，“数据展示：列表、图表”指向“接口”，“接口”指向“数据库”，“数据库”指向三个“数据源”。
画面 4: 架构图结构：从上到下，“数据展示：列表、图表”指向“接口”，“接口”指向“数据库”，“数据库”指向三个“数据源”，“BI系统”指向“接口”。
画面 6: 两个矩形框，左侧框内有“1. 0.0”字样，右侧框内有“数据管理：1. 定义数据源 2. 定义展现形式”。
画面 7: 两个矩形框，左侧框内有“定义数据源”，右侧框内有“数据展示”，左侧框指向右侧框。
画面 8: 三个空矩形框，中间的“数据映射”框，左侧三个框指向“数据映射”框。
画面 9: 三个空矩形框，中间的“数据映射”框，左侧三个框指向“数据映射”框，上方有“A.B.C字段”。
画面 10: 三个空矩形框，中间的“数据映射”框，左侧三个框指向“数据映射”框，上方有“A.B.C字段”，“数据映射”框内有“a.b.c”。
画面 11: 三个空矩形框，中间的“数据映射”框，左侧三个框指向“数据映射”框，上方有“A.B.C字段”，“数据映射”框内有“a.b.c”，“数据展示”框指向“接口”框。
画面 12: 表格数据：数据库、安装命令、SQLAlchemy 路径前缀。
画面 13: 文本内容：本例中我们使用superset展示mysql数据库和druid数据库。7.2 安装。使用Docker方式安装superset，Docker镜像地址为：https://hub.Docker.com/r/amancevice/superset。# 更改现有superset镜像。# 下载superset镜像。# 查看本地镜像。
画面 14: 表格数据：数据库、安装命令、SQLAlchemy 路径前缀。

5) 不要评价画面美观，不要输出与课程无关的内容。

