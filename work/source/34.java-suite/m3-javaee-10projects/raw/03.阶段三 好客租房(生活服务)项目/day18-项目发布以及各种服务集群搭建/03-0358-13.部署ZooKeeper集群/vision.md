# 画面线理解：13.部署ZooKeeper集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\13.部署ZooKeeper集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:32, 02:41, 03:00, 03:08, 03:16, 03:28, 03:34, 03:44, 03:52, 03:59, 04:14, 04:23, 05:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:54:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在三台服务器上使用 Docker 部署一个 ZooKeeper 集群，并通过 ZoolInspector 工具验证其状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“2.5.5 搭建ZK集群”的规划部分，包含一个表格，列出了三个服务（zk01, zk02, zk03）的端口（2181, 2888, 3888）、服务器IP（192.168.1.7, 192.168.1.18, 192.168.1.19）和容器名（zk01, zk02, zk03）。
画面2：显示在服务器 192.168.1.7 上的终端，提示符为 root@itcast01:~#，准备执行命令。
画面3：在服务器 192.168.1.7 的终端中执行了创建 zk01 容器的命令，命令为：docker create --name zk01 --net host -e ZOO_MY_ID=1 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4。
画面4：展示 Typora 文档中“2.5.2. 实施”部分，包含创建 zk01、zk02、zk03 容器的 Docker 命令，以及启动容器的命令。
画面5：与画面4内容相同，为文档的截图。
画面6：展示服务器 192.168.1.18 上的桌面，显示了多个应用程序图标，包括 Typora、Xshell、Chrome、Notepad++ 等，用于后续操作。
画面7：在服务器 192.168.1.7 的终端中，显示了 ZooKeeper 启动时的错误日志，提示无法连接到 192.168.1.19:2888。
画面8：在服务器 192.168.1.18 的终端中执行了创建 zk03 容器的命令，命令为：docker create --name zk03 --net host -e ZOO_MY_ID=3 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4。
画面9：在服务器 192.168.1.18 的终端中，显示了 zk02 容器启动后的日志，表明 zk02 成功启动并加入集群。
画面10：在服务器 192.168.1.7 的终端中，显示了 zk01 容器启动后的日志，表明 zk01 成功启动并加入集群。
画面11：在服务器 192.168.1.7 的终端中，显示了 zk01 容器启动后的日志，表明 zk01 成功启动并加入集群。
画面12：在服务器 192.168.1.7 的终端中，显示了 zk01 容器启动后的日志，表明 zk01 成功启动并加入集群。
画面13：在服务器 192.168.1.7 的终端中，显示了 zk01 容器启动后的日志，表明 zk01 成功启动并加入集群。
画面14：展示 Typora 文档中“2.5.2. 实施”部分，包含创建 zk01、zk02、zk03 容器的 Docker 命令，以及启动容器的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
服务	端口	服务器	容器名
zk01	2181, 2888, 3888	192.168.1.7	zk01
zk02	2181, 2888, 3888	192.168.1.18	zk02
zk03	2181, 2888, 3888	192.168.1.19	zk03
```
画面4：
```
#拉取zk镜像
docker pull zookeeper:3.4

#创建容器
docker create --name zk01 --net host -e ZOO_MY_ID=1 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

docker create --name zk02 --net host -e ZOO_MY_ID=2 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

docker create --name zk03 --net host -e ZOO_MY_ID=3 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

#启动容器
docker start zk01 && docker logs -f zk01
docker start zk02 && docker logs -f zk02
docker start zk03 && docker logs -f zk03
```
画面7：
```
2019-02-28 13:47:09,582 [myid:1] - INFO  [QuorumPeer$QuorumServer@184] - Resolved hostname: 192.168.1.18 to address: /192.168.1.18
2019-02-28 13:47:09,582 [myid:1] - WARN  [QuorumCnxManager@554] - Cannot open channel to 3 at election address /192.168.1.19:3888
java.net.ConnectException: Connection refused (Connection refused)
at java.net.AbstractPlainSocketImpl.socketConnect(Native Method)
at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:350)
at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:206)
at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:188)
at java.net.Socket.connect(Socket.java:589)
at org.apache.zookeeper.server.quorum.QuorumCnxManager.connectOne(QuorumCnxManager.java:558)
at org.apache.zookeeper.server.quorum.QuorumCnxManager.lookForLeader(FastLeaderElection.java:610)
at org.apache.zookeeper.server.quorum.QuorumPeer.run(QuorumPeer.java:957)
2019-02-28 13:47:09,582 [myid:1] - INFO  [QuorumPeer$QuorumServer@184] - Resolved hostname: 192.168.1.19 to address: /192.168.1.19
2019-02-28 13:47:09,582 [myid:1] - WARN  [QuorumCnxManager@554] - Cannot open channel to 3 at election address /192.168.1.19:3888
java.net.ConnectException: Connection refused (Connection refused)
at java.net.AbstractPlainSocketImpl.socketConnect
