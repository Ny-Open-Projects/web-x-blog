# 画面线理解：08.RocketMQ集群之搭建2m2s集群（操作）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\08.RocketMQ集群之搭建2m2s集群（操作）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 01:19, 01:58, 02:41, 03:34, 04:00, 04:35, 05:10, 05:57, 06:31, 07:39, 08:25, 09:18, 10:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:15:48

1) 这一组画面整体在讲如何使用 Docker 搭建 RocketMQ 的多 Broker 集群，并编写 Java 代码进行消息生产和消费测试。

2) 按时间顺序列出每张画面的要点：
画面1：EditPlus 编辑器打开，空白，准备编写或查看配置文件。
画面2：远程终端连接到服务器 172.16.55.185，准备执行命令。
画面3：在终端中执行 docker create 命令，创建名为 rmqserver01 的容器，配置了端口映射、环境变量和挂载目录。
画面4：EditPlus 中显示了创建 rmqserver01 和 rmqserver02 容器的完整 Docker 命令。
画面5：终端界面空白，准备执行下一步命令。
画面6：EditPlus 中高亮显示了创建 rmqbroker02 容器的 Docker 命令，用于配置 broker。
画面7：终端中显示了 RocketMQ 集群的配置信息，包括 brokerId、namesrvAddr、deleteWhen 等参数。
画面8：EditPlus 中高亮显示了创建 rmqbroker03 容器的 Docker 命令。
画面9：终端中执行了创建 rmqbroker03 容器的命令，并创建了配置文件目录。
画面10：浏览器打开 Google 搜索页，可能用于查找资料或准备下一步操作。
画面11：RocketMQ 控制台页面，显示了 broker01 的配置信息，包括 maxHashSlotNum、transactionTimeOut 等参数。
画面12：IntelliJ IDEA 中显示了 Java 代码，用于创建生产者并发送消息到 topic "my-test-topic"。
画面13：IntelliJ IDEA 中显示了 Java 代码，用于创建消费者并接收消息。
画面14：Adobe Reader 中显示了 PDF 文档，标题为“2.2、搭建2m2s集群”，并展示了创建 2m2s 集群的 Docker 命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver01/logs:/opt/logs \
-v /haoke/mq/rmqserver01/store:/opt/store \
foxiswho/rocketmq:server-4.3.2

画面4：
docker create -p 9877:9876 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver02/logs:/opt/logs \
-v /haoke/mq/rmqserver02/store:/opt/store \
foxiswho/rocketmq:server-4.3.2

docker create --net host --name rmqbroker01 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker01/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/mq/rmqbroker01/logs:/opt/logs \
-v /haoke/mq/rmqbroker01/store:/opt/store \
foxiswho/rocketmq:broker-4.3.2

画面6：
docker create --net host --name rmqbroker02 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker02/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/mq/rmqbroker02/logs:/opt/logs \
-v /haoke/mq/rmqbroker02/store:/opt/store \
foxiswho/rocketmq:broker-4.3.2

画面8：
docker create --net host --name rmqbroker03 \
-e "JAVA_OPTS=-Duser.home=/opt" \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-v /haoke/mq/rmqbroker03/conf/broker.conf:/etc/rocketmq/broker.conf \
-v /haoke/mq/rmqbroker03/logs:/opt/logs \
-v /haoke/mq/rmqbroker03/store:/opt/store \
foxiswho/rocketmq:broker-4.3.2

画面12：
DefaultMQProducer producer = new DefaultMQProducer(producerGroup: "haoke");
producer.setNamesrvAddr("172.16.55.185:9876;172.16.55.185:9877");
producer.start();

//发送消息
String msg = "我的第一个消息61!";
Message message = new Message(topic: "my-test-topic", tags: "delete", msg.getBytes(charset: "UTF-8"));
SendResult sendResult = producer.send(message);
System.out.println("消息id：" + sendResult.getMsgId());
System.out.println("消息队列：" + sendResult.getQueueOffset());
System.out.println(sendResult);

画面13：
#创建2m2s集群
docker create -p 9876:9876 --name rmqserver01 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver01/logs:/opt/logs \
-v /haoke/mq/rmqserver01/store:/opt/store \
foxiswho/rocketmq:server-4.3.2

#nameserver2
docker create -p 9877:9876 --name rmqserver02 \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/mq/rmqserver02/logs:/opt/logs \
-v /haoke/mq/rmqserver02/store:/opt/store \
foxiswho/rocketmq:server-4.3.2

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PDF 文档标题为“2.2、搭建2m2s集群”，内容包含创建 2m2s 集群的 Docker 命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
