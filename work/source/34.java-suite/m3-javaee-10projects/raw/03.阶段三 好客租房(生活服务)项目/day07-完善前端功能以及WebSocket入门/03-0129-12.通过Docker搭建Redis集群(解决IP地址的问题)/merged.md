# 12.通过Docker搭建Redis集群（解决IP地址的问题）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\12.通过Docker搭建Redis集群（解决IP地址的问题）【海量资源尽在 ubkz.com】.mp4
- 时长 6分56秒（音频 416s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下前面我们所提到的这个问题啊它怎么解决呢那么要想解决这个问题呢我们首先得需要去搞清楚Docker的一个网络的类型啊那么Docker的网络类型呢有这么几个啊那么第一种呢就是none就是说不给它设置网络啊这个呢我们一般呢其实是不需要去使用的第二种呢就是我们的这个container它呢是什么意思呢就是说呃是
[00:26] 它的作用就是我们容器直接去连接到我们对应的容器这种相对而言用的也比较少那么在未来的Docker中可能会废弃掉这种方式然后第三种是Host它是与我们主机共享网络然后共享网络IP地址也同样共享的是端口OK那么第四种是这种桥接桥接模式是Mod的那种模式
[00:54] 那么这四种模式那么我们为什么讲它的原因就是显然是默认的这种方式不能够去满足我们现在需求解决我们这个问题那么怎么样解决呢其实我们要使用的是host的这种方式所以我们重点给大家来关注我们去讲一下host的类型那么host的类型是什么意思呢是指
[01:17] 他所创建的这个容器没有自己独立的网络的命名空间和我们的物理组织共享一个网络空间也就是说并且共享的这个端口IP地址啊那么也就是说我们可以把这个容器看作是我们的一个主机上面安装的这个服务可能不要把它看作是容器OK因为他们是共享网络和IP地址的OK但是呢这样会存在一个问题就是
[01:45] 我们这个容器直接把这个这个是不是把容器是不是直接报复在我们这个网络中因为你只要能够访问到你这个主机的那么它就能够访问到我们这个容器所以说存在一个安全隐患但是呢我们现在呢遇到这样的问题只能通过这种方式去做一个解决了对吧所以我们来看一下下面这个图这个图呢它所讲的呢其实就是我们这个host的这种方式是什么意思呢我们来看一下
[02:12] 外面的这个大框呢是我们的主机它的IP地址呢是1010.0.7.197而里面这个橙色的这个框呢这个框呢它代表的是我们的一个Docker的容器那么这个容器呢它的IP地址多好呢同样也是这个IP地址就是跟这个IP地址是一样去共享这个IP地址并且这个端口也是一样的啊去做一个共享那么OK
[02:38] 好那么我们通过这种方式呢就可以去来解决我们这个问题怎么样解决呢来看一下那么我们去创建我们容器的时候啊那我们就需要指定我们这个网络的类型就是什么呢host的这种类型怎么样指定呢来看一下那么把这个格式我们先调一下先调一下这种格式然后呢这个往上面走然后呢下面这个然后呢往下面走然后把它
[03:11] OK好那么我们来看一下这个几个这个命令那么在这个位置是不是DogCreator去创建一个这个容器然后我们指定它的它是什么Net就是它这个网络我们所采用的不是默认的条件而是什么使用的是这个host的这种方式然后挂载是一样的然后后面这个是镜像然后后面这个都一样要注意的是在我们这个命令中少了一个什么端口的映射
[03:41] 那么为什么没有这个端口的映射呢原因是你的容器是不是跟我们主机的一个端口是不是做一个共享所以我们就不需要去做一个映射了而是我们需要给我们的容器来指定它容器对外所暴露的一个端口所以我们可以看到这个是6379下面是6380和6381那OK这个大家能够理解了吗好那么我们来看一下那么我们现在呢就需要重新去把我们这个容器给它创建一下那么
[04:09] 这样我们还是先把容器呢给它先停掉吧找到前面这个命令啊我们做一个这个停止然后我们先退出这个容器我们先把容器给它停止掉然后呢我们把这个容器呢给它删除掉删除这个容器然后呢我们再去做一个remote把这个目录也给它删除掉然后呢我们再来重新啊创建我们的这个容器把这三个拷过来要注意
[04:38] 它的一个host就变成net就变成一个host也就是它的一个网络的类型变成host这种类型好那么现在呢我们就已经创建成功了那么创建成功之后呢我们就来重新启动我们的这个容器来看一下那么重新启动那么往下面走找一下我们这个命令啊然后呢去把它拷贝一下
[05:02] 我们把三个容器启动起来那么启动起来之后我们进入到任意一个容器我们就进入第一个节点然后我们去输入下面的命令注意我们来看一下把这个命令我们拷出来那么我们可以看到这个命令是不是就是我们通过的是我们这个IP地址去直接去做一个创建要注意的是这个IP地址的端口
[05:28] 对吧端口号端口63796380和6381那么这个呢它既是我们主机上面的端口号也是我们对应的容器的这个端口号OK那么我们来创建一下看它是否能够创建成功的走yes走那么等待它的一个创建那么会不会发现它是可以创建成功的OK那么如果你不采用这种host这种方式的话那么你是创建不成功的
[05:56] 那么接下来我们来测试一下我们去查看一下吧查看一下我们集群的一个信息就叫cluster什么呢cluster nodes来查看那么可以看到是不是通过这样的IP地址去做组建了一个集群那么当我们把这个IP地址去对外我们进行暴露的时候那么我们的一个应用它是不是一定就能够去访问到对应的每一个服务
[06:24] 没错这样的话什么都能够访问到那么是不是就不存在这个问题了OK那么也就是说我们把前面这个问题是不是就解决了OK那么搭建成功了那我们可以来测一下吧这个集群可用吗那么我们就需要给他来一个-C然后呢做一个set什么的ABC123get什么的ABC来查看一下是不是也是可以拿到这个数据没有任何问题那么现在这个集群
[06:49] 到目前为止是不是就已经搭建成功了OK好的关于这个机器那个搭建我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 创建并配置 Redis 集群，包括容器网络模式选择、容器启动、集群初始化和节点验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，讲解 Docker 网络类型，包括 None、Container、Host 和 Bridge 模式。
画面2：展示 PPT 图形，说明容器内 eth0 网卡与主机 eth0 网卡共享 IP 地址 10.0.7.197。
画面3：展示 EditPlus 编辑器中的 Docker 命令，用于创建和启动三个 Redis 容器节点。
画面4：展示 PDF 文档内容，列出用于查看容器 IP、删除容器、清理数据目录和进入容器执行集群创建命令的步骤。
画面5：展示 PDF 文档内容，列出删除容器和清理数据目录的命令。
画面6：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面7：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面8：展示 PDF 文档内容，列出启动容器、进入容器执行操作和主机 IP 地址 172.16.55.185 的说明。
画面9：展示 EditPlus 编辑器中的 Docker 命令，高亮显示创建 redis-node03 容器的命令。
画面10：展示 Xshell 终端，执行 Docker start 启动容器，然后进入 redis-node01 容器执行 redis-cli 命令创建集群。
画面11：展示 Xshell 终端，显示集群创建过程，包括槽位分配、配置确认和节点加入。
画面12：展示 PDF 文档内容，列出启动容器、进入容器执行操作和主机 IP 地址 172.16.55.185 的说明。
画面13：展示 Xshell 终端，执行 redis-cli 命令查看集群节点信息。
画面14：展示 PDF 文档内容，列出查看集群信息的命令，同时终端显示了集群节点的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```
Docker create --name redis-node02 -v /data/redis-data/node02:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf
Docker create --name redis-node03 -v /data/redis-data/node03:/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf
Docker start redis-node01 redis-node02 redis-node03
Docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.1:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
redis-cli --cluster create 172.16.55.185:6379 172.17.0.1:6380 172.17.0.1:6381 --cluster-replicas 0
Docker create --name redis-node01 -net host -v /data/redis-data/node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
Docker create --name redis-node02 -net host -v /data/redis-data/node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
Docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面4：
```
Docker inspect redis-node01 -> 172.17.0.4
Docker inspect redis-node02 -> 172.17.0.5
Docker inspect redis-node03 -> 172.17.0.6

#删除容器
Docker stop redis-node01 redis-node02 redis-node03
Docker rm redis-node01 redis-node02 redis-node03
rm -rf /data/redis-data

#进入redis-node01进行操作
Docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.4:6379 172.17.0.5:6379 172.17.0.6:6379 --cluster-replicas 0
```

画面5：
```
#删除容器
Docker stop redis-node01 redis-node02 redis-node03
Docker rm redis-node01 redis-node02 redis-node03
rm -rf /data/redis-data

#进入redis-node01进行操作
Docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.17.0.4:6379 172.17.0.5:6379 172.17.0.6:6379 --cluster-replicas 0
```

画面6：
```
Docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面7：
```
Docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面8：
```
#启动容器
Docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
Docker exec -it redis-node01 /bin/bash

172.16.55.185是主机的ip地址
```

画面9：
```
Docker create --name redis-node03 -net host -v /data/redis-data/node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
```

画面10：
```
root@itcast:~# Docker start redis-node01 redis-node02 redis-node03
redis-node01
redis-node02
redis-node03
root@itcast:~# Docker exec -it redis-node01 /bin/bash
redis-cli --cluster create 172.16.55.185:6379 172.16.55.185:6380 172.16.55.185:6381 --cluster-replicas 0
```

画面11：
```
>>> Performing hash slots allocation on 3 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
M: 544e237d0cb57ab921e7f1e6ca4b980a3fc7b 172.16.55.185:6380
slots:[0-5460] (5461 slots) master
slots:[5461-10922] (5461 slots) master
slots:[10923-16383] (5461 slots) master
Can I set the above configuration? (type 'yes' to accept) : yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
```

画面12：
```
#启动容器
Docker start redis-node01 redis-node02 redis-node03

#进入redis-node01容器进行操作
Docker exec -it redis-node01 /bin/bash

172.16.55.185是主机的ip地址
```

画面13：
```
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
>>> Performing Cluster Check (using node 172.16.55.185:6379)
M: d59f1dd9

