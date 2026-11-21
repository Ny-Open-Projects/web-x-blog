# 05.通过非docker的方式进行RocketMQ的安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day09-分布式消息系统RocketMQ的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day09-分布式消息系统RocketMQ的入门\05.通过非docker的方式进行RocketMQ的安装【海量资源尽在 ubkz.com】.mp4
- 时长 11分26秒（音频 687s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好我们继续啊那么接下来呢我们来安装ROG的MQ那么首先我们来看一下这个下载下载呢当然通过这个官方是不是去做一个下载啊那么其实大家不需要下载了因为呢我已经下载好了然后呢在我们资料的那个文件夹里面大家能够拿到啊这个压缩包那么我们目前使用它的最新的版本啊就是4.3.2这个版本那么可以看到所下载的呢是一个4.3.2这样的一个ZIP的压缩包
[00:29] OK那么接下来呢我们来看一下安装那么安装呢有两种方式的安装一种是Docker的安装一种是非Docker的安装那我们先来看什么呢非Docker的安装那么后面我们再来看Docker的安装啊OK好那么下面我们来看一下这个非Docker的安装它应该怎么装呢那么我们先去把我们这个Zip的压缩包做一个解压Unzip
[00:54] 然后呢去进入到我们这个下面啊release这个这个目录下面然后呢去做这样的一个启动啊就可以了好那我们来实际的操作一下那么我们去进入到我们的这个浩克这个目录在这个目录下面呢我们可以看到是不是有一个rock的MQ这样的一个Zip的压缩包那我们把它去解压开来OK那么做一个解压那么解压之后呢我们可以看到是不是会有这样的一个目录啊
[01:20] 那么接下来我们就进入我们这个目录在这个目录下面我们就可以去启动我们的LockedMQ那我们来看怎么样启动首先我们需要去启动它的什么Nameserver然后再去启动它这个Broker那么是不是就前面我们所说的这两个组件对吧先要启动它然后再启动它这个顺序别搞错了OK那么下面我们来启动它怎么样启动我们是不是通过点斜杠
[01:49] 来一个LS把它看一下它是不是有一个启动脚本是不是点斜杠有一个叫做MQ什么的Name Server对吧Name Server就它然后我们点击这个回车走这样的话我们其实可以看到它是不是就开始去做一个启动了包括可以看到在这个位置说这个Server是吧已经这个boot这个success成功了
[02:15] 成功了,启动成功了,OK好,这个是不是就搞定就是Nameserver我们已经启动起来了接下来我们来启动我们的这个Block那么在启动Block的时候我们需要通过这个-n这个参数来指定它的一个Nameserver的一个地址那么要注意的是这个9876是我们这个Nameserver的一个默认的一个端口OK,好,那么我们就再把这个再复制一个再复制一个这个标签
[02:45] 然后我们去登录一下ok好那么把这个放大一点好那么下面我们进入cdhawk这个目录然后进入刚刚我们减压得到这个目录然后进入bin目录下面然后我们去通过什么通过这个MQ这个broke来做一个启动那就是点斜杠MQbroke然后通过杠n去指定他name server这样的一个地址是不是192.168
[03:15] 55.185然后的冒号9876来看一下没错吧是不是9876是他的一个是他的一个这个端口ok好那么要注意的是我这个我这个讲义中这个IP地址有点问题他应该是55.185但是这个里面写的是185.55这个其实没关系了这个要根据大家你自己的IP地址做一个修改就可以了
[03:44] 好然后呢我点击这个回车走那么你会发现呢在这个位置它其实它启动报错了为什么报错呢其实原因是啊原因是我们这个来来看一下啊那么能不能看到啊那么原因是呢我们在这个位置去做我们启动的时候啊它要去给我们去分配我们这个内存资源但是呢发现了发现了分配不了啊因为资源是不够的啊内存资源是不够的
[04:10] 那么可以看到需要分配有这么多的一些字节但是它分配不了那么这个是什么意思呢其实我们可以来看一下在我们讲义中的也有那么也就是说ROG的MQ它的一些默认的配置是默认是为什么配置呢是生产环境的一些配置那么所以它所设置的一些JVM的一些参数的值就比较大但是对于我们学习而言其实没有必要设置这么大
[04:39] 那么因为我们的测试机器往往可能内存资源都不是很大所以我们需要对它做一些调整那么怎么调呢我们来看一下那么我们找到我们的执行的脚本在这个下面有一个叫做ROM一个Block一个SH这样的一个脚本那么其实就是这个脚本我们来看一下
[05:00] 那么在这个脚本中我们来看一下它下面的脚本的内容那么其实我们可以看到在这个位置那么它是不是设置了一些相关我们的JVM的一些参数那么可以看到它的一些默认参数这个叫-XMS8G代表什么就是最大这个内存是不是8G那么MX这个是初始的内存大小是8G然后MN是代表的是我们年轻代的大小是4G
[05:30] 那么显然的配置是比较大的配置它其实比较适用于什么的我们生产环境但是目前我们这个并不是一个生产环境所以没有这么大的空间所以导致我们启动失败了所以我们需要对它去做一些调整那么我们给它设置什么的就设置它的 128 兆就可以了这个是设置我们的 name server这个是设置我们 broker 的一些参数我们分别来给它设置一下那么我们就这样来设置
[05:59] 那么我们最好是这样来我再来再启动再来创建一行然后呢我把它去拷贝一下到这OK好了然后呢我把上面这个给它注射掉OK好然后呢下面的去把这个做一些这个调整就可以了把这个改成什么呢128M128兆就够了因为我们测试也基本够用OK但是呢生产环境还是建议使用它的这个配置有可能比这个还要大
[06:30] 那么来一个128MOK好这个配置呢就搞定了那么我们再来修改有个叫做ROM一个什么server.sh这样的一个脚本这个是NameServer的一个启动的一个参数我们可以看到它的启动参数也是比较大的啊我们也调一下那么最大呢就给它来一个128M然后呢初始呢也是128M然后呢年轻代呢我们就给它去设置又128吧
[06:59] 这个我们可以设置小一点比如说设置64这个我们可以随意的去设置根据你的实际情况去做一个设置那么这个我们也给它设置64最大的metaspace的一个空间的这样的大小6464M64MOK这个我们设置64128MOK好那么我们保存退出这个我们就直接修改了保存退出
[07:25] 那么接下来呢我们就需要把这两个服务的重新动给他再启动一下哎OK我们再来启动一下好等待他这个启动成功这个是我们的一个Nameserver启动起来了那么接下来呢我们把这个Blockade启动起来来看一下启动走那么这回呢他就能够启动起来了因为我们已经做了一些这个参数的调整
[07:48] OK等待它的一个启动那么现在呢我们可以看到它是不是已经成功的就启动起来了那么它呢告诉我们说它的一个Nameserver的一个地址呢是这个地址OK好那么没有问题就启动起来了那么接下来呢我们来通过通过这个LogMQ中有一个工具类或者是一个工具包然后或者一个工具的脚本然后呢去做这样的一个执行让它去
[08:14] 让他去做一些这个生产者去发一些消息然后消费者去接受消息也就是说对我们刚刚所启动的这个ROG MQ的一个服务呢去做这样的一个测试看他有没有跑起来OK好那么我们还是重新需要再开一个这个标签再开个标签然后呢去登录一下好那么下面呢我们去做一个测试那么我们进入到这个浩克目录下面呢
[08:43] 有rock.mq这个目录下面进入bin下面在这个下面有一个叫tos.sh这个脚本通过这个脚本去做一个执行那么这样我们先给它去需要设置它的一个环境变量OK先做这样的一个设置那么这个环境变量是指我们设置了一个nameserver这样的一个配置就是我们的本机的一个9876OK然后我们去执行下面的这个脚本
[09:12] 把它拷过来我们去做一个执行走他呢就会去向我们的这个RobinQ去做一个发送但是呢会发现啊他那个发送这个消息出错了我们来看一下他是什么问题我们刚刚看到呢他是不是已经报错了但是呢通过排查呢会发现一个问题就是我们前面所写的IP地址他不对有问题啊就是我们启动这个Block他的IP地址是写错了
[09:39] 是我们的是要172.16不是192.168所以我们这个地址写错了我们来去看一下这个改成172.1655.185这个地址我们刚刚写错了重来一下然后呢把我那个Block呢重新启动一下然后呢我们再去做一个这样的一个测试啊好那么我们这样我们先把它清空一下然后呢我们重新再来给它去设置一下我们那个这样的一个环境变量
[10:09] 就是我们本机的9876然后我们再去做这样的一个执行OK这个其实是RockMQ所写好的这样的一个类去做一个测试好那么走看他是否能够去发动成功OK那么现在看到了就OK了他就会向我们的一个topic可以看到什么topic其实就是叫topic test这样的一个topic去发送这个消息OKBlocker的这个name是idcast
[10:36] OK这个是我们所给他去做的一些设置这可能他取的名字就是我们主机的名字OK好那么这个消息就已经发送成功了那我们看他是否能够去接收到我们这个消息那么我们去执行一下这个consumer我可以把它来执行一下到这走那我们来看他能不能拿到消息其实你会发现他是不是依然可以拿到消息那么现在其实就可以证明
[11:02] 我们这个RockitMQ的服务呢它已经就启动成功了哎呀OK那么这个是我们的Nameserver这个是我们的Broker服务启动成功了然后在这个位置呢通过它所写的这样的一个测试的一个工具然后去做这样的一个测试那么OK那么就这样是不是就OK了好嘞那么我们关于我们这个FateDock的一个安装我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在非Docker环境下手动安装并运行RocketMQ 4.3.2，并解决因内存不足导致的启动失败问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示PDF文档中“1.4.2. 非Docker安装”章节，包含下载地址和初始安装命令（cd /home, unzip, cd），以及启动NameServer和Broker的命令。其中Broker启动失败，提示“Cannot allocate memory”。
画面2：在远程服务器终端中，解压RocketMQ压缩包，查看解压后的目录结构。
画面3：显示SSH连接到Ubuntu服务器的登录界面。
画面4：PDF文档中解释Broker启动失败的原因是内存不足，并说明RocketMQ默认配置内存过大，建议调整默认值。
画面5：在终端中编辑并设置JVM配置，包括设置JAVA_HOME、CLASSPATH，并定义JAVA_OPT变量。
画面6：终端中执行numactl命令，根据NUMA节点分配内存。
画面7：在终端中执行启动NameServer命令，成功启动并显示“Name Server boot success”。
画面8：PDF文档中展示发送消息的示例代码（tools.sh org.apache.RocketMQ.example.quickstart.Consumer）。
画面9：PDF文档中展示发送消息的示例代码（tools.sh org.apache.RocketMQ.example.quickstart.Producer）。
画面10：终端中执行发送消息命令，出现“MQLClientException: No route info of this topic, TopicTest”错误，表明Topic未创建或配置错误。
画面11：PDF文档中再次展示发送消息的示例代码（tools.sh org.apache.RocketMQ.example.quickstart.Producer）。
画面12：PDF文档中展示消费消息的示例代码（tools.sh org.apache.RocketMQ.example.quickstart.Consumer）。
画面13：终端中执行启动NameServer命令，成功启动并显示“Name Server boot success”。
画面14：PDF文档中展示“1.4.2. 非Docker安装”章节，包含下载地址和初始安装命令（cd /home, unzip, cd），以及启动NameServer和Broker的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cd /home
unzip RocketMQ-all-4.3.2-bin-release.zip
cd RocketMQ-all-4.3.2-bin-release
#启动nameserver
bin/mqnamesrv
#启动broker
bin/mqbroker -n 172.16.185.55:9876 #-n 指定nameserver地址和端口

画面2：
root@itcast:~# cd RocketMQ-all-4.3.2-bin-release/
root@itcast:RocketMQ-all-4.3.2-bin-release# ll
total 52
drwxr-xr-x 2 root root 4996 Nov 5 16:46 ./
drwxr-xr-x 2 root root 4996 Nov 5 16:46 ../
drwxr-xr-x 2 root root 4996 Nov 5 16:46 benchmark/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 bin/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 conf/
drwxr-xr-x 2 root root 4996 Nov 5 16:46 lib/
-rw-r--r-- 1 root root 17339 Nov 5 16:46 LICENSE
-rw-r--r-- 1 root root 1257 Nov 5 16:46 NOTICE
-rw-r--r-- 1 root root 7482 Nov 5 16:46 README.md
root@itcast:RocketMQ-all-4.3.2-bin-release# cd bin/
root@itcast:bin#

画面5：
echo $ENVIRON: $! !!
exit 1
# JAVA Configuration
export JAVA_HOME=/usr/java
export JAVA_HOME=/usr/java
export BASE_DIR=$(dirname $0)/..
export CLASSPATH=:$CLASSPATH
# JVM Configuration
JAVA_OPT="$JAVA_OPT" -server -Xms8g -Xmx8g -Xmn4g
JAVA_OPT="$JAVA_OPT" -XX:UseCGroupMemorySize=16m -XX:GIReservePercent=25 -XX:InitiatingHeapOccupanc
yPercent=30 -XX:SoftMaxHeapSize=16m -XX:SurvivorRatio=8
JAVA_OPT="$JAVA_OPT" -verbose:gc -Xloggc:/dev/shm/mq_gc.log -XX:+PrintGCDetails -XX:+PrintDateStamps -XX
:PrintApplicationStoppedTime -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSiz=30m
JAVA_OPT="$JAVA_OPT" -XX:OmitStackTraceInFastThrow
JAVA_OPT="$JAVA_OPT" -XX:AlwaysPreTouch
JAVA_OPT="$JAVA_OPT" -XX:MaxDirectMemorySize=1g
JAVA_OPT="$JAVA_OPT" -XX:UseLargePages -XX:UseBiasedLocking
JAVA_OPT="$JAVA_OPT" -Djava.ext.dirs=$JAVA_HOME/jre/lib/ext -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -XX:ClassPath= -

