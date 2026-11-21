# 08.MongoDB复制集之增加arbiter节点

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\08.MongoDB复制集之增加arbiter节点【海量资源尽在 ubkz.com】.mp4
- 时长 9分28秒（音频 569s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下这个arbit的节点那么在前面呢我们讲过arbit呢主要是去做我们的集群中的一个投票选举它是一个中材者节点那么为了演示效果呢我们将我们集群中的这个节点数呢调整为偶数调整偶数那么目前呢我们是有三个节点那么也就是基数那么我们需要呢把其中的一个节点呢给它移除掉
[00:28] 然后呢我们去把它设置为偶数再来看一个情况好那么我们先来看一下当前这个节点的一个情况rs.stace那么当前的节点呢我们可以看到这个19然后呢18和17那么我们把这两个先给它跑起来吧因为目前呢只有一个啊那我们把这个start然后呢还有一个3那么我们看一下啊
[00:57] 那么目前呢我们应该是有三个这个节点来看一下那么可以看到19正在处于这个正常状态然后18也是正常状态那么17呢也OK没有问题那么现在呢我们做一个操作我们把这个193除6这个节点移除出去那么应该怎么去做呢那么首先呢我们要知道一点是那么我们对于节点的一个添加和移除呢都要在我们的主节点上面去做一个执行
[01:27] 点什么的remote这个命令去完成那么这个中的参数写什么呢就写这个我们的IP地址加端口把这个19移除那么这样的话呢看到这个OK是1那就说明这个节点呢就已经成功的被移除了那么下面我们来看一下它的一个这个状态那么我们会发现那么这个节点中是不是就剩下两个节点一个是我们的18
[01:54] 一个就是前面的这个17剩了两个这个节点好那么我们就从这个两个节点开始测试因为在我们的中产者呢他是对这个偶数节点是有效的啊那我们来看一下到底是怎么玩的那么目前呢我们来测试一下啊你比如说我们现在集群呢是有17和18是不是两个节点那么也就所对应的容器呢就是这个1和2这个节点
[02:17] 那么我们可以看到当前我们集群中它的一个主节点呢是18那么也就是02这个节点是我们的主节点那么我们先把这个重节点给它停掉看它会发生什么那么stop一下那么我们把这个01看一下1818是主那我们把这个01给它停掉停止然后呢我们再来看一下当前的一个集群的一个状态会发生什么样的变化那么当前这个集群会发现那么第一个
[02:46] 第一个这个他已经失去这个连接了对吧那我们再来看一下那么你会发现呢当我们的这个从节点当地的话那么我们这个集群他会发现呢我们之前的这个组会变成一个什么变成一个从变成一个从那么也就是说我们当前这个进行中并没有一个组节点那么没有组节点那么我们的这个集群呢就没有办法提供一个写的一个操作OK那么这个我们刚刚的
[03:14] 刚刚的一个操作呢是把我们这个从节点当机啊大家有同学可能会有个疑问就是我刚才我是把这个从这个节点当机了那么为什么会影响到我这个主节点的一个这样的一个这个角色呢那么原因是那么当我们把这个17这个节点我们当掉的话那我18这个节点呢是不是只剩下一个节点了对吧那么一个节点就没有办法满足那个大多数的原则就是过半这个原则
[03:43] 那么没有办法满足这个原则的话那么是不我们就没有办法选举出Parameter节点这样的话就会导致我们集群呢只能去读不能去写了OK是这样的一个原理那么我们可以呢把这个01的我们先再次给它跑起来再次跑起来之后呢它就会进入一个我们一个比较正常的一个状态那么可以看到这个17OK了18也是OK的那么如果我们把这个18停掉大家可以想一下Parameter停掉
[04:13] 就主节点没有了对吧那我们把这个02呢我们去做一个停止那么这样的话呢我们需要重新进入到我们的一个容器那么我们进入到01这个容器然后我们去做一个连接那么连接到它那么你会发现那么当前这个集群呢它还是一个second的节点那么也就是说我们依然没有主节点没有主节点那就说明那就说明什么那就说明我们的这个不能去写弱了对不对跟我们刚刚停掉一样那么也就是说
[04:43] 当我们的集群的节点数为偶数的时候那比如说一组一重这样的情况下面任意注意啊任意一个节点的当机都无法选举出parameter节点那么无法去提供什么呢写的操作啊无法提供写的操作当然了他可以读啊可以读那么要想解决这个问题呢我们就可以加尾一个arbit的节点去做一个解决那么OK那我们来看一下怎么去做啊那么为了演示这个效果呢
[05:12] 这个集群呢先给它恢复一个正常的一个状态然后呢我们再去做一个这个测试OK来看一下状态啊那么当前呢这个OK没有问题这个也没有问题那么当前我这个节点是变成了一个pyram节点OK好那么接下来呢我们来看一下那么下面呢我们来重新创建我们的一个实例啊重建一个实例这个实例呢叫做mongo04那么其他的参数呢基本上跟前面的差不多
[05:41] 那么来看一下端口呢是20端口然后呢这个是数据的一个挂载然后呢这个集群的这个ID依然是相同RS0然后呢设置一个BoundIP这样的一个参数OK那么我们来创建这个容器啊把这个容器呢创建出来那么创建出来之后呢我们把这个04这个容器呢给它跑起来跑起来之后呢我们就需要在我们的节点中去添加一个RBIT节点
[06:10] 那么怎么样添加呢我们需要进入到我们的主节点那么在主节点上面呢我们去执行这个命令叫做RS.AND.ARBIT这个节点去做一个添加那么要注意的是它端口呢是20这个端口然后呢做一个添加那么我们可以看到OK等于1那就说明我们这个添加动作已经成功了OK那么下面呢我们来看它的一个状态那么可以看到在这个状态中呢我们的节点呢有17然后呢有18
[06:39] 然后呢有这个18这两个我们节点啊那么可以看到我们这个20这个节点呢它的一个这个状态或者它的角色呢就是Rbit这样的一个节点那么到目前为止呢是不是我们已经把我们的Rbit的节点呢添加成功了好那么下面呢我们就来测试一下当我们的节点如果当机的话会怎么样那么首先呢我们可以来看一下目前呢我们主节点呢是我们的这个17啊17是我们的主节点
[07:08] 那么我们先来测试比如说我们把这个我们的这个18这个节点的去给他停掉那么就是这个02这个节点哎哎应该是stop掉stop掉那么这样的话呢我们来看一下集群会怎么样那么查看他的状态那么会发现呢我们的主节点是不是依然是主节点可以看到18已经是这个下线了
[07:31] 那么17依然是我们的主节点那么在前面测试中如果我没有Rbit节点的话那我的主节点是不是就会变成重节点对不对那么只能提供读的操作那么就不能提供写因为它选取不了我们的一个主节点那么现在当我们加入了Rbit节点之后你会发现我们这个主节点依然是主节点可以对外提供写的操作这就是我们Rbit节点的意义所在那么当我再次把这个
[08:00] 02跑起来之后呢他又会去加入到我这个集群中继续去提供这个服务来查看一下那么我们看一下啊那么这个里面呢这个18是不是就已经跑起来了OK那么大家应该看出这个效果了吧就是说没有我们的RP的节点呢那么如果我的偶数这是偶数的一个这个节点的话那么只要一个当掉的话那么我的另外一个是不是就从主就会变成从那么也就是说整个集群只有
[08:29] 只有读的这个操作读的这个服务没有了写的这个服务OK那么当我去加入了这个Abit节点之后呢它呢就相当于充当了一个我们的一个节点数然后呢去做一个选举那么就可以选举出一个Param那么就可以对外提供写的操作它就是这样的一个原理啊这样的一个逻辑OK好那么来看一下那么通过测试呢我们的添加之后呢是不是如果集群数
[08:55] 不满足这个的时候我们这个RB的节点可以作为一个什么呢凑数的这个节点你可以这么去理解啊但是可能不一定不一定完全准确但是呢可以帮助我们去做一个理解或者作为一个凑数的一个节点然后呢就可以达到一个什么呢就是这个大多数这个原则从而就可以选举出我们这个主节点
[09:17] 继续提供我们的读写的服务OK就是在这个就是阿比的他节点的一个作用啊OK好那么关于这个阿比的节点的一个这个讲解那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过添加仲裁节点（arbitrator）来解决 MongoDB 副本集在主节点故障时无法选举新主节点的问题。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1: 在 MongoDB 副本集的 SECONDARY 节点上执行插入操作，因不是主节点而报错。
画面2: 使用 Docker 命令停止 mongo03 容器。
画面3: 在 SECONDARY 节点上查询副本集状态，显示其同步源为 mongo01。
画面4: 使用 Docker 命令启动 mongo03 容器。
画面5: 在 SECONDARY 节点上查询副本集状态，显示其状态为 PRIMARY，但配置版本为 -1，表明存在配置不一致。
画面6: 在 PRIMARY 节点上执行 rs.status()，显示其状态为 PRIMARY，但随后日志显示尝试重新连接失败，接着成功重新连接。
画面7: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 2。
画面8: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 3。
画面9: 展示了 Markdown 文档中关于“增加arbitrator节点”的测试步骤。
画面10: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 5。
画面11: 使用 Docker 命令创建并启动一个新的 MongoDB 容器 mongo04，并将其加入副本集。
画面12: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 3。
画面13: 在 SECONDARY 节点上执行 rs.status()，显示其状态为 SECONDARY，配置版本为 5。
画面14: 展示了 Markdown 文档中关于“增加arbitrator节点”的测试步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
rs0:SECONDARY> db.user.insert({"id" : 1003, "name" : "wangwu"})
WriteCommandError({
  "operationTime" : Timestamp(1551779827, 1),
  "ok" : 0,
  "errmsg" : "not master",
  "code" : 10107,
  "codeName" : "NotMaster",
  "$clusterTime" : {
    "clusterTime" : Timestamp(1551779827, 1),
    "signature" : {
      "hash" : BinData(0, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="),
      "keyId" : NumberLong(0)
    }
  }
})
rs0:SECONDARY> db.user.find()
{ "_id" : ObjectId("5c7e43aebad2c3f5c4280dca"), "id" : 1001, "name" : "zhangsan" }
{ "_id" : ObjectId("5c7e47b24b6a894337b0b0e7"), "id" : 1002, "name" : "lisi" }
{ "_id" : ObjectId("5c7e47b24b6a894337b0b0e7"), "id" : 1003, "name" : "wangwu" }

画面2:
root@itcast:~# Docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# Docker stop mongo03
mongo03
root@itcast:~# Docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# Docker start mongo03
mongo03

画面3:
{
  "optimeDurable" : {
    "ts" : Timestamp(155179817, 1),
    "t" : NumberLong(2)
  },
  "optimeDate" : ISODate("2019-03-05T09:56:57Z"),
  "optimeDurableDate" : ISODate("2019-03-05T09:56:57Z"),
  "lastHeartbeat" : ISODate("2019-03-05T11:02:50.898Z"),
  "lastHeartbeatRecv" : ISODate("2019-03-05T11:02:51.421Z"),
  "pingMs" : NumberLong(0),
  "syncingTo" : "",
  "syncSourceHost" : "",
  "syncSourceId" : -1,
  "infoMessage" : "",
  "configVersion" : 1
}

画面4:
root@itcast:~# Docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
0fe207830106        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# Docker start mongo03
mongo03
root@itcast:~# Docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              NAMES
4b39968a0c1b        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
0fe207830106        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
c45c4b1594d        mongo:4.0.3         "Docker-ent..."      18 minutes ago      Up 3 minutes        mongo03
root@itcast:~# Docker start mongo03
mongo03

画面5:
{
  "id" : 1,
  "name" : "172.16.55.185:27018",
  "health" : 1,
  "state" : 1,
  "stateStr" : "PRIMARY",
  "uptime" : 4232,
  "optime" : {
    "ts" : Timestamp(1551783771, 1),
    "t" : NumberLong(3)
  },
  "optimeDurable" : {
    "ts" : Timestamp(1551783771, 1),
    "t" : NumberLong(3)
  },
  "optimeDate" : ISODate("2019-03-05T11:02:50Z"),
  "optimeDurableDate" : ISODate("2019-03-05T11:02:50Z"),
  "lastHeartbeat" : ISODate("2019-03-05T11:04:31.381Z"),
  "lastHeartbeatRecv" : ISODate("2019-03-05T11:04:31.381Z"),
  "pingMs" : NumberLong(0),
  "syncSourceId" : -1,
  "infoMessage" : "Error connecting to 172.16.55.185:27017 :: caused by ::"
}

画面6:
rs0:PRIMARY> rs.status()
2019-03-05T11:04:42.058+0000 I NETWORK  [js] trying reconnect to 172.16.55.185:27018 failed
2019-03-05T11:04:42.059+0000 I NETWORK  [js] reconnect 172.16.55.185:27018 ok
rs0:SECONDARY>

画面7:
2019-03-05T11:05:51.777+0000 I STORAGE  [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2019-03-05T11:05:51.777+0000 I STORAGE  [initandlisten] ** See http://dochub

