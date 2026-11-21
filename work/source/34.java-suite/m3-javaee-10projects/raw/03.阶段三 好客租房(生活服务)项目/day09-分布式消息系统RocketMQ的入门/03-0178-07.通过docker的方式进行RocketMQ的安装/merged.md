# 07.通过docker的方式进行RocketMQ的安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\07.通过docker的方式进行RocketMQ的安装【海量资源尽在 ubkz.com】.mp4
- 时长 6分5秒（音频 365s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊前面呢我们是通过非Docker的这种方式呢去做了一个安装那么接下来呢我们来通过Docker的方式做一个安装那么我们想要去通过Docker去做个安装呢我们就需要先去拉取它的一个镜像那么在这呢我们需要注意的是在这个位置我们所拉取这个镜像啊它并不是官方所提供的一个镜像啊为什么我们不使用官方的呢有两个原因第一个呢是官方呢
[00:29] 并没有去把这个镜像去push到哪里呢这个Docker的一个这个中央这个仓库里面去所以呢我们直接也拿不到这是第一个原因第二个原因的是那么我们想要使用这个官方的这个镜像的话那么你需要去拉到它的一个源码然后拉到它的一个扩展包这个源码然后呢去做一个构建才会得到一个这样的一个镜像
[00:55] 那么是不是说因为我们需要构建才不使用它呢并不是因为原因是那么我们要去使用它的话那么在后面呢我们去给它指定一些额外配置的时候会非常的麻烦啊那么这个哥们儿这个哥们儿呢对于这个官方的一个
[01:11] 基于官方这个镜像吧他做了一些这个优化啊做了些优化所以说我们使用他呢是比较方便的啊所以呢我在这呢就简单的把这个给大家去提一下就好了所以我们使用的镜像呢是这个镜像啊好那么把他两个呢就拉起下来我们来看一下那么我们就找一个在这吧来看一下Dark什么的Images来查看一下这个镜像那么我们所使用的
[01:40] 就是这两个这两个镜像那么要看到的是是不是前面其实我之前也用过官方的镜像但是是有点问题的我们就不去使用了不是很好用那么我们使用它就OK好那么下面我们来创建容器然后去启动容器那么我们去创建一个name server我们来看一下它的一个创建的一个脚本那么创建容器通过这个是给它指定一个端口的映射
[02:07] 这个是我们的一个名字啊RMQ Server然后呢这个是设置他的一些这个参数啊就是我们JBM的参数然后呢这个是指定他的两个目录一个是这个Logs一个是我们的Store存储那么Logs显然是不是就是我们的一些这个存储的一些日志对吧日志的一些目录然后呢这个Store是什么意思呢就是我们这个消息数据啊
[02:32] 你是不是发送到我们这个block里面来那么block是需要把我们的一个消息数据的保存起来那么保存到哪呢就保存到我们的文件里面去啊保存到文件那么保存到文件呢就需要他有个目录去做一个存储所以这个目录就是他所存储的一个目录啊哎OK那么把它呢我们拷贝过来Ctrl C到这个里面吧这样我们先把前面这两个都给他停掉啊然后呢我们再去做这样的一个创建容器
[02:59] 好那么这个停掉了那么我们把这个broke也给它停掉那么我们前面的非dock的安装那么我们就不使用了OK好那么把这个我们拿过来然后Ctrl C拷贝一下到这我们粘贴一下然后走好这个容器是不是就创建好了然后紧接着我们去创建下面这个broke这个容器那么在这个位置我们需要注意这么几个点来看一下
[03:25] 那么我们要给他去做两个端口的一个映射一个是10911一个是10909那么这两个端口是干嘛的呢他都是broker外界通信的一个端口其中一个呢是这个是什么这个是我们跟我们这个这个生产者和消费者进通信的一个端口而这个端口呢他是做这个组成的一个这样的一个端口后面我们再做一个集群搭建的时候呢会提到他
[03:52] OK好那么来看一下这个是它的启动参数这个没什么好说的这个要注意的是在这在这个点我们其实指定它的一个什么的配置文件它的一个配置文件那么配置文件前面这个路径注意前面这个路径是不是就刚刚我们所创建的一个路径然后后面这个路径是它容器中路径OK好那么依然有两个一个是logs一个是store
[04:17] 好嘞那么这个就是创建Block容器的一个这个命令把这个命令我们也拷贝过来然后到这然后呢贴到这来然后呢回车好嘞那么这样的话呢我们就把这个容器是不是也创建好了那么接下来呢我们来启动啊这两个容器然后到这来启动一下启动走那么把这两个容器呢启动起来那么启动起来之后啊那么我们就可以查看它首先我们这样查看它这个日志吧logs
[04:45] 那我们先来看一下我们这个Nameserver它的一个启动Nameserver的一个启动那么在这个Nameserver我们可以看到它的启动是不是就成功了对吧然后我们再来去查看一下我们的Block的一个启动好来看一下那么在这个里面可以看到它的一个这个Block的名字以及它的一个IP地址那都是OK的没有问题那就说明我们刚刚所制定的一个配置文件它肯定已经生效了对不对好嘞然后我们就可以来测一下
[05:15] 那么我们是否能够通过我们的这个producer去做一个发送消息测试一下走看他能不能够发动成功依然是不ok可以发动成功的那么没有问题对吧好然后我们再去再去通过什么通过我们的Controller去看一下消息的一个这个监听或者是消息的一个消费没有任何问题我们再测试一下我们的API看有没有问题走看他能不能够正常的做一个发送
[05:47] 如果要是可以正常发送那就说明什么是不是就说明我们的使用Docker的安装是不是就OK了可以其实可以发现使用Docker的安装是比较简单的对吧好嘞好那么关于Docker的一个安装我们就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 安装并运行 RocketMQ 服务，包括拉取镜像、创建容器、启动服务以及验证消息发送与接收。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“1.4.3. 通过Docker安装”章节，内容为拉取镜像的命令。
画面2：终端显示 Docker 镜像列表，包含 apache/RocketMQ-namesrv、apache/RocketMQ-broker 等镜像。
画面3：终端显示 Docker 镜像列表，与画面2相同。
画面4：PDF 文档中“1.4.3. 通过Docker安装”章节，展示创建 nameServer 容器和 broker 容器的 Docker 命令。
画面5：终端执行 Docker create 命令创建 nameServer 容器，随后执行 mkdir 创建配置目录，但提示目录不存在。
画面6：PDF 文档中“1.4.3. 通过Docker安装”章节，展示创建 nameServer 容器和 broker 容器的 Docker 命令。
画面7：终端执行 Docker create 命令创建 broker 容器，随后执行 Docker start 启动容器。
画面8：PDF 文档中“1.4.3. 通过Docker安装”章节，展示创建 nameServer 容器和 broker 容器的 Docker 命令。
画面9：终端执行 Docker start 启动 broker 容器，显示启动成功。
画面10：终端显示 Docker 镜像列表，与画面2、3相同。
画面11：终端显示 RocketMQ 消息发送与接收的详细日志，包含消息体、主题、队列等信息。
画面12：终端显示 RocketMQ 消息发送与接收的详细日志，与画面11类似，显示不同消息的发送与接收。
画面13：IntelliJ IDEA 中的 Java 代码，用于创建 RocketMQ 生产者并发送消息。
画面14：PDF 文档中“1.4.3. 通过Docker安装”章节，展示创建 nameServer 容器和 broker 容器的 Docker 命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
1.4.3. 通过Docker安装
#拉取镜像
Docker pull foxiswho/RocketMQ:server-4.3.2
Docker pull foxiswho/RocketMQ:broker-4.3.2

#创建nameServer容器
Docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver/logs:/opt/logs \
-v /haoke/rmq/rmqserver/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

#创建broker容器
Docker create -p 10911:10911 -p 10909:10909 --name rmqbroker \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/rmq/rmqbroker/logs:/opt/logs \
-v /haoke/rmq/rmqbroker/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

#启动容器
Docker start rmqserver rmqbroker

#停止容器
Docker stop rmqbroker rmqserver

画面4：
1.4.3. 通过Docker安装
#拉取镜像
Docker pull foxiswho/RocketMQ:server-4.3.2
Docker pull foxiswho/RocketMQ:broker-4.3.2

#创建nameServer容器
Docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver/logs:/opt/logs \
-v /haoke/rmq/rmqserver/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

#创建broker容器
Docker create -p 10911:10911 -p 10909:10909 --name rmqbroker \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/rmq/rmqbroker/logs:/opt/logs \
-v /haoke/rmq/rmqbroker/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

#启动容器
Docker start rmqserver rmqbroker

#停止容器
Docker stop rmqbroker rmqserver

画面7：
root@itcast:bin# Docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver/logs:/opt/logs \
-v /haoke/rmq/rmqserver/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

root@itcast:bin# Docker start rmqserver rmqbroker

画面8：
1.4.3. 通过Docker安装
#拉取镜像
Docker pull foxiswho/RocketMQ:server-4.3.2
Docker pull foxiswho/RocketMQ:broker-4.3.2

#创建nameServer容器
Docker create -p 9876:9876 --name rmqserver \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqserver/logs:/opt/logs \
-v /haoke/rmq/rmqserver/store:/opt/store \
foxiswho/RocketMQ:server-4.3.2

#创建broker容器
Docker create -p 10911:10911 -p 10909:10909 --name rmqbroker \
-e "JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m" \
-e "JAVA_OPTS=-Duser.home=/opt" \
-v /haoke/rmq/rmqbroker/conf/broker.conf:/etc/RocketMQ/broker.conf \
-v /haoke/rmq/rmqbroker/logs:/opt/logs \
-v /haoke/rmq/rmqbroker/store:/opt/store \
foxiswho/RocketMQ:broker-4.3.2

#启动容器
Docker start rmqserver rmqbroker

#停止容器
Docker stop rmqbroker rmqserver

画面13：
//Instantiate with a producer group name.
DefaultMQProducer producer = new
DefaultMQProducer(producerGroup: "test-group");
// Specify name server address:
producer.setNamesrvAddr("172.16.55.185:9876");
//Launch the instance.
producer.start();
for (int i = 0; i < 100; i++) {
//Create a message instance, specifying topic, tag and message body.
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

