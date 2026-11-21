# 09.部署Redis集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\09.部署Redis集群【海量资源尽在 ubkz.com】.mp4
- 时长 13分14秒（音频 794s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们部署了mycircle的集群那么接下来呢我们来看一下redis的集群那么我们redis集群呢我们将采用的是三组三重这样的一个架构那么也就意味着我们的redis将会部署有六个节点那么其中三个呢是主节点那么另外三个呢是重节点那么也就是说每一个
[00:27] 节点啊每一个这个主节点呢它都对应着一个重节点好那么下面我们来看一下这个规划那么在我们这个表格中呢其实我们可以看到那么总共呢有六个redis的节点那么我们可以看到那么前面呢这个redis的node01到03呢它呢是在这个18这个机器然后呢它呢是我们作为它是一个主节点
[00:53] 那么它的端口呢都是从这个6379,6380和6381这样的一个端口那么我们的这个重节点呢是radius 0.0的04到06这样的一个重节点那么它的端口呢是前面都有带一个1比如说叫16379,16380,16381那么这个16379它就是什么呢上面6379它的重那么同理呢这个16380呢
[01:22] 它呢就是这个6380啊它的一个重节点那么6381呢就是这个16381就是我们这个6381的一个重节点还是这样的做的一个安排啊那么要注意的是我们重节点呢是部署在我们的19啊这个机器上面那么也就是说我们会把它呢去做一个分开做一个部署那么它的容器名呢分别是后面的这个redis啊node01一直到06ok好那么下面我们就来看一下
[01:51] 具体的一个实施那么首先呢我们先来创建它的这个数据卷那么其中呢这个这个ready snow的01 02和03呢它呢是在18这个机器上面去做一个执行那么04 05 06呢是在19这个机器上面做执行这个大家一定要注意啊别搞错了按照你的这个规划来做一个执行那么我们来拷贝这三条命令然后呢进入到我们的18就是这个机器
[02:20] 然后呢去做执行那么三个数据券就已经创建好了那么下面呢我们来看这个04 05 06然后呢进入这个19然后呢我们去做一个创建那么数据券创建之后之后呢我们就可以去创建下面的容器了我们来看一下那么首先我们可以看到那么我们第一个呢是创建我们的redis node01啊这个节点那么我们所采用的网络形式呢是采用的这个host这样的一种方式
[02:50] 然后呢做一个数据卷的一个挂载然后呢我们需要去开启我们的cluster那么做一个enable呢是yes然后呢我们去设置它的classconfig的一个文件名呢是node01这样的config端口呢是6379那么同理呢其他就是6380,6381了那么这三个呢是在我们的18这个机器上面去做一个执行好那我们先来看一下
[03:17] 那我们先把这个第一个啊这个容器哎错了这个是在19那么回到这个18上面去做一个执行那么呃这个呢发现没有这个镜像他会自动去做一个下载那么我们稍微等待他的一个下载完成哎ok好那么到这里呢我们这个容器呢就已经创建好了那我们继续来创建我们的第二个这个容器走创建ok没有问题然后呢创建第三个啊这个容器把它呢创建出来
[03:45] 那么都是在我们这个18这个机器上面去做一个执行那么下面我们回到这个19那么在19这个机器上面我们来执行的是我们的另外三个这个节点它呢是我们前面主节点的重节点啊那么我们去把它创建出来然后呢这个呢同样也是创建它呃然后呢把它呢也创建出来创建出来哎OK好嘞那么到目前为止呢我们已经把我们的六个容器是不是就已经创建好了
[04:16] 那么下面呢我们就来启动我们的一些容器啊那么首先我们启动的是我们的这个010203那么它呢是在18这台机器去做一个启动然后呢我们在19上面去启动呢是启动我们的040506啊那么我们应该把这个这样来写一下先这么去call吧然后呢把这个在04啊这个040506
[04:42] 那么把它呢拷贝过来然后呢我们去做一个启动好那么到目前为止呢我们是不是就已经就跑起来了来查看一下啊那么在这个上面呢我们可以看到呃我们的radius05那么是没有跑起来吗我们看一下啊那么其他的没有跑起来那么我们看检查一下这个上面啊Docker检查一下那么这个上面呢会发现01020304
[05:09] OK没有问题那么我们的这个上面09上面他的我们这个04 05 06并没有跑起来那么为什么呢我们来检查一下那么04这个节点那么这个有点问题就是他所挂载的这个是应该是挂载04这个是挂载05那么这个挂载的是06刚刚我们可以看到这挂载呢有点问题那么这样的话呢
[05:35] 那么我们就这样吧我们把那个这几个容器呢全部都给它删除掉然后呢我们来做一个重新的做一个先停止吧先把这个停掉stop掉把它停掉然后呢我们再去把它删除掉重新做一个创建那么04然后呢0506然后呢我们也需要把这个我们的数据券啊那么全部也给它删除掉
[06:01] 那么目前呢是不是有这么多呀那么我们也给他来RM删除一下那我把这个03040506全部都删除掉那么他说这个0303正在使用正在使用中那么这样吧我们就直接我们就创建这个0405因为我们03其实是用不着的对吧那我们就把这个040506创建出来创建一下
[06:32] OK好那么这样的话就创建好了那么创建好之后呢我们就可以来重新创建我们的容器了那么把它这个拷贝过来啊就是040506这三个那么我们继续这个是是不是有点问题啊那么我们来创建一下那么这个呢是他说已经已经存在已经存在那么我们把我们这个容器呢还是去删除一下
[06:58] 那么Docker然后呢这个RM那么把这个04040506给它删除掉那么它说不能删除这个容器啊那我们来看一下正在运行的一个容器那么这个容器呢它是45的这个这个就是045我们正在运行嘛那么把它要停掉stop掉那么把它stop掉然后呢我们再去做一个
[07:27] 删除那么这样的话呢就已经删除掉了杠A来看一下是不是就没有了好那么接下来呢我们就可以来重新创建啊这几个容器那么我们一个一个来吧那么04看一下创建OK没有问题然后再来创建这个05没有问题那么再来创建这个06那么创建一下哎呃多了一个多了一个这个反斜杠好那么现在就创建好了那么下面我们是不是就可以来
[07:58] 启动啊这几个那么我们把这个靠一下04 05 06去做一个这个启动那么启动完成检查一下那么在我们的进程中呢是不是就有04 05但是0606还是没有那么04这个还是有点问题啊就是我们这个挂载的还是有点问题那么我们还是需要把它去先检查一下有没有启动好没有那么我们先把它呢
[08:29] 先把它呢就先remote掉吧就是叫做node06啊把它remote掉然后呢我们重新来创建一下创建一下然后呢我们再来启动我们的06啊就可以了OK那么我们再来看一下这个是启动06没有问题那么检查一下OK到这呢我们040506就全部都跑起来了好那么到目前为止呢我们就已经呢
[08:58] 把我们的六个节点是不是都已经跑起来了跑起来之后呢我们就可以来搭建我们的集群了那么搭建集群呢需要进入到我们的这个容器中呢去做执行那么我们选择这个node01啊作为我们的一个执行的容器那么OK那么我们首先呢先去进入到这个容器那么在这个18这个机器上面去做一个执行那么进入容器之后呢我们可以先来检查一下我们的redis是否可用呢叫一个命令乒乓啊没有问题
[09:28] 那么我们这样的话就可以去做执行了OK我来看一下那么下面这个命令呢其实就是我们去做组件集群的一个命令当然了我们这个蒋义忠啊他稍微有点问题就是这个IP地址他写错了啊那么我们把它修复一下那么在这然后呢还有一个就是19那么下面我们来看一下组件集群的命令那么在这个位置呢去通过release client然后呢去cluster然后指定一个create去做一个创建
[09:58] 并且我们在最后面去创建指定了它的一个参数就是replace的数量为1就是说每一个主节点都有一个重节点那么要注意的是在中间这个位置我们写了有6个这个节点那么在Redis 3.x版本中它使定规格是这样的就是先写的是M就是先写的是主节点后面写的是重节点那么做一个1对一个对应
[10:27] 但是目前我们使用的是5.0的话那么它会有所不同我们一起来看一下那么我们先把这个拷贝过来看一下创建的一个结果那么我们会发现那么当前我们可以看到它已经连接到我们的六个节点中那么它的会可以看到就是我们的这个M你可以看到这个是M对吧这个是M这个是MM它选择是6379
[10:55] 6380和16379那么也就是说他选择这个是没有一个顺序的那么我们就他会随机的去连接到我们的这六个这个节点然后随机选择其中三个的作为主另外三个作为从那么这个其实跟我们前面的规划稍微有所不同但是他不会影响我们整体的一个使用那我们可以看到这个是M这个是M那么这个6379是M那么这个16380就会变成他的一个从
[11:25] 那么16379是主那么这个6381呢就变成他的一个虫了OK然后呢这个6380是虫那么16381呢就是他的6380是主那么16381呢就是他的虫OK这样的一个分配那么这个呢对我们的集群是没有影响的那么我们点击这个yes输入yes那么去创建就可以了那么我们等待他的一个创建最后呢他就会把我们这个集群的创建成功
[11:53] 那么创建成功之后呢我们可以来测试一下啊那我们可以查看一下我们的这个info这个clustercluster然后呢我们查看一下nodenodes那么这个呢就是可以看到我们每一个这个节点的一些这个情况那么会发现这个6379就是自己它是主那么16379呢也是主16380是3五重
[12:20] 那么6381是从那么6380呢是主6381是从OK包括每一个主呢它都分配了我一个它的一个插槽的一个范围OK这样的话就可以形成一个完整的一个插槽好那么目前为止呢我们就已经把我们的这个集群呢就组件完成了OK那我们可以测试一下通过加-c一个参数比如说set abc然后它就会set abc123
[12:48] 然后呢就会它就会跳转到19上面的16379这个上面去做一个执行然后呢我们可以去get一个ABC那么它也会去拿到这个值没有问题那么我们把这个值呢就删除掉了那么ABC好删掉那么到目前为止呢我们是不是就已经把我们的Redis集群呢就已经搭建完成了OK好那么关于这个Redis的集群呢的搭建就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
部署 Redis 集群并验证其集群状态，随后开始部署 Elasticsearch 集群。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Redis 集群规划表，包含 6 个节点的端口、IP 和容器名。下方有创建卷的命令。
画面 2: 显示创建 Redis 容器的命令，从 redis-node01 到 redis-node06，每个容器指定不同的端口和配置文件。
画面 3: 继续显示创建 Redis 容器的命令，聚焦于 redis-node02 到 redis-node06 的创建。
画面 4: 显示终端中正在执行创建 redis-node04、redis-node05、redis-node06 容器的命令。
画面 5: 终端显示创建 redis-node04、redis-node05、redis-node06 容器的命令执行成功，随后执行 Docker ps 查看容器状态。
画面 6: 终端显示 Docker ps 命令的输出，显示 redis-node05、redis-node06 等容器已启动。
画面 7: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令。
画面 8: 终端显示创建 redis-node04、redis-node05、redis-node06 容器时因名称冲突报错。
画面 9: 终端显示尝试删除冲突容器，但 redis-node05 不存在，redis-node06 也不存在。
画面 10: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令，下方有 shell1 窗口显示 Redis 集群的 IP 地址。
画面 11: 终端显示 Docker ps 命令的输出，显示 redis-node05、redis-node06 等容器已启动。
画面 12: 显示 Redis 集群启动命令和进入 redis-node01 容器的命令，下方有 shell1 窗口显示 Redis 集群的 IP 地址。
画面 13: 终端显示 redis-cli 连接 Redis 集群并执行 cluster create 命令，显示集群状态。
画面 14: 显示 Elasticsearch 集群规划表，包含 3 个节点的端口、IP 和容器名。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```markdown
2.2. 部署Redis集群

2.2.1. 规划
服务	端口	服务器	容器名
Redis-node01	6379	192.168.1.18	redis-node01
Redis-node02	6380	192.168.1.18	redis-node02
Redis-node03	6381	192.168.1.18	redis-node03
Redis-node04	16379	192.168.1.19	redis-node04
Redis-node05	16380	192.168.1.19	redis-node05
Redis-node06	16381	192.168.1.19	redis-node06
```

画面 2:
```markdown
2.2.3. 实施
1 Docker volume create redis-node01
2 Docker volume create redis-node02
3 Docker volume create redis-node03
4 Docker volume create redis-node04
5 Docker volume create redis-node05
6 Docker volume create redis-node06
7 #创建容器
8 Docker create --name redis-node01 --net host -v redis-node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
9 Docker create --name redis-node02 --net host -v redis-node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
10 Docker create --name redis-node03 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
11 Docker create --name redis-node04 --net host -v redis-node04:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --port 16379
12 Docker create --name redis-node05 --net host -v redis-node05:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-05.conf --port 16380
13 Docker create --name redis-node06 --net host -v redis-node06:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-06.conf --port 16381
```

画面 3:
```markdown
14 Docker create --name redis-node01 --net host -v redis-node01:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-01.conf --port 6379
15 Docker create --name redis-node02 --net host -v redis-node02:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --port 6380
16 Docker create --name redis-node03 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 6381
17 Docker create --name redis-node04 --net host -v redis-node04:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --port 16379
18 Docker create --name redis-node05 --net host -v redis-node05:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-05.conf --port 16380
19 Docker create --name redis-node06 --net host -v redis-node06:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-06.conf --port 16381
```

画面 4:
```bash
root@itcast03:bin# Docker create --name redis-node04 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16379
45e0937ce1975c0af2ec9c2a8e88f5fe0fb3804b957c2e9f08931f09c143f
root@itcast03:bin# Docker create --name redis-node05 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16380
549d0cad953ad20a6d01537648e5b88a0a5909138e6998d3857734e6370
root@itcast03:bin# Docker create --name redis-node06 --net host -v redis-node03:/data redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --port 16381
7801e5663cd74975f5ca471fc4269d1713bf75b06b932a1d4303bc9aa63de
```

画面 5:
```bash
root@itcast03:bin# Docker start redis-node04 redis-node05 redis-node06
redis-node04
redis-node05
redis-node06
root@itcast03:bin# Docker ps
CONTAINER ID	PORTS	IMAGE	NAMES	CREATED	STATUS
549dcaf953a	redis:5.0.2	redis-node05	"Docker-entrypoint.s..."	57 seconds ago	Up 5 seconds
6961c4a418d	haproxy	1.9.3	haproxy	"Docker-entrypoint.s..."	34 hours ago	Up 18 minutes
3017fe035c3	percona:5.7.23	ms_node2	"Docker-entrypoint.s..."	35 hours ago	Up 18 minutes
5308acb31e22	percona:5.7

