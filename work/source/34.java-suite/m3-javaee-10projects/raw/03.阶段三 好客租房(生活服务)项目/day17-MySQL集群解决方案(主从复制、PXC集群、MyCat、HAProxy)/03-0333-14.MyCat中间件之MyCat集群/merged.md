# 14.MyCat中间件之MyCat集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\14.MyCat中间件之MyCat集群【海量资源尽在 ubkz.com】.mp4
- 时长 4分32秒（音频 272s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下Minecraft集群那么前面呢我们是通过一个Minecraft节点然后呢对接到有两个这个Minescope的集群对不对但是我们可以想一下那么如果在高并发的情况下面那么我们的这个系统肯定会面临着
[00:17] 性能的问题那么什么谁是可能会出现性的问题呢显然是Minecraft对不对因为我们现在所有的压力都会压到一个Minecraft上面那么也就意味着我们是需要给我们的Minecraft去做一个集群的那么也就意味着我们有这样的一个架构那么之前呢是有一个这个中间件就是Minecraft现在呢会有两个这个中间件去做这样的一个这个操作那么这样的话呢有两个中间件共同去做一个
[00:46] 这个中间件的一个这样的一个角色那么显然这个压力是不是得到一个平摊了对吧哎OK好那么下面我们来看一下如何去部署多个这个Minecat那么我们就这么来玩吧那么把它去到这个这个里面来看一下啊那么我们回到这个里面然后呢CPMinecat01到Minecat02然后呢来一个杠大写的R然后呢去做了一个复制然后呢我们进入Minecat02这个下面
[01:14] 然后呢我们需要去做一些修改由于呢我是在一台机器上面去启动有两个MICAT那么显然这个端口是吧要做一些设置啊要注意的是那么以下我这个动作呢是修改它的一些端口那么如果你的环境呢是在这两个MICAT在不同的机器那么其实没有必要去修改这个端口的而我现在是同一个机器是有必要啊
[01:40] 那么现在我们进入到config这个目录去做一个修改那么我们去打开这个配置文件然后下面有一个gmx这个端口的一个这个端口是要我们搜一下1981984默认1984把它改成1985保存最初好嘞第一个端口搞定那么第二个端口我们需要打开这个server配置文件
[02:07] 那么这个配置文件下面呢需要给他添加两个这个端口那么我们来看一下啊把这两个靠呃拷贝过来一个是我们服务的端口一个是管理的端口一个是8067啊呃默认是8066所以我们改成8067那么下面这个管理端口呢默认的是呃9066那么我也改把它改成9067啊那么把这个格式呢也整理一下来看一下来看一下啊整理一下好那么我们保存退出
[02:37] 那么这个配置呢就搞定了那么搞定之后呢我们就可以这两个端口我们就搞定了搞定之后呢我们就可以来做一个测试了然后呢进入到这个B目录下面我们把这个MICAD呢给它Q掉然后呢我们去做一个Q好那么Q之后呢我们就来去做一个重新做一个启动
[03:00] 那么启动之后呢它呢就启动了第二个MICAT的节点那我们来测试一下这个MICAT的一个我们再来创建一个这个连接吧192.168.1.181.18然后呢到MICAT02MICAT02然后呢它所连接的这个端口呢默认是不是8066啊我们改成8067啊8067那么这个是我们第二个这个节点别搞错啊是8067测试连接一下
[03:30] 那么我们密码不对这个是应该叫itcast然后密码是itcast123对吧123然后走你发现它连接成功了那么我们打开MACD02那么来看一下这个里面是不是也有这样的一个数据那么这两个MACD它所对接到的都是我们的两个这两个MySQL的集群所以他们的操作都是一样的对吧
[03:56] 所以我们也就是我们所实现了这样的一个架构但是大家可以想一下这个架构它已经实现了多个Minecraft集群那么我们是不是保障了Minecraft的一个性能以及它的可靠性但是我们应用程序是不是又要去对接到有两个中间件那么这个操作是不是又变复杂了对不对所以说我们需要通过一个负载均衡的一个方案来解决它OK
[04:24] 好 那么这个具体的负载均衡我们后面会讲那么关于这个MICAD的集群那我们先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何复制 Mycat 服务端配置文件并启动第二个 Mycat 实例，以实现集群部署。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于 Mycat 集群架构的说明，图示显示应用系统通过两个中间件连接数据库。
画面2：在终端中执行启动脚本，列出 Mycat 1.6.6.1 版本的依赖库文件路径。
画面3：在终端中查看 mycat01 目录内容，确认其包含配置文件。
画面4：在终端中将 mycat01 目录复制到 mycat02 目录，准备第二个实例。
画面5：在终端中进入 mycat02 目录，查看其内容，确认包含 bin、conf、lib、logs 等子目录。
画面6：在终端中查看 wrapper.conf 文件内容，显示 Java 应用配置。
画面7：在终端中进入 mycat02/conf 目录，准备编辑配置文件。
画面8：在终端中查看 server.xml 配置文件内容，显示 Mycat 服务的系统属性和用户配置。
画面9：在终端中进入 mycat02/conf 目录，准备编辑配置文件。
画面10：展示 PPT 页面，说明如何配置 MySQL 主从同步，并显示 Navicat 连接配置窗口。
画面11：在终端中进入 mycat02/bin 目录，准备启动 Mycat 服务。
画面12：在终端中执行启动脚本，列出 Mycat 2 的依赖库文件路径。
画面13：在 Navicat 中连接到 mycat02，显示正在插入数据。
画面14：在 Typora 文档中展示查询结果，显示数据已从两个节点汇总，确认集群功能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```bash
root@itcast02:bin# ./startup nowrap.sh
/usr/local/src/java/JDK 8.0_141/bin/java -DMYCAT_HOME="/haoke/mycat/mycat01" -classpath "/haoke/mycat/mycat01/lib/commons-collections-3.2.1.jar:/haoke/mycat/mycat01/lib/commons-lang-2.6.jar:/haoke/mycat/mycat01/lib/cursor-recipes-2.1.0.jar:/haoke/mycat/mycat01/lib/disruptor-3.3.4.jar:/haoke/mycat/mycat01/lib/ehcache-core-2.6.11.jar:/haoke/mycat/mycat01/lib/fastjson-1.2.12.jar:/haoke/mycat/mycat01/lib/guava-19.0.jar:/haoke/mycat/mycat01/lib/jackson-2.1.0.jar:/haoke/mycat/mycat01/lib/jdbc-2.0.jar:/haoke/mycat/mycat01/lib/joda-time-2.9.3.jar:/haoke/mycat/mycat01/lib/jsf305-2.0.3.jar:/haoke/mycat/mycat01/lib/kryo-2.10.jar:/haoke/mycat/mycat01/lib/log4j-1.2-api-2.5.jar:/haoke/mycat/mycat01/lib/log4j-1.2.17.jar:/haoke/mycat/mycat01/lib/log4j-core-2.5.1.jar:/haoke/mycat/mycat01/lib/log4j-slf4j-impl-2.5.1.jar:/haoke/mycat/mycat01/lib/mongo-java-driver-2.11.4.jar:/haoke/mycat/mycat01/lib/mysql-connector-java-5.1.35.jar:/haoke/mycat/mycat01/lib/mysql-binlog-connector-java-0.16.1.jar:/haoke/mycat/mycat01/lib/netty-buffer-4.1.9.jar:/haoke/mycat/mycat01/lib/netty-common-4.1.0.Final.jar:/haoke/mycat/mycat01/lib/netty-transport-4.1.0.Final.jar:/haoke/mycat/mycat01/lib/objenesis-1.2.jar:/haoke/mycat/mycat01/lib/reflectasm-1.03.jar:/haoke/mycat/mycat01/lib/sequoiadriver-1.12.jar:/haoke/mycat/mycat01/lib/slf4j-1.6.1.jar:/haoke/mycat/mycat01/lib/univocity-parsers-2.2.1.jar:/haoke/mycat/mycat01/lib/velocity-1.7.jar:/haoke/mycat/mycat01/lib/vr-apper.jar:/haoke/mycat/mycat01/lib/ZooKeeper-3.4.6.jar" -server -Xms2G -Xmx2G -XX:MaxPermSize=64M -XX:+AggressiveOpts -XX:MaxDirectMemorySize=2G io.mycat.MycatStartup > "/haoke/mycat/mycat01/logs/console.log" 2>&1 &
```

画面4：
```bash
root@itcast02:mycat# cp mycat01 mycat02 -R
```

画面5：
```bash
root@itcast02:mycat# ll
drwxr-xr-x 8 root root 4096 Feb 4 08:31 ./
drwxr-xr-x 3 root root 4096 Feb 4 01:02 mycat01/
drwxr-xr-x 8 root root 4096 Feb 4 08:31 mycat02/
```

画面6：
```properties
# Java Application
wrapper.java.command=jav
wrapper.java.mainclass=org.tanuiksoftware.wrapper.WrapperSimpleApp
wrapper.working.dir=.
# Java Classpath (include wrapper.jar). Add class path elements as
# needed starting from 1
wrapper.java.classpath.1=lib/wrapper.jar
wrapper.java.classpath.2=conf
wrapper.java.classpath.3=REPO_DIR/*
# Java Library Path (location of Wrapper.DLL or Libwrapper.so)
wrapper.java.library.path.1=lib
# Java Additional Parameters
"wrapper.conf" [dos] 113L, 4299C
```

画面8：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mycat:server SYSTEM "server.dtd">
<mycat:server xmlns:mycat="http://io.mycat">
  <system>
    <property name="nonePasswordLogin">0</property>
    <property name="useHandshakeV10">1</property>
    <property name="useSqlStat">0</property>
    <property name="sequenceHandlerType">2</property>
    <property name="subqueryRelationshipCheck">false</property>
    <property name="handleDistributedTransactions">0</property>
    <property name="useOffHeapForMerge">1</property>
    <property name="memoryPageSize">64k</property>
    <property name="spillFileBufferSize">1k</property>
    <property name="useStreamOutput">0</property>
    <property name="systemReserveMemorySize">384m</property>
    <property name="useZKSwitch">false</property>
  </system>
  <!--这里设置的itcast用户和虚拟数据库-->
  <user name="itcast" defaultAccount="true">
    <property name="password">itcast123</property>
    <property name="schemas">itcast</property>
  </user>
  <mycat:server>
    "server.xml" 25L, 1149C
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
架构图：
- 应用系统 → 读写操作 → 中间件
- 应用系统 → 读写操作 → 中间件
- 中间件 → 写操作 → 数据库
- 中间件 → 读操作 → 数据库

画面10：
PPT 标题：“搭建多节点 mycat”。
架构图：
- MySQL（主） ←→ 同步 ←→ MySQL（从）
- 192.168.1.18 mycat2 连接属性：
  - 主机名：192.168.1.18
  - 主机端口：192.168.1.18

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

