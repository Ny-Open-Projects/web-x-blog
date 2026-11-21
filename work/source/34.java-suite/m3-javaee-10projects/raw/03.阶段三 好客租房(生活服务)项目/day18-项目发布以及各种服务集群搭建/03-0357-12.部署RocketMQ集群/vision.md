# 画面线理解：12.部署RocketMQ集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\12.部署RocketMQ集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 02:36, 03:17, 04:57, 06:26, 07:03, 07:59, 08:48, 09:27, 10:27, 11:22, 12:15, 13:14, 14:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:53:50

1) 这一组画面整体在讲什么（一句话）：
部署 RocketMQ 集群，包括规划、创建 Docker 容器、配置 Broker 和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 文档中“2.4. 部署RocketMQ集群”的规划表，列出服务、端口、服务器和容器名。
画面 2: 在服务器 192.168.1.7 上，通过终端进入 logs 目录并删除旧日志文件。
画面 3: 显示 Typora 文档中创建 master 服务器的 Docker 命令。
画面 4: 显示 Typora 文档中创建第一个 master broker（rmqbroker01）的配置，包括 brokerId、brokerName、brokerIP1、brokerIP2、listenPort 等参数。
画面 5: 显示 Typora 文档中创建第二个 master broker（rmqbroker02）的配置，包括 brokerId、brokerName、brokerIP1、brokerIP2、listenPort 等参数。
画面 6: 显示 Typora 文档中创建第一个 master 服务器的 Docker 命令。
画面 7: 显示 Typora 文档中创建第一个 slave broker（rmqbroker03）的配置，包括 brokerId、brokerName、brokerIP1、brokerIP2、listenPort 等参数。
画面 8: 显示终端界面，准备执行命令。
画面 9: 显示 Typora 文档中创建第二个 slave broker（rmqbroker04）的配置，包括 brokerId、brokerName、brokerIP1、brokerIP2、listenPort 等参数。
画面 10: 在服务器 192.168.1.7 上，执行 docker create 命令创建 rmqserver02 容器，并启动 rmqserver01 和 rmqserver02。
画面 11: 在服务器 192.168.1.10 上，执行 docker create 命令创建 rmqbroker02 容器，并启动 rmqbroker01 和 rmqbroker02。
画面 12: 显示 RocketMQ 控制台日志，显示 broker01 和 broker02 已成功启动并加入集群。
画面 13: 显示终端界面，显示 broker02 的配置信息。
画面 14: 显示 Typora 文档中启动 slave broker 的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```bash
#创建第1个master
#nameserver1
docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver01/logs:/opt/logs \
-v /haoke/rmq/rmqserver01/store:/opt/store \
foxishwo/rocketmq:server-4.3.2

#nameserver2
docker create -p 9877:9877 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver02/logs:/opt/logs \
-v /haoke/rmq/rmqserver02/store:/opt/store \
foxishwo/rocketmq:server-4.3.2
```

画面 4:
```bash
#创建第1个master broker
#master broker01
docker create -net host --name rmqbroker01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker01/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker01/logs:/opt/logs \
-v /haoke/rmq/rmqbroker01/store:/opt/store \
foxishwo/rocketmq:broker-4.3.2

#配置
namesrvAddr=192.168.1.7:9876;192.168.1.7:9877
brokerClusterName=haokeCluster
brokerName=broker01
brokerId=0
fileReservedTime=48
brokerRole=SYNC_MASTER
flushDiskType=ASYNC_FLUSH
brokerIP1=192.168.1.19
brokerIP2=192.168.1.19
listenPort=10911
```

画面 5:
```bash
#创建第2个master broker
#master broker02
docker create -net host --name rmqbroker02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker02/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker02/logs:/opt/logs \
-v /haoke/rmq/rmqbroker02/store:/opt/store \
foxishwo/rocketmq:broker-4.3.2

#配置
namesrvAddr=192.168.1.7:9876;192.168.1.7:9877
brokerClusterName=haokeCluster
brokerName=broker02
brokerId=0
fileReservedTime=48
brokerRole=SYNC_MASTER
flushDiskType=ASYNC_FLUSH
brokerIP1=192.168.1.19
brokerIP2=192.168.1.19
listenPort=10911
```

画面 7:
```bash
#创建第1个slave broker
#slave broker01
docker create -net host --name rmqbroker03 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker03/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker03/logs:/opt/logs \
-v /haoke/rmq/rmqbroker03/store:/opt/store \
foxishwo/rocketmq:broker-4.3.2

#配置
namesrvAddr=192.168.1.7:9876;192.168.1.7:9877
brokerClusterName=haokeCluster
brokerName=broker01
brokerId=1
deleteWhen=04
fileReservedTime=48
brokerRole=SLAVE
flushDiskType=ASYNC_FLUSH
brokerIP1=192.168.1.18
brokerIP2=192.168.1.18
listenPort=10611
```

画面 9:
```bash
#创建第2个slave broker
#slave broker02
docker create -net host --name rmqbroker04 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker04/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker04/logs:/opt/logs \
-v /haoke/rmq/rmqbroker04/store:/opt/store \
foxishwo/rocketmq:broker-4.3.2

#配置
namesrvAddr=192.168.1.7:9876;192.168.1.7:9877
brokerClusterName=haokeCluster
brokerName=broker02
brokerId=1
deleteWhen=04
fileReservedTime=48
brokerRole=SLAVE
flushDiskType=ASYNC_FLUSH
brokerIP1=192.168.1.18
brokerIP2=192.168.1.18
listenPort=10611
```

画面 10:
```bash
root@itcast01:rmq# docker create -p 9877:9877 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver02/logs:/opt/logs \
-v /haoke/rmq/rmqserver0
