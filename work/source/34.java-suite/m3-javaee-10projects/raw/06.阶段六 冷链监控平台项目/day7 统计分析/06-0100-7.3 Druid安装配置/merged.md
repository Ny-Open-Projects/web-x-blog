# 7.3 Druid安装配置

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.3 Druid安装配置_【海量资源尽在 666java.com】.mp4
- 时长 21分56秒（音频 1316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一看Apache Droid它的一个安装配置首先呢我们来看一看我们当前的Apache Droid它需要的一个环境我们当前的服务器呢实际上是一个最低的配置是两核8G内存的一个才能运行起来我们的Apache Droid当然了内存越
[00:19] 越大越好一般情况下可能都需要几十个G几百个G的这样的一个内存它是一个构成一个集群来作为ApacheJ的因为我们当前是在一个演示环境里边所以说我们用到了是一个两G的一个八核内存那么我们当前的环境是CintOS7然后我们的JDK是1.8ApacheJ的是0.15.0那首先第一步的话我们需要安装JDK
[00:44] 我们安装的是Oracle GTKOracle GTK我们可以通过Oracle的官方网站上来查看它的一个JDK然后呢从中下载我们的这种JDK的一个RPM文件因为CineOS也好还是Ubuntu或者其他的这个
[01:04] Linux的操作系统每个操作系统它安装方式可能都不太一样有一些的话是用RPM来安装的有的话是用YAML来安装的或者说用其他的apt-get这种方式来安装我们的jar 包或者安装我们的软件工具
[01:21] 那么我们在我们synos里边我们用到了这些rpm包那rpm包的话我们首先我们进入到我们的叫一个目录里边opt下面的一个software目录我们用wget-c这个命令来下载rpmwget-c的话这个-c是一个什么意思呢是一个参数
[01:41] 这个三数的含义是说当前如果你在下载某一个文件的时候如果这个文件如果是当前网络不通了或者说我一场我把这个断掉了那么下一次我在重新运行这个命令的时候它就能够在原来的基础上进行断点序传这就是所谓的断点序传对吧那我们下载完我们的JDK之后呢我们把我们JDK安装到一个目录里边我们把它这个拷贝到另外一个目录里边
[02:10] 名字其实改成我们的这个名字IPM名字因为刚下载下来的时候名字其实挺长的而且它赋予的名字其实不是我们容易辨解的一个名字那么我把它进行移动然后改名改成这个JDK-8u202的一个这样的一个IPM的一个弧键名
[02:31] 我们执行rpm的安装命令rpm是rpm的安装方式然后我们在加参数的时候是-rvh然后-rvh然后直接在rpm此时我们安装完了之后我们就可以通过加完-rolin来查看当前的我们JDK的它的一个版本了此时我们看到它的版本其实就是JDK的JDK 1.8.0的202的一个这样的一个版本我们都看到了
[03:01] 添加完这个版本之后我们需要在Java Home里面来添加我们的一些环境变量因为当前其实都是在安装安装我们的一个JDK那么安装JDK的过程都比较简单一点我在这里就是给大家顺一遍我们整个安装过程那么我们在安装的Java Home的时候我们需要打开或者是编辑我们的ETCETC下面有一个profile文件
[03:31] 那么我们再添加几行的代码这一行来讲的话就是aggport-home等于我们的DDK安装的路径对吧那么然后我们还有aggport-passpass等于原来的pass冒号我们的加了home斜杠的加了一个bin目录那么我们也要
[03:55] export我们的castcast就是我们需要把我们加home下的labels里边的这个tools的价和dt的价然后放到我们的castpart里边去那紧接着我要使我们的profile进行生效我们就要执行source的一个source然后我们这个profile文件我们在这个讲义里面都会写上
[04:18] 那此时我们要修改我们的hostname就是vim我们的-etc-host然后在这里面我们给它添加我们的127.0.0.1然后是我们的hostname就是主机的名字这是我们安装JDK的安装JDK的过程相对来讲比较简单一点然后网络的编程网络上的一些教程也都挺多
[04:42] 下一步的话我们安装我们的MySQL驱动MySQL驱动的话本身来讲的话它是我们的一个在Droid里边要用到的一个我们首先需要下载我们的MySQL-connector-java的5.1.1的版本
[05:01] 5.1.44-B这个版本的话是我们Droid里面要使用的当然现在我们还没有安装Droid我们现在实际上是加载了一个我们从网上把这个价包给它下载下来下载下来之后呢回头来我们就把它拷贝到我们的这个Droid的目录里面去那么我们Droid就能够访问我们的访问我们的MySQL了或者说和MySQL进行关联访问了那
[05:27] 第二步的话我们要安装我们的Zookkeeper第三步我们安装Zookkeeper安装Zookkeeper的方式也比较简单我们简单的过一下它是我们wget-cwget什么意思我们断电续传对吧我们把3.5.5这个版本给下载下来下载下来之后进行解压解压tr-xzf然后在我们把它语语到某个目录里边改成个名叫ZK3.5.5然后我们要把我们的
[05:57] ZOO下滑线simple的cfg就是配置文件然后改名叫ZOO.cfg这个配置文件然后我们就可以执行我们的这个启动了其实相对来讲也都比较简单一点那如果是说我们要我们启动的时候启动命令就是zk-server.sh然后start这个命令我们就会启动了当然我们要如果安装多台的话我多个
[06:21] 多个的话我们其实就需要在配置里边就是启动的时候我们选择不同的配置文件这是我们安装和启动我们的LocableLocable的方式相对来讲也比较简单也不是我们的一个重点安装卡不卡的同样道理我们就要先下载我们的卡不卡下载解压之后然后修改我们卡不卡的一个
[06:43] 一些配置信息这些配置信息里边包括我们Zokeyboard到底是在哪Zokeyboard服务器的IP和端口如果是多个Zokeyboard的话我们需要用多号来分割包括我们的log文件在哪包括我们的端口开放的是什么端口然后下一步的话我们就可以启动我们的Zokeyboard这就是Kavaka启动Kavaka的时候其实就到了我们的Kavaka的目录里边然后在B目录下的一个kavakas-server-start.sh
[07:12] 然后选择我们的server的配置文件然后把它启动起来OK这就是我们在启动Kafka的一个过程那下面进入我们的主题我们安装和配置我们的DroidDroid来讲的话它是当前版本是0.15.0那么我们
[07:33] 首先直接把我们的这个版本来下载下来wget-c这个命令把这个版本给下载下来那下载下来之后呢当然现在的版本可能要高一些了我当前我在开发这个项目的时候用的是0.15.0那么这个我们下载完了之后这个jar 包啊我们需要对它进行解压解压之后呢我把这个解压之后的包
[07:56] 扔到了就是这个移动到拷贝到我们的这个opt下面的一个droid目录里边而这个目录里边我们能打开就能看到我们相应的一些这个文件目录了那我们看一下我们本身现在在这个opt目录下opt目录下有一个droid那么我们看到我们这个droid里边包含了这么几块文件的内容一个来讲的话是文件夹是有我们的bin那么bin里边我们看一下我们的bin
[08:27] 这个bin的话其实就属于我们的这种server的一个一些启动命令启动命令里边有一个的话叫dcircle那我们知道我们连接mycircle的时候在mycircle安装的那台机器上其实有一个circle的我们直接连接circle的客户端对吧这个dcircle其实也是一样但就是连接我们J的一个circle的一个客户端工具我们能在这里边执行查询语句后面我们会给大家详细讲一下dcircle的一个使用那另外的话
[08:58] 我们可能在开发和实际使用过程中会用到了服务器的一个启动那么服务器分成好几部分一部分来讲的话是属于我们的一个机群另一部分还有一类的话是我们单台机器做的一个机群我们单台机器做的机群里边其实还包括很多的一个类型的一种叫small小的一个单机机群
[09:19] 然后呢还有一个叫做XLARCH超大型的这个单机机器那么这些是什么意思呢它其实是说我的服务器我的本身我们前面讲过我们的Droid它是分成五个Node接点来启动的对吧我有一个这个Middle
[09:34] MadeManager有个Broker有个Historical等等各样的五个节点而这五个节点呢我们其实是放在一台机器里面来启动的这是本身JED已经给我们配置好了那么我们再可以在我们进行学习测试的一个过程中或者开发过程中我们直接使用单个节点就可以了
[09:54] 我们要验证我们的逻辑那么真正的实际的开发或者实际的生产环境里面那其实是需要我们的运维工程师来给我们安装配置我们server就是JIT server的集群那我们在我们本次来讲我们使用的是这个start single-server的一个small小的那它大和小或者说中等呢主要取决于每个每一个这个节点它的配置的内存的大小对吧这现在是我们的闭幕录像那么我们再给我
[10:23] 在看到除了B目录下的话无间夹里边还有一个Config目录那么这个Config目录的话是包括我们一些配置信息那么我们主要用的是Droid目录里边就是Config下的Droid目录那么Droid目录里边还有和我们刚才那个B目录下的相对应的一个是集群的一个是Single Server就单机服务器的这样的一个配置信息我们进入到我们的Single Server那Single Server里边的话有Large大的Middle
[10:53] 中等的,微小的,小的,超大的我们使用的是small,小的一个集群小的一个单机集群我们在这里面,我们可以看到第一个有个broker也是我们的五个节点中的一个一个是broker,一个是coordinate,overload一个是historical,maid manager,以及router这是五个节点的配置信息他们有一个核心的
[11:22] 配置的一个信息就是下方线的一个comment目录里边而这个下方线comment目录里边的主要的是我们叫comment runtime property
[11:30] 那么common runtime property我们在这里面可能给大家要稍微的花点时间详细的讲一点了在中间的话我们关心的有几个部分一个部分来讲的话有个叫做Droid的extension load list那什么意思呢也就是说本身Droid的服务器作为一个数据库作为一个这种集群的服务器那它是允许各种插件的它
[11:53] 其他它提供的一些服务是通过插件的方式来添加进来的而这种插件呢其实就属于我们要添加的这个插件而这个插件在哪呢也就是说Jade提供了一个开发方式我们根据这种开发方式开发了一个插件这个插件在我们Jade中就能够进行使用那比如说一些常用的一些插件Jade Kafka Indexing Service这种Indexing Service其实就是我们在Kafka里边就Jade里边直接监听Kafka的一个服务器
[12:22] Kafka的一个topicKafka的一个主题一个队列那么我们看看我们这个它放在哪呢在这个目录里边其实就是有一个extension而这个extension呢extension里边它会有一些Kafka默认的一些扩展那么这种扩展来讲你比如说Abrot是序列化反序列化的然后Bicycle是基础的这个安全的一些策略的这个filter的话是可能是过滤的一个但是我我也没用
[12:54] 这ETC EC2的话就是那个云服务器EC2的好像是那个但是我也没用这个谷歌的一个然后HDFS这个是我们常用的一个常用的一个扩展HDFS的话也就是说我们在把我们的数据进行深度存储的时候我们如果这个深度存储的介质我们存储的是HDFS里边那么我们可以在把我们的就是在配置文件里边我们的扩展需要把它加进来
[13:23] JadeHFS storage这是一个存储还有的话是一个比较重要的是我们的MySQLMySQL metadata的一个storage也就是说我们的Jade它本身包含了一些原数据一些表也就是说Jade自己它是一个应用程序对不对它自己是一个应用程序来讲的话它能干嘛呢它能
[13:47] 接收数据他能存储数据他能查询数据给返回结果但是他自己作为一个应用程序他自己也有一些他自己的一个数据库的表结构对不对我们开发应用程序开发程序代码开发他的数据结构开发他的数据数据然后存储存储数据结构存储进去对吗那么对于这种对的也是这样的一个道理那在这个时候我们使用的是mysql来进行存储那往下边的话有一个非常重要的一点是我们的这个我们的我看看
[14:17] 我们的这个Jade的一个hostJade的一个路径对吧主机那主机的话我们就使用我们当前Jade存储的一个主机那还有的话是我们的Zookable的地址Zookable它的文件的路径是什么那么我们在这地方配置那么
[14:37] 下面一个重要的其实是我们Droid它的源数据存储在哪刚才我们介绍了如果要加入这个Droid用MySQL作为源数据的一个存储的话我们需要加载我们的一个extension加载我们的一个扩展就MySQLMetaData的storage的extension那么我们这是有了一个有了基础了有了基础之后呢我们要配置使用MySQL作为它的一个存储那这种存储的话包括我们MySQL类型是属于MySQL那我也可以用的Durbar的这个数据库那么用MySQL也可以对吧
[15:06] 用MySQL之后我们连接的配置一些信息连接的字符刷用户名和密码等等这些是我们当然还可以用Postgres的一个Circle这种数据库这几个数据库都可以假设我们多选一对吧要么我选derby用的MySQL或者是Postgres Circle我选了MySQL的话我把其他两个要给它注释掉选完了之后我要看我们的深度存储深度存储的话我可以选择我们的Local
[15:35] 也可以选择我们的HDFS也可以选择S3就是AWT的或者说AWT他们的S3的一个存储方式这是我们的原数据的一个存储那么我们提到原数据存储我们还可以看看我们原数据库的我们的这种它的一个存储我们看看它的数据库的一个结构也就是说是DRAI的数据库它
[16:03] Zray的应用程序它自己的一个数据库这个是没有这个是我们没给它当前用户当前的用户没有打开权限权限里面没有OK我们先不管它了我们回头回过头来再看看Zray的它的数据库的一个表结构但是数据库表结构也挺有意思的一个表结构
[16:42] 那另外的话我们把这个这一块给讲完的另外一块是我们的叫什么呢我们的J的它的日志文件存储的一个路径那存储在我们的我们在这里面可以配置一下那还有的话是我们的比如说像overload的一个节点coordinate的一个节点monitor的配置这些是我们使用默认的一些配置方式就可以了那当前所以说我们就直接使用我们的这个此时就可以配置好了
[17:11] 那配置完了之后呢那下一步的话其实是我们可以看到进入到其他的比如说像进入到broker诶 cd broker对我听写错了那到了broker之后我们有一个我们的这个manman的话是定义它broker的我们定义主要是在jvm里边jvm是我们当前这个这个节点它的一个jvmjvm的内存的一个大小
[17:45] 这个配置我们可以从通过这里边配置我们当前的比如说我们当前那个broker这个节点它的啊最大的内存和最小内存到底是是多少啊咱们这个这个是在这儿主要是在这个地方来进行配置的OK那我们呃配置完了之后下一步的话我们就需要启动起来就可以了对不对那启动的话我们在啊实际上还是到我们到我们的并目录下这个并目录下
[18:20] 而这个闭目录下的话其实就是一些刚才也给大家介绍了是我们的有一个stutterstutter single server这个是可以的我们现在使用tmcd.t的一个对的然后进到这里面这个里面是我前面启动了一次的那我把它取消掉停止的时候我就可以停止掉但是我要是启动的时候我直接就把我们的命令
[18:50] 给它调用过来启动起来就OK的它其实就是optdroid我们辨一下start single server small这个命令然后就把我们这个服务给启动起来了那刚才给大家介绍的其实就是我们如何来进行下载下载我们的这个droid安装一些JDK安装卡布卡安装组gibre然后甚至于把Maseco对
[19:18] 这个地方其实给大家也要说我们要把MySQL的GDPC的驱动因为我们知道我们在刚才配置里边配置了我们的extension就是扩展然后使用的是MySQL的一个metadata的一个storage也就是说是我们把DRAID它的原数据存储在MySQL里边所以说我们需要把配置文件就是MySQL GDPC
[19:47] MySQL的GDPC,然后拷贝到我们的最大的一个目录里面而这个最大的目录里面就是opt的extension我们的extension其实是在MySQL里面我们实际上是要把MySQL-connector-java-5.1.44-bin的一个jar 包我们要把这个jar 包放到我们的最大的目录里面
[20:22] 放进去之后其实就可以使用了这是我们从安装安装记录本的环境然后呢我们把它解压然后再进行配置然后定性启动这是我们整个过程就添加完了那这样添加完了之后呢相应的它是有几个端口启动起来的服务有几个端口而这有一个端口就是我们的什么呢就是我们的这个
[20:50] 页面的一个管理端的一个接口因为管理端的接口是四个八而四个八的这个接口OK它现在其实还没有启动没有完全启动因为它需要加载原来的数据然后在这个过程中我们可以看到我们的里面的一些信息了这是我们的启动页面然后后台的我们可以启动那启动了之后它的日志文件呢日志文件我们看一看它是放在
[21:27] 它是放在这个目录里面的实际上是我们的opt下的vrsv因为我们在配置里面其实已经看到它了我们看到这里面的一些文件有些日志文件这几个日志文件我们在里面都能够看到它这是我们针对于apache-droid的一个安装配置

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下安装并配置 Apache Druid，包括 JDK、MySQL 驱动、Zookeeper、Kafka 和 Druid 本身，并启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
要点：展示课程文档“1.2 环境”章节，说明环境配置为 2核、8G内存、CentOS 7、jdk 1.8、apache-druid 0.15.6，并给出 Oracle JDK 下载页面链接。

画面 2：
要点：展示设置 JAVA_HOME 环境变量的命令，以及编辑 /etc/hosts 文件添加节点映射。同时展示将 MySQL 驱动文件复制到 Druid 的 metadata-storage 目录。

画面 3：
要点：展示安装 Kafka 的步骤，包括下载、解压、配置 server.properties 文件（包含 ZooKeeper.connect 和 log.dirs 等配置），并启动 Kafka 服务。

画面 4：
要点：展示下载 Druid 的命令，解压后查看目录结构，包括 bin、conf、extensions 等目录。

画面 5：
要点：展示进入 Druid 的 conf 目录，准备进行配置。

画面 6：
要点：展示下载 Druid 的命令，解压后查看目录结构。

画面 7：
要点：展示 Druid 的配置文件说明，包括不同模式（cluster、single-server）下的组件配置。

画面 8：
要点：展示 Navicat Premium 的启动界面，版本为 12.0.18，用于后续数据库操作。

画面 9：
要点：展示进入 Druid 的 broker 目录，准备进行配置。

画面 10：
要点：展示进入 Druid 的 bin 目录，准备启动服务。

画面 11：
要点：展示 Druid 的配置文件目录结构，包括 cluster、common、historical、middleManager、master、query、broker、router、single-server 等子目录。

画面 12：
要点：展示进入 Druid 的 extensions 目录，复制 MySQL 驱动文件到 metadata-storage 目录。

画面 13：
要点：展示黑马程序员官网页面。

画面 14：
要点：展示启动 Druid 单节点服务的命令，以及 Navicat Premium 中显示的 Druid 数据库连接成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```text
2核，8G内存，CentOS 7，jdk 1.8，apache-druid 0.15.6
https://www.oracle.com/technetwork/java/java-archive-139210.html
在下载页面选择java SE 8 rpm文件，下载过程中需要登录oracle网站，安装jdk：
[root@node2-vmb6 ~]# cd /opt/software/
[root@node2-vmb6 software]# wget -c https://download.oracle.com/otn/java/jdk/8u202-nh8/156187064c90e26a475fa801551e/jdk-8u202-linux-x64.rpm
AuthParam=156187064c90e26a475fa801551e/jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# mv jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# rpm -ivh jdk-8u202-linux-x64.rpm
[root@node2-vmb6 software]# java -version
```

画面 2：
```text
设置JAVA_HOME环境变量：
[root@node2-vmb6 ~]# vim /etc/profile
export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL
--此行之后插入以下设定
export JAVA_HOME=/usr/java/JDK 8.0_202-amd64
export PATH=$JAVA_HOME/bin:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
export CLASSPATH=.:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar
[root@node2-vmb6 ~]# source /etc/profile
设置hostname
[root@node2-vmb6 broker]# vim /etc/hosts
127.0.0.1 node2-vmb6.yyy
1.2.2 安装mysql驱动
将mysql驱动放置在extensions/mysql-metadata-storage目录下。
[root@node2-vmb6 ~]# cp /opt/software/jar/mysql-connector-java-5.1.44-bin.jar
/opt/druid/extensions/mysql-metadata-storage/
```

画面 3：
```text
# 下载Kafka
[root@node2-vmb6 software]# wget -c https://archive.apache.org/dist/Kafka/2.1.2-3.1.0.tgz
[root@node2-vmb6 software]# tar -zxvf kafka_2.12-2.3.8.tgz
[root@node2-vmb6 software]# cd /opt/software/kafka_2.12-2.3.8
# 配置Kafka服务器，日志目录，端口等
[root@node2-vmb6 config]# vim /opt/software/kafka_2.12-2.3.8/config/server.properties
ZooKeeper.connect=172.17.0.143:2181
log.dirs=/tmp/Kafka-logs
listeners=PLAINTEXT://172.17.0.143:9092
advertised.listeners=PLAINTEXT://172.17.0.143:9092
# 启动Kafka
[root@node2-vmb6 kafka_2.12-2.3.8]# cd /opt/software/kafka_2.12-2.3.8
[root@node2-vmb6 kafka_2.12-2.3.8]# ./bin/Kafka-server-start.sh config/server.properties &
# 关闭Kafka
[root@node2-vmb6 kafka_2.12-2.3.8]# ./bin/Kafka-server-stop.sh
```

画面 4：
```text
下载Druid，下载页面：https://druid.apache.org/downloads.html
[root@node2-vmb6 software]# wget -c http://mirrors.bjt.edu.cn/apache/incubator/druid/0.15.0-incubating/apache-druid-0.15.0-incubating-bin.tar.gz
[root@node2-vmb6 software]# tar -zxvf apache-druid-0.15.0-incubating-bin.tar.gz
[root@node2-vmb6 software]# mv apache-druid-0.15.0-incubating apache-druid
--执行文件
--配置文件
--扩展文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的Hadoop依赖文件
--Druid的H

