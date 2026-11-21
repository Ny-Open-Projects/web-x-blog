# 画面线理解：16.开发环境搭建-搭建项目服务-商品服务工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\16.开发环境搭建-搭建项目服务-商品服务工程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:26, 02:06, 03:03, 03:45, 04:33, 05:20, 05:53, 06:41, 07:37, 08:18, 09:12, 10:04, 10:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:44:37

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中创建并配置商户服务工程（shanjupay-merchant-api），并为该工程添加依赖和配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在项目结构中，右键点击 shanjupay-merchant 工程，选择“New” -> “Module”，创建名为 shanjupay-merchant-api 的模块。
画面 2: 在“Project Structure”中，选择“Modules”，确认新模块 shanjupay-merchant-api 的路径和名称。
画面 3: 在“New Module”对话框中，设置模块名称为 shanjupay-merchant-api，模块路径为 F:\teach\shanjupay\model2\code\shanjupay\merchant，点击“Finish”完成创建。
画面 4: 在 shanjupay-merchant 工程目录下，右键点击 shanjupay-merchant-api，选择“Add framework support...”，添加 Spring Boot 支持。
画面 5: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了父工程的配置，包括 artifactId、groupId、version 等。
画面 6: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了 <dependencies> 标签，其中包含 <version>1.0-SNAPSHOT</version>。
画面 7: 在 shanjupay-merchant-api 的 pom.xml 文件中，显示了 <dependency> 标签，其中包含 <artifactId>mysql-connector-java</artifactId>。
画面 8: 在 shanjupay-merchant-service 的 pom.xml 文件中，显示了 <dependency> 标签，其中包含 <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>。
画面 9: 在 shanjupay-merchant-service 的 bootstrap.yml 文件中，显示了 dubbo 配置，包括 scan、base-packages、protocol、name、port、registry、application、qos 等。
画面 10: 在 shanjupay-merchant-service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、nacos、discovery、config 等。
画面 11: 在 shanjupay-merchant-service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、nacos、discovery、config 等。
画面 12: 在 shanjupay-merchant-service 的 MerchantApplicationBootstrap.java 文件中，显示了 Spring Boot 启动失败的错误信息，提示未配置数据源。
画面 13: 在 shanjupay-merchant-service 的 bootstrap.yml 文件中，显示了 spring 配置，包括 application、main、allow-bean-definition-overriding、cloud、nacos、discovery、config 等。
画面 14: 在 shanjupay-merchant-service 的 pom.xml 文件中，显示了 <repositories> 标签，其中包含 <id>aliyun maven</id>。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1: 无代码或配置。
画面 2: 无代码或配置。
画面 3: 无代码或配置。
画面 4: 无代码或配置。
画面 5: 
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>shanjupay-merchant</artifactId>
        <groupId>com.shanjupay</groupId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>
    <artifactId>shanjupay-merchant-api</artifactId>
</project>

画面 6: 
<dependencies>
    <dependency>
        <groupId>com.shanjupay</groupId>
        <artifactId>shanjupay-commons</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>

画面 7: 
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>

画面 8: 
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>

画面 9: 
dubbo:
  scan:
    # dubbo 服务扫描基准包
    base-packages: com.shanjupay
  protocol:
    # dubbo 协议
    name: dubbo
    port: 20890
  registry:
    address: nacos://127.0.0.1:8848
  application:
    port: 22240 # dubbo qos端口配置 命令行注入
  qos:
    check: false
    timeout: 90000
    retries: -1

画面 10: 
spring:
  application:
    name: merchant-service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    nacos:
      discovery:
        server-addr: ${nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # spring boot http配置
          group: COMMON_GROUP # 通用配置组

画面 11: 
spring:
  application:
    name: merchant-service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    nacos:
      discovery:
        server-addr: ${nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # spring boot http配置
          group: COMMON_GROUP # 通用配置组

画面 12: 
Error starting ApplicationContext. To display the conditions report re-run your application with 'debug' enabled.
[...]
APPLICATION FAILED TO START
Description:
Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.

画面 13: 
spring:
  application:
    name: merchant-service
  main:
    allow-bean-definition-overriding: true # Spring Boot 2.1 需要设定
  cloud:
    nacos:
      discovery:
        server-addr: ${nacos.server.addr}
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8
        cluster-name: DEFAULT
      config:
        server-addr: ${nacos.server.addr} # 配置中心地址
        file-extension: yaml # 命令行注入
        namespace: a1fe663-5117-48c1-8dd5-e9ddc2af90a8 # 命令行注入
        group: SHANJUPAY_GROUP # 聚合支付业务组
        ext-config:
          refresh: true
          data-id: spring-boot-http.yaml # spring boot http配置
          group: COMMON_GROUP # 通用配置组

画面 14: 
<repositories>
    <repository>
        <id>aliyun maven</id>
        <name>aliyun maven</name>
    </repository>
</repositories>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.6.2 搭建商户服务工程”，内容为“在基础工程的基础上创建商户服务工程，商户服务工程包括接口和接口实现两个子工程。”
画面
