# 13-Zookeeper的安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\13-Zookeeper的安装【海量资源尽在 ubkz.com】.mp4
- 时长 14分43秒（音频 883s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来进行Zookeeper的一个安装那么要搭建Zookeeper这个机群我们来先看一下我们的计划有三台机子那么这个三台机子的IP然后这是主机名后面还有一列是MyID的值这个是什么意思呢你可以理解成每一个Zookeeper节点的一个编号你看我刚才给大家画了一张图这个Zookeeper本身它也是一个机群它里边有leader
[00:29] 有follow那么他的每一个主机他的编号就是myid待会呢咱要去设置id好那么安装呢一共有几步呢我这里呢给大家呢列了这么几步一共有六步左右我们先看第一步那么要安装首先的下载这个压缩包这个压缩包呢你可以去这个网站去下载我把它复制一下来我们来看一下这个网站
[00:57] 这个是阿帕奇提供的一个Zookeeper的一个下载一个位置那么在这里呢我们可以去下载各种各样的版本那在这里呢大家不用下我已经给大家下载好了在我的这个在我的这个里边资料里边资料里边有一个叫Zookeeper 3.4.9我们用这个就可以了那好了我们接下来呢我们需要将这个压缩包上传到我们的这个Linux里面来
[01:27] 我还是拿第一台机子我进到这个software在这里呢我需要将我的压缩包上传找到我那个目录我这个在机盘在Hadoop lesson第01然后呢资料里边有一个ZOOkeeper好把它上传稍等好上传完之后呢我们就拿到了好拿到了之后呢接下来我们呢需要将它解到
[01:58] Service这个目录来解压这个字体有点小我把它调大一点稍等啊这个地方字体我调成18号字体吧这样稍微大了一点好那么接下来我需要将这个压缩包啊解压到我们上一级的Service目录那就是tar xvfzookper然后呢-c上一级里边有个什么Service进去好把它解压一下稍等
[02:30] 好 解压完之后我们回到上一级的Service这个目录你看它已经有了一个已经有了一个zookable 3.4.9接下来我们对它呢进行一些配置好 那么怎么配置呢首先我们要去修改配置文件这个zookable的配置文件呢在这个里边有个configure文件夹来 那么进到这个文件夹下面之后呢我们需要去把它的一个配置文件的模板然后呢拷贝份出来
[03:00] 接下来呢我们还要建一个文件夹建一个目录这里边呢存放ZooKeeper的一些数据来我们一个来操作第一步我们要干嘛呢我们要进到这个ZooKeeper这里边有一个configure文件夹一个目录然后呢进来进来之后呢这里边有个配置文件这个呢叫Zoo这个configure那这个地方呢这sample configure呢它应该是一个什么东西呢
[03:31] 它应该是一个模板那我们需要将这个模板呢拷贝一个zoo.cfg这个文件那我们拷贝一下cp zoosample然后呢拷贝个zoo.cfgok拷贝个文件出来拷贝完之后呢我们需要对这个文件进行修改好接下来我们还要干个事我们要去建一个文件夹这个文件夹呢来存放ZooKeeper的数据
[03:59] 我把这个直接粘过来走一下好我已经在这个我们的Zookkeeper目录下面呢创建了文件夹叫ZKData4好做完这一步之后呢接下来我们来看如何去修改这个配置文件在这个配置文件里边呢我们首先打开来看一下VMZOO.CFG好打开之后呢我们需要做以下配置第一个我们要指定
[04:29] Zookeeper数据的存放目录就是Data DR这个Data DR呢一定要和你刚才创建那个文件夹的路径一致我刚才是不是在创建了这么一个文件夹我把它直接复制过来稍等然后呢直接粘在这个位置或者说呢你先退出然后呢你看一下你刚才有一个命令这个命令是不是在这
[04:58] 在这里边建立文件夹把这个目录拷贝一下也可以的好我再回来再回来回来之后第一个就配好了那接下来我们还要配置什么呢我们还要配置一个快照的一个保留数量这个snap routine count把它设成3我们来找一下好向下走向下走找一找snap routine countOK这个把这个注释打开这个默认是注释的把它打开好这个是
[05:30] 它的一个快照数量还有一个呢我们要去配置这个日子多长时间清理一次叫part interval那这个地方我们也把这个注释打开默认是一个小时这个单位呢是小时的意思好那接下来呢我们还要在这个里边呢加入一些其他的一些信息我们要去指定我们这个Zookeeper集群中啊它的服务器地址好这个比较重要我把它全部复制过来把它粘在这位置
[06:00] 这给大家解释一下是什么意思啊嗯首先呢这个地方呢server代表我们的服务服务器点一呢这个一呢其实就是我们刚才看到那个myid你看向上翻这边有个表叫myid吗123这是每一个zookkeeper的一个编号所以这个就是第一个zookkeeper它在哪台机子呢在node01这是它的一些访问端口都是固定的好这是第二个zookkeeper它呢在node02
[06:31] 第三个呢在node03好我把它都配置完之后直接保存退出好退出完之后呢接下来呢我们还要做一件事情就是添加刚才那个myid也就是每一个zookipper的编号刚才呢我在这个export Service里边建了一个文件建了一个目录是吧叫zkdx那这个文件呢这个里边呢我们可以建一些文件叫myid
[06:59] 这样买底注意这个在第一台机子上做然后呢我去在这个文件中写一个1进去你看IACO1把它写到哪里呢写到这个文件来我们呢可以这样做我们可以这样做把它呢给我复制过来然后呢放在这个位置这句话的意思是我要把1这个数字然后呢添加到添加到哪里去呢添加到这个目录下面ZKDATAS买底这个文件
[07:30] 这个文件现在不存在我们来回车好你来看一下我们回到上一集我们进到这个ZKDatas这里边是不是一个myid你打开看一下myid这里边就有一个1当然了你也可以直接打开这个文件在这里边写个1都是可以的好这是第一台机子这个第一台机子配好之后呢接下来我们需要干个事情
[07:59] 把我们第一台机子配置的信息啊分发给另外两台好你看这我们要分发给另外两台分发什么呢把你刚才配置好的这个Zookeeper这个文目录直接发送给第二台和第三台来我直接拷贝好拷贝之后呢咱粘一下好这个地方我要发给node02把它把我的这个文件夹放在它的export Service下面走稍等好同样的也要把它
[08:34] 这个远程拷贝给node03这台机子走好稍等好拷贝完了拷贝完之后我们还要做一件事情因为我们是完全拷贝第一台机子的那么它这里边的myid都是一样的那我们需要呢将第二台和第三台的myid呢分别设置为2和3你可以在第二台机子上来执行这条命令走这地方走一下好这个意思就是将2写到这个文件这个文件原来是不是1呀
[09:09] 注意这个地方一定要用这种一定要用一个这样的一个监验括号不能用这种方式不能用两个因为两个是追加相当于呢把以前的数据保留了如果我直接写一个监验括号表示把原来的数据干掉写出新的值回程然后接下来呢我们再来一个把这句话呢复制一下吧好第三台机子呢我给它追加我给它写一个什么呢3
[09:41] 好你如果不放心可以确认一下你可以export我本来就在export Service是吧这个zookkeeper下面有个zkdf.data4.myid你看一下里边是不是散啊OK这个配好了好配好之后呢基本上我们的zookkeeper的配置基本上就结束了那接下来呢我们来启动一下这个服务怎么启动这个服务呢我们呢需要在三台机子上依次执行这个命令
[10:10] 这个命令就是执行zoocouper下面有个beam目录这个beam目录里边有个脚本就zk server.sh然后呢执行start你可以把这句话复制过来或者你直接在这敲也行来我们来试一下在这个哪里呢在这个beam目录下面对吧zoocouper一个beam目录beam目录下面呢有一个叫zk server是吧那我们这样我们进到这然后呢beam下面一个zk server
[10:41] sh 后面跟什么 start 走好 他说已经已经运行了ok 咱们这样启动完之后呢咱们再启动第二台来看一下那我们来一样的bin 下面一个 zk server稍等啊这个地方是bin 下面啊稍等我进去这个export Service ZooKeeper下面一个bin zk serversh 然后 start 走稍等好 他说已经启动了
[11:13] 第三台我们同样的进到Zookkeeper下面并下面有一个叫ZK ServerSH然后Start稍等好这个也启完了启动完之后怎么证明他们启动成功呢我们可以这样我们可以用GPS这个GPS呢它这个PS呢是显示进程你当前启动的进程而这个GPS呢就是显示加尔相关的进程也就是显示有哪些GVM走一下
[11:43] 你会发现这里边有个进程这个就是Zookeeper好第二台我们来看一下GPS好这个也是Zookeeper启动完了第三台GPS好Quarterman也启完了好那么到此为止呢我们这个Zookeeper集群就给大家搭建成功了好搭建成功了之后呢我们来思考一个问题我们说这个Zookeeper集群呢如果有三台
[12:12] 它有一个是leader有两个是follower那么怎么看谁是leader谁是follower呢我们来看这里一个命令这个命令呢就是查看启动状态我们来看一下这个叫status我们看这个能不能查到好稍等我们拿这里走你会发现呢第一台机子这个model呢它是一个follower它是一个从机那再看第二个再看第二台
[12:44] 把这个呢依然复制一下走或者说你直接拿到这个命令然后呢这个地方改成status也行第二台是leader那第三台呢我们来看status它也是一个follower也就是中间这台机子呢是一个leader两边都是一个follower为什么这样子呢我们可以给大家简单说一下它里边有一个选举算法它默认的选举算法是非常简单的
[13:16] 就是我启动的时候呢我第一台先启动那这个时候呢他是不能选举的那么当我第二台启动的时候呢他就可以开始选举算法这个选举算法呢他们相当于呢各自给各自投了一票第一台呢给他自己投了一票第二台呢给他自己投了一票然后这个时候他会统计啊我现在的票数是否过半因为我们是三台机子
[13:44] 那么过半呢只需要两台就行了他发现了票数已经超过一半了那这个时候就是进行票数的一个PK你会发现第一台机子给自己投了一票那第二台呢也给自己投了一票是不是相当于两个人各有一票啊那这个时候如果票数相等呢他要去比较他的什么呢就是我刚才给大家说的MID的值就这个值啊MID的值这个MID的值越大呀那么他就去这个
[14:13] 竞争这个leader也就是说谁的myid值越大谁就是leader所以说呢第二台就是我们的leader那当第三台在启动的时候呢因为leader已经选举选举过了所以说第三台只能当followOK只能当follow所以这个和你的启动顺序是有关系的好那么这个搭建完之后呢我们呢这个东西我们先先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在三台 Linux 服务器上安装并配置 Zookeeper 3.4.9 集群，包括下载、解压、配置 myid 文件和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程 PPT 页面，内容为“7.2 Zookeeper安装”，包含服务器 IP、主机名和 myid 的对应关系表，以及下载地址 http://archive.apache.org/dist/ZooKeeper/。
画面 2：在 Apache Zookeeper 官网下载页面，显示了多个版本的文件夹，鼠标悬停在 ZooKeeper-3.4.9 上。
画面 3：在 node01 服务器的 SecureCRT 会话中，进入 /export/software 目录，准备上传下载的文件。
画面 4：在 node01 服务器的 SecureCRT 会话中，执行命令 ls，显示了 ZooKeeper-3.4.9 文件。
画面 5：在 node01 服务器的 SecureCRT 会话中，进入 /export/servers/ZooKeeper-3.4.9/conf 目录，查看了 zoo_sample.cfg 文件。
画面 6：在 node01 服务器的 SecureCRT 会话中，查看了 zoo.cfg 配置文件内容，包括 dataDir、clientPort、maxClientCnxns、autopurge.snapRetainCount、autopurge.purgeInterval 等配置项，并执行命令 mkdir -p /export/servers/ZooKeeper-3.4.9/zkdatas 创建数据目录。
画面 7：在 node01 服务器的 SecureCRT 会话中，显示了 zoo.cfg 配置文件内容，包括 clientPort、maxClientCnxns、autopurge.snapRetainCount、autopurge.purgeInterval 等配置项。
画面 8：展示课程 PPT 页面，内容为“第四步：添加 myid 配置”，指导在第一台机器的 /export/servers/ZooKeeper-3.4.9/zkdatas/ 目录下创建名为 myid 的文件，内容为 1。
画面 9：在 node01 服务器的 SecureCRT 会话中，执行命令 scp -r /export/servers/ZooKeeper-3.4.9/ node03:/export/servers/，将 Zookeeper 文件夹复制到 node03 服务器。
画面 10：展示课程 PPT 页面，内容为“第二台机器上修改 myid 的值为 2”、“第三台机器上修改 myid 的值为 3”、“第六步：三台机器启动 ZooKeeper 服务”，并给出了启动命令 /export/servers/ZooKeeper-3.4.9/bin/zkServer.sh start 和状态检查命令 /export/servers/ZooKeeper-3.4.9/bin/zkServer.sh status。
画面 11：在 node03 服务器的 SecureCRT 会话中，显示了空的命令行界面。
画面 12：在 node02 服务器的 SecureCRT 会话中，执行命令 echo 2 > /export/servers/ZooKeeper-3.4.9/zkdatas/myid，创建 myid 文件并写入值 2，然后执行命令 cd /export/servers/ZooKeeper-3.4.9/，再执行命令 bin/zkServer.sh start 启动服务，显示服务已启动，最后执行命令 jps 确认 QuorumPeerMain 进程。
画面 13：在 node02 服务器的 SecureCRT 会话中，执行命令 bin/zkServer.sh status，显示服务状态为 Mode: leader。
画面 14：在 node01 服务器的 SecureCRT 会话中，执行命令 bin/zkServer.sh status，显示服务状态为 Mode: follower。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 中的配置文件内容：
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just
# example sakes.
dataDir=/export/servers/ZooKeeper-3.4.9/zkdatas
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
# Be sure to read the maintenance section of the
# administrator guide before turning on autopurge.
# http://ZooKeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
# The number of snapshots to retain in dataDir
autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
autopurge.purgeInterval=1

画面 8 中的 PPT 内容：
第四步：添加 myid 配置
在第一台机器的
/export/servers/ZooKeeper-3.4.9/zkdatas/ 这个路径下创建一个文件，文件名为 myid 文件内容为 1

第五步：安装包分发并修改 myid 的值
安装包分发到其他机器
第一台机器上执行以下两个命令
scp -r /export/servers/ZooKeeper-3.4.9/ node02:/export/servers/

画面 10 中的 PPT 内容：
第二台机器上修改 myid 的值为 2
echo 2 > /export/servers/ZooKeeper-3.4.9/zkdatas/myid
[root@node02 servers]# more /export/servers/ZooKeeper-3.4.9/zkdatas/myid

第三台机器上修改 myid 的值为 3
echo 3 > /export/servers/ZooKeeper-3.4.9/zkdatas/myid
[root@node03 servers]# more /export/servers/ZooKeeper-3.4.9/zkdatas/myid

第六步：三台机器启动 ZooKeeper 服务
三台机器启动 ZooKeeper 服务
这个命令三台机器都要执行
/export/servers/ZooKeeper-3.4.9/bin/zkServer.sh start
查看启动状态
/export/servers/ZooKeeper-3.4.9/bin/zkServer.sh status

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“7.2 Zookeeper安装”，包含一个表格，列标题为“服务器IP”、“主机名”、“myid的值”，内容为：
| 服务器IP | 主机名 | myid的值 |
| --- | --- | --- |
| 192.168.174.100 | node01 | 1 |
| 192.168.174.110 | node02 | 2 |
| 192.168.174.120 | node03 | 3 |

画面 8：PPT 标题为“第四步：添加 myid 配置”，内容为“在第一台机器的 /export/servers/ZooKeeper-3.4.9/zkdatas/ 这个路径下创建一个文件，文件名为 myid 文件内容为 1”。

画面 10：PPT 标题为“第二台机器上修改 myid 的值为 2”、“第三台机器上修改 myid 的值为 3”、“第六步：三台机器启动 ZooKeeper 服务”，内容为“三台机器启动 ZooKeeper 服务”、“这个命令三台机器都要执行 /export/servers/ZooKeeper-3.4.9/bin/zkServer.sh start”、“查看启动状态 /export/servers/ZooKeeper-3.4.9/bin/zkServer.sh status”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

