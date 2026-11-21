# 13-1.MyCat中间件之实现数据分片

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\13-1.MyCat中间件之实现数据分片【海量资源尽在 ubkz.com】.mp4
- 时长 17分7秒（音频 1027s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么接下来呢我们来看一下数据分片那么什么叫做数据分片呢我们首先来看一下我们前面这个架构那么这个呢是我们一个中间件的一个架构对吧那么我们使用这种架构呢就已经实现了我们的读写分离但是呢我们好像似乎有一个问题还没有解决什么问题呢我们来看一下那么这个问题呢它就是那么我们把这个图
[00:25] 拿过来看一下啊那么这个问题呢就是那么我们所有目前的这个操作啊所有这个我们这个目前这个操作啊
[00:33] 我们都是把数据是不是写入到一个组结点中然后再同步到我们的重结点中对不对那么我们的组结点那么是不是它只是一个单结点在存储数据我们似乎并没有解决什么呢并没有解决我们这个数据存储量的问题因为我们的数据存储量依然决定于我们组结点它的一个存储量
[00:56] 对不对啊那么我们要想解决这个问题呢那么必须采用分片那么什么意思我们来看一下那么我们就需要呢可以有多个我们这个主节点或者说多对这个主从这个节点比如说我再来一个啊再来一个比如说呃我在这然后呢我再来一个我放到这对吧放到这呃然后呢我就可以这么去玩就说我的这个中间件呢可以写入数据的时候它可以写到这个里面来
[01:24] 对吧也可以去写到这个里面来然后呢数据在同步到这个筹啊同步到他左对的这个筹也就说他们是一对他们是一对他们是一对啊那么我们这个组和这个组以及这个组呢它呢其实形成的是一个整体那我可以把这三个节点看作是一个大的节点
[01:47] 然后呢去存储数据那么这个时候呢就会涉及到一个数据的分片你比如说我现在总共呢有三条数据去写入那我是不是就应该这个里面写一条这个里面写一条然后呢这个里面去再写一条那么这样的话是不是就能够去在我的这个把数据啊分摊到这么几个节点中那么我整个这个节点啊或者整个集群存储数据的能力是不是就变强了
[02:14] 对不对所以这个呢就叫什么呢就叫分片啊一定要区分出来它和之前的读写分离这样的一个区别那么在我们数据分片之后呢依然是可以做读写分离的你比如说他的一个读写是写到这个里面来读是到这个里面去读其实都是一样的啊这是一样的好嘞那么接下来呢我们就来看一下这个数据分片这个架构怎么去做那么我目前是不是已经有了一个集群一
[02:43] 对吧就是我们刚刚所搭建的这个3306和3307那么接下来呢我们来搭建一个机群2那当然我们这个图里面呢是有三个这个节点那么我们实施的时候呢我们搭建的是两个这个节点那么它的机器呢还是在这台机器然后呢端口呢是3316和3317好那么下面呢我们就来具体的实施一下参考下面的这个讲义的内容去做一个实施
[03:08] 那么我们把这个目录创建一下注意你看现在这个master是变成02对吧然后呢我们去创建一下这个目录呃走然后呢我们去进入到这个目录中呃然后呢我们在这个目录下面创建两个目录呃一个呢是config一个是我们的data好那么然后呢我们给他去做一个掃权呃然后呢进入到config目录vim打开一个my.config
[03:39] 好那么我们输入下面这个内容这个内容大家并不陌生了跟我们第一个主节点内容呢是完全一样的对吧那么服务ID呢也是1那么有同学可能会说了哎老师前面说过服务ID不是不能重复吗要注意的是这个因为它属于另外一个集群了对吧那么他们的这个只要他们在内部这个集群内部的服务ID
[04:03] 不重复就可以了它和另外的这个机群的伏歪地没有关系啊ok好那么保存退出好那么这个配置文件就搞定了那么下面呢我们来看一下创建容器这个容器呢所指向的目录都是我们刚刚所创建的这个master02的这个目录啊你可以看到在这儿然后呢还有呢是在这儿然后它的一个端口是3316啊3316然后呢我们来创建这个容器创建容器好然后呢我们去把这个容器呢去
[04:33] 启动起来等待它的一个启动那么启动成功之后呢它依然会去做一个这个初始化那么我们在这个位置呢再来去哎把这个把这个就关掉啊然后呢把这个关掉然后呢我们再来创建一个连接192.168.1.18然后呢master0202多少呢3316啊这个3316啊然后呢我们把这个IP地址拷贝一下拷到这
[05:05] 然后呢这个端口呢是3316密码是root然后呢测试连接连接成功了然后呢我们来看一下这个master02这个里面OK它呢也是OK的没有任何问题好嘞那么这个呢我们就搞定了
[05:23] 然后我们接着继续往下面看那么下面我们就需要去做一些授权这个动作因为它也要配置主从是不是然后我们在这个里面去点击查询创建一个查询走那么这三个内容这三行命令就不做一个解释了然后走好然后我们来看一下它的主的一个状态走那么这个它的主的一个状态一会儿这个数据我们需要
[05:50] 好那么接下来呢我们来配置我们的sleeve从注意这个sleeve02啊然后呢我们再来创建一个目录呃然后呢我们再去进入到这个目录中再去创建两个目录啊这个都是相同的步骤啊呃这个一定要别呃别搞错啊因为要是有这个01和02别搞错啊然后呢给他去做一个改变的权限呃然后呢我们再进入这个config目录创建一个配置文件买点config
[06:19] 然后呢我们把下面这个内容拷贝过来然后呢去拷贝一下然后呢要注意的是这个ID就不能重复了所以把它设置为2好嘞然后呢我们接着去创建容器我们来看一下这个容器呢所指向的都是3502然后呢它所对应的这个端口呢是3317好嘞然后呢我们去做一个容器的一个创建走这个容器的创建好了然后把这个容器呢给它去
[06:49] 启动起来走好那么我们再来创建一个连接然后呢来一个叫做192.168.1.18-46502然后呢3317啊就是3317然后呢这个是18然后呢这个3317然后呢密码呢是root
[07:15] 然后连接测试一下OK搞定那么这个也就连接成功了那么所以说明我们容器就跑起来了没有任何问题好嘞那么接下来我们是要给我们的master这个sleeve去设置master的信息那么我们去创建一个查询那么它的host是18然后url是idcastidcast没有问题
[07:40] 然后他的master的端口呢是331616也没有问题然后呢这个log fail呢我们去把这个拿过来这个也没有问题这个到这然后他的位置呢是左对的758然后呢把这个758呢也丢到这个位置来好搞定那么这样的话他的master所对应的master信心呢就修改完成了然后呢我们去启动啊去启动我们的一个slave走去启动那么启动之后呢去查看一下这个状态
[08:09] 看有没有问题走那么可以看到在是我们的这个sleeve这个状态也没有问题这两个呢都为yes那就说明我们的主从现在就已经搞定了好那么接下来呢我们就针对于我们的这个测试呢针对于我们这两个的主存库做一个测试啊那么我们依然的是在我们的这个sleeve这个master02这个下面去创建数据库这个数据库呢就叫itcast它要跟我们前面这个保持一致啊
[08:39] 这个里面是不是有个ITcast那么我们也创建一个ITcast这样的一个数据库然后呢我们去来一个这个编码呢是U8然后呢走然后呢创建完成之后呢在下面创建这张表就是刚刚我们所创建的这个AE的这张表因为我们一会儿呢要做个测试把这个表呢创建出来然后呢这个里面下面显然这个表就有了对吧然后呢这个3317这个下面我们来刷新一下
[09:08] 那么数据库是不是也有了表是不是也有了对吧没有任何问题好那么下面呢我们来看一下mycat的配置那么在前面呢我们在mycat中呢只是配置了一个集群而我们现在呢有多个这个集群对吧我有两个这个mycircle的集群那么显然呢我们需要重新去配置我们的mycat那么下面我们来看它的一个配置那么在下面这个位置呢我们是不是又去添加了一个我们这个
[09:35] 主虫的一个一对主虫那么3316是主然后3317是虫那么去做一个读写分离并且我们也指定它的一个balance等于3那么做这样的一个负载均衡OK好这个就是我们的一个配置对吧然后上面这个位置是不是又有一个集群那么我们想把这两个集群是不是就添加到添加到我们DataNode可以看到是不是定义了两个DataNode
[10:03] 一个是cluster1一个是cluster2然后呢我们把这个cluster1和cluster2都取命名从命名为什么DN1和DN2然后呢把这两个是不是添加到我们这个位置来对吧是不是DataNode是DN1和DN2OK这样的话呢我们这个scammer就配置完成了那么下面呢我们把这个呢
[10:27] 拷贝过来然后呢去找到我们的这个mycat浩克下面的mycatmycat01下面config好然后呢我们去打开一个叫scammer配置文件那么把这个内容给它删除掉然后呢我们重新去写入内容这个呢就是我们写入的一个内容检查一下有没有问题好那么这样的话呢就没有问题了好保存退出那么下面呢我们去进入到bin目录下面然后呢去执行一下mycat console
[10:59] console我们来测试一下看有没有问题如果看到什么呢看到这个启动成功那就现在呢我们可以看到它是有点问题的那么它是有问题那么什么问题呢我们一起来看一下好那么我们来看一下它有什么错误啊去查看一下一致用一个mode然后呢点点斜杠下面有个logs查看一个mycatlog那么往下面看来看一下啊那么最后呢会发现呢它其实是一个端口被占用的这样的一个错误
[11:29] 那么也就是说我们前面的麦克并没有停掉对吧那么给它停一下Q然后呢去这个361里走好那么我们来去检查一下那么我们这个进程呢就没有了那么下面呢我们去做一个重新做一个启动
[11:44] 然后呢去把这个就是Minecat console那么可以发现呢现在是不是就已经成功了对吧OK那么Ctrl C结束好那么接下来呢我们就来启动Minecat走那么把它跑起来跑起来之后呢我们就可以去做一个测试了然后呢我们可以看到现在呢我们现在是不是有两个集群一个是Must01一个是Must02那么现在呢我们都是通过了什么呢我们这个Minecat是不是去对接到这两个集群
[12:13] 并且做了什么分片要注意的是当然我们刚刚这个配置会有点问题就是我们的还有一个配置没配置完大家想一下那么我们现在这个MySQL数据库的集群是不是有两个对吧有两个那么也就意味着我们去做数据分片的时候我们通过我们的ID去做一个取模的时候那么显然我们是不是需要去设置为它的count为什么呢为2
[12:40] V2并不是1并不是1这个位置呢我们并没有做修改我们来看一下要修改成2那么这样的话才能去做一个这个取模比如说我第一个放到第一个集群里面第二个呢放到第二个这个集群里面就可以了好那么我们再来修改一下这个配置文件还没有修改完成那么我们来进入到config目录下面去修改一个我们的一个这个规则那我们来搜索一下吧搜索一下它然后呢去搜一下走
[13:09] 然后呢这个我们要改成2如果不改成2的话那么你的这个去做一个存储是有问题的OK好嘞好那么下面呢我们再进入bin目录下面然后呢点点bin下面然后呢我们再去把我们的minecart去kill掉然后呢做一个重新做一个启动好那么我们就直接来启动了然后呢start好那我们稍等一下等待它启动完成之后啊那我们就可以去做一个测试了
[13:38] 好那么下面呢我们来测试一下数据那么目前呢我们这个mycat呢它呢是对接到两个我们的mycoco机群的对不对好那么并且做了一个分片那么我们来测试一下那么我们这样我们去把我们的这个测试语句呢我们拷贝过来那么大概有这四条身后语句去做一个测试那么也就意味着我们对应的有四条数据啊ID分别是1234啊然后呢我们来测一下然后第一条走那么是执行
[14:07] 执行结束了吗执行结束了那么执行结束之后我们来看这条数据落在哪里是在Must01里面吗还是Must02我们来看一下Must01里面没有数据那么是不是又进入到Must02呢我们来看一下Must02是不是有数据然后我在执行第二条这个数据看它会怎么样走那么在Must01里面看有没有数据发现有数据Must02下面是不是就没有数据了
[14:33] 对吧没有数据然后我们再去做一个执行那么就把这两个这两条先执行这条然后再执行这一条然后我们来看一下must01这个里面那么它的数据有两条它的ID是24然后我们的must0102这个下面它的数据也是有两条数据是1和3
[14:57] 那么这样的话我们是不是就实现了一个分片的效果那么有两这两个这个集群共同来承担着我们这个存储的这个任务那么总共有四条数据那么各承担两条的存储OK好那么我们检查一下它所对应的这个重节点那么这个是死利501下面所对应的应该是一和三数据我看一下应该是死利5330对的24这个对的
[15:25] 没有问题跟他是一样的然后呢3317所对应的数据呢那就是一和三了对吧一和三没有任何问题好那么接下来呢我们再来测试一下
[15:35] 测试什么呢就是我们这个MICAD下面啊由于我们MICAD是不是对接到有两个集群那么他读取数据的时候能不能把这两个集群数据全部都读到呢来看一下打开它来看一下你会发现它是不是有四条数据啊但是有同学会发现哎他返回这个结果好像并没有按照一个顺序去做一个排序你会发现ID呢是2413大家可以想一下那么他为什么会这样呢原因是
[15:59] 我们的麦克的是不是去做读取的时候因为我们有两个节点比如说我先把这个的先这个拿掉没有这个啊没有他那么我目前是不是只有两个节点啊那么去做读取的时候他肯定会这样对吧先去发起请求到这读取也会到这个里面去做一个读取那么读到数据之后呢我们来换一个颜色啊换一个颜色比如说我们读到数据返回读到数据是他这个呢读到数据的也是返回到他那么读到
[16:26] 读到中间件里面之后然后再去做一个什么做一个汇总那么在我们这个mega中去做一个汇总那么汇总完成之后再去做一个返回那么由于它仅仅是做汇总不做一个排序所以我们可以看到数据是ok没有问题有4条但是它的顺序是有问题的那么当然了我们可以做一个排序就可以了比如说我们根据这个ID去做一个叫做生讯排序这样的话就搞定了
[16:53] OK好嘞好那么这个呢这就是我们所给大家所讲的什么呢这个使用这个MICAD来做一个数据的一个分片做数据的分片OK好那么关于这个数据分片那我们先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置和测试 MySQL 数据分片架构，包含主从复制、中间件 MyCat 的配置与数据分片测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 MySQL 数据分片架构，列出 master 和 slave 节点的主机、端口、容器名称和角色。
画面2：展示数据分片架构图，应用系统通过中间件分别向 MySQL（主）和 MySQL（从）执行写和读操作。
画面3：在终端中配置 MySQL master 节点，设置 log-bin、server-id 和 sql_mode。
画面4：MySQL master 节点启动日志，显示 InnoDB 初始化、插件加载和服务器就绪。
画面5：在终端中创建 slave02 数据目录并进入。
画面6：在终端中创建 slave02 数据目录、配置文件并创建容器。
画面7：在 Navicat 中配置 slave02 的 master 信息，包括 master_host、master_user、master_port、master_log_file 和 master_log_pos。
画面8：展示 MyCat 的 schema.xml 配置文件，定义了两个数据节点和一个写节点。
画面9：在终端中启动 MyCat 服务。
画面10：在 Navicat 中查看 tb_ad 表，显示数据已同步到 slave02。
画面11：在终端中查看 MyCat 启动日志。
画面12：展示 MyCat 的 rule.xml 配置文件，定义了分片规则，并显示测试 SQL。
画面13：在 Navicat 中查看 tb_ad 表，显示数据已插入。
画面14：在 Navicat 中并列显示两个 slave 节点的 tb_ad 表，验证数据分片和同步。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
MySQL集群1：
主机 端口 容器名称 角色
192.168.1.18 3306 percona-master01 master
192.168.1.18 3307 percona-slave01 slave
MySQL集群2：
主机 端口 容器名称 角色
192.168.1.18 3316 percona-master02 master
192.168.1.18 3317 percona-slave02 slave

画面3：
log-bin=mysql-bin #开启二进制日志
server-id=1 #服务id，不可重复
sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_US
ER,NO_ENGINE_SUBSTITUTION'

画面4：
InnoDB: 32 non-redo rollback segment(s) are active.
InnoDB: Percona XtraDB (http://www.percona.com) 5.7.23-23 started;
log sequence number 11904408
[Note] Plugin 'FEDERATED' is disabled.
InnoDB: Waiting for purge to start.
InnoDB: Buffer pool(s) load completed at 190203 23:58:53
Found ca.pem, server-cert.pem and server-key.pem in data directory
Trying to enable SSL support using them.
[Warning] CA certificate ca.pem is self signed.
Skipping generation of SSL certificates as certificate files are present in data directory.
[Note] Server hostname (bind-address): '*' port: 3306
[Note] IPv6 is available.
[Note] Server socket created on IP: '::'.
[Note] Event Scheduler: Loaded 0 events
Version: '5.7.23-log' socket: '/var/lib/mysql/mysql.sock' port: 3306 Percona Server (GPL), Release 23, Revision 500fcf5
[Warning] IP address '192.168.1.2' could not be resolved: Name or Service not known

画面5：
root@itcast02:conf# mkdir /data/mysql/slave02
root@itcast02:slave02# cd /data/mysql/slave02
root@itcast02:slave02# chmod 777 -R .
root@itcast02:slave02# ll
drwxr-xr-x 4 root root 4096 Feb 4 08:00 ./
drwxr-xr-x 6 root root 4096 Feb 4 08:00 ../
drwxr-xr-x 2 root root 4096 Feb 4 08:00 data/
root@itcast02:slave02# vim conf/

画面6：
root@itcast02:conf# Docker create -v /data/mysql/slave02/data:/var/lib/mysql -v /data/mysql/slave02/conf:/etc/mysql/conf.d -v /data/mysql/slave02/logs:/var/log/mysql --name percona-slave02 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
4df1197a4d6871c67a0f18308e55d5b67132c607c5e607c5e4a4c5a0f4c

画面7：
CHANGE MASTER TO
master_host='192.168.1.18',
master_user='itcast',
master_password='itcast',
master_port=3306,
master_log_file='mysql-bin.000003',
master_log_pos=xxxx;

画面8：
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">
  <schema name="itcast" checkSqlSchema="false" sqlMaxLimit="100">
    <table name="tb_ad" dataNode="dn1,dn2" rule="mod-long">
      <primaryKey name="id"/>
    </table>
  </schema>
  <dataNode name="dn1" dataHost="cluster1" database="itcast"/>
  <dataNode name="dn2" dataHost="cluster2" database="itcast"/>
  <dataHost name="cluster1" maxCon="1000" minCon="10" balance="3" writeType="1" dbType="mysql" switchType="1" slaveThreshold="100">
    <heartbeat>select user() from dual</heartbeat>
    <writeHost host="W1" url="192.168.1.18:3306" user="root" password="root"/>
    <readHost host="R1" url="192.168.1.18:3317" user="root" password="root"/>
  </dataHost>

画面9：
root@itcast02:conf# cd /haoke/mycat/mycat01/conf
root@itcast02:conf# vim schema.xml
root@itcast02:mycat01# cd bin/
root@itcast02:mycat01# ./mycat console
Running Mycat...
wrapper --> Wrapper Started as Console
jvm 1
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=64M; support was removed in 8.0.
Wrapper (Version 3.2.3) http://wrapper.tanukisoftware.org
Copyright 1999-2006 Tanuki Software, Inc. All Reserved.
wrapper --> Wrapper Stopped
root@itcast02:bin#

画面11：
root@itcast02:mycat01# cd ..
root@itcast02:mycat01# ll
drwxr-xr-x 8 root root 4096 Feb 4 01:02 ./

画面12：
<function name="mod-long" class="io.mycat.route.function.PartitionByMod">
  <property name="Count">2</property>
</function>

重新启动mycat进行测试：
./startup_nowrap.sh && tail -f ../logs/mycat.log

画面13：
INSERT INTO tb_ad (id, type, title, url, created, updated) VALUES ('1', '1', '天虹购物中心', 'http://itcast.haoke.css.cn 2018-11-26 11:28:49', '2018-11-26 11:28:49');
INSERT INTO tb_ad (id, type, title, url, created, updated) VALUES ('2', '1', 'Unicity万和天空之城', 'http://itcast.haoke.css.cn 2018-11-26 11:28:51', '2018-11-26 11:28:51');

画面14：
<function name="mod-long" class="io.mycat.route.function.PartitionByMod

