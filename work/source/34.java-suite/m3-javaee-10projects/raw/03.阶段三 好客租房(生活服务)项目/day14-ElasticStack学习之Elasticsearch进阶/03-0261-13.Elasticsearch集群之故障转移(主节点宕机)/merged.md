# 13.Elasticsearch集群之故障转移（主节点宕机）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\13.Elasticsearch集群之故障转移（主节点宕机）【海量资源尽在 ubkz.com】.mp4
- 时长 5分10秒（音频 311s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下那么下面我们要演示的呢就是如果我们的主节点当机那么会怎么样啊那么我们来看一下当前我们这个集群的一个状态啊它呢是我们的node03是我们的主节点那么这样我们把它呢停掉看一下会发生什么啊那么把这个3给它干掉然后呢我们就需要连到9200了对吧然后呢去连接那么这个时候呢
[00:29] 还没有完全停止要稍微等一下然后我们去等待一下920192029202现在应该是连不到了还可以连到吗我们是刚刚是start这个命令敲错了那当然如果启动的话我看一下我们现在03肯定处于启动状态那么刚刚我们这个命令敲错了来一个stop把它stop掉
[00:59] 好那么我们再来当然这个你需要连到是9200了走那么你会发现node01和02是OK的那么03是不挂掉了那么这个时候我们需要观察一下那么这个主变成谁了是变成那个node02了对吧node02然后我们这个主节点是node02然后我们对的节点还是node01那么我们现在集群状态是yellow然后我们的主节点现在是012345那么我们主节点是OK的
[01:26] 但是我们的分片呢是有问题的对吧但是我们这样的集群也是可用的一个状态啊然后呢刷新一下啊没有问题刷新一下啊刷新一下那么我们就需要去一会来看一下那么它这个上面的一个那么一会是不是也会恢复到一个绿色的一个状态啊对吧那我们等待着这个时间呢我们来看一下我们的一个讲义啊咱们在讲义中呢它是这样的就是那么我们是把node02停掉停掉之后呢会出现在那个结果
[01:55] 然后从这个结果中可以看出是不是我们集群对master做了重新的一个选举选举了node01为master这集群状态变成了一个黄色那么我们现在是不是把这个master选成这个02然后状态也变成一个黄色是不是没有任何问题那么等到过一段时间就会变成一个绿色对吧这回是不是就变成绿色了那么OK
[02:21] 那么接下来我们就需要去测试一下如果我把这个node02节点恢复那么也就是说我们需要把刚刚的我们这个案例中的node03恢复那么要注意一个区别要跟这个讲义要区分开来然后我们把这个node03给它跑起来就是我们之前的那个master那么它跑起来之后它还是老大吗那我们需要去测试一下了然后走
[02:46] 我们需要去等待一下等待它这个启动因为它启动的需要花点时间那我们把视频呢暂停一下好那么我们等待了一段时间呢然后我们做一个刷新会发现呢好像没有任何的变化那么也就好像看起来说我们现在我们这个03呢它跑起来了对吧但是呢我们这个集群呢好像跟它没有任何关系
[03:09] 对吧那么还是原来这个状态那么我们其实可以尝试的我们去连接到这个02我们测试一下这个02是不是就是我们的这个node03那个节点对吧连接来看一下那么这个时候你会发现那么在这个集群中在这个信息中我们可以来看一下那么在node03这个节点中你会发现那么node03它自己又变成什么呢一个新就代表什么它是一个主节点那么并且在这个主节点中
[03:39] 他还分配了这么一堆这个分片并且还有一个这样的一个索引然后呢并且呢这个他的这个显示集群这个状态是一个红色那么感觉是不是就好像说我们现在其实好像变成什么变成了有两个集群啊对吧你看这个是9200和9201还他俩显示的是一个集群对吧然后呢我们进入9202发现相当于好像又进入另外一个集群那么为什么会变成这样呢
[04:07] 对吧那么首先我们先来解释一下这个为什么是红色原因是在在这个node03这个里面这个他的这个集群中啊你会发现这个1和3这个组结点不可用的代表就是红色啊哎OK好嘞那么为什么会这样啊为什么会这样其实这个就会涉及到我们下面所要讲的一个问题啊就是我们这个脑裂问题啊就是我们这个集群中的一个脑裂问题那么
[04:36] 其实我们观察的现象就是之前我们是一个集群那么现在我们好像变成了两个集群对吧那么也就Node01和02他们在维护着一个集群那么Node03他也维护着一个集群那么为什么会这样那就是我们需要讲的脑裂的问题OK好那么关于我们这个主节点的一个当机我们就先演示到这里对吧先演示到这里然后我们下面来讲一下脑裂问题
[05:04] OK这样的话我们这个就讲完整了好嘞好那么关于这个组结点和当机那就先讲到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 Elasticsearch 集群中，通过停止并重启节点来观察集群状态变化及“脑裂”问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档内容，说明 node01 恢复后重新加入集群并重新分配节点信息，下方给出命令：Docker stop es-node02。
画面2：Elasticsearch Head 界面显示集群状态为绿色（12 of 12），node01、node02、node03 分别持有分片 0123、1345、0245。
画面3：Elasticsearch Head 界面空白，无数据。
画面4：终端显示 node01 被停止，node03 被启动，集群健康状态从 RED 变为 YELLOW，再变为 GREEN。
画面5：终端显示 Docker ps 命令输出，列出容器状态，包括 es-node01、es-node02、es-node03。
画面6：Elasticsearch Head 界面空白。
画面7：PDF 文档内容，与画面1相同，说明将 node02 停止。
画面8：Elasticsearch Head 界面显示集群状态为黄色（8 of 12），node01 为 master，node03 持有分片 0245，下方文字说明集群重新选举并状态变黄。
画面9：Elasticsearch Head 界面空白。
画面10：终端显示 Docker ps 命令输出，列出容器状态，包括 es-node01、es-node02、es-node03。
画面11：Elasticsearch Head 界面空白。
画面12：终端显示 Docker stop es-node03 命令，随后 Docker start es-node03 命令。
画面13：Elasticsearch Head 界面空白。
画面14：PDF 文档内容，说明恢复 node02 后，发现 node02 未加入集群，指出这是“脑裂”问题。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
Docker stop es-node02

画面4：
root@itcast:node03# Docker stop es-node01
root@itcast:node03# Docker start es-node01
root@itcast:node03# Docker stop es-node01
root@itcast:node03# Docker start es-node03
root@itcast:node03# Docker ps

画面5：
root@itcast:node03# Docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
5f18b673160        Elasticsearch:6.5.4   "/usr/local/bin/do..."   21 minutes ago      Up 21 minutes       9200/tcp, 9300/tcp   es-node01
620a4f1649b3        Elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 20 minutes       9200/tcp, 9300/tcp   es-node02
ead2df7792aa        Elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 2 minutes        9200/tcp, 9300/tcp   es-node03
ffbebf54f1a        mongo:4.0.3           "Docker-entrypoint..."   3 weeks ago          Up 28 hours         0.0.0.0:27017->27017/tcp   mongodb
a081ff6822e        percona:5.7.23        "Docker-entrypoint..."   7 weeks ago          Up 28 hours         0.0.0.0:3306->3306/tcp   percona

画面10：
root@itcast:node03# Docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
5f18b673160        Elasticsearch:6.5.4   "/usr/local/bin/do..."   21 minutes ago      Up 21 minutes       9200/tcp, 9300/tcp   es-node01
620a4f1649b3        Elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 20 minutes       9200/tcp, 9300/tcp   es-node02
ead2df7792aa        Elasticsearch:6.5.4   "/usr/local/bin/do..."   59 minutes ago      Up 2 minutes        9200/tcp, 9300/tcp   es-node03
ffbebf54f1a        mongo:4.0.3           "Docker-entrypoint..."   3 weeks ago          Up 28 hours         0.0.0.0:27017->27017/tcp   mongodb
a081ff6822e        percona:5.7.23        "Docker-entrypoint..."   7 weeks ago          Up 28 hours         0.0.0.0:3306->3306/tcp   percona

画面12：
root@itcast:node03# Docker stop es-node03
root@itcast:node03# Docker start es-node03

画面14：
Docker start es-node02

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：
PPT 标题：从结果中可以看出，集群对 master 进行了重新选举，选择 node01 为 master，并且集群状态变黄。
架构图/流程图结构：
- node01（master）指向分片 012345。
- node03 指向分片 0245。
- 集群状态显示为黄色（8 of 12）。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

