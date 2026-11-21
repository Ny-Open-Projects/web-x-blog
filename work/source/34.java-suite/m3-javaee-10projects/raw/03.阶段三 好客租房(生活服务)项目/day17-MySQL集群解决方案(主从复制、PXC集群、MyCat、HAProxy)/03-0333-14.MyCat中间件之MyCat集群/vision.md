# 画面线理解：14.MyCat中间件之MyCat集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\14.MyCat中间件之MyCat集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 00:59, 01:09, 01:13, 01:41, 01:47, 02:01, 02:07, 02:37, 02:45, 02:49, 02:59, 03:46, 04:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:38:22

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
/usr/local/src/java/jdk1.8.0_141/bin/java -DMYCAT_HOME="/haoke/mycat/mycat01" -classpath "/haoke/mycat/mycat01/lib/commons-collections-3.2.1.jar:/haoke/mycat/mycat01/lib/commons-lang-2.6.jar:/haoke/mycat/mycat01/lib/cursor-recipes-2.1.0.jar:/haoke/mycat/mycat01/lib/disruptor-3.3.4.jar:/haoke/mycat/mycat01/lib/ehcache-core-2.6.11.jar:/haoke/mycat/mycat01/lib/fastjson-1.2.12.jar:/haoke/mycat/mycat01/lib/guava-19.0.jar:/haoke/mycat/mycat01/lib/jackson-2.1.0.jar:/haoke/mycat/mycat01/lib/jdbc-2.0.jar:/haoke/mycat/mycat01/lib/joda-time-2.9.3.jar:/haoke/mycat/mycat01/lib/jsf305-2.0.3.jar:/haoke/mycat/mycat01/lib/kryo-2.10.jar:/haoke/mycat/mycat01/lib/log4j-1.2-api-2.5.jar:/haoke/mycat/mycat01/lib/log4j-1.2.17.jar:/haoke/mycat/mycat01/lib/log4j-core-2.5.1.jar:/haoke/mycat/mycat01/lib/log4j-slf4j-impl-2.5.1.jar:/haoke/mycat/mycat01/lib/mongo-java-driver-2.11.4.jar:/haoke/mycat/mycat01/lib/mysql-connector-java-5.1.35.jar:/haoke/mycat/mycat01/lib/mysql-binlog-connector-java-0.16.1.jar:/haoke/mycat/mycat01/lib/netty-buffer-4.1.9.jar:/haoke/mycat/mycat01/lib/netty-common-4.1.0.Final.jar:/haoke/mycat/mycat01/lib/netty-transport-4.1.0.Final.jar:/haoke/mycat/mycat01/lib/objenesis-1.2.jar:/haoke/mycat/mycat01/lib/reflectasm-1.03.jar:/haoke/mycat/mycat01/lib/sequoiadriver-1.12.jar:/haoke/mycat/mycat01/lib/slf4j-1.6.1.jar:/haoke/mycat/mycat01/lib/univocity-parsers-2.2.1.jar:/haoke/mycat/mycat01/lib/velocity-1.7.jar:/haoke/mycat/mycat01/lib/vr-apper.jar:/haoke/mycat/mycat01/lib/zookeeper-3.4.6.jar" -server -Xms2G -Xmx2G -XX:MaxPermSize=64M -XX:+AggressiveOpts -XX:MaxDirectMemorySize=2G io.mycat.MycatStartup > "/haoke/mycat/mycat01/logs/console.log" 2>&1 &
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
