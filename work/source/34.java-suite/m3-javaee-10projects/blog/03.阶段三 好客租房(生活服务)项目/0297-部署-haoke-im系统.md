# haoke-im 上线：打包、外置配置与双客户端联调

即时通讯服务与前面两个 dubbo 服务气质完全不同：它不开 dubbo 协议，靠 WebSocket 长连接与客户端对话；它的健康与否，不是看注册中心里有没有名字，而是看两个在线用户之间一句话能不能准时送达。部署 haoke-im 的套路与 haoke-manage 一脉相承，打包插件、`mvn install`、`java -jar` 一套动作重复一遍，差别在配置项、部署位与验证手段上。

## 先给结论

- 打包插件与前两课同构，唯一的差别是 `mainClass` 要换成 haoke-im 自己的启动类全限定名。
- 外置配置三处关键：服务端口 18081，MongoDB 暂连 192.168.1.7 单节点，RocketMQ 的 NameServer 指向集群两个地址 `9876` 与 `9877`。
- 部署节奏是先在 1.7 上打包试跑，验证逻辑没问题后再 `scp` 把 jar 搬到正式部署位 192.168.1.19，两台机器目录结构保持一致。
- 验证靠 WebSocket 客户端：两个连接分别以 1001、1002 身份接入，互发 `toId` 加 `msg` 的 JSON，双向可达即部署成功。
- 长连接服务上线后用 `&` 挂后台，别让 SSH 会话替你托管进程。

## 部署位与启动类：插件照抄，路径要换

按域名规划，haoke-im 对应 `im.haoke.com`，正式部署位是 192.168.1.19；打包环节沿用 1.7 这台已经装好 Maven 的机器。pom 里的打包插件直接从房源服务那篇拷过来，改一处即可：

```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <!-- 指向 haoke-im 自己的启动类全限定名（类名为按本课写法补全的示例） -->
        <mainClass>com.haoke.im.ImApplication</mainClass>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

改插件时最容易犯的错是只换了包名却漏了结构：`mainClass` 必须嵌在 `<configuration>` 里，`repackage` 的执行声明必须嵌在 `<executions>` 里，复制粘贴时层级错一位，插件就不生效，打出来的还是跑不了的普通 jar。

## 外置配置：端口、MongoDB 与 RocketMQ 集群

IM 服务自己长连接扛服务、消息落 MongoDB、跨节点通信靠 RocketMQ，配置按生产环境逐项对齐：

```properties
# Spring boot application
spring.application.name = haoke-im
server.port = 18081

# MongoDB：单节点先跑起来，集群化在后续课程
spring.data.mongodb.uri = mongodb://192.168.1.7:27017/testdb

# RocketMQ：指向集群的两个 NameServer，分号分隔
rocketmq.name-server = 192.168.1.7:9876;192.168.1.7:9877
# 生产者分组
rocketmq.producer.group = haoke-im-websocket-group
```

NameServer 写两个地址是这轮改动里唯一与集群部署强相关的调整：两个 NameServer 都在 1.7 上，分别占 9876 与 9877，客户端拿到地址列表后会择一连入，一个挂了换另一个，路由服务永远有备份。NameServer 本身不存消息数据，broker 的拓扑靠 broker 主动上报，所以这里不需要写 broker 的任何地址。另外提示一点：画面里的配置键还是旧前缀 `spring.rocketmq.nameServer`，那是当年整合包未进官方仓库时的自定义键，官方 starter 发布后统一用 `rocketmq.name-server`，语义相同。

## 打包与跨机分发：先试跑，再搬迁

流程与 haoke-manage 的打包完全一致，源码压缩上传、解压、整体安装、拷 jar：

```bash
# 开发机把源码打成 zip，上传到 192.168.1.7:/haoke/publish
cd /haoke/publish
unzip haoke-im.zip
cd haoke-im
mvn install -Dmaven.test.skip=true

# 产物拷到发布目录并启动
cp target/haoke-im-1.0-SNAPSHOT.jar /haoke/publish/haoke/
cd /haoke/publish/haoke
java -jar haoke-im-1.0-SNAPSHOT.jar &
```

启动日志没有报错，服务就先在 1.7 上跑通了一轮逻辑验证。真正要部署的位置是 1.19，跨机搬运用 `scp`：

```bash
# 1.19 上先建出与 1.7 一致的目录结构
ssh 192.168.1.19 "mkdir -p /haoke/publish/haoke"

# 跨机拷贝 jar，scp 走 ssh 协议，需要输入 1.19 的密码
scp haoke-im-1.0-SNAPSHOT.jar 192.168.1.19:/haoke/publish/haoke/

# 登录 1.19 启动
ssh 192.168.1.19
cd /haoke/publish/haoke
java -jar haoke-im-1.0-SNAPSHOT.jar &
```

先试跑再搬迁有个好处：逻辑错误在打包机上就能暴露，等搬过去才发现问题，每次调试都要多走一遍拷贝。目录结构在两台机器上保持一致同样不是为了好看，路径统一后，启动命令、日志排查、后续的脚本化运维都是同一套写法，不用记两份。整条链路画出来：

```mermaid
flowchart LR
    A["开发机源码"] -->|"zip 上传"| B["1.7 解压"]
    B --> C["mvn install 打包"]
    C --> D["1.7 试跑 18081"]
    D -->|"验证通过"| E["scp 到 1.19 同目录"]
    E --> F["1.19 正式启动"]
    F --> G["双客户端联调"]
```

## 双客户端联调：一句话送进对面窗口

WebSocket 服务不能拿 curl 或浏览器地址栏测，协议都不对。用浏览器里的 WebSocket 客户端工具开两个窗口，分别建立连接，地址形如 `ws://192.168.1.19:18081/1001` 与 `ws://192.168.1.19:18081/1002`（地址尾段即用户 id，握手拦截器按它识别身份，此写法按本课测试方式整理）：

```json
{"toId": 1002, "msg": "你好"}
```

1001 的窗口发出这条 JSON，1002 的窗口立刻收到「你好」；把两个 id 反过来，1002 发一条「您也好」，1001 同样秒收。双向可达，部署成立。

这条消息在服务端走过的路值得拆开看。`MessageHandler` 收到报文后解析出 `toId` 与 `msg`，先落 MongoDB，历史消息与已读状态因此有了着落；接收方在线就当场推送。跨节点场景靠 RocketMQ 收口：本节点查不到目标用户的会话，就把消息发布到 `haoke-im-send-message-topic` 主题，各节点以广播模式消费，谁的本地握着目标用户的连接谁负责送达。两个 NameServer 在这里的价值就是让这条路由链不因单个注册服务故障而中断。

验证完把进程留在后台：启动命令带上 `&`，Ctrl C 结束的只是前台查看，服务继续运行，`jps -l` 随时可查。至此三大件里最后一个应用也上线了，后台服务、接口门面、即时通讯全部就位，剩下的域名与前端交给 Nginx 统一收口。

## 常见误区

- **拿 HTTP 工具测 WebSocket 服务。** `curl` 与浏览器地址栏走的是 HTTP，WebSocket 握手与帧协议都不是它俩能完成的，测试必须用 WebSocket 客户端，看到连接状态变为已连接才有意义。
- **1.19 上不建目录直接 scp。** scp 不会替你创建目标路径，目录不存在就报错；或者建出来的结构与 1.7 不一致，后续按路径写的启动脚本、日志位置全部对不上。先建同构目录，再拷贝。
- **NameServer 还指着单机或写错端口。** 单机地址一旦出现故障，跨节点的消息就发不出去，表象是同节点能聊、跨节点丢消息，排查方向在 RocketMQ 的发送端报错里。
- **前台启动占住会话。** 没加 `&` 的服务跟着 SSH 会话共存亡，断线即停。长连接服务尤其注意：会话断了，所有在线用户的连接跟着断。

## 面试可能被问到的问题

1. 面试官追问：「长连接服务的部署验证与普通 REST 服务有什么不同？」
   答：REST 服务验证一条请求的往返即可，WebSocket 服务要验证连接建立、身份识别、消息双向送达三个环节，至少两个客户端互发才能证明收发链路都通。此外还要关注连接保持，会话断开、进程退出都会直接影响在线用户。

2. 面试官追问：「分布式 WebSocket 为什么要引入 RocketMQ？」
   答：用户连接落在哪个节点由负载决定，本地查不到目标会话时，需要一个所有节点都可达的通道转发消息。RocketMQ 以广播模式让每个节点都收到副本，持有目标连接的节点负责推送，其余忽略。它是节点间的消息总线，替代不了本地推送。

3. 面试官追问：「NameServer 配了两个地址，客户端是怎么用的？」
   答：客户端把地址列表拿来做容错选择，连不上一个就换下一个，定期更新路由信息。NameServer 无状态、实例间不同步，任何一个存活都能提供全量路由，所以两个地址已经能挡住单点故障，配置顺序无关紧要。

4. 面试官追问：「scp 和 cp 的区别是什么？还有哪些跨机拷贝方式？」
   答：cp 在本机文件系统内复制，scp 基于 ssh 协议在主机间复制并自带传输加密。同类工具还有 rsync（支持增量同步，大文件与目录重复同步更省流量）、sftp，或者先用压缩包再传输。生产环境批量分发常用配置管理工具统一拉取。

5. 面试官追问：「IM 消息为什么先落库再推送，而不是直接推？」
   答：直接推只服务在线场景，推送失败或用户不在线消息就丢了。先落 MongoDB 让每条消息都有持久化归属，历史消息查询、已读未读状态都依赖它；推送只是落库之后的投递动作，失败可以靠拉取补偿。存储与投递分离，可靠性才有着落。

## 配套资料

- 本教学日无源码包：`materials/code/03/day18-项目发布以及各种服务集群搭建/` 下仅有解压清单 `_extracted.json`（解压文件数为 1，内容为房源抓取测试数据 `data.json`）。
- 端口、MongoDB 与 RocketMQ 配置抄录自本课画面线，地址按 `0293-部署RocketMQ集群.md` 的集群部署更新为两个 NameServer；配置键名沿用 `0181-实现分布式WebSocket之具体实现(发送消息).md` 的官方 starter 写法。
- 启动类 `ImApplication`、WebSocket 客户端地址与测试报文为按本课写法补全的示例；测试所用客户端为浏览器 WebSocket 插件，不随资料包提供。
- haoke-im 工程的分布式实现与广播消费细节见 `0180-实现分布式WebSocket之回顾实现方案.md` 与 `0181-实现分布式WebSocket之具体实现(发送消息).md`。
