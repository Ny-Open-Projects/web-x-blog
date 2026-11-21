# 24.综合应用之部署MyCat集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\24.综合应用之部署MyCat集群【海量资源尽在 ubkz.com】.mp4
- 时长 11分23秒（音频 684s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来部署我们的mycat这个集群那么在前面的架构中呢我们来看一下那mycat呢是有两个这个节点来完成的那么来部署一下首先呢我们先来部署我们的节点1那么我们进入的首先进入到我们这个date的这个目录进入到date的这个目录然后呢我们这个下面呢它没有mycat的这个目录我们来创建一个mycat的目录然后呢我们再进入到这个mycat的这个目录
[00:28] 然后我们再去做我们的一个复制就是我们在之前是不是有一个叫做浩克下面有个mycat,mycat01然后能复制到当前的目录这个-r复制到我们当前的目录然后我们去做一些做个重命名跟我们这个简易都保持一致然后我们就把它设置为是一个node1mv它然后到一个它走好这样的话就
[00:58] 已经就从命名完成了好那么下面呢我们来修改它的配置文件那么首先第一个呢是它的server的配置文件那么把它呢就拷贝过来这个应该是一样的啊那么我们来看一下吧然后呢进入它然后呢在这个里面进入config然后呢我们进入我们的这个server.xml文件把这个就全部都拿掉吧然后呢我们重新再去写入内容好那么这个就是我们的一些配置基本的配置
[01:27] 好那么接下来呢我们来配置我们的scam文件scam文件呢就相对而言比较重要了我们一起来看一下那么在scam文件中呢我们首先需要配置的有三个这个集群首先第一个集群呢是我们的这个PXC集群第一个分片所以它是13306和13307OK那么并且在这个位置我们设置为它的一个负载均衡策略的V2我们来看一下为什么设置V2呢我们回到在前面我们找到
[01:56] 我们的这个找到我们的mycat的这个位置找到mycat在下面的有一个有一个我们的一个读写分离这个下面是不是有一个我们这个balance的一个说明如果为二的话就代表着所有读所有的这个读操作都随机的会被分配到我们的这个写节点和我们的读这个节点上面去为什么要这样去做呢原因是我们前面也说过
[02:24] 在我们的PXC集群中所有的节点都可以参与读写所以说我们选择策略为二这个一点要注意那么这个是我们的第一个集群就是PXC的第一个集群那么下面这个是PXC的第二个集群它是13308和13309同样采用的策略也是为二这个策略好那么第三个集群是我们的这个组从复制的集群
[02:52] 他所采用的策略是三这个策略去严格的去区分读写的操作那么在这个位置是有一个23306和23307没有任何问题然后继续往上面看那么在这个位置我们指定了这三个集群中的三个集群并且每个集群的一个数据库也做了一个指定并且给他们分别命名为DN1,DN2和DN3然后关键点来了看上面那么在这个位置定义这个schema的时候我们可以看到
[03:22] 那么如果是房源数据那么它所使用的这个DataNode是DN1和DN2然后并且采用的这个策略就是我们的一个根据这个ID取模这样的一个策略然后如果是我们的AD这张表所使用的是DN3也就是下面的这个就是我们主从复制的这样的一个集群的一个架构ok好嘞那么这样的话Scam是不是就已经配置好了好我们来打开我们Scam做一个处理好那么我们来打开这个Scam
[03:51] 然后呢把这个内容呢我们还是全部给它删除掉吧然后呢相当于做一个覆盖好那么我们去把我们这个拷贝一下然后呢到了粘贴哎OK好那么这样的话呢我们就已经把我们的Skymark配置文件呢全部都已经丢过来了应该是没有任何问题的然后呢保存退出一下好那么接下来呢我们来去修改我们的一些这个规则那么规则呢要把它改成二我们现在的几呢来看一下然后呢去搜一下走
[04:22] 那么现在就是没有问题OK搞定然后我们接下来就可以去做一些启动了当然我们要设置它的一个启动的一个端口我们还是打开一个配置文件我们去搜一下198然后我们把它改成几这是改成85改成85然后这个就搞定了对吧然后我们下面在我们的server中再添加这两个配置文件的一个端口然后我们再打开server
[04:51] 然后我们进入到这个位置来那么来创建这两个属性一个是18067一个是19067好这两个我们前面都加了一个1好把上面这个我们也整理一下把它整理到后面来OK好这样的话就搞定了server就搞定了那么下面我们就可以做一个启动了进入BIM目录然后我们尝试先去测试一下Minecart Console
[05:23] 然后呢我们去执行一下看他能不能够启动成功OK没有问题好嘞那么我们来检查一下当前有没有我们的Minecraft在跑在运行呢有先把这两个就杀掉了和505050走好那么再来检查一下没有了好那么我们就可以来启动他了那启动命令呢就可以使用他去做一个启动走那么我们这个就擦掉了那么他只要去能启动就OK了
[05:51] 好那么下面呢我们来做一个测试啊那我们依然的去连接到我们的这个呃mycat这个集群那么来创建一个192.168.1.18然后呢浩克然后呢mycat然后呢node1呃然后呢它的端口呃它的IP地址呢就是它它的端口呢是我们前面所说的啊这个叫做什么呢18067那么这个改成18067呃67
[06:21] 好那么它的一个账户名叫做itcast然后密码也是叫做itcast123连接测试一下没有问题连接成功了OK来看到是不是有两张表一个就是我们的ADD这张表一个就是我们房源数据表OK那么一会儿我们可以来做一下测试那么我们接下来去把这个数据我们去插入一下来看一下这个效果那么首先我们先把这个就拷贝过来
[06:49] 然后我们注意现在我们连接到的是我们的mycat然后我们把我们来看在这个位置创建一个新创建一个查询比较混那么我们先执行一条数据走那么这个数据是不是就已经插入成功了那么这个数据是会插入到哪里是不是它会插入到我们的pxc集群中那么pxc集群我们来看一下是不是我们的pxc集群是在这里对吧那么
[07:17] 这个里面有数据呢没有数据然后呢来看一下这个里面有没有数据呢发现他是不是有数据啊那么我们执行第二条数据来看一下那么第二条数据呢是在我们的node1里面有没有数据你发现有是不是有这个ID为2的数据那么在这个里面有没有数据呢你发现没有没有这个ID为2的这条数据那就说明什么呢说明我们的PXC它的一个分片是不是就已经启动用了哎呀OK那么两条数据一个里面是不是存储了一条数据啊做了分片
[07:46] 那我们再来看一下我们这个AD走那么AD呢我们要找到前面我们的这个Must那么来看一下数据没有问题那么这个Sleeve呢有没有问题啊找一下啊这个Sleeve01下面来看一下同样是不是也是没有问题的那就说明什么说明我们现在的这个主从复制这个集群中也能够正常去使用了同样也可以说明我们的Minecart的功能是不是正常我们刚刚的配置呢是一切是OK的没有问题
[08:14] 好嘞那么测试结果呢可以看到那么这个是我们PXC的Node1上面有一条数据PXC的节点上面有另外一条数据做了这样的一个分片而我们的主从的一个节点呢做了这样的一个配置没有问题哎OK这个呢就是我们的一个Minecart的节点的节点1的一个配置啊好那么下面我们来看一下节点2的一个配置那么节点2相比较节点1呢就变得更为简单了我们只要做一个复制就可以了我们来测试一下好那么我们来去
[08:43] 进入到我们的前面这个位置然后我们去做一个复制把它复制成node2ok好那么下面我们只需要修改端口是不是就可以了那么我们依然去修改它的配置文件我们进入这个mycatnode2下面进入config然后我们打开配置文件然后我们搜索198然后我们把1985改成1986看一下对不对1986直接改成
[09:12] 11986都可以那么就11986跟我们讲义保持一致好保存退出然后下面我们来继续修改我们的server配置文件那么这个原来叫18067我们全部改成68好那么往下面走在这个位置把它改成这个把它改成这个67改成68下面这个改成68好嘞保存退出
[09:39] 这样的话我们是不是都已经把端口三个端口就改完了那么下面我们来把它启动起来进入到B目录下面我们依然先做一个测试Console好那么来看一下它能不能够启动成功的没有问题好那么我们来检查一下我们的进程目前是不是有一个Minecart进程这是OK的没有问题好那么下面我们就来启动它直接启动那么启动之后它肯定就会有两个进程了OK好那下面我们再来测试一个连接那么把它关掉不关掉
[10:09] 把它也合起来然后呢我们刚刚是不是有一个这个sleeve有这个macad node1对吧那么我们这样我们把它这个名字呢我们来复制一下然后我们再来创建一个这个连接那么就是改成2就可以了然后呢这个IP这个IP地址是它然后呢这个端口呢刚刚我们所改的是这个18068所以改成18068
[10:36] 然后用用户名是叫做itcast密码叫做itcast123然后连接测试一下发现ok没有问题那么这个就是我们的第二个这个集群就是miket的第二个第二个节点那么这两个是不是他就组成了一个集群对吧组成了一个集群ok好没有问题没有问题ok那么在这个下面查询数据他同样也是没有问题的好嘞那么到目前为止我们的
[11:04] Minecart集群它的节点一和节点二是不是都已经创建完成了OK好那么到目前为止那么我们是不是就已经实现了在这个位置对吧后面这个是不是全部都已经搞定了这个也搞定了接下来是不是就要部署它就OK了好那么关于我们一个Minecart的集群的一个部署那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置和启动 MyCAT 分库分表中间件，并通过 Navicat 验证数据插入与分片效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Typora 中查看文档，弹出“新建数据库”对话框，设置数据库名为“haoke”，字符集为“utf8 → UTF-8 Unicode”。
画面2：在终端中进入 mycat 目录，创建 mycat01 文件夹。
画面3：在终端中编辑 mycat 的 server.xml 配置文件，显示了系统属性和用户配置。
画面4：在 Typora 中查看 schema.xml 文件，显示了数据库 schema 定义和分片规则。
画面5：在 Typora 中继续查看 schema.xml，显示了写库和读库的配置。
画面6：在终端中列出 mycat-node1 目录下的文件，然后编辑 schema.xml、rule.xml 和 wrapper.conf。
画面7：在终端中进入 mycat-node1 的 bin 目录，准备启动 MyCAT。
画面8：在 Navicat 中连接到 192.168.1.18:3306，查看数据库结构。
画面9：在 Navicat 中切换到 192.168.1.18:3307，查看数据库结构。
画面10：在 Navicat 中执行 SQL 插入语句，向 tb_house_resources 和 tb_ad 表插入数据。
画面11：在终端中查看 MyCAT 启动日志，显示连接建立。
画面12：在终端中进入 mycat-node2 的 conf 目录，准备启动 MyCAT。
画面13：在终端中启动 MyCAT 服务，显示启动成功。
画面14：在 Typora 中查看测试结果，显示数据已插入到 tb_house_resources 表中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
<DOCTYPE mycat:server SYSTEM "server.dtd">
<mycat:server xmlns:mycat="http://io.mycat">
  <system>
    <property name="name" value="mycat"/>
    <property name="useHandshakeV10" value="1"/>
    <property name="useSqlStat" value="0"/>
    <property name="useGlobalTableCheck" value="0"/>
    <property name="sequenceHandlerType" value="2"/>
    <property name="subqueryRelationshipCheck" value="false"/>
    <property name="processorBufferPoolType" value="8"/>
    <property name="handleDistributedTransactions" value="0"/>
    <property name="useOffHeapForMerge" value="1"/>
    <property name="memoryPageSize" value="64k"/>
    <property name="spillsFileBufferSize" value="1k"/>
    <property name="useStreamOutput" value="0"/>
    <property name="systemReserveMemorySize" value="384m"/>
    <property name="useZKSwitch" value="false"/>
  </system>
  <!--这里是设置的itcast用户和默认账户-->
  <user name="itcast" defaultAccount="true">
    <property name="password" value="itcast123"/>
    <property name="schemas" value="haoke"/>
  </user>
</mycat:server>

画面4：
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat">
  <schema name="haoke" checkSQLSchema="false" sqlMaxLimit="100">
    <table name="tb_house_resources" dataNode="dn1,dn2" rule="mod-long" />
    <table name="tb_ad" dataNode="dn1" />
  </schema>
  <!--配置分片关系-->
  <dataNode name="dn1" dataHost="cluster1" database="haoke" />
  <dataNode name="dn2" dataHost="cluster1" database="haoke" />
  <!--配置读写库-->
  <dataHost name="cluster1" maxCon="1000" minCon="10" balance="2"
            writeType="0" dbType="mysql" dbDriver="native" switchType="1"
            slaveThreshold="100">
    <heartbeat>select user()</heartbeat>
    <writeHost host="w1" url="192.168.1.18:3306" user="root" password="root">
      <readHost host="r1" url="192.168.1.18:3307" user="root" password="root"/>
    </writeHost>
  </dataHost>
  <dataHost name="cluster2" maxCon="1000" minCon="10" balance="2"
            writeType="0" dbType="mysql" dbDriver="native" switchType="1"
            slaveThreshold="100">
  </dataHost>
</mycat:schema>

画面5：
<writeHost host="w1" url="192.168.1.18:3306" user="root" password="root">
  <readHost host="r1" url="192.168.1.18:3307" user="root" password="root"/>
</writeHost>

画面10：
INSERT INTO tb_house_resources (`id`, `title`, `estate_id`, `building_num`, `building_unit`, `building_floor_num`, `rent`, `rent_method`, `payment_method`, `house_type`, `covered_area`, `use_area`, `floor`, `orientation`, `decoration`, `facilities`, `pic`, `house_desc`, `contact`, `mobile`, `time`, `property_cost`, `created`, `updated`) VALUES ('2', '城南三室一厅', '1', '2', '2', '2', '2000', '整租', '月付', '普通住宅', '100.00', '100.00', '2', '南北', '精装修', '有', 'http://itcast-haoke.oss-cn-qingdao.aliyuncs.com/Images/2018/11/26/154230290762227.jpg', '18888888888', '18888888888', '2018-11-16 11:34:02', '2018-11-16 11:34:02');
INSERT INTO tb_ad (`id`, `type`, `title`, `url`, `created`, `updated`) VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',

