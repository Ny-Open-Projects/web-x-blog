# 画面线理解：16.部署-haoke-im系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\16.部署itcast-haoke-im系统【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:32, 01:18, 02:11, 02:48, 03:25, 03:46, 04:10, 04:55, 06:27, 06:51, 07:53, 08:38, 09:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:57:17

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 RocketMQ 集群，并通过 Spring Boot 应用连接 RocketMQ 发送和接收 WebSocket 消息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Typora 中的 RocketMQ 配置文件内容，包含 Docker 启动命令和 broker 配置。
画面 2: 显示 IntelliJ IDEA 中的 Maven 插件配置，用于 Spring Boot 项目。
画面 3: 显示 application.properties 文件中的 Spring Boot 配置，包含 MongoDB 和 RocketMQ 的连接信息。
画面 4: 黑马程序员和博学谷的课程平台启动画面。
画面 5: 在远程服务器终端中执行 mvn install 命令，生成项目 jar 包。
画面 6: 在终端中执行命令，启动 Dubbo 服务并关闭 ZooKeeper 会话。
画面 7: 在终端中执行命令，启动 ZooKeeper 客户端并连接到服务器。
画面 8: 在终端中执行命令，启动 Spring Boot 应用。
画面 9: 在浏览器中打开 Simple WebSocket Client，准备发送消息。
画面 10: 在 Simple WebSocket Client 中发送 JSON 消息，接收服务器返回的响应。
画面 11: 在终端中执行命令，复制生成的 jar 包到指定目录。
画面 12: 在终端中执行命令，启动 RocketMQ 的管理服务。
画面 13: 在 Simple WebSocket Client 中再次发送消息，接收服务器返回的响应。
画面 14: 显示 Typora 中的 Maven 构建命令和 Ant Design Pro 项目结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
# 部署2个master broker
# master broker01
docker create --net host --name rmqbroker01 \
  -e "JAVA_OPTS=-server -Xms128m -Xmx128m -Xmn128m" \
  -v /opt/rmq/rmqbroker01/config/broker.conf:/etc/rocketmq/broker.conf \
  -v /opt/rmq/rmqbroker01/store:/opt/store \
  foxswh/rocketmq-broker:4.3.2

# master broker02
nanoserverAddr=192.168.1.7:9876;192.168.1.7:9877
brokerClusterName=haokecluster
brokerName=broker02
brokerId=0
deleteWhen=04
fileReservedTime=48
brokerRole=ASYNC_MASTER
flushDiskType=ASYNC_FLUSH
```

画面 2:
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <!-- 替换成实际的完整路径 -->
    <mainClass>cn.itcast.haoke.dubbo.server.DubboProvider</mainClass>
    <configuration>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </configuration>
</plugin>
```

画面 3:
```properties
# Spring boot application
spring.application.name = itcast-haoke-im
server.port = 18081

spring.data.mongodb.uri=mongodb://192.168.1.7:27017/testdb
spring.rocketmq.nameServer=192.168.1.7:9874
spring.rocketmq.producer.group=haoke-websocket-group
```

画面 5:
```bash
root@itcast01:publish# ll
total 636
drwxr-xr-x 5 root root 4096 Feb 18 22:45 ./
drwxr-xr-x 2 root root 4096 Feb 28 22:24 192.168.1.7
drwxr-xr-x 2 root root 4096 Feb 28 22:28 haoke/
drwxr-xr-x 2 root root 4096 Feb 28 22:28 itcast-haoke-im/
drwxr-xr-x 7 root root 4096 Feb 25 17:00 itcast-haoke-manage/
-rw-r--r-- 1 root root 522574 Feb 22 14:00 itcast-haoke-manage.zip
root@itcast01:itcast-haoke-im# cd target
root@itcast01:target# ll
total 32
drwxr-xr-x 6 root root 4096 Feb 28 23:00 ./
drwxr-xr-x 3 root root 4096 Feb 28 22:58 ../
drwxr-xr-x 3 root root 4096 Feb 28 22:58 git/
drwxr-xr-x 3 root root 4096 Feb 28 22:58 .gitignore
drwxr-xr-x 4 root root 4096 Feb 28 22:58 pom.xml
drwxr-xr-x 6 root root 4096 Feb 28 22:58 src/
drwxr-xr-x 6 root root 4096 Feb 28 22:58 target/
```

画面 6:
```bash
d after connection closed.). Possibly consider using a shorter maxLifetime value.
[2019-02-28 23:05:51.656] INFO 12903 --- [ Thread-5] o.s.s.concurrent.ThreadPoolTaskExecutor : Shutting down ExecutorService applicationTaskExecutor
2019-02-28 23:05:52.772 INFO 12903 --- [ bboShutdownHook] org.apache.zookeeper.ClientCnxn : EventThread shut down for session: 0x10002cfa3490002
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="
