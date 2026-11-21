---
title: "RocketMQ 控制台部署与收发消息功能验证"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, RocketMQ]
---

# RocketMQ 控制台部署与收发消息功能验证

NameServer 和 Broker 跑起来之后，RocketMQ 还差两步才算真正可用：一是让外部客户端能远程连上 Broker，二是装上 RocketMQ Console 控制台，把集群状态、Topic、消费进度这些信息放进可视化界面里管理。这一章完成收尾——配置远程连接、部署控制台、用官方工具脚本做一轮收发消息验证，最后把 mqadmin 的常用管理命令过一遍。

## 先给结论

- Broker 默认通过私有 IP 启动，外部客户端无法远程连接，必须在 broker.conf 里把 namesrvAddr 与 brokerIP1 绑定为对外可访问的 IP，多网卡机器要指定对外物理网卡的地址。
- 启动 Broker 时带上 autoCreateTopicEnable=true，Topic 不存在时自动创建；不加这个参数，发送端往不存在的 Topic 发消息可能直接报异常。
- 控制台 rocketmq-console-ng 是 Spring Boot 应用：Maven 打包出 jar，同目录放一个 application.properties 配好端口 9800 与 NameServer 地址，java -jar 即可启动。
- 控制台页面提示日期异常时，是虚拟机时间不对：用 NTP 同步阿里云时间并检查时区，重启控制台即恢复。
- 功能验证用官方 tools.sh 脚本跑通生产与消费：54 条消息发到 TopicTest 并全部消费，控制台上 Broker Offset 与 Consume Offset 指向最后一条。
- 排错要点：消息发送重试三次仍失败，基本是 Broker 对外 IP 配错；改完 broker.conf 重启时必须用 -c 指定配置文件路径，否则修改不生效。

## 远程连接配置：让外部客户端连上 Broker

RocketMQ 的 Broker 默认通过私有 IP 启动，外部客户端没有办法远程连接，所以要先修改配置文件，绑定能够对外访问的 IP 地址。上一章安装配置时已经采用了对外 IP；如果机器有多块网卡，这里必须指定能够对外访问的物理网卡对应的地址。broker.conf 中的两个关键项：

```properties
namesrvAddr=10.10.20.251:9876
brokerIP1=10.10.20.251
```

另外一个实用参数是 autoCreateTopicEnable：启动 Broker 时在命令行加上，或者在配置文件中配置都可以。它的作用是 Topic 不存在时自动创建；不加的话，消费端或发送端往不存在的 Topic 发送消息，可能就会报异常。完整启动命令：

```bash
sh bin/mqbroker -n 127.0.0.1:9876 autoCreateTopicEnable=true -c /usr/local/rocketmq_4.4.0/conf/broker.conf &
```

## 部署 RocketMQ Console 控制台

控制台是 Web 管理界面，能帮助维护和管理 RocketMQ 服务。Rocket Console 的源码在 GitHub 上，下载到本地后要用 Maven 打包编译，打包成功后会在 target 目录下生成一个可执行 jar，这就是控制台本体。整个编译打包需要较长时间，课程直接使用已经编译完成的 jar 包，上传到虚拟机进行配置和运行。

部署步骤很轻：解压安装包，新建一个 rocketmq-console 目录把 jar 放进去，便于管理。它本质是一个 Spring Boot 应用，只需要新建一个 application.properties 配置文件和 jar 包放在同一目录，配置信息只改两项——运行端口和 NameServer 的 IP 信息：

```properties
server.port=9800
rocketmq.config.namesrvAddr=127.0.0.1:9876
```

NameServer 就在本机，所以地址写 127.0.0.1。启动与验证：

```bash
nohup java -jar rocketmq-console-ng-1.0.0.jar > /dev/null 2>&1 &
ps -ef | grep console        # 确认进程已启动
```

浏览器直接访问虚拟机 IP 加端口（http://10.10.20.251:9800/#/），就进入了控制后台。首次访问页面提示日期存在问题——虚拟机时间不对。通过 NTP 命令同步虚拟机时间、指向阿里云的地址，重启控制台进程后再次访问，提示消失。之后测试再遇到这种情况，先检查时间日期是否正确，同时检查时区设置，确保与系统时间一致即可。

控制台里值得关注的功能：仪表盘对整个 RocketMQ 机器做整体监控，包括 Broker 信息等使用情况；Cluster 页面监控集群信息；Topic 页面可以做日常维护——删除某个 Topic、重置消费位点（即消费进度）、查看 Topic 当前运行状态，都有详细记录；此外还有 Consumer 消费信息、Producer 生产者信息、Message 消息管理。

## 收发消息验证与 mqadmin 管理命令

### 生产消费全链路验证

先在虚拟机指定好环境变量，也就是配置 NameServer 的地址，因为接下来的测试要用官方工具脚本：

```bash
export NAMESRV_ADDR=localhost:9876
```

生产者测试——在 RocketMQ 运行目录下执行，脚本会生产一批消息，Topic 名称是 TopicTest：

```bash
sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer
```

打开控制台查看 TopicTest 的状态：最大消息数是 54，说明刚才这个脚本已经发送了 54 条消息。再用消费者消费：

```bash
sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer
```

消费者拿到了对应的消息并逐条打印。回到控制台看这个 Topic 的消费情况：Broker Offset 与 Consume Offset 都已消费完成，消费进度指向了最后一条消息——收发链路全部验证通过。

### mqadmin 常用命令

bin 目录下的 mqadmin 脚本负责日常运维查询，课程演示了五个高频命令（单节点环境下 clusterList 只展示当前节点的 IP、端口与版本信息）：

```bash
./mqadmin clusterList -n 127.0.0.1:9876                          # 查看集群情况
./mqadmin brokerStatus -n 127.0.0.1:9876 -b 127.0.0.1:10911      # Broker 状态：版本、提交日志、message 等
./mqadmin topicList -n 127.0.0.1:9876                            # 列出 MQ 中所有主题
./mqadmin topicStatus -n 127.0.0.1:9876 -t TopicTest             # Topic 状态：消费进度、maxOffset、最后发送更新时间
./mqadmin topicRoute -n 127.0.0.1:9876 -t TopicTest              # 路由信息：打印 Broker 连接地址
```

topicRoute 的输出会把 Broker 的连接信息打印出来；如果是多节点或集群，这里会显示多个 Broker 的地址信息。

### FAQ：发送重试三次仍失败

配置运行过程中如果遇到这样的报错——`Send [3] times, still failed, cost [575]ms, Topic: ..., BrokersSent: [broker-a, broker-a, broker-a]`——意思是消息重试了三次仍然失败，报错里带着耗费的时间、出问题的主题名称和 Broker 运行情况。根因通常是 Broker 的对外连接 IP 配置不对：在 broker.conf 里把 brokerIP1 改成对外能够访问的 IP；改完之后重启 Broker 时要用 -c 参数指定配置文件路径，否则启动脚本找不到修改过的配置，属性改了也不生效。

## 小结

至此 RocketMQ 单机环境全部就绪：远程连接靠 broker.conf 里的对外 IP 与 autoCreateTopicEnable，管理靠 rocketmq-console-ng 这个 Spring Boot 控制台（9800 端口、指定 NameServer 地址、注意时间同步），收发验证用 tools.sh 官方脚本跑通生产与消费，日常运维依赖 mqadmin 的五个查询命令。收尾补一个认知点：RocketMQ 是性能优秀的开源消息队列，单机吞吐量虽不及 Kafka，但 Topic 数量增加时不会产生线性衰减——Kafka 会随 Topic 增多出现性能线性衰减——正是这个特性让 RocketMQ 可以通过集群扩展提升整体吞吐能力。集群安装后面会做专题讲解，先把单节点安装配置、控制台管理与常用命令掌握扎实，后续项目业务功能开发就能直接运用。
