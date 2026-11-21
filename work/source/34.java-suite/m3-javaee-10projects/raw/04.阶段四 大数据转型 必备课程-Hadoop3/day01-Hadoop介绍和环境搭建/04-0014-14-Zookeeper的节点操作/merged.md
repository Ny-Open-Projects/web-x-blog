# 14-Zookeeper的节点操作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\14-Zookeeper的节点操作【海量资源尽在 ubkz.com】.mp4
- 时长 13分53秒（音频 833s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在搭建好ZooKeeper的一个集群环境之后接下来我们利用这个集群对ZooKeeper上的一些文件系统进行一个增传改查好 那么在做这些操作之前我先给大家讲一下ZooKeeper的一个文件系统的布局好 我们来看一下ZooKeeper的文件系统这个ZooKeeper文件系统和我们的Linux非常的相似它最上面也有一个根
[00:31] 那根下面呢有很多的子目录子目录或者子节点都行比如说我APP1那这个地方是APP2好那么这个它呢连在根这个节点下面而这个APP1和APP2呢它被称为在Zokey里边呢被称为Znode这个Znode右边呢这个也被称为Znode而每一个Znode呢
[01:04] 都可以使用一个路径来表示那这个比如说呢这个Znode它的路径呢是什么呢是根下面的APP1这么一个路径好那接下来呢每一个Znode下面呢还可以有子节点来继续来我再画一个比如说这个呢是A这是A这个是B而这两个呢也被称为ZnodeZnode呢是整个这个Zookeeper文件系统中
[01:38] 最基本的一个组成单位好那么这个这个Znode比如说我要用路径来描述呢它这个地方应该这样写它在哪呢在App1下面的这个AOK好了这是它一个路径好有了这个之后呢大家注意这个Znode相当于一个节点这个节点呢和Linux很像但是它又不同不同在哪里呢注意这个Znode呢它既具备目录的特性
[02:06] 什么意思呢就是它下面还可以再有新的一些节点是不是像一个目录啊它又有文件的特性为什么说这个Znode又有文件的特性呢因为它本身呢是可以存数据的啊待会我给大家演示这里边可以存数据这个数据量呢一般有限制一般呢不能超过一兆主要是放一些配置信息好 这是这个而每一个Znode呢基本上有三部分组成我来记一下
[02:35] 每一个Znode有三部分组成哪三部分呢第一部分呢是它的状态State就它的一些状态信息第二个呢是它的一个数据Data第三个呢是它的一些这个Trader它的一些子节点OK有三个组成好那么咱们先了解到这里接下来我们就可以通过命令对这些节点呢它的数据
[03:09] 进行送上改差回到我们的Linux那我接下来问大家一个问题我在哪里去敲这个命令呢那么在闭幕的下面有一个文件这个文件我们刚才用的是ZK Server来启动我们的Zookip它还有一个叫ZK Client这个ZK Client就是我们的客户端有两个上面这个呢我们不用我们用下面这个Share脚本那就是ZK Client SH
[03:40] 直接回车就可以了稍等你看呢这个时候呢它有一个有一个这么一个终端那这个地方呢我们可以输入一些东西当你不知道输什么的时候呢你可以随便敲一个回车你看这里边呢有了一些信息这些信息呢就是一些帮助信息告诉你呢你在这里可以敲哪些呢命令好你比如说呢有一个RS后面跟一个路径它可以显示这个路径下面的信息来我来弄一个
[04:10] LS比如说我写个根也就是我想看一下根下面呢有哪些目录走你会发现这里边有一个zookip这个是一个默认的一个节点这个节点是系统的好那接下来呢我们呢可以在这里边创建我们自己的一些节点怎么创建呢我们来看这个命令这个命令呢第一个命令叫create就创建xeno的也就创建我们的节点这个里边有两个参数一个是-s
[04:40] 一个是杠1然后呢后面跟上路径然后再跟上它的数据这个里边呢大家注意这个杠S呢是创建顺序节点而杠1呢是创建临时节点它们分别怎么用好我来给大家演示接下来我给大家创建一个简单的节点在这里怎么用呢我来create然后呢后面跟上一个路径我在根目录里边创建一个app1
[05:09] 然后我给它携带一个数据比如说携带一个数据叫hello回车好咱们来看ls根你会发现这里边多了一个节点app1就这么简单这是创建一个非常普通的一个节点好那这个地方呢我可以给大家记到这里这是创建节点那我记到这个位置吧好第一呢是创建普通节点好在这在这里
[05:47] 好那接下来呢我们来看第二个我们还可以创建什么呢我们还可以创建一个顺序节点创建顺序节点什么叫创建顺序节点呢我们只需要在这里写个create然后呢这个地方呢我写一个-s加个-s参数app2然后这地方呢我写个也给它写了一个参数word走来我们来看
[06:19] 你会发现很奇怪我明明写的是APP2它在后面给我加了一个数字加了一个编号这就是所谓的顺序节点那假如说我再创建一个再创建APP3你看这走来LS你会发现这个地方呢APP3呢它的数字是02刚才是01 02然后依次递增这是它的一个顺序节点那我把这个呢给大家复制一下好稍等
[06:50] 这是创建顺序节点好那我们还可以创建什么节点呢我们还可以第三我们还可以创建临时节点好创建临时节点呢有一个参数叫-1这个-1呢是一个临时节点OK那来我们来回到这个地方我们可以来来一个-1比如说我写个temp好吧temp node然后这个写的参数呢随便写了一个比如说写了一个加吧好走我们来看一下
[07:25] 你发现这里有一个type node大家请注意这个临时节点它的状态是临时的当我的客户端和服务器之间断开之后这个数据就消失了来 不行 我们试一下比如说我现在我退出这个客户端输个quit就可以退出好 退出之后我再进来稍等再进来之后我们来看ls来 看看根目录走你会发现我刚才别的节点都有
[07:55] 只有那个temp是不是没有了这是一个临时节点这个临时节点很有用的我们后边呢会结合其他内容给大家讲解好大家先记住这个临时节点好那么还有一个呢还有一种方式我可不可以把这两个都用一下呢就是既有杠S又有杠E那这个是什么意思啊这个表示是不是既是顺序节点是不是又是一个临时节点当然是可以的好我先把这个笔记给大家记一下
[08:24] 刚才是创建临时节点把这个复制一份这个地方呢这个地方是加杠1然后呢这个地方是temp然后node好了那么咱看最后一个创建顺序的临时节点好拿到这里那我就create杠s杠1然后呢这个地方我写一个temp node2这个地方可以加个数据吧aa
[08:58] 大家请注意这个顺序节点就是它在后面加了一个编号而这个临时节点就是数据是临时的走我们来看一下这个地方我们来看刚才是我创建的是temp node02是不是然后这个地方是4这个地方也有个编号好这就是一个节点的四种创建方式希望大家下去练习一下我把这个也复制一下好稍等好拿到这里
[09:33] 那么创建完这个节点之后呢它还有其他的一些命令比如说我们来看一下比如说get这个呢可以获取节点的数据那这地方呢比如说呢我们回到这里我刚才创建了一个节点叫app1比如说我想获取它的数据就是getapp1好走你发现了这个getapp1之后呢它输出了很多的信息那这个就是它节点的数据下面呢就节点了一些其他的信息就是状态信息
[10:02] 比如说这个number求准你有没有子节点呢没有你的数据长度呢是5这么一个东西那一个节点呢我可以给它创建子节点比如说我这样子你看啊我create然后呢我app1然后呢这个地方我写个test1这个什么意思呢这个表示我在app1这个节点下面呢又创建个test1我也可以给它写了一个数据比如说这个数据呢我随便写一个
[10:32] 比如说我写个HadoopOK回车好那么这个时候呢我们再来看我们来看get app1走你会发现它说它有一个子子节点1那比如说我要想获取这个test1我怎么写呢注意你应该这样写get app1test1回车这个时候我们是不是拿到了这个Hadoop这个数据好这是这个get
[11:01] 那还有什么呢还有一个这是getget我再记到这里吧第五获取节点数据那这个就是get然后呢跟上一个目录比如说呢app1那就行了哦这地方来我们来记下那接下来呢我们除了可以可以创建获取之外呢我们还可以对它进行了修改那第六我们可以修改节点数据修改节点数据呢
[11:33] 这个地方有一个方有个有个命令叫site来我们来试一下比如说呢我site我想把app1的数据呢改成别的就是site app1然后呢后面跟上一个值吧比如说跟上值叫OK走好那这个时候我们为了证明它已经修改了我们再来获取app1走一下你看数据是不是已经更改了好这是site那最后再看一个要删除delete
[12:03] 好删除可以删除一个节点比如说呢我想把谁删呢我想把app1删了delete app1走你会发现它有个提醒它说node not empty说app1这个节点呢它不为空也就是说app1有子节点那这个你是删不了的那我非得想删怎么办呢那这个地方呢还有一个叫地归删除的命令叫rmr这个呢它可以去地归删除r
[12:34] m r然后呢app1走哎你会发现他这个已经被删除了啊这个东西大家注意这里边有一个节点就是zoomkeeper这个不能删除这是系统的好注意这是删除最后呢还有一个叫history这个是列出历史的一些记录哎我们来试一下storhistory这是你曾经输过的一些meaning呢都在这里好这是他的节点操作
[13:02] 那么这个地方我们来记一下修改数据就是siteapp1后面跟上一个比如说XX好这个地方这样子第七我们可以删除节点有两个一个叫delete这个删除节点删除的节点不能为空不能用子节点有子节点好那这个地方还有一个叫rmr
[13:38] app1这个是地归删除就是我不管你有多少个子节点全部删除好这里边呢就是这么几个操作常用的就这么多我们先停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 ZooKeeper 的 Shell 客户端进行节点（Znode）的创建、读取、修改和删除等基本操作，并展示其特性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 2: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，列出了可用的命令，如 stat、set、ls、delquota、ls2、setAcl、setquota、history 等。
画面 3: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 4: 展示了 Typora 文档中“Znode 的特点”部分，说明 Znode 是文件系统的核心，选取时需用路径形式，Znode 本身不是文件，是树状结构，具有原子性，数据最大长度为 1M。
画面 5: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create /app1 hello、create -s /app2 world、create -s /app3 world 等命令，创建了三个节点。
画面 6: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create -e /tempnode java 命令创建了一个临时节点，然后执行 quit 命令退出会话。
画面 7: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，显示了客户端连接 ZooKeeper 服务器的详细日志，包括 session id 和连接建立成功。
画面 8: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create -s -e /tempnode2 aaa 命令创建了一个带数据的临时节点。
画面 9: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 10: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create /app1/test1 Hadoop、get /app1 命令，获取了节点数据。
画面 11: 展示了 Typora 文档中列出的 ZooKeeper 操作步骤，包括创建普通节点、创建有序节点、创建临时节点、获取节点数据、修改节点数据、删除节点。
画面 12: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 delete /app1 命令，提示节点不为空，无法删除。
画面 13: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 rmr /app1 命令删除节点，然后执行 ls / 和 history 命令查看目录和历史记录。
画面 14: 展示了 Typora 文档中列出的 ZooKeeper 操作步骤，包括创建临时节点、获取节点数据、修改节点数据、删除节点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
/export/servers/ZooKeeper-3.4.9/bin/zkServer.sh status
```
画面 2:
```
ZooKeeper -server host:port cmd args
stat path [watch]
set path data [version]
ls path [watch]
delquota [-n|-b] path
ls2 path [watch]
setAcl path acl
setquota -n|-b val path
history
redo cmdno
printwatches on|off
delete path [version]
sync path
listquota path
rmr path
get path [watch]
create [-s] [-e] path data acl
```
画面 3:
```
/export/servers/ZooKeeper-3.4.9/bin/zkServer.sh status
```
画面 4:
```
Znode 的特点
• 文件系统的核心是 Znode
• 如果想要选取一个 Znode，需要使用路径的形式，例如 /test1/test11
• Znode 本身并不是文件，也不是文件夹。Znode 因为具有一个类似于 Name 的路径，所以可以从逻辑上实现一个树状文件系统
• ZK 保证 Znode 之间的原子性，不会出现部分 ZK 节点更新成功，部分 ZK 节点更新失败的问题
• Znode 中数据是有大小限制的，最大只能为 1M
```
画面 5:
```
[zk: localhost:2181(CONNECTED) 1] ls /
[ZooKeeper, app1]
[zk: localhost:2181(CONNECTED) 2] create /app1 hello
Created /app1
[zk: localhost:2181(CONNECTED) 3] ls /
[ZooKeeper, app1]
[zk: localhost:2181(CONNECTED) 4] create -s /app2 world
Created /app2000000001
[zk: localhost:2181(CONNECTED) 5] ls /
[ZooKeeper, app1, app2000000001]
[zk: localhost:2181(CONNECTED) 6] create -s /app3 world
Created /app3000000002
[zk: localhost:2181(CONNECTED) 7] ls /
[ZooKeeper, app1, app2000000001, app3000000002]
[zk: localhost:2181(CONNECTED) 8] 
```
画面 6:
```
[zk: localhost:2181(CONNECTED) 9] create -e /tempnode java
Created /tempnode1
[zk: localhost:2181(CONNECTED) 10] quit
Quitting...
2019-04-22 15:32:59,601 [myid:] - INFO [main:ZooKeeper@684] - Session: 0x16a43cbfb150003 closed
2019-04-22 15:32:59,603 [myid:] - INFO [main-EventThread:ClientCnxnEventThread@519] - EventThread shut down f
or session: 0x16a43cbfb150003
[root@node01 ZooKeeper-3.4.9]#
```
画面 7:
```
2019-04-22 15:33:02,441 [myid:] - INFO [main:Environment@100] - Client environment:user.name=root
2019-04-22 15:33:02,442 [myid:] - INFO [main:Environment@100] - Client environment:user.home=/root
2019-04-22 15:33:02,442 [myid:] - INFO [main:Environment@100] - Client environment:user.dir=/export/servers/zoo
keeper-3.4.9
2019-04-22 15:33:02,449 [myid:] - INFO [main:ZooKeeper@438] - Initiating client connection, connectString=loca
lhost:2181 sessionTimeout=30000 watcher-org.apache.ZooKeeper.ZooKeeperMain$MainWatcher#950c6589e
Welcome to ZooKeeper!
2019-04-22 15:33:02,504 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@1032] - Opening
socket connection to server localhost:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknow
n error)
JLine support is enabled
2019-04-22 15:33:02,600 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@876] - Socket co
nnection established to localhost:0:0:0:0:0:0:1:2181, initiating session
2019-04-22 15:33:02,623 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@129

