# 画面线理解：13-1.MyCat中间件之实现数据分片

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\13-1.MyCat中间件之实现数据分片【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:35, 03:46, 05:22, 06:06, 06:44, 07:53, 10:26, 11:08, 11:58, 12:59, 13:53, 14:42, 16:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:36:54

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
[Warning] IP address '192.168.1.2' could not be resolved: Name or service not known

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
root@itcast02:conf# docker create -v /data/mysql/slave02/data:/var/lib/mysql -v /data/mysql/slave02/conf:/etc/mysql/conf.d -v /data/mysql/slave02/logs:/var/log/mysql --name percona-slave02 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23
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
