# 17即时查询-统计分析-使用hbase注意事项

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\17即时查询-统计分析-使用hbase注意事项_【海量资源尽在 666java.com】.mp4
- 时长 6分31秒（音频 391s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,这里说一个使用HBase的注意事项,由于咱们这个项目是使用容器编排的方式进行启动的,而且咱们主要使用的容器都配置了开机启动,但是开机启动也有一个问题,因为HBase是强依赖ZOOKEYPAD的,如果在HBase启动的时候,ZOOKEYPAD没有启动,就会造成一个问题,HBase启动失败。
[00:29] 这里呢咱们这里是运行是ok的我来演示一下咱们这个出错的这种情况由于HBase启动的时候它需要Zookable这个时候呢我先把HBase和Zookable这两个容器都给都给停止了咱们呢使用Dock Compose这个编排命令把这个容器给停止了咱们是XC online首先呢是HBase
[01:08] 把HBase给停了停完之后呢咱们再把ZK给停了停止完成咱们再把ZK给停了停止完成之后呢咱们再把HBase来启动来模拟ZK没有启动成功的情况下咱们来启动HBase这种情况这个时候呢ZK是没有启动的咱们呢把HBase给启动了启动它的时候因为咱们现在是启动的容器
[01:52] 容器呢肯定是显示它是启动成功的但是但是它依赖于ZKZK是咱们依赖ZK是咱们HBase这个服务HBase这个容器启动了不代表它这个容器内的HBase就一定启动成功了咱们呢可以查看这个端口进行一个数据的一个浏览这里呢由于HBase咱们压根就没有启动
[02:24] 他呢访问的时候他一个端口都没有启动成功因为这些呢都是咱们HBase的外部端口这里HBase没有那个ZK没有启动HBase呢就是这种情况但是如果是ZK没有启动完成的时候他就是出现这种没有出售话的这种情况这个时候你执行程序他肯定是报错了咱们呢这个时候把ZK再给起来
[02:58] ZK起盘之后呢ZK的服务是OK的咱们呢可以登录到这个容器中进行一个查看这里呢咱们先登录到ZK容器查看ZK这个服务是否是启动成功了这里呢可以看到ZK的一个启动进程它是启动的咱们退出来再来看HBaseHBase呢你是可以看到它是有启动进程的但是呢
[03:34] 他刚才是没有启动成功了HBase启动完成之后呢咱们再来刷新因为没有启动命令这个呢还是挂的就是还是没有启动成功了咱们呢来切到HBase的这个B模组这里呢直接使用StarsHBase进行一个启动即可来刷新刷新他那个是说原来呢已经有程序在运行了但是呢因为咱们运行这个程序没有那个啥呀
[04:09] 没有运行成功所以说需要先把它给停了如果是容器ZK的容器是在启动没有启动完成的情况下咱们直接执行STAR命令它会自动的就是把咱们需要的给就是没有启动成功的给启动起来但是现在的这种情况HBase在启动的时候ZK是完全挂的情况下咱们这个地方还需要先把它给停止了再启动
[04:39] 你们在用的时候呢这个地方如果是开机启动的它就是这种情况因为咱们开机启动只会遇到这一种情况咱们来看它停止完成了ZK这里呢还在停止中这个呢停止的进程这个是会有一点问题的因为ZK呢是压根没有启动的它那个注册的时候没有注册成功咱们呢使用
[05:13] q 的方式把它给干掉q 干9好现在就没有了接下来咱们直接启动就行了好这个时候呢显示已经 ok咱们来刷新这个时候呢你可以已经看到咱们h base 的这个服务已经是 ok 的ok 咱们呢也可以开到主线条的这个可以看到有一个就是有一个 master 然后呢有一个 worker这个时候呢h base 就开用了
[05:56] 这个因为现在这个场景是不好演示的就是HBase没有启完的情况这个ZK没有启完的情况然后来启动HBase这个情况咱们现在是不好演示的但是就是如果ZK没有启动成功或者是未启动HBase一定不会启动成功这个是一定要注意的如果你在代码中遇到了这样的问题就可以来检查一下你的这个HBase
[06:25] 以及检查你的ZK好,HBase的这部视像就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何排查和解决 HBase 服务因 ZooKeeper 启动异常导致无法正常访问的问题。

2) 按时间顺序列出每张画面的要点：
画面 1: 在终端中执行 `hbase(main):006> scan 'LearningOnlineDetail'` 命令，显示 HBase 表数据，但提示 `NameError: undefined local variable or method 'a' for #<Object:0x42507640>`，表明 HBase 客户端可能未正确初始化。
画面 2: 执行 `hbase(main):006> exit` 退出 HBase Shell，然后执行 `Docker-compose stop xc-online-hbase` 停止 HBase 容器。
画面 3: 执行 `Docker-compose start xc-online-zk` 启动 ZooKeeper 容器，但终端提示 `Docker-compose: command not found`。
画面 4: 浏览器访问 HBase Web 端口 `http://xc-online:60030`，显示“无法访问此网站”错误。
画面 5: 在 Typora 文档中，显示 HBase 使用注意事项，指出 HBase 严重依赖 ZooKeeper，若 ZooKeeper 未启动，HBase 无法正常工作，并展示“RegionServer is initializing”错误信息。
画面 6: 执行 `Docker-compose stop xc-online-hbase` 停止 HBase，然后执行 `Docker-compose start xc-online-hbase` 启动 HBase。
画面 7: 在 HBase 容器内执行 `ps aux` 查看进程，显示 HBase 服务未启动，然后执行 `cd $HBASE_HOME/bin` 进入 HBase bin 目录。
画面 8: 在 HBase bin 目录下执行 `ls` 查看脚本，然后执行 `./start-hbase.sh` 启动 HBase。
画面 9: 在 Typora 文档中，再次展示 HBase 使用注意事项，强调 HBase 依赖 ZooKeeper。
画面 10: 在 HBase bin 目录下执行 `./stop-hbase.sh` 停止 HBase，然后执行 `./start-hbase.sh` 启动 HBase。
画面 11: 浏览器访问 HBase Web 端口 `http://xc-online:60030`，显示“无法访问此网站”错误。
画面 12: 浏览器成功访问 HBase Web 端口 `http://xc-online:60030/rs-status`，显示 HBase RegionServer 的软件属性信息。
画面 13: 在 Typora 文档中，展示 HBase Web 端口 `http://xc-online:60030/rs-status` 的成功访问页面。
画面 14: 在 Typora 文档中，再次展示 HBase Web 端口 `http://xc-online:60030/rs-status` 的成功访问页面。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
hbase(main):006> scan 'LearningOnlineDetail'
COLUMN=learning_online_detail.course_id, TIMESTAMP=1576176882366, VALUE=15843a4e69b0d3a7401490.704b3f7e6b0d1d
COLUMN=learning_online_detail.course_id, TIMESTAMP=1576176882366, VALUE=15843a4e69b0d3a7401490.704b3f7e6b0d1d
...
```
画面 2:
```
hbase(main):006> exit
```
画面 3:
```
Docker-compose stop xc-online-hbase
```
画面 6:
```
Docker-compose stop xc-online-hbase
Docker-compose start xc-online-hbase
```
画面 7:
```
ps aux
```
画面 8:
```
ls
./start-hbase.sh
```
画面 10:
```
./stop-hbase.sh
./start-hbase.sh
```
画面 12:
```
Software Attributes
Attribute Name Value Description
HBase Version 1.2.0-cdh14.0 revision=Unknown HBase version and revision
HBase Compiled Sat Jan 6 13:40:03 PST 2018, jenkins When HBase version was compiled and by whom
HBase Source Checksum 8ab06ca3829671d227c0971e565326226 HBase source MD5 checksum
Hadoop Version 2.6.0-cdh14.0 revision=0b1d933383c7980c18ba917ccaa106a17699 Hadoop version and revision
Hadoop Compiled 2018-01-06 21:24 GMT When Hadoop version was compiled and by whom
Hadoop Source Checksum 4adde4598a334aa91db2aa8d731f Hadoop source MD5 checksum
ZooKeeper Client Version 3.4.5-cdh14.0 revision=1 ZooKeeper client version and revision
ZooKeeper Client Compiled 01/06/2018 21:24 GMT When ZooKeeper client version was compiled
ZooKeeper Quorum xc-online-zk:2181 Addresses of all registered ZK servers
Coprocessors []
RS Start Time Thu Dec 12 19:02:56 UTC 2019 Date stamp of when this region server was started
HBase Master xc-online.hbase:60010 Address of HBase Master
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 5、9、13、14:
- 标题：3.2.4 使用hbase注意事项
- 内容：
  1. 访问hbase web端口（hbase web url: http://xc-online:60030）不能正常显示hbase相关信息，如下图所示：
     - The RegionServer is initializing!
  2. 代码操作hbase时抛socket超时异常
     - Exception in Thread "main" org.apache.Hadoop.hbase.client.RetriesExhaustedException: Failed after attempts=36, ...
  3. 解决方法：
     - ① 登陆hbase容器
       - Docker exec -it xc-online-hbase bash
     - ② 切换到hbase bin目录
       - cd $HBASE_HOME/bin
     - ③ 执行运行命令
       - ./start-hbase.sh
     - ④ 访问hbase web http://xc-online:60030，如下图所示，说明hbase启动成功

5) 无

