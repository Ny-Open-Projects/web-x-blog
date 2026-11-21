# 08.搭建SparkHA高可用集群（实施搭建）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\08.搭建SparkHA高可用集群（实施搭建）_【海量资源尽在 666java.com】.mp4
- 时长 18分27秒（音频 1107s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就动手来搭建我们基于Zookeeper的我们Spark的高可用的集群那么要想去搭建我们的这个高可用集群呢我们首先得有Zookeeper的这个服务那么当然了最好是我们要去搭建一个Zookeeper的集群那么在这呢我们为了简单去使用呢那我们就来搭建一个Zookeeper的一个单节点那么其实这个单节点呢
[00:29] 那么在前面的课程中其实已经搭建好了对吧其实我们可以直接来使用啊就可以了好那我们来看一下呃那么在我的这个机器啊就是31.81这个机器啊上面呢呃有一些我们这种服务啊可以看一下那么在这个位置呢其实是已经啊有一个这个猪keeper啊这样的一个服务了那我们就可以直接来使用它了好那我们下面来看一下怎么样去使用呢
[00:57] 那么首先呢是需要在我们的三台这个节点上面的去添加一个host端口的一个映射啊那我们先来找一下这三台机器那么我们来打开这个ETC下面的hosts然后呢我们在最下面吧去添加一条就是这个ZK映射到是这个31.81啊这样的一个服务地址然后呢我们同样的在第二台机器呢也做啊相同的这个操作那么放到最下面来
[01:27] 那么也是这个ZK指向到我们的31.81然后我们继续进入到第三个节点然后我们到下面来去做一个添加然后保存退出我们可以尝试的去拼一下ZK那么会发现是不是可以识别并且可以拼到我们这台机器没有问题那么接下来我们就需要去修改我们的SPARK的配置文件那么我们进入到我们的
[01:56] host进入到我们这个根目录下面itcast下面有一个Spark下面呢是不是有一个config这个目录然后呢我们打开这个sparkenv啊这样的一个运行的啊这样的一个配置项然后呢在这个中呢我们需要把这个配置项给它注释掉啊把这个注释掉然后呢我们再来添加一个配置那么来看一下什么配置呢我们把这个呢拷贝过来拷贝到这
[02:25] 那么我们来看一下这个配置中的一些这个内容那么我们是给他去指定了一个java的一个OPTS就是一些这个启动的一些参数那么我在这个位置指定了什么Spark.deployrecovermodel是一个什么呢就是发现模式呢是通过这个zookkeeper这种方式
[02:46] 然后呢并且呢去指定这个ZooKeeper的URL就是这个ZK注意这个是我们刚刚所配置的那个ZK的这个域名的这个映射然后呢冒号2181就是我们这个ZooKeeper的端口然后呢这个呢是去指定我们的这个数据啊保存到ZooKeeper中的目录就在根目录下面的SPARK要注意这个呢是在ZooKeeper中的目录
[03:15] 可不是我们的这台机器啊所部署的目录啊这一点一定要啊搞清楚啊然后呢我们来保存退出一下好那么这个配置项是不是就搞定了那么我们接下来呢就来把这个配置文件呢我们来拷贝到其他的这个机器啊那么SCP那么我们拷贝到这个拷贝这个到哪呢就是我们的node2冒号下面的itcast
[03:40] 下面的Spark下面的config拷贝到这个目录下面来然后呢我们来把再拷贝到我们的这个node3这个机器啊在这呢其实我们需要去提一下这个配置项里面的这个内容啊那么大家也可以去思考一下啊就是那么我们为什么哎呀要把这一项去注释掉呢是吧为什么要注释掉大家可以自己想一下那么其实原因呢就是
[04:08] 在我们之前的这个模式中呢就是非HA的这种模式中啊那我们直接指定了谁呢我们这个Must这个接电啊这个主机是谁但是呢我们如果去要玩的是集群模式的话那么我们是不是就不能够把这个Must写死而是要通过Zookeeper是不是来做一个这个选举啊对吧所以说呢我们不能够去写死要把它注视掉
[04:36] 这一点大家想明白了吗好那么我们来退出一下好那么到目前为止呢我们其实已经呢就把配置文件呢就搞定了那么接下来呢我们就先把我们之前所启动的服务呢先停止掉吧那我们来看一下这个里面是不是有个stop什么呢那我们做一个stop来GPS查看一下然后呢我们到第二台机器查看一下第三台机器我们来查看一下
[05:05] 会发现什么呢我们这个进程是不是都没有了服务都停掉了对不对好那么接下来呢我们就来做一个启动啊那么我们还是呢通过我们之前的这个startall这个方式呢做一个启动我们看它是否能够正常的启动起来呢也ok好那么接下来呢我们就来启动一下通过这个start然后呢all做一个启动那么我们来等待一下
[05:34] 可以看到跟我们之前启动啊ok是一样的啊呃然后呢这个呢是我们的master下面都是这个worker可以来通过我们的gps查看一下是不是没有问题然后到这个里面呢再来查看一下到这个里面呢再来查看一下是不是跟我们之前是一样的呢对不对好那么呃前面我们说到啊即使我们现在既然我们现在玩的是一个集群模式那我们必然要启动多个这个master
[06:02] 那么我们现在只启动了一个这个想象就不是高可用了对不对那么应该怎么做呢我们要把什么呢我们第二台这个机器呢也跑起来那我们进入到这个itcast下面呢有一个Spark-sb然后呢我们来看一下这个下面其实有一个脚本呢叫做start什么呢master这个呢是单独去启动这个master的好那我们来尝试着去启动一下什么呢master那么我们
[06:31] 可以稍微等待一下啊然后呢我们可以看到在这个中呢是不是也有了master这个进程了然后呢我们在第三台机器呢去做一个启动那我们进入到根目录下面的Spark下面的sb目录然后呢我们同样按照相同这个方法去启动这个master走那么把它呢也跑起来那跑起来之后呢我们再来去查看一下它的进程那么会发现呢进程中是不是也同样啊有一个master
[07:00] 这样的一个这个节点了对吧好那么接下来呢我们就来测试一下我们这个高可用是否真的是高可用呢那么怎么样测试呢我们先来看一下我们这个效果那我们刷新一下这个是我们的node1对不对啊那么node1中呢我们会发现我们的进程数只有两个这个时候是不是就会发现是有点问题的呢那么你会发现呢而且是第一个这个
[07:29] 进程啊或者是这个worker他已经什么呢死掉了是不是而我们的第二个才是一个活跃的一个啊这样的一个这个worker哎这个是什么情况呢大家前面还记得啊就说我们直接来访问node1的8080的话那能够看到的worker数其实是有三个啊才对那么接下来呢我们再来尝试的访问一下我们node2这个8080
[07:54] 来看一下它会怎么样啊那么可以会发现呢这个里面呢OK没有这个worker那么我们到load3里面去查看一下会发现的也是没有这个worker那么显然这个时候呢会发现是有问题的对不对那么当然我们可以进一步的做一个测试啊就是那么我们假设啊现在呢我们把我们的这个就是第一台机器的这个mask直接cue掉就是相当于我们在模拟一个当机的这样的一种情况走
[08:24] 那我们可以看一下第一个在做刷新的时候会发现它呢是肯定访问不了了对不对那我们来看一下第二个这个节点呢能够访问但是它依然处于什么呢stand by啊这样的一个状态啊那么第三台机器呢也是这样的一个状态那么我们可以稍微啊等待几分钟好那么我们稍微等待了一两分钟之后呢我们会发现那我们load1啊显然呢肯定是访问不了那load3呢我们来访问一下可以访问但是呢
[08:54] 它也是一个standby这样的一个状态显然是一个不可用或者说备用的一个状态那我们来看一下node2刷新一下那么会发现这个node2是不是处于一个活跃的状态对吧然后我们会发现它有了两个这个work进程对吧但是它并没有第三个这个work进程并没有第三个work进程或者说没有达到我们的预期
[09:19] 正确的一个结果呢应该是我们要有三个我们的一个work这样的一个节点啊对不对啊那么这个时候显然是有问题的那么究竟是什么问题呢我们其实呢可以来跟踪一下我们第三个这个节点的这个什么呢日志信息啊那么为什么要跟踪第三个呢原因是我们可以在这个work这个节点中呢并没有发现我们的第三个这个节点那我们可以来看一下
[09:48] 他的这个日志啊那我们进入到第三个这个节点在这儿那我们点cd点点回去啊进入logs这个目录那么这个下面呢显然是不是有一些这个日志信息那我们来看一下我们看哪个呢显然我们看的是不是这个就是work的这个的一个日志信息啊那我们通过一个mode做一个查看然后呢可以看一下他的信息啊然后可以看到他报错了啊那么这个信息错误来看一下
[10:18] 他说去连接到我们这个master出错了那么master谁呢是itcast7077那么也就是说他找到我们的master是谁呢是itcast7077但是大家可以回想一下我们的环境啊那么我们这个master那我们这个master这个itcast是先把它先停掉啊有点卡啊稍微等待一下
[10:47] 好那么我把先把这个呢停掉啊那我们可以尝试去拼一下谁呢ITcast那么其实这个ITcast是谁呢就是什么呢本机啊就是本机那么这个时候呢会发现那么它去连接到我们本机的这个7071那显然呢是有问题的因为我们本机的7077的这个master呢它呢正处于一个standby这样的一个状态是不能够被连接的啊这个大家能够理解吗也就是说
[11:16] 他正确的应该找到谁呢找到我们的第二台这个机器作为master去做一个连接但是你发现他并没有而是他是连接到本机的作为一个master去做一个连接这显然呢是有问题的那么所以说呢啊那么当我们去使用这个HA的高可用的时候呢就不能够采用我们之前的这个什么start out的方式去做一个启动了会导致什么呢找不到
[11:44] 正确的这个master哎OK那么应该怎么做呢应该这样来玩那么我们先把什么呢先把我们这种所有的进程呢全部都给他kill掉把这个worker啊kill掉然后呢把这个里面的进程呢也kill掉kill这个谁呢就是master和这个worker全部都kill掉然后呢这个呢也给他kill掉好那我们来看一下正确的操作啊是什么呢
[12:13] 好那么可以检查一下三个节点是不是都已经是OK了没有问题没有问题好那么我们正确的玩法呢是首先呢我们需要在三台机器把我那个Must启动起来注意注意不是这个Start All我们启动的是什么呢Start这个Must启动它先把这个Must呢先跑起来那么这是第一台机器
[12:41] 然后呢我们进入到第二台机器把这个start这个must也跑起来然后呢再进入到我们的第三台机器进入这个SB目录然后呢再做一个启动那么这个时候呢我们三台机器的must呢就已经跑起来了那么接下来呢我们可以尝试的来访问一下那么可以看到第一台这个机器啊它正在做一个这个恢复啊然后呢我们看第二台机器啊它是stand by
[13:08] 那第三台机器呢也是一个standby那么基本上呢可以啊我们可以认为啊就是我们这个master这个集群他们master这个他们之间的这个集群呢就已经组建ok了啊这个大家能够理解吗那么他们之间ok了但是呢目前呢还没有这个worker为什么没有worker呢你会发现呢这个时候他状态是一个位置的状态那我们刚刚是不是直接把我们这个就是83上面这个
[13:36] 的这个呃我可直接给kill掉了对不对好那我们再来刷新一下那么其实可以我们稍微等待一下这个就会这个进程就会死掉的啊就会死掉的那么这样的话呢我们就来在我们的三台机器再来启动谁呢我们把我们这个work呢再来启动起来那我们启动我们work呢其实启动就是slave那么启动slave呢我们需要去指定一个什么呢我们这个18个地址
[14:03] 这个地址从哪来呢我们就是在这个位置其实可以看到啊就这样的一个地址当然了我们要把这个ITcast去指向到我们当前的一个master的一个这个地址我们当前的这个master组呢其实就是在这台机器啊因为这两个呢都是什么呢standby啊这样的一个状态刷新一下哎可以看到他呢是不是就是处于一个这个呃dead状态啊就死已经死掉了而他的一个这个状态呢就是一个活跃的一个状态
[14:32] 好那我们显然是不是指向它呀那么如果说我们能到到20活跃那就指向到到2就可以了好那我们把这个来拷贝一下然后呢我们做一个启动那么我们先来这个里面查看一下吧那么start什么呢这个slave其实有两个一个是单个一个是一个是有s一个是没有的那么这个呢是启动一个这个slave这个是启动我们这个这个集群中所配置的所有的slave
[14:59] 当然我们一个一个把它启动起来那么在前面的我们是不是配置过一个sleeves这样的一个配置文件那么如果我们使用这个sleeves的话就会启动这三个这个大家应该知道好然后我们去做这样的一个启动那么我们去指定我们当前的一个master然后我们回车走那么前面的我们测试是吧会发现他找到找我们这个master是不是有问题找不到对吧或者找错了
[15:27] 那我们给它直接来做一个指定那么这个下面呢也去启动它也指向到这个里面来那么同样第三个节点也指向过来OK好启动起来了然后呢我们就进入到我们的第一个这个节点中刷新一下那么就可以发现呢我们正常是不是已经有了三个我们这个work这个节点了OK没有任何问题只是我们数期望看到的一个效果那么接下来呢我们就来测试一下
[15:53] 当我的第一个这个节点的Must当机的话那么会怎么样呢那么我进入到第一个这个节点那么GPS来查看一下那么我们可以来看一下不是这台机器那么是在这个上面那么可以看到是我有三个这个进程我直接Q-9直接把我这个Must杀死那么Must杀死之后呢那我们来看一下这个显然肯定是访问不了对不对
[16:23] 那我们来看一下第二个的这个节点的访问那么他呢依然处于stand by的状态那么来看一下第三个也是stand by那么这个时候呢前面我说到过啊整个集群的恢复呢是需要一点时间的让我们稍微等待一下OK那么我们刚刚呢大概等待了有一分钟的时间啊然后呢我们可以发现在我们node2这个节点啊node2的这个节点呢那么可以看到当前这个master就是node2这个master
[16:52] 它的状态已经变成一个什么活跃的状态那么并且关键点来了那么我们的三个work节点是不是都已经被它发现了对吧都已经被它发现了那么显然我们现在高可用集群是不是就正常了对吧那么我们再来看一下load3这个节点那么这个节点依然处于standby这样的一个状态也没有这个work的一个节点是OK的符合预期
[17:18] 那么Node1呢这个肯定访问不了对吧那么接下来呢我们也可以尝试的把我们Node1呢可以再跑起来我们再来试一下啊那我们要启动的话那么要注意现在指向的就是Node2对不对不能再指向这个Node1了哎把它呢哎我们不是启动它啊我们要启动的是MustStart-Must把它呢跑起来那么它跑起来之后呢我们这个Must这个Must
[17:46] 它的一个状态那么显然就应该是一个stand by这样的一个状态了那么这个是没有问题的那么这个呢同样也是没有问题的OK那么大家也可以接着去测试比如说我们把这个node2 kill掉那么看它会发生什么样的一个情况它是不是又会在node1和node3之间去做一个选举呢对吧OK好那么其实这个呢就是给大家所讲的这个通过这个ZooKeeper来搭建一个HA的一个Spark这样的一个集群
[18:15] OK这个大家理解了吗OK好那么关于我们的这个基于我们的Zookeeper来搭建我们的高可用的这样的一个机群呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 ZooKeeper 实现 Spark HA（高可用）集群部署，包括配置文件修改、服务启动与故障恢复测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档中关于基于 ZooKeeper 的 Spark HA 高可用集群部署的说明，包含配置文件修改和参数说明。
画面2：在终端中执行 ping 命令测试与 ZooKeeper 服务器的连通性。
画面3：在 Spark 安装目录下查看启动脚本文件列表。
画面4：在终端中执行 jps 命令查看当前运行的 Java 进程，确认无 Spark 进程。
画面5：打开浏览器，准备访问 Spark Web UI。
画面6：访问 Spark Master Web UI，显示初始状态（Status: STANDY）。
画面7：在 Spark 日志目录下查看日志文件，确认 Master 和 Worker 的日志文件存在。
画面8：在终端中执行 start-master.sh 启动 Spark Master，然后执行 jps 命令确认 Master 和 Worker 进程已启动。
画面9：在终端中查看日志，发现 Worker 无法连接到 Master，执行 kill 命令终止 Worker 进程。
画面10：在终端中执行 kill 命令终止 Worker 进程后，再次执行 start-master.sh 启动 Master。
画面11：访问 Spark Master Web UI，显示 Worker 状态为 DEAD。
画面12：访问 Spark Master Web UI，显示 Worker 状态为 ALIVE。
画面13：访问 Spark Master Web UI，显示无法访问，提示连接被拒绝。
画面14：展示课程文档中关于 Spark 角色介绍和架构的说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
o 将Spark 集群部署到同一个ZooKeeper 实例并启动多个Master . 利用ZooKeeper 提供的选举和状态保存功能，可以使一个Master 被选举成活着的Master，而其他Master 处于Standby 状态。
o 如果现任Master 死去，另一个Master 会通过选举产生，并恢复到旧的Master 状态，然后恢复流量。整个恢复过程可能需要1分2钟。
2.5.2、基于ZooKeeper 的Spark HA 高可用集群部署
该HA 方案做起来很简单，首先需要搭建一个ZooKeeper 集群，然后启动Zookeeper 服务，最后在不同节点上启动Master。
参数说明：
• Spark deploy.recoveryMode：恢复模式（Master 重新启动的模式）
o 有三种：(1) ZooKeeper (2) FileSystem (3) NONE
• Spark deploy.ZooKeeper.url：ZooKeeper 的Server 地址
```

画面2：
```
[root@itcast sbin]# ping zk
PING zk (192.168.31.81) 56(84) bytes of data.
64 bytes from zk (192.168.31.81): icmp_seq=1 ttl=64 time=1.86 ms
---
zk ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 952ms
rtt min/avg/max/mdev = 1.867/1.867/1.867/0.000 ms
```

画面3：
```
[root@itcast sbin]# cd sbin/
[root@itcast sbin]# ll
总用量 92
-rwxr-xr-x. 1 1000 1000 2803 5月 1 13:19 slaves.sh
-rwxr-xr-x. 1 1000 1000 5689 5月 1 13:19 Spark-config.sh
-rwxr-xr-x. 1 1000 1000 1262 5月 1 13:19 Spark-daemon.sh
-rwxr-xr-x. 1 1000 1000 1190 5月 1 13:19 start-all.sh
-rwxr-xr-x. 1 1000 1000 1274 5月 1 13:19 start-history-server.sh
-rwxr-xr-x. 1 1000 1000 2050 5月 1 13:19 start-mesos-shuffle-Service.sh
-rwxr-xr-x. 1 1000 1000 1423 5月 1 13:19 start-mesos-dispatcher.sh
-rwxr-xr-x. 1 1000 1000 3151 5月 1 13:19 start-shuffle-Service.sh
-rwxr-xr-x. 1 1000 1000 1857 5月 1 13:19 start-slave.sh
-rwxr-xr-x. 1 1000 1000 1527 5月 1 13:19 start-thriftserver.sh
-rwxr-xr-x. 1 1000 1000 1478 5月 1 13:19 stop-all.sh
-rwxr-xr-x. 1 1000 1000 1056 5月 1 13:19 stop-history-server.sh
-rwxr-xr-x. 1 1000 1000 1080 5月 1 13:19 stop-mesos-shuffle-Service.sh
-rwxr-xr-x. 1 1000 1000 1064 5月 1 13:19 stop-mesos-dispatcher.sh
-rwxr-xr-x. 1 1000 1000 1067 5月 1 13:19 stop-slave.sh
-rwxr-xr-x. 1 1000 1000 1064 5月 1 13:19 stop-thriftserver.sh
```

画面4：
```
[root@itcast ~]# jps
2545 jps
2582 Worker
2631 Jps
```

画面6：
```
Spark Master at Spark://itcast:7077
URL: Spark://itcast:7077
Alive Workers: 0
Cores in use: 0 Total, 0 Used
Memory in use: 0.0 B Total, 0.0 B Used
Applications: 0 Running, 0 Completed
Drivers: 0 Running, 0 Completed
Status: STANDY
```

画面7：
```
[root@itcast logs]# ll
总用量 48
-rw-r--r--. 1 root root 15966 8月 9 17:33 Spark-root-org.apache.Spark.deploy.master.Master-1-itcast.out
-rw-r--r--. 1 root root 20956 8月 9 17:33 Spark-root-org.apache.Spark.deploy.worker.Worker-1-itcast.out
-rw-r--r--. 1 root root 2114 8月 9 17:27 Spark-root-org.apache.Spark.deploy.worker.Worker-1-itcast.out.1
-rw-r--r--. 1 root root 2061 8月 7 11:12 Spark-root-org.apache.Spark.deploy.worker.Worker-1-itcast.out.2
```

画面8：
```
[root@itcast sbin]# start-master.sh
starting org.apache.Spark.deploy.master.Master, logging to /itcast/Spark/logs/Spark-root-org.apache.Spark.deploy.master.Master-1-itcast.out
[root@itcast sbin]# jps
2658 Master
2582 Worker
2631 Jps
```

画面9：
```
19/08/09 17:28:07 WARN Worker: Failed to connect to master itcast:7077
org.apache.Spark.SparkException: Exception thrown in awaitResult(ThriftUtils.scala:226)
at org.apache.Spark.util.ThreadUtils.awaitResult(ThreadUtils.scala:75)
at org.apache.Spark.rpc.RpcEnv.setupEndpointRefByURI(RpcEnv.scala:101)
at org.apache.Spark.rpc.RpcEnv.setupEndpointRef(RpcEnv.scala:109)
at org.apache.Spark.deploy.worker.Worker$registerAllMasters$1.run(Worker.scala:253)
[root@itcast logs]# ping itcast
PING itcast (192.168.31.84)

