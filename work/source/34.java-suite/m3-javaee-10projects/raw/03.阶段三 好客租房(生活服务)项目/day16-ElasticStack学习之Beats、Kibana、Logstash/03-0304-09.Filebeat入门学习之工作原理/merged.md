# 09.Filebeat入门学习之工作原理

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\09.Filebeat入门学习之工作原理【海量资源尽在 ubkz.com】.mp4
- 时长 6分24秒（音频 385s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续那么接下来我们来看一下Failbit它的工作的原理那么把这工作原理给大家简单的去说一下那么Failbit有两个非常重要的组件一个叫Postpactor这个我们翻译成中文叫做探测器然后还有一个HaiVest那么这个我们前面是不是已经提到过它是一个叫搜割机,对吧
[00:21] OK那么分别来看这两个的一些作用那么首先我们来看一下这个Postpactor它是负责什么它是负责去管理Hivast并且去查找到所需要去读取的文件的一个来源那么要注意的是这个收割机Hivast它是负责去读取文件那么谁去勘测去找这个文件呢是通过它来去做一个找OK这要记住
[00:46] 那么如果我们输入类型是日志的话那么他就会去匹配这个路径下面所有的这个文件然后并为每一个文件所启动一个海外斯特去做一个读取那么failbit目前支持有两种pospector一个叫log一个叫就是standin那么这个就是一个标准的一个输入这个我们前面是不是说过OK
[01:07] 那么海外的这个前面前面我们其实也说过了他就是负责去读取我们文件的内容如果我们文件在读取的时候注意被重命名或者是删除的时候Filebit将继续去读取这个文件啊这个一定要注意然后呢接下来呢有一个这个疑惑或者疑问或者说一个小的一个知识点需要给大家去说一下那就是Filebit如何去保持文件的一个状态
[01:32] 那么什么意思呢来看一下那么你比如说我现在有一个文件我们就随便找一个文件就我们刚刚所写这个文件那么我这个文件那么我有四行这个数据
[01:43] 那么我的这个Failbit他在读取我这个日志文件的时候那么他是从第一行开始读还是从最后一个行开始读还是说如果他这个程序意外如果出现这个当机的话那么又会从哪个位置接着去读呢等等一系列问题也就是我们的读取文件的一个状态这个问题需要给大家去说清楚那么Failbit呢保存了每一个文件的状态并且呢把这个状态的刷新到磁盘上面一个注册文件中要注意在一个文件里面做一个记录
[02:13] 那么该状态呢用于记录我们海巴斯特去读取的读取的这最后的一个偏移量那么确保发送所有的日志行那么会记录你在最后一行在读到哪个位置要把这个记录下来如果我们发现你的输出比如说输出到elixir或者logstash的时候那么如果说你的elixir挂掉了对吧不能够去输出了那么这个时候呢Fairbit呢会去跟踪最后发送的这个行也就是把这个最后
[02:40] 发送这一行的先记录下来然后呢并且输输出再次可用的是可用是继续做一个去读取这个文件继续做一个输出那么也就是说当你这个服务不可用那OK我先记录下来然后等到你这个服务可用的时候呢我再继续向你去发送这个数据就可以了OK好那么这是这个点好那么我们接着继续往下面看那么下面我们来看一下在failbit运行的时候啊那么我们会为每一个pulse paleter去内存中的去
[03:10] 他却会保存一个文件的一个状态那当我们去重启注意去重启我们filebit的时候呢我们呢将去注册文件中去找到你原来一个文件的状态然后呢会从这个状态以后再去做一个读取OK那么这个文件的一个状态一个记录在哪里呢我们来找一下那么是在我们这个目录下面啊那么我们把这个先停掉它呢是在这个下面有一个data目录注意啊在这有一个
[03:38] Data这个目录那么Data目录下面呢又会有一个叫做Register那么我们来看一下这个Register的一个内容那么可以看到在这个里面它是不是就是所记录了我们的某一个文件你看这个是不是就是我们文件的一个路径那么它的一个Offset就是它的一个偏移量是多少以及它的一些这个时间呢一个类型呢啊等等那么是不是就会把一些偏移量的数据都保存到
[04:03] 这个里面来啊OK好那么这个就是给大家讲的他的一个基本的一个工作的原理啊相对而言还是比较简单的啊好那么下面我们需要给大家再说一下就是这个启动命令那么前面的我们启动的时候是不是都会通过这种方式去做一个启动对吧最后呢我们是不是也是将我们的数据是不是发送到了elax中那么现在就会有一个问题了就是我现在呢比如说啊我现在我起
[04:28] 我把这个退出去然后cd点点回去然后我执行一个命令来看一下
[04:33] 那么我执行这个命令要注意那么他是不是会把数据发送到elac设置中那么我现在如果想要在控制台去查看他的一个发送情况的话是不是就非常的不方便因为他没有任何的输出他只是把数据发送到了我们的elac设置中ok那么但是有些时候我们还是需要在这个控制台上让他打印出来对吧方便我们去做一些这个调试那么这个时候他也支持通过一个什么的杠D来指定一个publish
[05:02] 就可以输出一些我们的一些debug的信息那我们来看一下那么后面我们再去加一个-dpublish走那我们来看一下它会出现什么样的一些日式情况呢我们这样我们还是呢去给他去输入一些这个内容比如说我输入什么333保存对数走然后呢我们再进入到这个里面来看一下那么可以看到啊你看这个是不是就来了这个内容是不是333然后呢上面是他的一些debug的一些信息可以看到这是一个debug看到没有是debug的一个publish
[05:32] 然后去做一个publish的一个invent就是一个事件然后下面这个就是它的一些内容那么通过这种方式是不是就可以得知你这个数据它是如何去它发送的一些具体的细节是什么OK这样的话其实就是方便我们去做一些调试如果我们真正要去启动的时候或者说在生产环境运行的时候我们是不需要后面这个参数的OK这个要注意一下
[05:56] 好嘞那么我们来看一下除了我们刚刚所说这个杠D那么还有前面两个参数我们来再来说一下啊杠E呢是指我们要输出到我们这个标准的一个输出里面去默认的他会输出到我们那个系统的一个log下面以logs这个目录下面去ok杠C呢其实指定的是我们的配置文件啊ok好那么杠D刚才说过了就是debug好嘞那么这个呢就是我给大家去讲的啊这样的一个他的工作原理好那么关于failbit的一个工作原理那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Filebeat 的工作原理、配置文件结构、启动命令及日志数据如何被采集并发送到 Elasticsearch。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“2.6、Filebeat工作原理”章节，说明 Filebeat 由 prospector 和 harvester 两个主要组件组成，分别负责发现文件和读取单个文件内容。
画面2：终端显示文件 a.log 的内容，包含数字 456、789、111、222，用于演示日志数据。
画面3：终端显示文件 a.log 的内容，包含数字 456、789、111、222，用于演示日志数据。
画面4：PDF 文档中“2.6、Filebeat工作原理”章节，详细说明 harvester 和 prospector 的功能，以及 Filebeat 如何保存文件状态。
画面5：终端显示 Filebeat 的安装目录内容，列出多个配置文件，如 fields.yml、filebeat.reference.yml、filebeat.yml、haoke-es.yml、kibana.yml 等。
画面6：PDF 文档中“2.6、Filebeat工作原理”章节，展示 Filebeat 的启动命令和参数说明。
画面7：终端显示进入 data 目录，查看 registry 文件。
画面8：Elasticsearch Head 界面，显示索引 monitoring 中的文档，包含来自 Filebeat 的日志数据。
画面9：终端显示 Filebeat 停止后，日志信息显示“filebeat stopped”。
画面10：终端显示 Filebeat 启动并成功安装，输出配置路径、日志路径、Beat UUID 等信息。
画面11：终端显示 Filebeat 启动后，连接到 Elasticsearch，输出连接成功信息。
画面12：终端显示 Filebeat 发送的 JSON 数据，包含 message、prospector、input、from、host 等字段。
画面13：终端显示 Filebeat 发送的 JSON 数据，包含 timestamp、@metadata、offset 等字段。
画面14：PDF 文档中“2.6、Filebeat工作原理”章节，再次展示 Filebeat 的启动命令和参数说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
启动命令：
```
./filebeat -c haoke.yml "publish"
```
参数说明：
```
-c：指定配置文件
-d：输出debug信息
```
画面5：
```
total 35484
drwxr-xr-x 6 root root 4096 Jan 15 17:51 ./
drwxr-xr-x 4 root root 4096 Jan 15 17:51 ../
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .build.hash.txt
drwxr-xr-x 2 root root 4096 Jan 15 17:51 data/
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .cache
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .circleci
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .elastic
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .git
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .idea
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .m2
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .vscode
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarn
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2

