# 16.部署-haoke-im系统

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\16.部署itcast-haoke-im系统【海量资源尽在 ubkz.com】.mp4
- 时长 9分22秒（音频 562s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来把我们的im这个系统呢去部署到我们的这个生产环境那我们来看一下im系统呢我们计划呢是把它部署到我们的这个19服务器但是呢我们还是选择在17上面去做一个打包那么我们首先呢找到我们这个项目然后呢给他去添加一些我们的插件那么我们去添加一个我们这个打包的这个插件啊把这个plugin我们拷贝过来
[00:29] 然后呢拷贝到下面这个位置OK好那么要注意的是这个路径呢要改成我们具体的这个im的这个启动类的这样的一个路径那么拷贝一下那么找到它然后呢我们去做一个处理到这OK好那么下面呢我们来检查一下它的一些这个配置那么我们可以看到它的端口呢是18081啊以及呢我们可以看到呢它的这个
[00:58] 连接到mongodb这样的一个地址是不变的那么下面是rock.mq那么这个显然是稍微一点变化就是我们部署了rock.mq的一个集群那么我可以看到这个集群是在这个位置对吧那么我们可以拷贝一下这个配置那么这个配置其实就是我们去指定了name server的这个节点因为我们有两个所以我们指定一个是9876一个是9877来做这样的一个配置
[01:26] 好那么现在呢我们是不是就可以去把这个项目的源码上传到我们的1.7这个服务器上面去做一个打包操作了对吧好那我们来找一下那我们找到这个code下面呢有一个idcast的号客然后呢有一个这个im的这个包然后呢我们去打一个这个zip包然后呢这个zip包呢打好之后啊那我们就可以去做一个上传了
[01:51] 那么上传到哪里呢上传到我们的浩克下面呢有一个叫做publish这个下面ok那么我们就pwd一下吧然后呢我们去把这个路径的拷贝一下拷贝之后呢就丢到这个里面来然后呢我们看一下啊这个路径拷到这然后呢我们就把这个我们刚刚打好包的这个这个的包呢就上传到我们的这个位置来
[02:18] 那么等待它的一个上传那么上传之后呢我们去做一个解压解压之后呢就可以去做一个具体的一个install了啊好那么来看一下那么来一个unzip嗯zip去做一个解压这个im啊im这个压缩包那么解压之后呢就会得到这样的一个im的一个目录然后呢我们去做一个打包这个打包呢依然还是有刚刚的我们这个
[02:45] 命令就去做一个manual install啊就可以了好那么我们把它呢去做一个manual install那么等待它的一个安装啊就可以了好那么现在呢它就已经呢就构建好了那么下面呢我们还同样的还是去呃进入到啊呃进入到我们这个呃目录下面然后呢我们找到target目录然后这个下面呢会有一个这个加包那么同样的把它拷贝走拷贝到哪里呢跟目录下面
[03:14] 好客下面有个publish然后呢有个好客这个目录那么我们进入到刚刚这个里面当然了这个如果我们刚刚把它擦掉的话那么它肯定就结束掉了对吧那我们最好呢是去给它后面去来一个什么的按的符号这样的话呢就没有问题了好那它在保持在后台运行就OK那么接下来呢我们还是去回到我们刚刚的这个拷贝这个目录中
[03:42] 然后我们把这个IM这个项目也跑起来那我们进行做一个测试OK好那么我们来查看一下那么这个下面的显然是有我们这个项目对吧那我们去执行一下那么稍微等待一下等待他这个把日志刷完然后我们去执行一下就是加了-加然后呢叫ITcastIM这样的一个这个包我们去执行一下看一下效果
[04:12] 我们看它启动会不会报错如果没有报错的话那就说明我们是这个是OK的如果报错的话肯定就有问题那么到目前为止已经就跑起来了那我们可以来测试一下那么怎么测呢就是我们需要通过客户端工具去做一个连接OK好那么接下来呢我们来测试一下看它怎么测呢那么我们需要去进入到的是我们的这个工具之前这个工具我们装过就是
[04:39] 有一个这个simple的这个工具那么我们去尝试连接一下那么它呢是192.168.1.7然后呢冒号端口呢是端口呢我们是18081对吧18081然后下面呢有一个ws然后下面呢是一个id比如说我们是1001然后做一个连接走ok那么会发现它的状态是不是就已经连接成功了
[05:06] 对吧OK好然后呢我们还需要再开启一个因为我们要做两个人之间的一个通信那么我们看一下怎么去玩呢那么我们想要再开一个它怎么开呢我可以把这个这样拖一下然后呢我再打开一个再打开一个就可以了那么我把这个地址呢拷贝一下那么这个我改成1002
[05:27] 然后呢去open一下那么现在呢我其实是有了两个这个客户端一个是1001一个是1002那我是不是就可以1001给1002去发一个消息那么这个消息内容大家还记得吗就是有这么两个内容啊一个是叫做to id然后呢比如说我发送给是1001哎哎他发给是1002然后呢我们再去呃给你一个我们的消息内容比如说你好
[05:55] 那么做这样的一个发送走那么你看我们这个1001是不是就发出去了那么检查1002是不是就收到消息了说这个你好然后呢同理呢我1002是不是也可以给1001去发消息那么我把它也拷贝过来那么这个改成1001改成你也好你也好走发送那么我们可以看到在1001的这个下面呢他也同样收到这个消息那就说明什么呢说明我们这个
[06:22] 程序部署是没有问题的对不对但是呢其实会有一个小问题就是前面我们说过我们需要把我们这个im服务呢部署到19但是我们现在只部署到了这个7那么所以我们需要把我们这个呢先停掉对吧然后呢我们去把它拷贝到我们的远程去啊那么这样的话我们需要在我们19这个下面的先去创建一个浩克下面一个目录那么这个目录呢最好呢跟我们这个在
[06:52] 在我们这个就是1.7这个下面的目录保持一致啊所以说我们也去创建啊这样的一个目录好那么我们来创建一下make dir然后呢烤焙钢屁好那么这个目录呢就创建好了创建好之后呢我们做一个scp就可以了那么scp呢就是这个价包然后呢到哪里呢192.168.1.19然后呢冒号
[07:21] 下面的路径呢其实还是我们刚刚的这个路径啊那么就这么来call吧把它呢拷贝过来到这然后呢我们去做一个scp这样的一个拷贝然后呢输入我们的密码然后呢等待它的一个拷贝就可以了那么它呢就会把这个加包呢去拷贝到我们这个19这个服务器那么我们就可以在19这个服务器呢去做一个测试了那么其实测试跟我们刚刚是一样只是我们需要把刚刚这个地址呢
[07:51] 这个1.7改成1.19就OK了好那么我们稍微等待一下好那么现在呢它已经拷贝完成了拷贝完成之后呢我们进入到这个19那么我们进入到浩克下面publish浩克下面呢是不是有一个这个加包啊那么来给它去启动一下启动它好那么我们来稍微等待一下它的一个启动OK那么我们这个服务呢在19这个服务器上面就跑起来了
[08:18] 那么下面我们来做的测试就是把这个地址的我们改成19就可以了效果的应该都是一样的那么我们点击open好已经创建连接了那么这个呢我们也改成改成这个19然后连接一下好那么我们可以发送消息了你比如说我这个把它清把这个消息都清理掉然后呢我这个1002给1001去发消息反过来吧就1001给1002发消息走
[08:47] 发送那么1001里面收到消息了对吧同样的1002给1001发消息那么发一个您也好那么在这个里面同样也收到消息那就说明我们这个服务呢没有任何问题那么到目前为止呢我们是不是就已经完成了我们这个IM这个系统的一个部署啊那么把它部署到是一个1.19这个服务器上面那么我们可以把它呢先这个
[09:12] 把它关掉然后我们启动的时候后面加一个&符号让它后台启动就可以了好嘞那么关于这个IM项目的一个部署就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
Docker create --net host --name rmqbroker01 \
  -e "JAVA_OPTS=-server -Xms128m -Xmx128m -Xmn128m" \
  -v /opt/rmq/rmqbroker01/config/broker.conf:/etc/RocketMQ/broker.conf \
  -v /opt/rmq/rmqbroker01/store:/opt/store \
  foxswh/RocketMQ-broker:4.3.2

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
spring.RocketMQ.nameServer=192.168.1.7:9874
spring.RocketMQ.producer.group=haoke-WebSocket-group
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
2019-02-28 23:05:52.772 INFO 12903 --- [ bboShutdownHook] org.apache.ZooKeeper.ClientCnxn : EventThread shut down for session: 0x10002cfa3490002
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiHouseResourcesService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="false" id="cn.itcast.haoke.dubbo.server.api.ApiIdService" />
2019-02-28 23:05:52.817 INFO 12903 --- [ Thread-5] f.c.ReferenceAnnotationBeanPostProcessor : <dubbo:reference Service="cn.itcast.haoke.dubbo.server.api.ApiIdService" version="1.0.0" generic="

