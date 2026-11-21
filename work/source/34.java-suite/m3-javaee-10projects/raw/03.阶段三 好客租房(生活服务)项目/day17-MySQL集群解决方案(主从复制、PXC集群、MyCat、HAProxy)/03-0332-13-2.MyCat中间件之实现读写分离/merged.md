# 13-2.MyCat中间件之实现读写分离

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\13-2.MyCat中间件之实现读写分离【海量资源尽在 ubkz.com】.mp4
- 时长 13分28秒（音频 808s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就使用mycat来实现读写分离那么我们目前的mycircle的服务呢情况是这样的就是我们在这个1.18这台机器上面呢我们去跑了两个Docker的容器那么一个是3306一个3307然后他们角色一个是bust一个是sleeve好那么下面我们来看一下这个mycat怎么去那么我们进入我们的服务器然后呢进入到根目录下面吧然后呢我们进入到根目录下面有一个hooker
[00:28] 在这个下面呢我们去来上传一些我们的这个mycat这样我们去这样吧我们去创建一个目录吧叫make dr然后呢叫mycat然后呢我们进入了这个mycat的目录然后呢我们去找到我们的一个mycat的一个安装包这个呢给大家已经下载好了然后呢把它去上传到我们在这个下面有一个号客然后呢有个mycat把它呢丢到这个里面来
[00:58] 这样去做一个等待它的一个上传那么上传结束之后啊那么我们就可以去使用它了那么这样的话就OK了然后呢我们去做一个解压把这个压缩包呢解压开来然后呢没有去输入这个文件名字那么这样呢就修改就我们就已经解压完成了那我就把这个删掉吧把它删掉
[01:22] 然后我们去把它去做一个重命名比如说叫mycat然后重命名成mycat01比如说我们的第一个mycat然后我们进入mycat里面然后我们需要去修改它的一些配置文件配置文件是在config这个下面那么config里面有这么几个首先第一个需要修改的它的server.xml文件这个是所配置就是我们的一些全局性的一些配置项
[01:50] 以及我们的一些用户相关的一些信息那我们先来找到这个server的配置文件这个里面它呢有原有配置很多的一些内容那么把这个内容全部都给它删除掉然后呢我们再去做一个这个配置把这个全部都删掉那么按住这个D啊双选这个D啊然后呢就可以去做一个这个删除那么我们去那么稍等一下现在呢有点有点卡
[02:20] 然后我们把这个配置内容拷贝过来那么拷贝过来我们再来做一个解释那么在这个配置内容中前面这个配置项是它的一些全局的一些配置项然后下面这个是配置我们的一个User这个User是干嘛的是用于我们的客户端去连接到我们这个MAC去做一个使用的那么设置它的一个用户名是itcast密码是itcast123
[02:45] 那么他所去使用的一个scammer就是我们的一个数据库就什么呢叫做一个这个逻辑库啊叫做itcastok好保存这样的话保存退出那么这个server这个配置文件就搞定了那么下面我们来看一下scammer配置文件在这个配置文件中呢就是去指定我们的一些这个主从啊相关的一个配置项那我们一起来看这个配置的
[03:11] 那么我们可以看到在这个配置文件中首先我们来配置一个这个scammer就是我们前面所提到这个ID cast这个scammer然后它的一个表我们设置为是一个tb的ad这个表这个表是用于我们测试的一张表然后是data node设置为是一个DNE然后它的一个分片的一个规则是通过一个mode null就是我们去
[03:39] 作为一个取模其实我们现在呢只有一个分片啊这个这个其实你不配置也是可以的那么下面我们来看下面的配置啊在下面这个配置项中呢我们去配置了一个DataHost那么也就是我们数据的这个节点那么这个节点的名字叫做Cluster1然后呢然后我们下面去指定它的相关的配置项那么在这个里面有一个关键点就是一个balance等于3那这个balance等于3什么意思呢我们来看下面有一个说明就是
[04:08] 那么如果等于这个0呢这个balance首先呢它代表的是负载均衡如果等于0呢这代表着我们不开启读写分离的机制那么也就意味着我们肯定不能选它了对吧我们目的是要实现读写分离然后呢balance等于1呢代表的是代表是我们全部的这个读和这个被选的这个写参与这个select那么什么意思呢叫做
[04:33] 如果我们采用的是双组这种模式的话那么就M1和M2互为做一个组备那么这个时候是什么意思呢就是M1和S1是一对主虫那么M2和S2是一对是一个这个也是个主虫那么M1和M2是互为组备这种情况下面那么M2和S1以及S2
[04:57] 作为我们的一个slag的一个这样的一个负载均衡那么也就是说什么意思我简单的说一下就是那么我们有在等于一的时候就是我们有一个被选的一个这个master也要参与我们的一个读也就是说之前我们所说的读写分离是所有的我们这个读的这个操作都去进入到我们的sleeve节点上面OK那么如果balance等于二就代表了什么呢
[05:26] 我们所有的读的请求都随机的发送到我们的这个写和我们这个读的这样的一个机器上面去那么这个是二那么三的是所有读的这个请求发送给我们所有读的请求随机发送给我们这个reader就是读写这个请求所对应的读的那个上面然后呢写的这个机器不负责这个读的这个压力OK当然你要注意的是这个balance等于三呢是在1.4
[05:55] 以后才有的一个版本版本的才有的那么我们可以看到在这个位置所选用的是3那么就代表着我们会把所有的这个读放到这个读的这个节点上面去所有写的这个请求的去进入这个写的请求上面去也就是说我们彻底的去做一个读写的一个分离OK好那么其他这些参数的没有什么太好解释的然后在这个位置是一个心跳的检测去通过slack user去做一个查看然后下面注意
[06:24] 这个是关键的配置项来指定它的一个写的一个这个节点那么写的这个节点的是3306然后它的用户名是root密码的也是root然后呢这个写所对应的一个读的节点呢就是3307那么给它命名为是w1,1这么答案它的名字叫w1ok用户名的也是root和root
[06:50] 那么这样的话呢我们通过我们这样的一个配置呢就已经实现了一个读写的一个配置它俩是一对那么这个是这个是写这个是读ok然后呢我们把这个cluster1然后呢去配置到我们那个datanode这个上面来并且给datanode去指定它的一个我们这个叫什么呢它的一个名字叫做DNE啊就是我们的一个这个datanode的一个名字然后呢把它的又配到这个位置来
[07:19] 当然了在这个位置来指定我们的这个数据库中所使用的一个数据库叫什么呢叫itcast这个一定要注意好嘞那么接下来呢我们来打开我们这个scammer配置文件那么把所有内容给它删除掉然后呢我们再去做一个相关的一个配置ok好那么我们把这个配置内容呢我们拷贝过来那么我们来看一下那么我们做一个拷贝
[07:47] 好然后呢保存退出这样的话就OK了然后呢下面呢我们还需要配置什么呢配置我们的这个这个就是弱就是我们的规则由于前面呢我们在这个位置指定了一个分片指定了一个分片那么需要去配置它的一个值因为它要根据我们的一个ID呢去做一个取模当然其实我们说过你不配置也是可以的当然了我们还是严格的去做一个这个配置
[08:15] 那我们去这样我们去搜一下它吧然后呢去做一个搜索啊搜然后呢往下面搜然后看一下啊在哦在这个位置那么它的model是3那么我们现在只有一个节点设置为1就可以了哎好嘞然后呢当我们去三个配置文件全部修改完成之后啊那我们就可以去做一个启动了那么进入这个B目录
[08:38] 然后这个下面呢有一个叫做mycat啊这样的一个脚本那么执行一下mycat然后呢我们通过一个console那么去做一个测试看它是否能够跑起来那么当我们看到一个success的时候呢就代表着哎这个看到它的时候代表mycat就启动成功了那么这个时候呢我们就可以去做一个真正的做一个启动了然后呢执行这个下面的有一个脚本脚本叫什么呢叫做啊叫做我们这个startup去做一个启动那么点斜杠
[09:08] startup启动走那么这样的话他就跑起来了ok那么顺便我们来说一下minecraft怎么停止通过一个jps查看他的一个进程然后做一个q去做一个sus就可以了ok好那么现在我们那个minecraft就跑起来了跑起来之后我们就可以通过我们客户端去做一个连接那么下面我们来看一下连接怎么样去做一个连接那么我们在这个位置去新建一个mycircle注意还是新建mycircle
[09:35] 那么192.168.1.18然后呢我们来一个叫mycat吧然后mycat01然后呢我们来看一下到达然后呢它的这个端口是多少的我们来看一下这个讲义端口呢是默认是8066因为我没有修改就采用默认那么就是8066那么在这个位置叫8066然后呢
[09:59] 用户名要注意是不是刚刚我们所设置的用户名和密码就是谁的itcast在上面这个位置在这就是itcast和itcast123ok那么用户名就是itcast密码就是itcast123然后到这点击重新点击连接就可以了点击成功那么要注意那么现在我们所连接到的是mycat
[10:27] 他还会去连接到我们的MySQL做一个操作OK点击确定那么我们来打开这个MyCat来看一下那么等待他的一个连接可能会稍微有点慢我们来看他会什么情况
[10:44] 刚刚的那个去反应慢呢是原因是啊我们没有去创建一个数据库啊原因是我们刚刚在这个位置来看一下啊那么我们是不是指定所使用的数据库呢是itcast由于我们并没有数据库它呢会导致一个比较慢啊所以说呢我们在我们这个master里面创建一个数据库这个数据库就叫itcast然后呢我们来看一下它的编码设置为是utf-8好那么这个时候呢我们再来做一个测试啊那么咱们把它就关闭掉
[11:13] 打开这个时候是不是就非常快了哎OK好那么现在呢我们就已经连接到我们的mycat那么下面呢我们来做一个测试那么我们去创建这样的一张表我们在这个呃我们在这个itcast这个表这个数据库下面啊去创建这样的一张表那么这个表现在目前它是不存在的啊那么我们来创建一下那么怎么样创建呢在这做一个创建然后呢我们去做一个创建走那么现在显然是不是就已经创建成功了
[11:42] 然后我们在这个位置来刷新一下刷新一下这个表然后打开来看一下这个表就存在了那么接下来我们去向我们的这个数据库去插入数据要注意那么现在我所有的操作都是在哪里都是在基于这个Minecart做一个操作那我把这两个关闭掉别搞混然后做一个执行走那么数据是不是就插入成功了那么我们再进入这个里面刷新一下数据是不是就有然后我们就去
[12:09] 打开我们的真正的数据库注意这个是Minecat这个真正数据库那么你会发现下面这个数据库的数据依然是存在的把它关闭掉那么G5-3307这个里面的数据它同样的也是依然存在的OK好嘞那就说明什么我们现在通过Minecat是不是就已经可以对我们的数据库是不是做一个操作了OK那么这样的话它就会做一个读写分离因为我们在下面的这个位置
[12:38] 下面我们在这个位置是不是设置它的一个balance负载均衡的一个策略它会把所有读的请求呢去发送到这个3307上面来所有写的请求呢去进入3306OK那么这样的话是不是就实现了一个读写分离啊所以我们这样就通过这个mycat就实现了一个读写分离OK好那么你会发现那么我们是不是通过这个mycat去实现了读写分离之后呢是不是就正如前面我们数
[13:07] 说的这个架构那么我们应用程序是不是只需要去连接到MICAD就可以了没有必要去连接到我的两个这个节点对不对啊OK那么这样的话呢我们是不是就相当于说我们是不是使用的是一个这个节点啊OK好嘞好那么关于这个使用这个MICAD来实现一个读写分离那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置和启动 MyCAT 数据库中间件，包括环境准备、配置文件修改、服务启动及数据库连接测试。

2) 按时间顺序列出每张画面的要点：
画面1：
- 在 slave01 节点的 mysql 目录下查看内容，进入 master01 目录。
- 执行命令：cd master01
- 执行命令：cd conf
- 执行命令：ll（列出目录内容）
- 执行命令：vim my.cnf
- 执行命令：Docker restart percona-master01

画面2：
- 在 /haoke/ 目录下创建 mycat 文件夹。
- 执行命令：cd /haoke
- 执行命令：mkdir mycat
- 执行命令：cd mycat

画面3：
- 解压 Mycat-server-1.6.6.1-release-20181031195535-linux.tar.gz。
- 执行命令：rm -rf Mycat-server-1.6.6.1-release-20181031195535-linux.tar.gz
- 执行命令：mv mycat mycat01

画面4：
- 显示 mycat-server.xml 配置文件中的部分属性设置。
- 代码内容：
  <system>
    <property name="nonePasswordLogin" value="0"/>
    <property name="useHandshakeV10" value="1"/>
    <property name="useSqlState" value="0"/>
    <property name="useGlobalTableCheck" value="0"/>
    <property name="sequenceHandlerType" value="2"/>
    <property name="useCompression" value="1"/>
    <property name="fakeMySQLVersion" value="5.6.20"/>
    <property name="processorBufferChunk" value="40960"/>
    <property name="processors" value="1"/>
  </system>

画面5：
- 终端界面空白，等待输入。

画面6：
- 显示 schema.xml 文件内容，定义了数据表的分片规则。
- 代码内容：
  <schema name="TESTDB" checkSQLSchema="false" sqlMaxLimit="100">
    <!-- auto sharding by id (long) -->
    <table name="travelrecord" dataNode="dn1,dn2,dn3" rule="auto-sharding-long" />
    <!-- global table is auto cloned to all defined data nodes, so can join with any table whose sharding node is in the same data node -->
    <table name="company" primaryKey="ID" types="global" dataNode="dn1,dn2,dn3" />
    <table name="goods" primaryKey="ID" types="global" dataNode="dn1,dn2,dn3" />
    <!-- random sharding using mod shardin rule -->
    <table name="hotnews" primaryKey="ID" autoIncrement="true" dataNode="dn1,dn2,dn3" rule="mod-long" />
    <!-- table name="dual" primaryKey="ID" dataNode="dn1,dn2" types="global" needAddLimit="false" -->
    <table name="worker" primaryKey="ID" dataNode="jdcb_dn1,jdbc_dn2,jdbc_dn3" rule="mod-long" />
    <table name="orders" primaryKey="ID" joinKey="customer_id" parentKey="id" />
  </schema>

画面7：
- 列出 conf 目录下的文件，包括 schema.xml。
- 执行命令：vim schema.xml

画面8：
- 列出 conf 目录下的文件，包括 server.xml。
- 执行命令：vim server.xml
- 执行命令：vim rule.xml

画面9：
- 启动 MyCAT 服务。
- 输出日志：
  Running Mycat-server...
  wrapper -- Wrapper Started as Console
  wrapper -- Launching as Console
  wrapper -- MyCAT Server startup successfully. see logs in logs/mycat.log
  wrapper -- INT trapped. Shutting down.
  wrapper -- Wrapper Stopped

画面10：
- 在 Navicat 中新建连接，填写主机地址 192.168.1.10 和端口 8066。
- 弹出窗口显示“讲义.md - Typora”。

画面11：
- 显示 schema.xml 文件内容，包含 dataHost 配置。
- 代码内容：
  <dataHost name="cluster1" maxCon="100" minCon="10" balance="3"
    writeType="0" dbType="mysql" dbDriver="native" switchType="1"
    heartbeat="select user() from dual">
    <writeHost host="w1" url="192.168.1.18:3307" user="root"
      password="root" />
    <readHost host="r1" url="192.168.1.18:3307" user="root"
      password="root" />
  </dataHost>

画面12：
- 在 Navicat 中查看 tb_ad 表，显示为空。

画面13：
- 显示 PPT 页面，包含 MySQL 集群配置表。
- 表格内容：
  MySQL集群1：
  | 主机 | 端口 | 容器名称 | 角色 |
  |---|---|---|---|
  | 192.168.1.18 | 3306 | percona-master01 | master |
  | 192.168.1.18 | 3307 | percona-slave01 | slave |

  MySQL集群2：
  | 主机 | 端口 | 容器名称 | 角色 |
  |---|---|---|---|
  | 192.168.1.18 | 3316 | percona-master02 | master |
  | 192.168.1.18 | 3317 | percona-slave02 | slave |

画面14：
- 显示 MyCAT 架构图。
- 结构：应用系统 → 中间件 → MySQL（主）和 MySQL（从），中间件与 MySQL（主）和 MySQL（从）之间有同步箭头。

