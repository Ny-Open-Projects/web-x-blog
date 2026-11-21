# 18-flume拦截器-模型分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\18-flume拦截器-模型分析【海量资源尽在 ubkz.com】.mp4
- 时长 9分14秒（音频 554s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来看Flume的一个案例这个案例是这样的有两台主机这两台主机里面呢有一些日志服务它们分别会产生三个日志文件比如说是access.logngix.logweb.log这三个日志文件呢是由不同的服务产生的那么现在呢我们要求这样做将两台机子上产生的日志文件呢汇总到第三台机子也就C机器上
[00:30] 并且在C机器上做一个统一的汇总那怎么汇总呢你把两台机子的access的log放在第三台机子比如说这个HDFS的这个目录把两台机子的ngx的log放在第三台机子HDFS的这个目录将两台机子web的log它的内容放在第三台机子HDFS的web这个目录下面要做这么一件事情
[00:58] 好 为了给大家讲得更清楚一点呢来 我们来看这个图打开画图好 这里有一张图我们来看上面是A机器下面是B机器那么它们呢在A机器上有三个日志文件这三个日志文件呢是不停地在更新的那这三个日志文件有了下面这台机子呢也有三个日志文件我要求呢在C机器上将这两个
[01:27] 这两个机子的日志文件分别进行汇总汇总的时候呢要求啊把来看一下汇总的时候要求把这个AuxSenseLog和这个AuxSenseLog它俩汇总在一起而呢把这两个我变个颜色把这个和这个汇总在一起而呢把这个和这个汇总在一起也就是相同的日志文件呢相同类型的
[02:02] 把它汇总在一起汇总完之后保存在哪里呢我们要保存的Hadoop基群也就是HDFS它对应的目录下面Oxas NGX Web分别放这些对应的日志文件信息那要做这么一个需求大家来想想是不是用我们今天讲过的Flume那关键是这个Flume如何去做一个配置呢来 接下来看另外一张图我们来看一下好 这是另外一张图
[02:32] 这个就将我们刚才的需求变成flum的一个模型上面这台机子我可以去设计一个flum实例这个flum里边这个地方是sauce这里边我们认为有三个sauce第一个这个sauce它监控的是一个文件的变化这个文件叫accaccess.log监控的是这个文件第二个是ngx
[03:06] ngs.log而第三个呢监控的是一个web.log好那么这三个是不是作为我们的一个source源呢我们要监控这三个文件的一些变化那你想想在这个flum里边我们的source有三个那么我们的source类型写什么呢我们可以写个escc我们可以用一个tl.f来监控这三个文件的变化这个没问题吧好
[03:36] 那么这个MEMO呢我们还是选Channel而这个Sync呢我们选的是Error因为这个呢数据要汇总到C机子所以说呢它要发送给下一机所以说这个地方呢我们选的是Error那接下来看下边这台下边这个台呢它也有三个AccessNex然后呢Web好那么同样的在这个地方也有三个Source它们也是ESCC分别监控
[04:07] Memory然后Channel是Memory而这个Sync是Evry关键是这两个Sync他们最终汇总到一个服务器上由这个服务器的Flume来接收那接下来我们来看这个Flume这个Flume它的Source是EvrySource它的Channel是Memory它的Sync它要存到HDFS那现在问题是问题是什么呢比如说我收到了一个数据
[04:37] 我要交给下一个服务器下一个服务器C那他怎么知道我这个数据是来自谁呢你比如说呢在这个三个日志里边呢都产生了三个文件三个数据比如说都叫hello来我们来标一下好也就是说Auxes呢也有个helloNGX呢也有个helloWeb呢也有个hello那么最终我要汇总的时候呢我要求呢这三个hello呢要放在不同的目录下面
[05:08] Auxis里边的HELLO那你就放在Auxis这个目录对不对你是NGXLOG里边的HELLO你就放在NGX目录那怎么样把这个相同的数据来区分它们是来自不同的日志文件呢这个时候我们要给大家引出一个东西这个东西叫拦截器拦截器好 这叫拦截器这个拦截器是干嘛呢这个拦截器说白了就是给每一个日志文件中的数据呢打一个标记
[05:39] 怎么打标记呢这个标记呢有两部分组成一个是k一个是value一个是k一个value而这个也就是一个箭着对这是一个箭着对而这个箭着对呢你可以自己来指定可以自己来指定比如说呢这里的k呢我们来换个颜色吧这样比如说这个k啊我们给它指定成一个一个什么呢我们指定一个type这个k是type而这个
[06:12] value呢这个value呢我们可以指定个accex好 指定这么一个类型好 标一下好了 那么大家想如果说我给这个hello打一个标记并且携带这个标记呢把这个数据呢发送给下一集好 发送给下一集好 那下一集收到这个数据之后呢它可以根据这个k呀根据这个k来获取这个value拿到这个value之后呢哦 它就知道
[06:40] 如果说你的value是access他就知道是access log里边的一些数据那这个时候他再去把数据存到hdfs的时候他就会存在hdfs目录这个存在access目录OK这么一个效果好存放到这个目录好那么咱同样的咱们想想看那么同样的我在这个nx这个地方呢我也可以给他打个标记比如说我打个标记这个k还是type
[07:11] 而这个value呢我写成一个index好把它向上拿一点好我也打一个index那这个时候呢大家注意当下游收到这个数据之后呢它根据这个type来获取这个value值是index那这个时候呢它就会把这个数据呢放在index目录好我们依此类推好那么到这个web的时候呢我们也给这个hello打个标记也是一个key和valuekey呢是type
[07:47] value呢是web好那么到下游的时候呢它根据这个k是type获取这个value是web它就应该放在web目录好web目录那好依次类推我们只说了上面这个那下面是不是也一样啊下面假如说也有很多的hello那这个时候我们依次类推给它打个标记那给下面那个也打个这么一个标记好那最下面呢我们也打一个标记好前面都个hello
[08:22] 好HelloHello那这样子我们再把数据发给下游的时候它也是根据这个k呢来获取valueAqual获取value之后呢大家注意这个时候呢它就会把这个数据呢根据value放在access然后根据这个数据呢放在index然后根据这个这个value呢会放到我们的对应的web那这样子两台机子上不同的一些不同的一些fulum呢它就会把相同日子的数据呢会放在同一个目录下面
[08:52] 这个就达到我们的需求了OK那么这是他一个思路那关键是如何给他打标记其实这个就是拦截器拦截器使用起来呢并不复杂我们只需要对配置文件做一些设置就可以了OK那么关于这个他的这个一个简单的模型呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解Flume日志采集系统如何从A、B两台服务器收集access.log、Nginx.log、web.log日志，并通过中间服务器C汇总后写入HDFS。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录和Flume案例一的场景描述，要求将A、B服务器的日志采集汇总到服务器C，再写入HDFS，同时列出具体日志路径。
画面2：展示数据流向图，A、B服务器的/data目录下的access.log、Nginx.log、web.log通过“数据流入”指向“服务器C”的“汇总”模块。
画面3：在画面2基础上，将“汇总”模块指向“Hadoop集群”，并标注“数据存放格式”为“/source/logs/access/20160101/”、“/source/logs/Nginx/20160101/”、“/source/logs/web/20160101/”。
画面4：在画面3基础上，将“数据存放格式”中的年份从“20160101”改为“20160101”，并补充“/source/logs/web/20160101/”。
画面5：展示Flume架构图，A、B服务器的access.log、Nginx.log、web.log通过“static interceptor”、“memory channel”、“avro sink”发送到服务器C的“avro source”。
画面6：在画面5基础上，对服务器B的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面7：在画面5基础上，将服务器C的“avro source”指向“memory channel”，再由“memory channel”指向“hdfs sink”。
画面8：在画面5基础上，对服务器A的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面9：在画面5基础上，对服务器A的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面10：在画面5基础上，对服务器A的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面11：在画面5基础上，对服务器B的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面12：在画面5基础上，对服务器B的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面13：在画面5基础上，对服务器C的“avro source”指向“memory channel”，再由“memory channel”指向“hdfs sink”。
画面14：在画面5基础上，对服务器A的“access.log”和“Nginx.log”添加“hello”和“type”字段，用于区分日志类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
1 /source/logs/access/20180101/**
2 /source/logs/Nginx/20180101/**
3 /source/logs/web/20180101/**

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
- 服务器A的/data目录下的access.log、Nginx.log、web.log → 数据流入 → 服务器C的“汇总”模块
- 服务器B的/data目录下的access.log、Nginx.log、web.log → 数据流入 → 服务器C的“汇总”模块
- 服务器C的“汇总”模块 → 指向“Hadoop集群”
- “数据存放格式”：
  - /source/logs/access/20160101/
  - /source/logs/Nginx/20160101/
  - /source/logs/web/20160101/

画面5：
- 服务器A的access.log、Nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source
- 服务器B的access.log、Nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source

画面7：
- 服务器C的avro source → memory channel → hdfs sink

画面14：
- 服务器A的access.log、Nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source
- 服务器B的access.log、Nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source

