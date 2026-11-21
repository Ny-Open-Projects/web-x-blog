# day08-1-入门案例-功能实现1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-3 Shardind-JDBC
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-3 Shardind-JDBC\day08-1-入门案例-功能实现1_【海量资源尽在 666java.com】.mp4
- 时长 5分38秒（音频 339s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 其实到目前呢我们已经在本机上把咱们这个入门案例当中的整个数据库环境全部打印好其实主要就是一个什么呀对主从数据库的一个环境那咱接下来的话就开始动手编码来实现这个案例那具体来说的话其实主要就是使用sharding-gdbc在主从架构还有分库分表的情况下如何实现
[00:31] 数据库的增长感察还有什么呀读写分离功能那这边呢我们也是模仿p2p这个项目有一个总体的一个副工程里边管理依赖还有一个sharding-gdbc-demo这是我们入门案例的这个工程在这里边我们就具体实现数据的增长感察还有读写分离这些功能大家看一下我在idea当中呢已经把工程给打开了这就是副工程它里边就是一个碰文件吧来管理这个依赖了
[01:02] 比方这里边他都设置了版本是不是然后这个呢就是我们具体的入门案例这个工程然后呢我们就需要在POM文件当中引入依赖那咱接下来整体过一遍啊看看咱们这个入门案例当中他都这个引用了哪些依赖我们就直接在ADIR里边打开这个POM文件了这边咱整体过一遍吧大家看这是Spring BootStarter Web这一块然后还有什么呀
[01:36] 这都是死人布特的对不对到这你看是mybattist啊mybattist然后这是连接池阿里巴巴的德路一对吧sweager啊这都是sweager嗯还有是lambook的啊mycircle的驱动gdbc驱动啊这是整合的mybattist跟sirmanboot整合的德路一的整合的最后这个就是咱们sharding-gdbc啊跟sirmanboot的一个整合包这是我们导入了相关的什么呀对依赖
[02:05] 一代导入进来之后呢按照咱以往的套路接下来是不是要搞配置是吧对大家看一下我们的配置文件我们这个案例当中的配置文件采用的是properties这种格式的配置文件我们打开看一下这个配置文件内容非常多咱拆成两块去给大家说这是第一大块第一大块我们叫基本配置就是这里面配置大家相对来说比较熟经常见第二大块就是从这开始
[02:34] 这就是sharding-gdbc 涉及到的配置非常非常多这一块咱一会单独来说那咱先看看这个基本配置吧我们去讲一里边瞅一瞅基本配置基本配置对吧基本配置咱大家瞅一眼吧你看大概这么多这个是咱这个微服务工程占用的端口号不再说了这是它的什么对应用程序的名字这是它的基本访问路径这些都不再说了
[03:01] 像这些是一个一个一个ATDP UTF-8的一些编码的一些处理这是不咱开启咱这个sweagg咱这个项目当中他也用到了sweagg在这是不是他也用到sweagg和这呢是sweagg一个开关吧然后接下来我要重点说一说这个配这个配置是这样的这个配置呃大家慢慢以后可能用的会多一些这个配置干嘛呢给大家说一说
[03:31] 大家知道我们现在在加这一块做这个项目做开发的时候呢会引进来各种各样的框架对吧会使用各种各样的框架而且呢我们都是用Spring Boot进行整合来使用那随着你用的框架越来越多难免会出现什么情况Spring会发现它遇到了两个B名字是一样它管理的时候但是呢这两个B来自于两个不同的什么呀框架也就是说你在
[04:01] 开发这个项目的时候可能会用到A框架也用到B框架然后在A和B这两个框架里边都出现了一个名字一样的这个B那么这时候呢死平生在管理的时候呢就会遇到一定的问题那这时候呢我们加上这个配置指的是如果遇到同名的B那时候我们可以对一些配置一些配置项可以进行这个值的一个覆盖这是我们将来可能难免会遇到的一种情况
[04:31] 那下这个大家应该见过吧我这有注视就是我们可以把表里边啊这个字段有的是不带着下滑线吗这个我们可以让它自动映射为椭风格式的那个实体类的属性嗯我们挑一个例子啊这个大家应该有印象比如说我们看我们现在这个表里边有吗这个都是我们挑个有这个吧你看这个字段的名字叫以麦几下滑线URL对吧
[05:02] 那么刚才那个配置它就可以映射为这么一个属性叫image下弹线就没了就变成url这是驼峰格式了它就会跟这个属性类当中的这个属性进行对应这在以前讲MateBattis的时候应该是提过这是我们这个Rumani当中一些基本配置咱就说到这儿那一会咱们重点重点重点要学习的就是下面这一堆跟什么有关的配置
[05:32] 对,Sharding-GDBC相关的配置这个咱一会儿重点给大家做讲解

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
# 开启 Swagger
Swagger.enable = true
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

