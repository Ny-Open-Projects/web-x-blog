# 画面线理解：07.RocketMQ集群之搭建2m2s集群（配置说明）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\07.RocketMQ集群之搭建2m2s集群（配置说明）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 01:12, 01:53, 02:33, 02:54, 03:15, 03:50, 08:42, 08:55, 09:56, 10:31, 10:33, 10:38, 10:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:15:06

1) 这一组画面整体在讲什么（一句话）：
通过 Docker 搭建 RocketMQ 的 2 主 2 从集群，包括创建服务器容器、主从 Broker 容器及启动命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示创建 master 服务器的 Docker 命令，包括端口映射、环境变量和镜像版本。
画面 2: 展示创建第二个 master 服务器的 Docker 命令，与画面 1 命令结构相同。
画面 3: 展示创建 master broker01 的 Docker 命令，包含挂载配置文件和日志目录。
画面 4: 展示一个简化的流程图，包含“Consumer”和“与客户端交互的端口”。
画面 5: 展示一个简化的流程图，包含“与本集群中其他节点交互的端口”。
画面 6: 展示创建 master broker01 的 Docker 命令，包含挂载配置文件和日志目录。
画面 7: 展示 master broker01 的配置信息，包括 brokerName、brokerId、brokerRole 等。
画面 8: 展示创建 master broker02 的 Docker 命令，包含挂载配置文件和日志目录。
画面 9: 展示 master broker02 的配置信息，包括 brokerName、brokerId、brokerRole 等。
画面 10: 展示创建 slave broker01 的 Docker 命令，包含挂载配置文件和日志目录。
画面 11: 展示创建 slave broker02 的 Docker 命令，包含挂载配置文件和日志目录。
画面 12: 展示启动所有容器的命令：docker start rmqserver01 rmqbroker02 rmqbroker03 rmqbroker04。
画面 13: 展示创建 slave broker01 的 Docker 命令，包含挂载配置文件和日志目录。
画面 14: 展示创建 slave broker01 的 Docker 命令，包含挂载配置文件和日志目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
#创建2master
#nameserver1
docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver01/logs:/opt/logs \
-v /haoke/rmq/rmqserver01/store:/opt/store \
foxisho/rocketmq:server-4.3.2

#nameserver2
docker create -p 9877:9876 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver02/logs:/opt/logs \
-v /haoke/rmq/rmqserver02/store:/opt/store \
foxisho/rocketmq:server-4.3.2
```

画面 3:
```bash
#创建第1个master broker
#master broker01
docker create --net host --name rmqbroker01 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/rmq/rmqbroker01/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker01/logs:/opt/logs \
-v /haoke/rmq/rmqbroker01/store:/opt/store \
foxisho/rocketmq:broker-4.3.2
```

画面 7:
```properties
namesrvAddr=172.16.55.185:9876;172.16.55.185:9877
brokerClusterName=ItcastCluster
brokerName=broker01
brokerId=0
deleteWhen=04
fileReservedTime=48
brokerRole=SYNC_MASTER
flushDiskType=ASYNC_FLUSH
brokerIP1=172.16.55.185
brokerIP2=172.16.55.185
listenPort=10911
```

画面 8:
```bash
#创建第2个master broker
#master broker02
docker create --net host --name rmqbroker02 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/rmq/rmqbroker02/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker02/logs:/opt/logs \
-v /haoke/rmq/rmqbroker02/store:/opt/store \
foxisho/rocketmq:broker-4.3.2
```

画面 9:
```properties
namesrvAddr=172.16.55.185:9876;172.16.55.185:9877
brokerClusterName=ItcastCluster
brokerName=broker02
brokerId=0
deleteWhen=04
fileReservedTime=48
brokerRole=SYNC_MASTER
flushDiskType=ASYNC_FLUSH
brokerIP1=172.16.55.185
brokerIP2=172.16.55.185
listenPort=10911
```

画面 10:
```bash
#创建第1个slave broker
#slave broker01
docker create --net host --name rmqbroker03 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/rmq/rmqbroker03/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker03/logs:/opt/logs \
-v /haoke/rmq/rmqbroker03/store:/opt/store \
foxisho/rocketmq:broker-4.3.2
```

画面 11:
```bash
#创建第2个slave broker
#slave broker02
docker create --net host --name rmqbroker04 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/rmq/rmqbroker04/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/rmq/rmqbroker04/logs:/opt/logs \
-v /haoke/rmq/rmqbroker04/store:/opt/store \
foxisho/rocketmq:broker-4.3.2
```

画面 12:
```bash
#启动容器
docker start rmqserver01 rmqbroker02 rmqbroker03 rmqbroker04
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: 展示一个简化的流程图，包含“Consumer”和“与客户端交互的端口”。
画面 5: 展示一个简化的流程图，包含“与本集群中其他节点交互的端口”。
画面 3: 展示一个架构图，包含“master broker01”、“broker (Master)”、“broker (Slave)”等节点，以及它们之间的连接关系。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
