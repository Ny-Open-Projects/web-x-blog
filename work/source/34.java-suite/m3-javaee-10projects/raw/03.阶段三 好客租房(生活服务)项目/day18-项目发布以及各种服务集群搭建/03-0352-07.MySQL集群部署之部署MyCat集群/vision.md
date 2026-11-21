# 画面线理解：07.MySQL集群部署之部署MyCat集群

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\07.MySQL集群部署之部署MyCat集群【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:37, 02:16, 03:48, 04:39, 07:33, 08:37, 09:49, 11:47, 12:50, 14:03, 14:48, 15:52, 17:09, 18:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:50:15

1) 这一组画面整体在讲什么（一句话）：
演示如何部署和配置 Mycat 中间件，包括 MySQL 主从复制、Mycat 配置文件编写、数据分片规则以及通过 Navicat 进行数据库操作和验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Mycat 部署文档的 Typora 编辑器页面，其中包含创建 MySQL 主从复制的命令，如：
```bash
#启动
docker start ms_node1 && docker logs -f ms_node1

#创建同步账户以及授权
create user 'haoke'@'%' identified by 'haoke';
grant replication slave on *.* to 'haoke'@'%';
flush privileges;

#查看Master状态
show master status;
```

画面 2: 展示了在远程服务器上通过文件管理器查看 Mycat-server-1.6.1-release-201910... 的安装包。

画面 3: 在终端中列出 Mycat 安装目录下的配置文件，如 `schema.xml`、`wrapper.conf`、`server.xml` 等，并执行 `vim server.xml` 命令。

画面 4: 展示了 Mycat 的 `schema.xml` 配置文件内容，其中定义了数据库 `haoke` 的分片规则和数据节点映射：
```xml
<?xml version="1.0"?>
<!DOCTYPE mycat:schema SYSTEM "schema.dtd">
<mycat:schema xmlns:mycat="http://io.mycat/">
  <!--配置数据表-->
  <schema name="haoke" checkSQLSchema="false" sqlMaxLimit="100" rule="mod-long">
    <table name="tb_ad" dataNode="dn1,dn2" />
    <table name="tb_estate" dataNode="dn3" />
  </schema>

  <!--配置分片关系-->
  <dataNode name="dn1" dataHost="cluster1" database="haoke" />
  <dataNode name="dn2" dataHost="cluster2" database="haoke" />
  <dataNode name="dn3" dataHost="cluster3" database="haoke" />

  <!--配置连接信息-->
  <dataHost name="cluster1" maxCon="1000" minCon="10" balance="2"
    writeType="1" dbType="mysql" dbrDrivers="native" switchType="1"
    slaveThreshold="100">
    <heartbeat selectUser="root" />
    <writeHost host="W1" url="192.168.1.18:13306" user="root" />
    <readHost host="W2" url="192.168.1.19:13310" user="root" />
  </dataHost>
```

画面 5: 展示了 Mycat 配置文件 `wrapper.conf` 和 `server.xml` 的部分内容，包括端口配置：
```xml
#设置javaw窗口
wrapper.java.additional.7=-Dcom.sun.management.jmxremote.port=11986

#设置服务端口以及管理端口
<property name="serverPort" value="8069" />
<property name="managerPort" value="19069" />
```

画面 6: 展示了 Mycat 的 `rule.xml` 配置文件内容，定义了分片函数：
```xml
<function name="mod_long" class="io.mycat.route.function.PartitionByMod">
  <property name="count" value="2" />
</function>
```

画面 7: 在终端中查看 Mycat 的 lib 目录下的 JAR 包，并执行 `tail -f ../logs/mycat.log` 命令。

画面 8: 展示了在 Navicat 中连接 Mycat 服务器的界面，填写了主机地址 `192.168.1.19`、端口 `13311`、用户名 `root`。

画面 9: 展示了在 Navicat 中连接成功后，进入数据库 `haoke` 的界面。

画面 10: 展示了在 Navicat 中查看表 `tb_house_resources` 的结构。

画面 11: 展示了在 Navicat 中查看表 `tb_estate` 的结构，包括字段 `id`、`name`、`province`、`city`、`area`、`address`。

画面 12: 展示了 Mycat 部署文档中关于创建和测试表的代码，包括创建 `tb_ad` 和 `tb_estate` 表的 SQL 语句，以及插入数据的语句。

画面 13: 展示了 Mycat 部署文档中关于创建和测试表的代码，包括创建 `tb_ad` 和 `tb_estate` 表的 SQL 语句，以及插入数据的语句。

画面 14: 展示了 Mycat 部署文档中关于创建和测试表的代码，包括创建 `tb_ad` 和 `tb_estate` 表的 SQL 语句，以及插入数据的语句。
