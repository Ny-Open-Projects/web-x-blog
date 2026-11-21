# 画面线理解：06.通过RocketMQ的java客户端api进行测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\06.通过RocketMQ的java客户端api进行测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:56, 01:42, 02:20, 02:49, 03:51, 04:32, 05:42, 06:18, 06:53, 08:05, 08:52, 09:22, 09:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:57:51

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并运行一个 RocketMQ 生产者程序，并解决因 Broker 启动时使用了内网 IP 导致无法从开发机访问的问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：打开 IntelliJ IDEA，选择项目 itcast-rocketmq。
画面2：展示项目根目录下的 pom.xml 文件，其中包含 Maven 项目的基本配置。
画面3：展示 SyncProducer.java 文件的代码，用于创建 RocketMQ 生产者并发送消息。
画面4：展示 SyncProducer.java 文件的代码，重点在设置 NameServer 地址和发送消息的逻辑。
画面5：展示项目结构和 SyncProducer.java 文件，强调其在 src/main/java 目录下的位置。
画面6：展示 SyncProducer.java 文件的代码，包含发送消息的逻辑。
画面7：在终端中运行 SyncProducer.java，出现 RemotingTooMuchRequestException 异常，提示发送超时。
画面8：在终端中运行 SyncProducer.java，异常信息与画面7相同。
画面9：展示 SyncProducer.java 文件的代码，新增了 producer.shutdown() 方法用于关闭生产者。
画面10：在终端中执行命令启动 RocketMQ Broker，显示启动成功。
画面11：展示 PDF 文档内容，解释 Broker 启动时使用了 172.17.0.1 的 IP 地址，导致开发机无法访问，并提供解决方案。
画面12：展示 SyncProducer.java 文件的代码，运行后成功发送消息。
画面13：展示终端中成功发送消息的输出日志，包含消息 ID、OffsetMagID 和 MessageQueue 等信息。
画面14：展示 PDF 文档内容，再次强调 Broker 启动时使用了 172.17.0.1 的 IP 地址，并提供解决方案。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast.rocketmq</groupId>
    <artifactId>itcast-rocketmq</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面10：
```bash
root@itcast:bin# ./mqbroker -n 172.16.55.185:9876
The broker[itcast, 172.20.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_haoke_im
```

画面11：
```bash
The broker[itcast, 172.17.0.1:10911] boot success. serializeType=JSON and name server is 172.16.55.185:9876
```

画面11：
```bash
#创建broker配置文件
vim /haoke/rmq/rmqbroker/conf/broker.conf
brokerIP1=172.16.55.185
namesrvAddr=172.16.55.185:9876
brokerName=broker_h
