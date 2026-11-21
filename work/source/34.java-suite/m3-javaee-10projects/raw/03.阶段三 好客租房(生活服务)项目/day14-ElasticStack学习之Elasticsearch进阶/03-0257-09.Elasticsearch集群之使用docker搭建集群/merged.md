# 09.Elasticsearch集群之使用docker搭建集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\09.Elasticsearch集群之使用docker搭建集群【海量资源尽在 ubkz.com】.mp4
- 时长 20分5秒（音频 1205s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就正式的来搭建啊我们的elux search的集群那么我们依然呢是采用这个Docker这种方式去做一个搭建呃那么我们来看一下下面的一些这个命令那么我们需要去创建一个这个escluster这样的一个目录然后呢在这个目录中啊再去创建两个node01和node02也就是说
[00:23] 我们目前所搭建的一个集群呢我们只有两个节点啊只有两个节点的一个集群好那我们实际的来操作一下那么在这个下面呢我们去创建一个目录啊叫做什么呢ES-cluster然后呢我们进入我们的ES-cluster之后呢创建两个目录一个叫node01一个叫node02那么有两个叫那个节点然后呢我们进入这个node01
[00:50] 然后呢我们去需要给他去设置一些我们的一些配置啊配置那么我们配置像在哪里呢我们需要去拷贝一下我们还是回来吧退出到我们的这个ES这个目录中这个是我们最开始安装的那个elag search对吧然后呢我们进入他下面有个config那么我们需要有两个配置文件啊那么一个呢是我们的这个elag search.yaml文件
[01:18] 然后还有一个是我们的jvm的一个options文件把它都拷贝到我们根目录下面的浩克es下面的cluster下面的node01里面来但node02也需要那么我们就先这样先拷贝到node01一会儿我们修改完之后再把它拷贝到node02然后进入到cluster然后node01出了
[01:45] Node01然后在这个里面我们去做一些配置文件的一些修改那么修改哪些内容我们来看一下首先第一个是这Cluster Name就是我们集群的名字那么集群名字我们叫什么就跟我们讲一中保持一致那么我们就把它拷贝过来叫ESIT Cluster我们把这个名字贴过来这是第一个需要去做的一个配置下面还有一个叫做Node
[02:15] node.name然后这个我们改成node01然后下面我们接着继续往下面看这个我们先保持默认就不管那我接着往下面看往这个位置下面还有一个是就是到network我们的host那就它OK那么如果我们需要给它做不限制的话那就设置为四个0就可以了那么或者你设置它也行那么我们这个端口把这个端口打开那这个我们
[02:44] 调成9200为什么把端口打开呢因为一会我们是比较启动多个端口肯定不能不能这个相同对吧OK那么我们接着继续往下面看OK这个也是需要去设置的一个参数那么这个参数是什么意思呢就是我们集群发现的一种模式或者说设置它的一个host就广播的一个host那么这个需要设置我们的一个这个就是我们的IP地址把它拷贝一下然后贴到这个位置来那么我们目前呢
[03:13] 就在我一台机器是不是去搭建这个集群啊那么我们就设置一个啊就可以了然后呢下面的还有这个啊这个呢是我们需要去设置它的一个最小的一个master的一个这个节点那我们先把它设置为一啊后面我们会再说这个配置啊后面我们再说然后呢下面这两个就保留吧那我们大致的来看一下跟我们刚刚的这个配置有没有一些内容没有的啊这个我们配置过对吧
[03:43] 那么这个配置过这两个我们是不是没有对吧这两个没有那我们需要给它添加一下然后这个有这个是不是有这个也有这两个是不是也有OK那么就缺这两个那我们把这两个拷贝过来那么拷贝过来之后就任意找位置那么就我们要不就放最下面这个无所谓放哪里都行那么我们就把它丢到这里来
[04:10] 然后设置为to那么注意一下那么我们设置什么呢date这个node.must to就代表着它有资格是不是作为一个must然后node.date那么就是一个我们那个date节点对吧它同样的可以作为must也可以作为一个我们那个date这样的一个节点那么保存退出这个是不是就是我们第一个这个配置对吧OK
[04:35] 好那么这个呢是我们第一个配置第二个呢我们去修改我们那个JVM的一个这样的一个配置那么默认大小呢是1G这个有点太大了我们给它设置成比如说128M128M或者256 512都行然后呢我们保存退出一下
[04:53] 那么这两个配置文件是我们所需要的配置文件同样的我们需要把这两个配置文件拷贝到我们的node02这个目录里面来cd到我们的node02这个目录然后我们再去做一些修改那么这个里面要修改内容是不是就是要区别于我们node01好那么我来看那么这个class name这个肯定要保持一致因为他们俩要组建一个集群对吧
[05:19] 然后呢这个是node1这个node的名字node01这个显然要改成node02那么继续往下面看那么下面这个呢是来看一下啊那么这个是我们的network啊network然后呢这个这个ok没问题还是我们本机IP地址然后呢要注意这个我们要调成9201了不能一致啊不能一样然后呢继续往下面看这个要一样对吧然后这个也是它然后没有问题然后呢一直往下面看
[05:47] 这几个是不是都没有问题我们来看一下对照一下我们这个讲义那么这个里面把它设置为false那么咱们要把它设置为false这个就是说我只有node只有我的node01有资格被选为must那么我这个
[06:04] 这个二啊或者node02这个没有资格被选为这个must这个他只是有没有资格不是确定他就是must这个要注意那么后面我们再讲故障转移的时候呢我们还会重点讲这个点啊那么我们一会再来再来去做一个详细讲解那么现在呢我们先把这个集群搭起来再说好那么这个呢我们是不是就可以保存保存退出了OK好那么保存退出那么保存退出之后呢我们可以去
[06:30] 去跟我们这个去做一个对比这个配置做一个对比那么我们在这个位置可以通过一个小的一个技巧叫group去查找一个这个井号查找一个井号然后去有一个-v-v-小写的v然后我们去elac search中去查找这样的话你看这样的话查询出来的一个结果注意你看
[06:57] 这个结果是不是把我们的配置文件中的一些注释全部都去掉对吧因为说有个反选然后去把它查找出来OK那么这个就是我们真正所配置的一些内容这个是不是跟我们讲义中的就基本上就一致了OK好那么到这里我们是不是就已经把两个节点的配置文件我们是不是都已经准备好了对吧好那么接下来我们来创建容器那我们把这个命令拷贝出来
[07:26] 拷贝出来之后我们需要去调整一下这个格式肯定会有点问题调一下那么我们把这个往下面走这个往上面走一个空格把它整成一行空格这个不需要空格了然后我们下面同样是它然后空格这个空格然后往上面走然后好嘞这就好了好那么我们点击W那么来看一下上面这个命令我们简单的来看看命令
[07:55] 那么我们创建一个ES Node01这个节点它的一个网络模式或者网卡模式呢是一个host然后呢-v呢就是去做一个我们的一个这个目录的一个挂载然后呢这个这个是不是指定我们Node01的配置文件是不是给它指定到这个位置来那第二个呢是去
[08:17] 做一个这个JVM参数的一个这样的一个挂载然后呢还有一个就是我们Date目录的一个挂载大家要注意的是我们现在这个Date这个目录啊还没有对吧但是没关系它会自动做一个创建OK那么下面的这个是不是就类似了这个是01这个下面就是0202相关系操作OK好那么我们把这两个容器创建出来然后呢把这个mini拷贝一下然后呢进入到我们这个控制台走好那么这个容器创建好了
[08:46] 然后我们来把它也创建一下好那么这两个容器就OK了那么我们先启动一个那么start是不是启动es-node01对吧然后启动成功之后我们需要去查看一下它的logs-f去查看它的一个日志node01走那么我们来看一下它会怎么样呢它说这个启动是失败的
[09:15] 那么为什么是启动失败呢我们来看一下那么在这个里面呢是不是我们这个目录目录不对啊目录不对有可能目录不对啊那么来检查一下那么我们可以看到这个目录啊它是有点有点问题啊那问题在哪呢其实还是我们去拷贝的问题啊就是我们从这个pdf里面拷贝出来之后呢它会丢掉一个横杠啊就是我们来看一下是不是这个横杠的问题就是es杠那么我们来看一下啊
[09:42] 这个是你看这个位置是不是就缺一个就是我们这个下面的它然后这个也缺一个这个横杠那么我们就需要先把这两个容器先删除掉然后再来做一个创建然后RMES-load01把它删掉load02删除掉然后我们再来去做一个启动我可以把它拷贝一下到这个里面走好创建好了
[10:11] 然后我们再把它拷贝一下然后到这下面我们就执行我们刚刚那个命令就是启动这个容器并且去查看它日志轴那么发现这个容器正在启动了对吧那我们来看一下它有没有一些错误OK那么发现了有错误那么这个错误是什么意思呢就是说你看它是全线访问拒绝或者访问受限那么就是它去读取这个文件或者去往这个里面去写这个
[10:39] 写这个内容之后呢是写不进去的为什么呢我们来看一下啊这个目录是哪里的目录呢你同学这个目录我们好像不认识啊那么要注意的是这个目录其实我们是不是刚刚做了一个挂载那么我们其实挂载的是这个Date的这个目录啊其实是它对比一下啊那么对比着它Date下面有个Notice那么也就是说我们的Elite Search它在启动之后需要向我们这个里面去写一些内容但是我们现在是不是在容器中给它做了一些挂载而这个
[11:08] 是不是实际上他写内容是我们在容器外部的一个地址就这个地址那么这个地址我们现在有没有目录呢我们来进入我们cd到这个目录看一下他的确是有目录的对不对没有任何问题但是回去我们来看一下那么在这个里面我们会发现这个date的这个目录是不是我们刚刚说我没有创建他自动创建好了创建好之后他的一个所属的一个用户呢是root用户而我们的elac search要注意那么我们前面说过elac search他启动
[11:36] 是不是必须要以什么呢就是Elasticsearch的一个用户去做个启动也就是说非root用户那么在容器内部它是不是以一个非root用户的一个权限去启动那么去读取或者去访问这个目录的时候它实际的访问的是我们这个目录而我们这个目录要求是一个root用户的一个权限那么显然我们这个内部是不是没有办法没有权限去写我们的内容到我们的这个目录中所以会导致这样的一个权限的一个问题
[12:04] 那么怎么样解决这个问题呢我们就简单粗暴一点调Sysmod一下然后777给他设置一个这样的一个权限然后-R那么这样的话我们就修改了这个Data这个目录就是说你可以看到任何的用户是不是都可以对他有读写这样的一个权限那我们再来启动一下那么再来检查一下我们去检查一下现在有没有运行那么现在会发现这个还在就这个我们之前在运行我们先把这个给他停掉
[12:34] 然后呢Electro Search把它停掉把原来这个停掉再检查一下那么我们现在有MarcoDBPrescana这个我们先不管它先跑先启动起来然后呢我们再来去启动我们刚刚的这个Node 011那么把它也启动起来走那么看一下这回它的一个启动的一个这个结果会怎么样
[12:55] 那么它现在就能够你可以看到现在是不是又可以正常去做一些这个启动对吧这种启动那么在前面它是没有全线去做一些这种读写的操作的好那么我们现在就等待它的一个启动等它启动那么启动完成之后我们就来启动我们的node02那么启动之后这样的话那么它的整个集群就打解完成了好那么现在我们其实可以看到它在启动过程中是不是就打印出了一些我们前面所看的一些关键词对吧study然后study的
[13:24] 然后呢一些我们这个IP地址加专口没有任何问题都是OK的好那么第一个是不是就我们第一个节点是不是就搞定了那么下面我们是不是要去启动我们的node02以及我们查看node02这个日志它同样是不是也会有前面我们所说的一个问题就是我们那个目录权限的问题OK是不是有问题啊好那么我们来看一下这样我们先进入这个node01这个里面啊那么我们来看一下Data目录在Data目录中是不是已经有一些
[13:54] 文件的生成OK没有问题好嘞好然后我们去进入到node02这个里面那么这个文件这个目录它的一个权限是不是也有问题就其他用户不能去写入对吧那么我们简单粗暴一点sysmon一下777然后加一个date并且设置杠就是做一个地归然后来看一下这个里面权限是不是就修改了然后我们再去做一个启动刚刚那个应该是没有启动起来看一下
[14:24] 那么没有跑起来那我们再来跑一下那么再来跑一下跑找到刚刚敲的命令那么node02就他走那么再来做启动那么这回应该就可以了那么我们稍微等待一下好那么我们集群我们node02就跑起来了那么看几个关键词对吧study然后study的跑起来了在这跑起来了然后它的端口是9201
[14:51] 还有这个9300这个我们后面会用到这个端口OK好那么到这里就两个节点是不是就跑起来了那么接下来我们是不是需要去打开我们的客户端工具来看一下刷新走那么可以看到那么这个就是我们的一个集群的节点对吧然后一个node01和node02那么在我们这个集群节点中那么谁是老大呢显然这个新是老大他是一个master这个是一个date这样的一个节点OK好嘞
[15:21] 那么我们现在是不是就已经有了两个节点那么OK好那么我们尝试的去创建一个索引我们看它会怎么样那么我们在这个索引这个位置点击一个新建索引比如说我们来一个浩克浩克然后分片数我们比如说设置6然后副本数的设置为1那么什么是分片什么是副本后面我们会再说那么我们点击这个OK走那么这个节点这个是不是就创建成功了对吧
[15:48] 然后我们来看一下它的一个盖蓝的情况那么看到这个里面会有一些这样的一些方框那我们来简单的说一下在这个框里面会发现有一些0123这个什么意思那么在其实这个所代表就是我们的分片但是在这个框里面会发现有些框是粗框有些框是细框那么要注意的是这个粗框它是一个就是我们的一个主节点或者主分片
[16:16] 然后呢这个细框呢是这个主分片的一个副本那么相当于这个0就它的副本它呢是它的副本做这样的一个交叉这样的一个效果那么你比如说我们再来做个测试我再来创建一个新建一个索引比如说来一个test索引然后呢分片数呢设置为6然后呢副本数设置为2看它会发生什么情况走那么是不是我们也创建了一个这样的一个索引对吧那么我们来刷新看一下效果
[16:43] 它现在会有点就是因为它还缺少我们第三个第三个这样的一个第三个这个节点那么这样的话它是那么但是我们可以先看一下这个效果什么意思呢就是我们设置为这个这个是我们的一个0这是我们的一个主节点主的一个这个分片它就会有两个会有两个看到没有会有两个这样的副本而这个1也是也是这样的这个是我们这个
[17:13] 主的一个分片那么也有两个这样的一个副本所以说代表副本的这个意思OK好那么当然可以看到在这个里面比较醒目的其实不是在这个位置而是在这儿在这儿它其实我们会后面会讲到我们这个集群会有这么几个颜色那我们来一起来看一下那么在后面这个内容中那么我们可以看到集群的状态其实会有三种颜色绿色它就代表着我们所有的这个分片和副本是都可用
[17:43] 那么就是绿色这样的一个标识最开始我们那种状态是绿色第二种呢就是我们这个yellow就是黄色啊黄色代表什么呢主分片可用但是不是所有的副本方片呢可用那么我们可以看到在我们这个里面呢是不是相当于这个哎他这个呃这个副本副本的分片是不是不可用现在这个不可用但是我们的主分片都是可用的所以我们现在进行状态呢是一个yellow的一个状态
[18:08] 那么还有一种状态呢就是比较糟糕的一种状态了就是什么呢red红色那么如果是红色的话就代表什么呢所有不是所有的这个主分片都可用就是说有一些分片是挂掉了比如说这个里面它挂掉了那么你总共的一个分片呢显然就不完整了对吧不完整了那这样的话呢这个整个集群是非常糟糕的一个状态哎OK好嘞那么这个呢就是我们所演示的这样的效果比如说我把这个给它删掉啊我把这个分片删掉
[18:37] 我把这个分片删掉之后呢那么我们状态又会变成什么呢看一下啊就会变成一个绿色对吧所有的这个组有没有组还有它这个副本分片呢都可用啊OK那么其实呢除了我们这个客户端工具呢我们还有一个命令那么通过这个命令查询呢也可以去得到我们的一个这个集群的一个状态啊我们还可以给大家来演示一下把它拷过来做一个发动轴
[19:04] 那么会得到这样这个显示的内容是不是相对比较少差不多那么在这个里面也是去显示出一些我们的一些集群的名字以及它的一些状态这个是不是就刚刚我们所提到的状态包括它其他的一些参数包括它的一个什么nodes的参数data nodes的参数等等都可以去查看它的信息那么其实我们这个客户端工具是不是也是根据这样的一个
[19:34] 信息来展现出不同的一个这样的一个界面出来的对吧OK好那么这个呢我们就是我们所搭建的集群那么搭建了两个节点这样的一个集群那么这个我们刚刚是不是说过了粗的一个框就是主分片细的一个框呢就是副本副本或者是被分片OK好嘞那么
[19:53] 这个就是我们所讲的通过这个Docker来搭建这个集群那么希望大家呢动手去把这个去实际的敲一下OK好嘞那么关于这个搭建呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Docker 搭建并配置一个 Elasticsearch 集群，包括配置文件修改、容器创建和集群健康检查。

2) 按时间顺序列出每张画面的要点：
画面 1: 登录到远程服务器，终端提示符为 root@itcast:~#，左侧显示 /root 目录结构。
画面 2: 编辑 Elasticsearch 配置文件，显示 node.name: node01，node.attr.rack: r1，path.data: /path/to/data，path.logs: /path/to/logs，bootstrap.memory.lock: true。
画面 3: 继续编辑配置文件，显示 discovery.zen.ping.unicast.hosts: ["172.16.55.185"]，http.cors.enabled: true，http.cors.allow-origin: " "，node.master: true，node.data: true。
画面 4: 继续编辑配置文件，显示 network.host: 172.16.55.185，http.port: 9201。
画面 5: 在 node02 上执行命令，显示 grep 结果：cluster.name: es-itcast-cluster，network.host: 172.16.55.185，http.cors.enabled: true，http.cors.allow-origin: " "，node.master: false，node.data: true。
画面 6: 在 EditPlus 编辑器中，显示用于创建 Docker 容器的命令：Docker create --name es-node01 --net host -v /haoke/es-cluster/node01/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/node01/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4。
画面 7: 在 EditPlus 编辑器中，显示用于创建 Docker 容器的命令：Docker create --name es-node02 --net host -v /haoke/es-cluster/node02/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/node02/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4。
画面 8: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 9: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 10: 在终端中，进入 es-cluster 目录，列出 node01 和 node02 目录，进入 node01 目录，列出 jvm.options 和 Elasticsearch.yml 文件。
画面 11: 在终端中，显示 Elasticsearch 启动失败的错误日志，包含 java.nio.file.AccessDeniedException。
画面 12: 在浏览器中打开 Elasticsearch Head 插件，页面为空白。
画面 13: 在 PDF 文档中，显示集群状态查询结果：{"cluster_name": "es-itcast-cluster", "status": "green", "timed_out": false}，并说明主分片和副本分片。
画面 14: 在 PDF 文档中，显示使用 Docker 搭建集群的步骤，包括创建目录和修改配置文件，配置内容为：
cluster.name: es-itcast-cluster
node.name: node01
node.master: true
node.data: true
network.host: 172.16.55.185
http.port: 9200
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
discovery.zen.minimum_master_nodes: 1
http.cors.enabled: true
http.cors.allow-origin: " "

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
node.name: node01
node.attr.rack: r1
# Paths
path.data: /path/to/data
path.logs: /path/to/logs
# Memory
bootstrap.memory.lock: true

画面 3:
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
# Prevent the "Split brain" by configuring the majority of nodes (total number of master-eligible nodes / 2 + 1):
discovery.zen.minimum_master_nodes: 1
# Block initial recovery after a full cluster restart until N nodes are started:
gateway.recover_after_nodes: 3
# Require explicit names when deleting indices:
action.destructive_requires_name: true
http.cors.enabled: true
http.cors.allow-origin: " "
node.master: true
node.data: true

画面 4:
# Network
network.host: 172.16.55.185
http.port: 9201

画面 5:
cluster.name: es-itcast-cluster
network.host: 172.16.55.185
http.cors.enabled: true
http.cors.allow-origin: " "
node.master: false
node.data: true

画面 6:
Docker create --name es-node01 --net host -v /haoke/es-cluster/node01/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/node01/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/node01/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4

画面 7:
Docker create --name es-node02 --net host -v /haoke/es-cluster/node02/Elasticsearch.yml:/usr/share/Elasticsearch/config/Elasticsearch.yml -v /haoke/es-cluster/node02/jvm.options:/usr/share/Elasticsearch/config/jvm.options -v /haoke/es-cluster/node02/data:/usr/share/Elasticsearch/data Elasticsearch:6.5.4

画面 14:
cluster.name: es-itcast-cluster
node.name: node01
node.master: true
node.data: true
network.host: 172.16.55.185
http.port: 9200
discovery.zen.ping.unicast.hosts: ["172.16.55.185"]
discovery.zen.minimum_master_nodes: 1
http.cors.enabled: true
http.cors.allow-origin: " "

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13: PDF 文档中，架构图显示 node01 和 node02，node01 有 5 个分片（0-4），node02 有 5 个分片（0-4），并标注“主分片”和“副本分片”。表格数据为集群状态查询结果：{"cluster_name": "es-itcast-cluster", "status": "green", "timed_out": false}。

5) 不要评价画面美观，不要输出与课程无关的内容。

