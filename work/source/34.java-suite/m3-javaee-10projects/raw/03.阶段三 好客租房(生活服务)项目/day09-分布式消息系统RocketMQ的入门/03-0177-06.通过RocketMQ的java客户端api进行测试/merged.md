# 06.通过RocketMQ的java客户端api进行测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\06.通过RocketMQ的java客户端api进行测试【海量资源尽在 ubkz.com】.mp4
- 时长 9分58秒（音频 598s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们将通过这个加码代码的方式进行做一个测试那么测试什么呢测试我们前面所启动这个服务它是否OK的啊那么我们为什么要通过加码代码去做这个测试呢原因是在这个里面它其实会藏着一个问题啊所以呢我们需要去测试一下好那么下面我们来创建工程去做一个测试我们拷贝这个工程名导測然后呢我们去创建一个projector然后呢点击下一步
[00:27] 然后呢artifact id就它然后呢gob id呢我们就叫cn.itcast点什么呢locked mq然后呢点击这个下一步然后呢去拷贝然后点击finish完成好这个工程它就创建好了哎ok没有问题创建的ok好那么下面我们来看一下这个工程所需要的一些这个依赖包把一些依赖包拷贝进来把它呢拷进来
[00:55] 那么显然呢它是一个我们的RockMQ的一个客户端的工具对吧4.3.2 RockMQ Client客户端的工具OK然后呢在这个里面呢我们去把它是不是点击一下叫EnableAutoImport去自动启用一个自动的一个导入相关的一些依赖来看一下那么RockMQ的相关依赖是不是就导入进来了那么接下来呢我们去
[01:23] 写一个先创建一个包在包下面的去做一个测试那么这个包就叫就叫 idcidcast然后rockmq然后点击右键创建一个packager就它然后我们把这个类的内容的靠过来要注意类的一些内容编写的我们暂时先不做一个讲解因为我们是直接拷贝子的官方的一个事例
[01:51] 为什么呢为什么我们现在要去写这样的一个代码呢原因是我们前面说过也是要去找这个问题那么大家先不要去太关注这个里面代码是怎么样去做一个编写那我们先把它拷贝过来能够去跑起来就可以了好那么做一个拷贝然后呢我们去到这个里面粘贴一下好那么这个代码就贴过来了贴过来之后呢我们对这个格式呢做一个简单的一个整理
[02:19] 那么他会有报错有报错吗我们来看一下应该是没有错误应该是ok的来看一下他有什么错误在哪在这这里有什么错少一个是不是少一个括号少一个大括号那么给他加一个大括号还是少一个大括号还少吗两好嘞那么这回就对了他少了三个大括号
[02:52] 好 那么我们把这个格式呢简单的去整理一下这个就不做过多的一个讲解因为我们后面的会做详细的讲解这个就别着急好 那么把这个格式的简单的去调一下就可以了把这个简单调一下那么在这个里面呢我们可以大致的去来读下这个代码就是我们可以看到在这个位置是不是设置了我们的NameserverNameserver的一个地址是不是就171655.1859876
[03:22] 然后呢我们就去向我们的这个服务去发送消息那么所发送消息topic呢就是这个topic test11这个topic然后去做这样的一个发送OK好那么我们来看一下是否能够发送成功呢然后呢点击右键我们去做一个发送走你看他是否能够发送成功那如果能够发送成功的话那么在这个位置是否我们去把它的一个
[03:52] 这个send result去打印出来那么我们等待他的一个发送稍微等待一下好那么这个结果出来了我们来看一下那么他显然是报错了对吧报什么错呢我们来看一下他报的错误是一个这个叫call一个什么呢timeout就是说这个我们去需要把我们这个消息发送到我们的RockMQ的时候发现他超时了timeout超时OK那么这到底是什么问题呢
[04:24] 怎么会超时呢那么我们刚刚通过我们这个官方所给的工具进行发送的时候没有任何问题对不对但是我们在编码的时候他为什么就出现这个问题呢其实呢我们来看一下那么在我们刚刚启动我们这个broker的时候大家有没有注意到啊那么在我们启动的时候呢他在这个位置所打印出来的一些信息那么IDcast这个是我们的主机名这个没有问题但是要注意的是
[04:52] 这个有个IP地址加个端口那么这个是17220.0.1这个IP地址加一个什么呢10911这个端口那么10911这个端口呢其实是谁的端口呢其实是我们这个blocker他的一个端口注意他的一个端口那么9876是谁的端口呢是name server他的端口那么也就是说我们的这个生产者
[05:20] 需要通过我们Name Server找到我们这个Block然后呢去连接到我们这个Block是不是做一个发送消息的动作啊对不对但是大家想一想那么这个Block它的地址是不是就是什么呢就是这个17220.0.1这个地址大家想一想那么我现在我这个地址它是否能够连接到我的这个地址呢
[05:47] 那么连接到他显然肯定是连接不到对不对那么你看在我们这个代码中仅仅所配的是一个NameserverNameserver是172.16.55.185这个没有问题这个是OK的那么通过它是不是就找到了我们所对应的所对应的我们这个Block的地址但是这个Block地址是不是就不能够进行正常通讯
[06:10] 所以也导致这样的一个超时所以前面我们说过它在这个里面会隐藏着这样的一个问题所以我们来解决这个问题怎么解决呢来看一下那么就需要去给它设置它的一个设置它的一个这个IP地址那么怎么设置呢我们就需要给它设置它的一个具体的一个配置文件了那么配置文件呢我们需要给它去创建一个文件那么咱们就这么来玩那么把这个地址先拷贝一下Ctrl C拷贝一下
[06:39] 然后到这我们先把我们之前的这个broken先给它停掉然后我们再去做一个这样的一个设置等待它停止然后创建一个目录创建这样的一个目录然后创建加一个-P因为有些目录是不存在的好然后我们进入到这个目录中我们就不进入了这样我们直接就把这个拷过来
[07:10] 这样的话是不是直接可以创建一个文件然后把下面这个内容拷过来把这个内容拷过来我们在这个位置给它设置了有三个内容那么分别是什么来看一下那么在这我们分别设置它得是一个broker IP注意有个1broker IP1那么当然它还有一个broker IP2在后面我们也会讲到那么设置它IP地址就是172.1655.185要注意
[07:37] 这个IP地址一定是你自己的那个IP地址别搞错然后下面这个是Nameserver的地址就是172.16.55.185然后有一个9876这个跟我们刚刚选配置是一样的然后下面在这个位置我们给它设置的是一个Block的一个Name就名字那么名字就叫Block的一个浩克IM这样的一个名字好那么我们是不是有了一个配置文件了搞定
[08:01] 那么接下来呢我们就来启动我们这个block通过什么呢通过一个-c来指定这个配置文件好那么咱们就这么来玩一下然后呢ctrl c一下然后呢我们再来启动启动它这个是我们刚刚的启动的命令啊把后面的刚刚这个参数就拿掉了因为我们那个name server的IP地址是不是已经写到这个配置文件中了所以通过-c指定这个配置文件就可以了走那么这样的话它就会重新
[08:29] 启动我们的Block这个服务那么我们可以看到在这个位置我们的Block的名字是不是也发生了一个改变并且他的一个IP地址也发生了一个改变对不对OK好那么接下来我们来测试一下那么我们这个通过我们的Java的客户端是否能够去访问到我们的Rock的Rock.mq的一个服务呢来看一下走等待他的一个执行OK那么其实我们现在可以看到
[08:58] 已经完成了这个消息的一个发送对吧可以看到他的一个发送状态其实是这个散的OK对不对好那么这样的话我们是不是就可以去可以去做出这样的一个判断就是我们现在服务也OK了那么无论是我们通过他官方所给的一个托使的一个工具以及我们那个Java API的一个访问
[09:23] 他都是OK的这样的话我们这个服务是不是到这儿是不是才算是搭建的成功啊搭建完成了OK好那么关于我们前面所说的他隐藏的个问题在哪呢其实就是他的一个IP地址的这个问题啊IP地址这个问题那么怎么样解决呢我们通过一个配置文件去做一个解决那么给他指定配置文件的通过什么呢通过这个启动时候-C这个参数来指定一个配置文件
[09:49] 这样的话呢这个问题就得到一个解决了OK好那么关于这个JavaAPI的一个测试呢我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中编写并运行一个 RocketMQ 生产者程序，并解决因 Broker 启动时使用了内网 IP 导致无法从开发机访问的问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：打开 IntelliJ IDEA，选择项目 itcast-RocketMQ。
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
    <groupId>cn.itcast.RocketMQ</groupId>
    <artifactId>itcast-RocketMQ</artifactId>
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

