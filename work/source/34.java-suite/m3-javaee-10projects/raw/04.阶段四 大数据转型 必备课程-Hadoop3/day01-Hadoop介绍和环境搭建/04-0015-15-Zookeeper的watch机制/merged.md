# 15-Zookeeper的watch机制

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\15-Zookeeper的watch机制【海量资源尽在 ubkz.com】.mp4
- 时长 6分30秒（音频 390s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习Zookeeper中的通知机制也就是Zookeeper中的Watch机制什么是Watch机制呢就是说呢它可以去监控一个节点的变化当一个节点呢发生了删除修改或者创建或者子节点发生改变的时候呢它就会通知相应的客户端这个特点是非常有用的来 接下来给大家讲一下这个Watch机制呢在我们这个大数据里边它主要有两种作用第一种是呢
[00:29] 发布订阅机制发布订阅那比如说呢我这里呢有一个主题订阅者订阅一个主题OK那么这个是订阅者那我们这个订阅者呢他呢去关注了某个主题当这个主题的内容发生变化的时候呢我们会通知订阅者当你的订阅者有多个的时候呢他会把这些信息啊全部通知全部通知给这些订阅者
[01:08] 那这就是一个这就是一个类似于Walk机制的一个特点而我们Zokeyper里边呢就可以使用Walk机制来实现这个订阅功能好这是第一个第二个呢咱们再说后面我们要给大家搭建一个Hadoop集群Hadoop集群集群好那么Hadoop集群呢它也有一些节点比如说呢我这里呢是node01好这个地方呢是node0102
[01:44] 那么我们在后面会讲一个东西叫高可用什么意思呢就假如说呢有两个节点当一个节点挂掉的时候呢第二个节点作为替补或者作为替换那么这个时候就有一个问题就是我如何判断第一个节点挂掉呢或者叫当机呢这个时候呢我们可以使用这个WALT机制我们来看好在这里呢我们有一个ZOE KEEPER机群
[02:26] zokeeper集群那么在这个zokeeper集群下面呢有一个zokeeper的节点zokeeper节点我们把它叫做zokeeper节点这个地方呢比如说这里边有一个zokeeperzokeeper节点那在这个节点里边呢我们可以使用Wallet机制来监控这个节点是否当机怎么去做呢是这样的当这个节点启动的时候它需要做一件事情
[03:04] 什么事情呢它可以在这个ZooKeeper这个节点里边呢创建一个临时节点创建临时节点呢比如说就create-1对吧在根目录下面比如说创建一个临时节点timeport node好那么当它创建这个临时节点的时候呢这个里边就相当于在根目录下面有个timeport这个node那这个时候呢我可以借用这个watch机制watch机制
[03:36] 这个watch机制干嘛呢我来监控这个节点的变化那么临时节点是这样的你可以把这个node01当成这个zoekeeper节点的一个客户端如果哪一天呢这个node01当机了那么就会造成啊这个node01和这个zoekeeper节点之间的断开一旦断开那这个临时节点呢就会消失那一旦消失呢我们这个watch机制啊就可以监控到这个节点的变化
[04:06] 然后呢进而呢通知我们的机群告诉机群node01已经当机了那这个时候呢那么这个时候呢我们的机群会通知node02立刻作为替补OK做这样的一个机制说这个呢我们可以以后呢用一个高可用里边一个单点故障的一个切换问题好就可以通过这个watch机制好那么这是watch机制的两个作用一个是可以做一个发布订阅机制一个呢可以做一些单点故障切换
[04:35] 来监控一个临时节点的变化好那么有了这个概念之后呢接下来我给大家演示一下这个Watch机制那比如说呢我想监控一个节点的变化那这个地方呢我们来看一下我有哪些节点好在这里呢我再给大家创建一个节点普通节点Create然后呢在根目录下面创建一个好Node01吧Node01好给它一个数据比如说Hello好这个时候呢我们已经
[05:05] 装甲好了那接下来呢我们来这样我们来get这个node01根换一下node01然后呢注意这个get后面可以加一个watch表示我要去监控这个node01的变化走稍等加了一个监控机制接下来我再打开一个客户端我把这个绘画刻龙一起分好再回到这个zooki party bin下面再打开一个客户端
[05:37] 好打开扣断sh然后呢直接回车稍等好进来之后呢接下来呢我你不是要监控node01吗我对node01这个数据我进行修改比如说呢我setnode01我给它改一个数据比如说改成word好大家请看走这个时候你会发现这个地方有个蓝色的竖线这个表示这个中段的数据发生了变化我们来点开看一下
[06:05] 你会发现这个watch机制已经监控到数据的变化了它说一个watch时间然后状态这个node data数据被改变了它的路径是根目录下面node的样也就是说这个watch被触发了这就是它的一个很简单的watch机制好 关于watch机制我们先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Zookeeper 的 Watch 机制，通过在客户端设置 Watcher 来监听节点数据变化，并展示数据变更后 Watcher 触发的通知事件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前章节为“Zookeeper 的 Watch 机制”，并列出了 Znode 属性和通知机制的要点。
画面 2: 展示了“发布/订阅机制”的概念图，包含“主题”、“订阅者”、“发布者”；右侧是“Zookeeper 集群”架构图，显示“Zookeeper 节点”通过“watch 机制”与“Hadoop 集群”中的“node01”和“node02”节点交互。
画面 3: 在 SecureCRT 中，执行了 Zookeeper 命令，包括 `ls /`、`get /app1`、`create /app1/test1 Hadoop`、`set /app1 xxx`、`delete /app1` 等操作，用于创建和管理 Znode。
画面 4: 继续在 SecureCRT 中执行命令，创建了节点 `/node01` 并设置其数据为 `hello`。
画面 5: 显示了 `ls /` 命令的输出，确认 `/node01` 节点已创建。
画面 6: 执行 `get /node01 watch` 命令，查看节点数据并设置 Watcher。
画面 7: 画面内容与画面 6 相同，未新增操作。
画面 8: 连接到 node03.Hadoop.com 的 SSH 登录界面。
画面 9: 在 node03 上执行了 `cd /export/servers/ZooKeeper-3.4.9/bin` 命令，进入 Zookeeper 的 bin 目录。
画面 10: 画面内容与画面 6 相同，未新增操作。
画面 11: 在 node03 上执行了 `./zkCli.sh` 命令，连接到 Zookeeper 服务器，输出了连接成功的日志。
画面 12: 在 node03 上执行了 `set /node01 world` 命令，修改了节点 `/node01` 的数据。
画面 13: 执行 `get /node01 watch` 命令，输出了 Watcher 触发的通知事件 `WatchedEvent state:SyncConnected type:NodeDataChanged path:/node01`。
画面 14: 画面内容与画面 12 相同，未新增操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```
[zk: localhost:2181(CONNECTED) 10] rmr /app1
[zk: localhost:2181(CONNECTED) 11] ls /
[app3000000002, tempnode2000000004, app2000000001, ZooKeeper]
[zk: localhost:2181(CONNECTED) 12] history
2 - ls /
3 - get /app1
4 - create /app1/test1 Hadoop
5 - get /app1
6 - set /app1 xxx
7 - get /app1
8 - delete /app1
9 - rmr /app1
10 - ls /
11 - history
12 - ls /
[zk: localhost:2181(CONNECTED) 13] ls /
[app3000000002, tempnode2000000004, app2000000001, ZooKeeper]
[zk: localhost:2181(CONNECTED) 14] create /node01 hello
Created /node01
```

画面 4:
```
[zk: localhost:2181(CONNECTED) 14] create /node01 hello
Created /node01
```

画面 5:
```
[zk: localhost:2181(CONNECTED) 16] ls /
[app3000000002, tempnode2000000004, app2000000001, node01, ZooKeeper]
```

画面 6:
```
[zk: localhost:2181(CONNECTED) 16] get /node01 watch
hello
cZxid = 0x100000014
ctime = Mon Apr 22 16:28:50 CST 2019
mZxid = 0x100000014
mtime = Mon Apr 22 16:28:50 CST 2019
pZxid = 0x100000014
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 5
numChildren = 0
```

画面 11:
```
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.dir=/export/servers/ZooKeeper-3.4.9
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.library.path=/usr/java64
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.tmpdir=/tmp
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.compiler=CNA
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:os.name=Linux
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:os.arch=x86_64
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.name=root
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.home=/export/servers/ZooKeeper-3.4.9
```

画面 12:
```
[zk: localhost:2181(CONNECTED) 0] set /node01 world
```

画面 13:
```
WatchedEvent state:SyncConnected type:NodeDataChanged path:/node01
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
- PPT 标题：“发布/订阅机制”。
- 架构图：
  - 左侧：一个“主题”节点，通过箭头指向“订阅者”和“发布者”。
  - 右侧：一个“Zookeeper 集群”节点，通过“watch 机制”指向“Zookeeper 节点”。
  - “Zookeeper 节点”通过“create -e /tempnode”指向“node01”和“node02”节点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

