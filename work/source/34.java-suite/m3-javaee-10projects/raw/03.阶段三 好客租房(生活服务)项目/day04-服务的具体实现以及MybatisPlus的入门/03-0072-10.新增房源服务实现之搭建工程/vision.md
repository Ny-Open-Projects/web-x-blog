# 画面线理解：10.新增房源服务实现之搭建工程

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\10.新增房源服务实现之搭建工程【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:55, 01:17, 02:40, 03:37, 05:25, 06:00, 06:22, 07:14, 07:51, 08:33, 09:16, 10:00, 10:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:44:58

1) 这一组画面整体在讲什么（一句话）：
讲解如何创建并配置一个用于管理房产服务的 Spring Boot + Dubbo 项目，包括数据库表结构设计和 Maven 项目模块化配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：4. 新增房产服务
- 子标题：4.1. 数据结构
- 展示了数据库表 tb_estate 的创建语句：
CREATE TABLE `tb_estate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL COMMENT '楼盘名称',
  `province` varchar(10) DEFAULT NULL COMMENT '所在省',
  `city` varchar(10) DEFAULT NULL COMMENT '所在区',
  `area` varchar(10) DEFAULT NULL COMMENT '所在区',
  `address` varchar(100) DEFAULT NULL COMMENT '具体地址',
  `year` varchar(10) DEFAULT NULL COMMENT '建成年代',
  `type` varchar(10) DEFAULT NULL COMMENT '建筑类型',
  `property_cost` varchar(10) DEFAULT NULL COMMENT '物业费',
  `property_company` varchar(20) DEFAULT NULL COMMENT '物业公司',
  `developers` varchar(20) DEFAULT NULL COMMENT '开发商'

画面2：
- 展示了项目目录结构，包含三个子工程：
  - itcast-haoke-manage-dubbo-server-house-resources
  - itcast-haoke-manage-dubbo-server-house-resources-interface
  - itcast-haoke-manage-dubbo-server-house-resources-dubbo-service

画面3：
- 展示了 Navicat Premium 连接数据库的界面，连接到名为 "haoke" 的数据库。

画面4：
- 标题：4.2. 创建 itcast-haoke-manage-dubbo-server-house-resources 工程
- 展示了数据库表 tb_payment_method 的创建语句：
CREATE TABLE `tb_payment_method` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL COMMENT '支付方式',
  `code` varchar(20) DEFAULT NULL COMMENT '支付方式编码',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='支付方式表';

画面5：
- 展示了项目结构图，突出显示了三个子模块：
  - itcast-haoke-manage-dubbo-server-house-resources
  - itcast-haoke-manage-dubbo-server-house-resources-interface
  - itcast-haoke-manage-dubbo-server-house-resources-dubbo-service

画面6：
- 展示了 IntelliJ IDEA 中右键创建 Maven 项目时的弹出菜单，但提示“failed to create a Maven project”。

画面7：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-interface</artifactId>
    <packaging>pom</packaging>
    <modules>
      <module>itcast-haoke-manage-dubbo-server-house-resources-interface</module>
      <module>itcast-haoke-manage-dubbo-server-house-resources-dubbo-service</module>
    </modules>

画面8：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
  </dependency>

画面9：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>com.baidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.0.5</version>
    <optional>true</optional>
  </dependency>
  <dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.47</version>
    <optional>true</optional>
  </dependency>

画面10：
- 标题：4.3.2. itcast-haoke-manage-dubbo-server-house-resources-dubbo-service
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-service</artifactId>

画面11：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface</artifactId>

画面12：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface</artifactId>

画面13：
- 标题：4.3.2. itcast-haoke-manage-dubbo-server-house-resources-dubbo-service
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-service</artifactId>

画面14：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
  </dependency>
  <dependency>
    <groupId>cn.itcast.haoke.manage</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
    <version>1.0-SNAPSHOT</version>
  </dependency>
