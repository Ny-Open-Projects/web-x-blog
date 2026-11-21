# 画面线理解：13-2.MyCat中间件之实现读写分离

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\13-2.MyCat中间件之实现读写分离【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 00:54, 01:31, 01:59, 02:23, 07:32, 07:50, 08:35, 09:02, 10:04, 10:52, 11:51, 12:37, 13:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:37:34

1) 这一组画面整体在讲如何配置和启动 MyCAT 数据库中间件，包括环境准备、配置文件修改、服务启动及数据库连接测试。

2) 按时间顺序列出每张画面的要点：
画面1：
- 在 slave01 节点的 mysql 目录下查看内容，进入 master01 目录。
- 执行命令：cd master01
- 执行命令：cd conf
- 执行命令：ll（列出目录内容）
- 执行命令：vim my.cnf
- 执行命令：docker restart percona-master01

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
