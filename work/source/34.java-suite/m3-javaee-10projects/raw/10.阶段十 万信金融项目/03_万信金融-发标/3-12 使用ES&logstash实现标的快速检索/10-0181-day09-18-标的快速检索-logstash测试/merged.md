# day09-18-标的快速检索-logstash测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-18-标的快速检索-logstash测试_【海量资源尽在 666java.com】.mp4
- 时长 9分48秒（音频 588s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们给大家介绍了一下logstash是如何使用的包括它的一些工作原理都给大家做了介绍接下来咱就要进行测试看一看咱们电脑上logstash现在能不能正常工作对不对能不能从mycircle当中采集到数据然后给它输出到什么地方对ES当中咱们接下来进行测试测试的时候为了变异测试我这给大家提供了一个伺服脚本
[00:29] 这个搜索脚本呢是往你的标的信息表里边插入一些测试数据了因为咱之前这个发标就发了一次标嘛反正我的表里边数据有一条可能一测试也就没了所以说我这儿多提供几条这个测试数据给大家用在这儿图像里边有就这个这个你可以看一下这里边其实就是一堆insider语句往这个标的信息表里边吧多插入了一些测试数据你给你自己的情况你要是表里边有
[01:00] 这些这个好几条测试数据的话你就不用执行这个然后呢接下来呢我们要测试是不是要把ES给启动一下还有什么header插件还有就是谁啊log,stetch这三样都得启动咱一个一个来吧先找到我的Elasticsearch怎么启动啊是不是找到闭目录然后双击谁啊Elasticsearch.bat双击就是说你要观察控制台看有没有报错啊这边你就看这个日志的级别这个info
[01:33] 这个级别这一块啊看有没有出现error对吧一旦出现error那就是启动失败了呗你就看中间这一块就行了这是这个级别你看目前都是info info对不对那我这里边是不是有ak分子器吧这个提前已经配好啊这让他继续启动吧然后咱接下来要要启动谁啊黑的插件对不对我们一会要观察效果吧我们要启动黑的插件黑的插件咋启动在他的根目录下面啊我们要点右键执行哪个命令啊
[02:10] 叫 n p m 是前端的东西对吧 run s t a r t 这回事他启动应该比较快是不是这青蛙9100是不是是他已经启动了我们再看刚才这个这边应该也启动了应该启动了咱一会访问一下试就行然后还要启动谁还要启动log stash是不是log stash 咋启动注意了咱讲一里边说了看好了啊你要去什么呀
[02:41] logstash的b目录当中然后执行这么一个执行这么一个命令啊来咱看一下这是我本机上的logstash要去哪啊b目录下面然后呢执行一个命令啊那个命令啊就这个命令稍等一下刚才粘的时候啊前面少粘一个点是不是点啊那这个命令是什么意思呢咱进来看一看这个命令什么意思
[03:19] 那我们要想启动这个logsdash其实主要就执行这里面的这个谁呢你看这有个BAT文件叫logsdash.bat你看是不是执行了它对不对执行它的时候呢我们-f是来设置我们刚才给他的那个配偶链在哪就mycircle-es.conf这个配偶链我们是不是放到那个configger那个目录下边你看你要后退一级是不是configger里边在哪呢这个我们还没考过来呢是不是那我这呢
[03:51] 提供的一友啊就是他客家人员有然后呢你得考到这个地方一下刚才呢我们只是把某种面口过来那然后呢就是在这啊你需要呢就是指定一下这个配用年的路径就想路径别嫌错了啊然后这就ok了你去要回车然后也是要观察一下这个启动工程当中啊看这个空调有没有报错那么在logs在这起落过程当中有可能你的电脑会碰到这样一个报错就是内存溢出的一个报错有可能啊
[04:29] 但是不一定每个同学的电脑都有出现这种问题这个要看你电脑内存够大不够大如果你的内存不够大的话你要做这么一个配置把logstash它的内存给它减少logstash有这么一个配置你自己找configure下面它本身它这里边的默认占用的内存是1G如果你报这个内存一输这个错了你找到这个配置把它改小一点比方我这就改成什么256然后这个错就解决了改小一点
[05:01] 我们观察一下这个启动的过程咱看看有没有报错呀你还是就看这个音份啊看这个日志的级别主要这里边没有出现什么呀error就行了就证明就没有问题了你看它这里边其实都已经开始工作了你看你看这是啥这这不就是那个啥呀这不是在执行咱那个伺候语句吗是不是你看它这个日期的这个值对不对当然它现在采集不到数据啊因为咱这个表里边数据我动了没有
[05:32] 没有发生变化没有发生变化呢他其实他该执行执行每个声表执行一次但其实他在执行这个搜据局的时候会采集到数据吗那倒不会因为我们表里面数据我们没动嘛所以在执行搜据局的时候根本查不出来数据那咱现在怎么测试那很简单啊我在这就是人工的直接去表里边去手动的去修改这个数据了手动去修改那咱先看看这个ES里边ES里边现在有一条数据这是我以前的测试
[06:02] 哪一条数据白德女士第一次接款这个数据采取过了是不是那接下来我就再找一个数据比如找这个谁啊找这个左邱先生吧第二次接款找他啊这是倒数第二行数据那找到他干嘛呢我要改一个值这里边字段值你其实随便改啊比如说我就把这个字段的值把它改成这个值可以吧
[06:27] 然后我们前面说过了你在修改数据的时候这个modify data值一定要改对吧而且是不是要改成当前的这个什么呀日期时间对不对当前的日期时间你在这可以选一下你看当前是不是11点22分42秒对不对49秒我点击确定然后赶紧刷新一下赶紧更改是吧然后呢你就等着他干什么呀采集就行了当然你也不用看这个控制台了我们直接去哪ES里边你就在这刷新就行了
[07:00] 看他一会儿是不是会多采集到一条数据每隔十秒钟对不对就采集到了大家看已经采集到大家看一下你稍微等一下你看变成两条是不是然后我们看这个数据浏览你看这个左丘先生第二次接款采集到了没有就采集到数据了你看是不是证明我们的logstash在正常工作然后你也可以去这个什么控制台他控制台应该对你看这也打印的有数据你看这就采集到数据了
[07:34] 如果你没有采集到数据的话似乎于下面是没有这些数据的你看咱之前采集的在没有采集到数据的时候啊这都是采集到数据了啊之前没有采集到数据的时候你看这些似乎于下面会有他采集到这些数据的一个打印吗不会有啊不会有你看这儿就有就采集了然后呢你还可以再观察一个地方观察哪观察我们说他是不是有个地方记录了那个执行的时间吗呃是在哪呀是在考虑的里边吗
[08:05] 是哪个地方啊我们看一下当时咱配置的是是这个文件logs-metadata是不是这个文件我放到哪我们来找一下啊是在根目录下边啊是在这个b目录下边啊你看就是logs-metadata然后我们打开你看这里面是不是记录了我们最后一次是不是这个执行了什么这个时间你不用管这个时间呢有可能不是咱那个呃
[08:41] 这个咱应该是东八区是不是他要记录应该是那个格雷尼治的那个时间但是这个你不用管因为我们当时设计的有黑五年里边是不是加了那个时区的配置了他会给我们做转换其实就加上八嘛这个大家不用管啊但是你只需要知道那的确记录这个时间了就行了就是这个地方让大家观察这个地方是其实主要就是你就是要看一看这个颜色当中这个数据到底同步过来没有
[09:11] 那么接下来你要想继续测试的话还是一样你在这你也可以自己新增一条数据是不是新增数据的时候这个值一定要改到这个稍微大一点让他能采取到或者说你也拿现有的数据反正你随便挑子弹改一改这个时间你也得改一改改的稍微大一点让他一定得超过上一次的那个什么执行时间那么这个数据他就能干什么呀而且大家观察到了我们有没有进行重复采取没有所以说这个你就下去自己可以进行测试就行
[09:40] 所以说呢这就是我们把咱本机当中logstash这块给它测试了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Logstash 将 MySQL 数据库中的项目表数据同步到 Elasticsearch，并展示数据在两个系统中的状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，其中包含“4.4.3 测试”小节，说明启动Logstash并修改jvm.options文件以调整堆内存。
画面2：展示Elasticsearch 7.3.1安装目录结构，包含bin、config、data等文件夹。
画面3：在Elasticsearch的bin目录下，通过命令行启动服务，显示加载了多个插件。
画面4：在Logstash的bin目录下，通过命令行启动服务，显示加载了多个插件。
画面5：在Windows PowerShell中，执行Logstash启动命令：.\logstash.bat -f ..\config\mysql-es.conf。
画面6：再次展示课程PPT内容，强调修改jvm.options文件以调整堆内存。
画面7：在PowerShell中，展示Logstash的SQL查询语句，用于从MySQL中读取数据。
画面8：在PowerShell中，执行SQL查询语句，将数据写入Logstash的管道。
画面9：在Solving Professional 64软件中，展示MySQL数据库中project表的数据。
画面10：在Elasticsearch的Kibana界面中，展示wanxing2p_project索引的状态，显示有11个文档。
画面11：在PowerShell中，展示Logstash的SQL查询语句，用于从MySQL中读取数据。
画面12：在Elasticsearch的Kibana界面中，展示wanxing2p_project索引中的数据。
画面13：展示课程PPT内容，其中包含Logstash的配置文件模板，用于定义数据同步规则。
画面14：在Solving Professional 64软件中，展示MySQL数据库中project表的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.4.3 测试
1. 找到案件中的"标的"信息表,测试.sql并执行
2. 启动ES和head插件,然后在Logstash的bin目录中执行如下命令启动Logstash
.\logstash.bat -f ..\config\mysql-es.conf
3. 如果遇到内存溢出的报错,修改config目录下的jvm.options文件,把1g的默认内存改小:
```
画面2：
```
bin
config
data
jdk
logs
modules
plugins
LICENSE.txt
NOTICE.txt
README.txt
```
画面3：
```
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-common]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-geotools]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-geoip]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-user-agent]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-mutate]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T1

