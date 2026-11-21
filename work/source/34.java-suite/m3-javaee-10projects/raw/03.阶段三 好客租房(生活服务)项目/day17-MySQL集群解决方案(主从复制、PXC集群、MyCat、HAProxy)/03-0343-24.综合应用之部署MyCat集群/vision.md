# 画面线理解：24.综合应用之部署MyCat集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\24.综合应用之部署MyCat集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:48, 01:19, 02:26, 03:58, 04:33, 05:23, 05:55, 06:56, 07:42, 08:43, 09:18, 09:54, 11:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:44:05

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
