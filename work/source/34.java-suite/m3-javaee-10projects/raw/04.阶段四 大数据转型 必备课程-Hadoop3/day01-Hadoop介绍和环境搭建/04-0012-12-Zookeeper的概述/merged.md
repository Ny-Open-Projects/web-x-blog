# 12-Zookeeper的概述

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\12-Zookeeper的概述【海量资源尽在 ubkz.com】.mp4
- 时长 9分57秒（音频 597s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习咱们大数据的第一个框架Zookeeper这个Zookeeper非常重要它是我们后边很多框架的一个基础这个Zookeeper它是一个开源的分布式的协调服务框架它主要是来管理我们的集群的它可以为我们的应用系统提供一致性服务还有Zookeeper它是谷歌一个恰北的一个开源
[00:29] 第三Zookeeper是一个分布式的文件系统它里面主要存的是一些小文件那么接下来我给大家画一个图给大家讲一下Zookeeper的一些基本特点我们打开画图软件比如说这里有一个我们的集群我们的集群这个集群里面有很多的主机比如说我画几台主机
[01:03] 这个主机呢比如说呢我们说Node01这个Node01呢代表第一台主机接下来呢这个是Node02这边Node03这边Node04好那么这是我们的一个集群是我们的Hadoop集群吧Hadoop集群OK那么这些集群呢他们需要组成一个整体对外呢提供服务
[01:36] 那这些集群呢有时候需要一个问题就是说这些集群呢有时候呢需要保证这些数据都是一致的什么意思呢比如说呢我有一个配置文件我需要让这些集群中所有的节点呢都能看到这个配置文件而且他们看到的配置文件的信息呢都是相同的那这个怎么去做呢这个就可以借助我们今天学的这个ZOO Keeper这个ZOO Keeper呢
[02:10] 你可以认为呢它主要是对我们的集群进行管理能够保证我们集群呢各个事情呢能够协调一致那这个Zookeeper它本身呢它又有自己的一个小集群我把这个东西呢给大家放大大家看一下我向右呢再画一张图我把这个Zookeeper本身呢给大家放大这个Zookeeper长什么样子呢这个Zookeeper呢它本身呢也是一个集群那比如说呢
[02:43] 我这样子画这是一个这是ZokeyPal中的稍等这是ZokeyPal一个集群中的一个节点然后再来一个节点好再来一个节点也就是这个ZokeyPal呢它也是一个集群我们把它叫ZokeyPal集群假如说呢这个集群里边呢有三台主机那么三台主机这三台主机呢就组成了一个ZokeyPal集群
[03:20] 这个Zookeeper集群里边呢为了管理这些集群的主机呢其中呢这些集群呢被分成两类一个呢是这个集群的管理者叫做leader而其他呢被称为这个集群的一些一些从机叫followersok那么一个集群里边只有一个leader而剩余呢都是followers好这个地方呢也是followers
[03:52] 好他们三个呢组成一个集群当然了还可以有其他的一些主机注意只有一个leader其他是follow好这三台把它合在一起就称为zokeeper集群这个zokeeper集群呢它可以对外提供一些服务那比如说呢我们呢去访问的时候呢访问的访问的东西呢我们称为客户段clientclient比如说呢有两个client那么他可以去访问我们的这个
[04:26] follow或者说我们的leader或者说我们其他的followOK那么访问的时候我们他可以做什么呢比如说呀我们这个整个这个Hadoop集群中呢有个配置文件那假如说我要去读取这个配置文件比如说我们的客户端要读这个配置文件那他可以去任何一个Zookeeper中的集群中读他们每一个节点中看到的数据都是一致的比如说这个配置文件呢假如说啊
[04:55] 这个配层件它保存了一个信息这个信息比如是IP等于比如说192.168.174.100假如说有这么一个信息那么意味着这三个Zokekeeper他们保存的信息都是相同的都是相同的OK所以说我这个client从任何一个节点中获取的数据都是一致的好这是读请求读请求那么咱再说写
[05:31] 假如说这个client需要干一件事情需要去修改这个配置信息那这个时候呢他就相当于啊向我们的ZooKeeper集群发了一个什么呢发了一个写请求请注意如果说他把这个写请求呢发给这个followers这个followers是没有能力处理的因为呢写写数据啊这个写请求呢他牵扯到一个事物操作
[05:58] 好那这个时候follow没有办法处理怎么办呢其实呢他会把这个请求呢转发给leader也就是我们的管理者这个leader就有能力去处理这个写请求他怎么去处理呢比如说呢我要去修改他呢会在他这个节点里边呢把这个数据做一个修改比如说改成改成110那这时候改成110我来改一下110OK好把它改成110
[06:32] 放在这位置好他改完之后呢接下来呢他会去让这两个follow都跟着去做修改也就是把这两个台机子里边呢他的这个IP呢也改成10也改成10好那这个时候呢就会出现问题假如说他去把自己的改完之后呢再去修改这个这个follow中的这个IP那这个时候呢又有一个client又有一个client
[07:01] CR Indicant他干嘛呢他想去读取这个IP读取这个IP有一个问题那他向谁读呢假如说这个时候他向第三台接点这个接点这个接点去读去读这个IP读取读请求好那么这个时候就有一个问题因为在写的时候他需要将这个IP进行更改这个时候他只是把自己的改了一下
[07:31] 并且把第一台机子也改了一下第三台的IP是不是还有没有来得及改啊那这个时候他在读的时候呢就有可能呢在不同节点里边他读到这个值是不一致的那么我们的ZokeyPen如何解决这个问题呢我们的ZokeyPen呢就可以这样做他呢必须先保证我这个写请求执行完了之后你这个读请求才能执行那这样子呢
[07:59] 就保证了我们这个操作的原子性也就是我只有把这个数据全部更新完你才能看到我要去读的数据OK这就是一个Zookeeper非常强大的一个地方保证数据的一致性好那我们来接下来再看我们的讲义这个Zookeeper它内部啊你可以认为它是一个分布式的文件系统什么意思呢我们来看这张图这个图这个图呢比如说我的客户端呢
[08:28] 要去访问Zookeeper中的数据那这个Zookeeper中的数据它怎么存的呢它有自己的一个文件系统它是一个分布式的它这个文件系统也有根目录根目录下面有一些子目录这个很像我们的LinuxOK那我们看到的是一个整体其实这些文件呢可以分布在不同的节点上那对外界来讲呢他们看到的是一个统一的一个文件系统OK那么这里边呢比如说这个是leader这是follower这是follower
[08:57] 他们之间呢去共同维护这个集群那这里边就牵涉的问题在三台机子里边你说谁去当这个leader谁去当follow呢这里边有一个叫选举机制那就是说他们之间要投票来选举这个leader谁得到的票多那这个时候谁就是leader关于他们的选举等我们把这个环境搭建起来之后呢我们再给大家讲解好
[09:26] 那么咱们再看看这个Zookeeper能干什么事比如说可以做发布订阅还可以做命名服务分不识锁还要分不识协调好这些东西呢等我们在学的后期的时候呢我们会一个一个来解不管怎么样这个Zookeeper是一个基础性的框架我们必须安装好才能呢进行后期的其他操作好关于它的介绍呢我先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Zookeeper 的基本概念、分布式文件系统特性、集群架构及客户端交互机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 Typora 文档中关于 Zookeeper 的介绍，包含其定义（开源分布式协调服务框架、Google Chubby 开源实现、分布式文件系统）。
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“Zookeeper 是一个开源的分布式协调服务框架，主要用来解决分布式集群中应用系统的一致性问题”、“Zookeeper 是 Google Chubby 思想的一个开源实现”、“Zookeeper 本质上是一个分布式文件系统，适合存放小文件，通过文件系统来实现分布式协调”。

画面 2:
- 展示了两个架构图：左侧是“Zookeeper 集群”指向“Hadoop集群”（包含 node01、node02、node03）；右侧是“ZooKeeper集群”（包含 leader、follower）的详细结构，显示了客户端（client）向 follower 发送读请求和写请求。
- 文字：“ZooKeeper集群”、“ip=192.168.174.110”、“ip=192.168.174.110”、“ip=192.168.174.100”、“follower”、“leader”、“client”、“读请求”、“写请求”。

画面 3:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 4:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 5:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 6:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 7:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 8:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 9:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 10:
- 展示了“举个例子？”部分，包含一个架构图：Zookeeper 集群（包含 /server/slave1、/server/slave2）连接到 Master、Slave1、Slave2。
- 文档中文字：“比如有一个常见的分布式主从系统，如果有 ZK 在的话，主节点不需要和每个从节点时连接，只需要监听从节点创建的 Znode，便可以知道在线”、“Zookeeper 能做什么？”、“发布订阅”、“命名服务”、“分布式锁”。

3)

