# 画面线理解：19-flume拦截器-测试运行

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\19-flume拦截器-测试运行【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:45, 01:03, 01:45, 02:16, 02:46, 02:58, 03:12, 03:25, 03:54, 04:05, 04:33, 04:48, 05:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:42:41

1) 这一组画面整体在讲如何在 node01 和 node02 上开发 shell 脚本模拟生成日志数据，并在 node03 上配置 Flume 服务以收集这些日志数据。

2) 按时间顺序列出每张画面的要点：
   画面1：在 node01 上创建并编辑 shell 脚本 server.sh，用于模拟生成 access.log、web.log 和 nginx.log 日志。
   画面2：在 node01 上使用 scp 命令将配置文件 exec_source_avro_sink.conf 分发到 node02。
   画面3：在 node01 上编辑 server.sh 脚本，添加写入日志文件的命令。
   画面4：在 node01 上编辑 server.sh 脚本，完成写入日志文件和休眠的代码。
   画面5：在 node01 上使用 scp 命令将 server.sh 脚本分发到 node02。
   画面6：在 node03 上配置 Flume，定义 source、interceptor、channel 和 sink。
   画面7：在 node03 上启动 Flume 服务，显示加载 Hadoop 和 Hive 库的环境信息。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
   画面1：
   ```
   cd /export/servers/shells
   vim server.sh
   ```
   ```
   #!/bin/bash
   while true
   do
   date >> /export/servers/taillogs/access.log
   date >> /export/servers/taillogs/web.log
   date >> /export/servers/taillogs/nginx.log
   sleep 0.5;
   done
   ```

   画面2：
   ```
   [root@node01 conf]# ls
   agent.conf
   exec_source_avro_sink.conf
   ...
   [root@node01 conf]# scp exec_source_avro_sink.conf node02:$PWD
   100% 1392 1.4KB/s 00:00
   ```

   画面3：
   ```
   #!/bin/bash
   while true
   do
   date >> /export/servers/taillogs/access.log
   date >> /export/servers/taillogs/web.log
   date >> /export/servers/taillogs/nginx.log
   sleep 0.5;
   done
   ```

   画面4：
   ```
   #!/bin/bash
   while true
   do
   date >> /export/servers/taillogs/access.log
   date >> /export/servers/taillogs/web.log
   date >> /export/servers/taillogs/nginx.log
   sleep 0.5;
   done
   ```

   画面5：
   ```
   [root@node01 shells]# cd ..
   [root@node01 servers]# ls
   Apache-Flume-1.8.0-bin hadoop-3.1.1 shell taillogs zookeeper-3.4.9
   ...
   [root@node01 shells]# scp server.sh node02:$PWD
   100% 188 0.2KB/s 00:00
   ```

   画面6：
   ```
   a1.channels = c1
   #定义source
   a1.sources.r1.type = avro
   a1.sources.r1.bind = node03
   a1.sources.r1.port = 41414
   #添加时间拦截器
   a1.sources.r1.interceptors = i1
   a1.sources.r1.interceptors.i1.type = org.apache.flume.interceptor.TimestampInterceptor$Builder
   #定义channels
   a1.channels.c1.type = memory
   a1.channels.c1.capacity = 20000
   a1.channels.c1.transactionCapacity = 10000
   #定义sinks
   a1.sinks.k1.type = hdfs
   a1.sinks.k1.hdfs.path=hdfs://192.168.174.100:8020/source/logs/%{type}/%Y%m%d
   "avro_source_hdfs_sink.conf" [New] 38L, 1195C written
   [root@node03 conf]# cd ..
   [root@node03 apache-flume-1.8.0-bin]#
   ```

   画面7：
   ```
   Info: Sourcing environment configuration script /export/servers/apache-flume-1.8.0-bin/conf/flume-env.sh
   Info: Including Hadoop libraries found via /export/servers/hadoop-3.1.1/conf/flume-env.sh for Hive access
   Info: Including Hive libraries found via /export/servers/hadoop-3.1.1/share/hadoop/hive/lib/ for Hive access
   ...
   SLF4J: Class path contains multiple SLF4J bindings
   SLF4J: Found binding in [jar:file:/export/servers/hadoop-3.1.1/share/hadoop/common/lib/slf4j-log4j1.6.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
   SLF4J: Found binding in [jar:file:/export/servers/hadoop-3.1.1/share/hadoop/common/lib/slf4j-log4j1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
   SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
   ```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
   无。

5) 不要评价画面美观，不要输出与课程无关的内容。
