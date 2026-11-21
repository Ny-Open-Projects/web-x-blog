# 画面线理解：day08-1-入门案例-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-1-入门案例-功能实现1_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:11, 01:27, 01:37, 01:45, 01:50, 01:57, 02:17, 02:32, 02:39, 02:48, 03:10, 05:16, 05:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:42:30

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IDEA 中为 Sharding-JDBC 项目配置 Maven 依赖和 application.properties 配置文件，以实现分库分表功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PPT 页面，标题为“2.3.5 功能实现”，内容包括“基础环境搭建”和“在 pom 文件中引入 maven 依赖”。
画面 2: PPT 页面，展示在 pom.xml 中引入的三个依赖项，包括 spring-boot-starter-web、spring-boot-starter-actuator 和 spring-boot-configuration-processor。
画面 3: IDEA 中打开的 sharding-jdbc-demo 项目的 pom.xml 文件，显示了父工程配置和部分依赖。
画面 4: IDEA 中 pom.xml 文件，高亮显示了 spring-boot-configuration-processor 依赖项，并添加了 <optional>true</optional> 标签。
画面 5: IDEA 中 pom.xml 文件，高亮显示了 springfox-swagger2 依赖项。
画面 6: IDEA 中 pom.xml 文件，高亮显示了 mysql-connector-java 依赖项。
画面 7: IDEA 中 pom.xml 文件，高亮显示了 sharding-jdbc-spring-boot-starter 依赖项。
画面 8: IDEA 中 application.properties 文件，显示了部分依赖配置。
画面 9: IDEA 中 application.properties 文件，高亮显示了数据源配置，包括数据源名称、驱动类、URL、用户名和密码。
画面 10: IDEA 中 application.properties 文件，高亮显示了分库分表的配置，包括分表策略、分片键、分片算法和绑定表。
画面 11: PPT 页面，标题为“（3）基本配置”，内容包括 server.port、spring.application.name、server.servlet.context-path 等配置。
画面 12: IDEA 中 application.properties 文件，显示了 server.port、spring.application.name、server.servlet.context-path 等配置。
画面 13: PPT 页面，标题为“（4）配置 sharding-jdbc”，内容包括“怎么使用 sharding-jdbc？在编程中主要就是玩儿配置”。
画面 14: IDEA 中 application.properties 文件，高亮显示了 sharding-jdbc 的配置，包括数据源名称、驱动类、URL、用户名和密码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
(1) 基础环境搭建
用IDEA打开dbsharding工程，以dbsharding为总体父工程，用来管理依赖，sharding-jdbc-demo为入门案例工程，用来实现功能。
(2) 在pom文件中引入maven依赖

画面 2:
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-configuration-processor</artifactId>
<optional>true</optional>
</dependency>

画面 3:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <artifactId>dbsharding</artifactId>
        <groupId>com.itheima.dbsharding</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>sharding-jdbc-demo</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-configuration-processor</artifactId>
            <optional>true</optional>
        </dependency>

        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
        </dependency>

        <dependency>
            <groupId>org.apache.shardingsphere</groupId>
            <artifactId>sharding-jdbc-spring-boot-starter</artifactId>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

画面 4:
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-configuration-processor</artifactId>
<optional>true</optional>
</dependency>

画面 5:
<dependency>
<groupId>io.springfox</groupId>
<artifactId>springfox-swagger2</artifactId>
<version>2.9.2</version>
</dependency>

画面 6:
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>8.0.28</version>
</dependency>

画面 7:
<dependency>
<groupId>org.apache.shardingsphere</groupId>
<artifactId>sharding-jdbc-spring-boot-starter</artifactId>
<version>5.1.1</version>
</dependency>

画面 8:
spring.http.encoding.force = true
# 开启 swagger
swagger.enable = true
# 同名 bean 允许覆盖
spring.main.allow-bean-definition-overriding=true
# 将带有下划线的字段映射为驼峰格式的实体类属性
mybatis.configuration.map-underscore-to-camel-case = true

画面 9:
# 真实数据源定义
spring.shardingsphere.datasource.names = m0,m1,m2,s0,s1,s2
spring.shardingsphere.datasource.m0.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m0.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m0.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&zeroDateTimeBehavior=convertToNull
spring.shardingsphere.datasource.m0.username = root
spring.shardingsphere.datasource.m0.password = 123
spring.shardingsphere.datasource.m1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver-class-name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url = jdbc:mysql://localhost:3306/store_db?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&zeroDateTimeBehavior=convertToNull
spring.shardingsphere.datasource.m1.username = root
spring.shardingsphere.datasource.m1.password = 123

画面 10:
# product_info 表分表，分布在 ds1, ds2, ds3 中，分片列为 product_id % 4，product_id 为分片键，分片算法为取模算法
spring.shardingsphere.sharding.tables.product_info.actual-data-nodes = ds$->{0..2}.product_info
spring.shardingsphere.sharding.tables.product_info.strategy.inline.sharding-column = product_id
spring.shardingsphere.sharding.tables.product_info.strategy.inline.algorithm-expression = product_id % 4
spring.shardingsphere.sharding.tables.product_info.key-generator.type = SNOWFLAKE

# product_description 表分表，分布在 ds1, ds2, ds3 中，分片列为 product_id % 4，product_id 为分片键，分片算法为取模算法
spring.shardingsphere.sharding.tables.product_description.actual-data-nodes = ds$->{0..2}.product_description
spring.shardingsphere.sharding.tables.product_description.strategy.inline.sharding-column = product_id
spring.shardingsphere.sharding.tables.product_description.strategy.inline.algorithm-expression = product_id % 4
spring.shardingsphere.sharding.tables.product_description.key-generator.type = SNOWFLAKE

# 设置 product_info, product_description 为绑定表，两张表中的分片键名字必须一致
spring.shardingsphere.sharding.binding-tables = product_info,product_description

画面 11:
(3) 基本配置
server.port=56081
spring.application.name = sharding-jdbc-demo
server.servlet.context-path = /sharding-jdbc-demo
spring.http.encoding.charset = UTF-8
spring.http.encoding.force = true

画面 12:
server.port=56081
spring.application.name = sharding-j
