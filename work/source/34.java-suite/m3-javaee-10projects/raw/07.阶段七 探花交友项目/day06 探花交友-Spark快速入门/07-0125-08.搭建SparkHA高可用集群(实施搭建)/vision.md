# 画面线理解：08.搭建SparkHA高可用集群（实施搭建）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\08.搭建SparkHA高可用集群（实施搭建）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:54, 04:52, 05:53, 07:52, 08:37, 09:58, 11:20, 12:13, 12:51, 14:32, 15:40, 17:20, 18:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:22:23

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 ZooKeeper 实现 Spark HA（高可用）集群部署，包括配置文件修改、服务启动与故障恢复测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档中关于基于 ZooKeeper 的 Spark HA 高可用集群部署的说明，包含配置文件修改和参数说明。
画面2：在终端中执行 ping 命令测试与 ZooKeeper 服务器的连通性。
画面3：在 Spark 安装目录下查看启动脚本文件列表。
画面4：在终端中执行 jps 命令查看当前运行的 Java 进程，确认无 Spark 进程。
画面5：打开浏览器，准备访问 Spark Web UI。
画面6：访问 Spark Master Web UI，显示初始状态（Status: STANDY）。
画面7：在 Spark 日志目录下查看日志文件，确认 Master 和 Worker 的日志文件存在。
画面8：在终端中执行 start-master.sh 启动 Spark Master，然后执行 jps 命令确认 Master 和 Worker 进程已启动。
画面9：在终端中查看日志，发现 Worker 无法连接到 Master，执行 kill 命令终止 Worker 进程。
画面10：在终端中执行 kill 命令终止 Worker 进程后，再次执行 start-master.sh 启动 Master。
画面11：访问 Spark Master Web UI，显示 Worker 状态为 DEAD。
画面12：访问 Spark Master Web UI，显示 Worker 状态为 ALIVE。
画面13：访问 Spark Master Web UI，显示无法访问，提示连接被拒绝。
画面14：展示课程文档中关于 Spark 角色介绍和架构的说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
o 将spark 集群部署到同一个ZooKeeper 实例并启动多个Master . 利用zookeeper 提供的选举和状态保存功能，可以使一个Master 被选举成活着的Master，而其他Master 处于Standby 状态。
o 如果现任Master 死去，另一个Master 会通过选举产生，并恢复到旧的Master 状态，然后恢复流量。整个恢复过程可能需要1分2钟。
2.5.2、基于zookeeper 的Spark HA 高可用集群部署
该HA 方案做起来很简单，首先需要搭建一个zookeeper 集群，然后启动Zookeeper 服务，最后在不同节点上启动Master。
参数说明：
• spark deploy.recoveryMode：恢复模式（Master 重新启动的模式）
o 有三种：(1) ZooKeeper (2) FileSystem (3) NONE
• spark deploy.zookeeper.url：ZooKeeper 的Server 地址
```

画面2：
```
[root@itcast sbin]# ping zk
PING zk (192.168.31.81) 56(84) bytes of data.
64 bytes from zk (192.168.31.81): icmp_seq=1 ttl=64 time=1.86 ms
---
zk ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 952ms
rtt min/avg/max/mdev = 1.867/1.867/1.867/0.000 ms
```

画面3：
```
[root@itcast sbin]# cd sbin/
[root@itcast sbin]# ll
总用量 92
-rwxr-xr-x. 1 1000 1000 2803 5月 1 13:19 slaves.sh
-rwxr-xr-x. 1 1000 1000 5689 5月 1 13:19 spark-config.sh
-rwxr-xr-x. 1 1000 1000 1262 5月 1 13:19 spark-daemon.sh
-rwxr-xr-x. 1 1000 1000 1190 5月 1 13:19 start-all.sh
-rwxr-xr-x. 1 1000 1000 1274 5月 1 13:19 start-history-server.sh
-rwxr-xr-x. 1 1000 1000 2050 5月 1 13:19 start-mesos-shuffle-service.sh
-rwxr-xr-x. 1 1000 1000 1423 5月 1 13:19 start-mesos-dispatcher.sh
-rwxr-xr-x. 1 1000 1000 3151 5月 1 13:19 start-shuffle-service.sh
-rwxr-xr-x. 1 1000 1000 1857 5月 1 13:19 start-slave.sh
-rwxr-xr-x. 1 1000 1000 1527 5月 1 13:19 start-thriftserver.sh
-rwxr-xr-x. 1 1000 1000 1478 5月 1 13:19 stop-all.sh
-rwxr-xr-x. 1 1000 1000 1056 5月 1 13:19 stop-history-server.sh
-rwxr-xr-x. 1 1000 1000 1080 5月 1 13:19 stop-mesos-shuffle-service.sh
-rwxr-xr-x. 1 1000 1000 1064 5月 1 13:19 stop-mesos-dispatcher.sh
-rwxr-xr-x. 1 1000 1000 1067 5月 1 13:19 stop-slave.sh
-rwxr-xr-x. 1 1000 1000 1064 5月 1 13:19 stop-thriftserver.sh
```

画面4：
```
[root@itcast ~]# jps
2545 jps
2582 Worker
2631 Jps
```

画面6：
```
Spark Master at spark://itcast:7077
URL: spark://itcast:7077
Alive Workers: 0
Cores in use: 0 Total, 0 Used
Memory in use: 0.0 B Total, 0.0 B Used
Applications: 0 Running, 0 Completed
Drivers: 0 Running, 0 Completed
Status: STANDY
```

画面7：
```
[root@itcast logs]# ll
总用量 48
-rw-r--r--. 1 root root 15966 8月 9 17:33 spark-root-org.apache.spark.deploy.master.Master-1-itcast.out
-rw-r--r--. 1 root root 20956 8月 9 17:33 spark-root-org.apache.spark.deploy.worker.Worker-1-itcast.out
-rw-r--r--. 1 root root 2114 8月 9 17:27 spark-root-org.apache.spark.deploy.worker.Worker-1-itcast.out.1
-rw-r--r--. 1 root root 2061 8月 7 11:12 spark-root-org.apache.spark.deploy.worker.Worker-1-itcast.out.2
```

画面8：
```
[root@itcast sbin]# start-master.sh
starting org.apache.spark.deploy.master.Master, logging to /itcast/spark/logs/spark-root-org.apache.spark.deploy.master.Master-1-itcast.out
[root@itcast sbin]# jps
2658 Master
2582 Worker
2631 Jps
```

画面9：
```
19/08/09 17:28:07 WARN Worker: Failed to connect to master itcast:7077
org.apache.spark.SparkException: Exception thrown in awaitResult(ThriftUtils.scala:226)
at org.apache.spark.util.ThreadUtils.awaitResult(ThreadUtils.scala:75)
at org.apache.spark.rpc.RpcEnv.setupEndpointRefByURI(RpcEnv.scala:101)
at org.apache.spark.rpc.RpcEnv.setupEndpointRef(RpcEnv.scala:109)
at org.apache.spark.deploy.worker.Worker$registerAllMasters$1.run(Worker.scala:253)
[root@itcast logs]# ping itcast
PING itcast (192.168.31.84)
