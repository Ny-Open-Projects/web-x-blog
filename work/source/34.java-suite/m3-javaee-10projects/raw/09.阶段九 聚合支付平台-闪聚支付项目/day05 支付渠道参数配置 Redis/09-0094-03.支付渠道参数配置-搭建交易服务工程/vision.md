# 画面线理解：03.支付渠道参数配置-搭建交易服务工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\03.支付渠道参数配置-搭建交易服务工程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:53, 01:22, 01:39, 02:13, 02:42, 03:05, 03:40, 04:19, 04:55, 05:37, 05:57, 06:23, 06:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:18:45

1) 这一组画面整体在讲如何搭建并配置一个基于 Spring Boot 和 Nacos 的交易服务工程，包括导入项目、配置 Nacos 服务发现与配置管理。

2) 按时间顺序列出每张画面的要点：

画面1：
- PPT标题：5.2.2 搭建工程
- 内容要点：
  1. 复制提供的 shanjupay-transaction 目录到 shanjupay 根目录，导入 shanjupay-transaction 及 api 和 service 三个工程。
  2. 添加 Module 到 IDEA 中。
- 代码/配置：
  ```sql
  INSERT INTO `pay_channel` (`ID`, `CHANNEL_NAME`, `CHANNEL_CODE`)
  VALUES
  (1, '微信JSAPI', 'WX_JSAPI'),
  (2, '支付宝手机网站支付', 'ALIPAY_WAP'),
  (3, '支付宝条码支付', 'ALIPAY_BAR_CODE'),
  (4, '微信支付扫码支付', 'WX_MICROPAY'),
  (5, '微信native支付', 'WX_NATIVE');

  /*!40000 ALTER TABLE `pay_channel` ENABLE KEYS */;
  UNLOCK TABLES;

  LOCK TABLES `platform_pay_channel` WRITE;
  /*!40000 ALTER TABLE `platform_pay_channel` DISABLE KEYS */;
  INSERT INTO `platform_pay_channel` (`ID`, `PLATFORM_CHANNEL`, `PAY_CHANNEL`)
  VALUES
  (1, 'shonju_b2c', 'WX_MICROPAY'),
  (2, 'shanju_b2c', 'ALIPAY_BAR_CODE'),
  (3, 'wx_native', 'WX_NATIVE'),
  (4, 'alipay_wap', 'ALIPAY_WAP'),
  (5, 'shonju_c2b', 'WX_JSAPI'),
  (6, 'shanju_c2b', 'ALIPAY_MAP');
  ```

画面2：
- 文件资源管理器显示项目目录结构，包含 `shanjupay-transaction`、`shanjupay-merchant-application`、`shanjupay-transaction-api` 等文件夹。
- 底部命令行提示：`shanjupay` 项目已构建完成。

画面3：
- IDEA 导入模块界面，选择“Import module from external model”，并选中 Maven。

画面4：
- IDEA 项目结构设置界面，显示 `shanjupay-transaction` 模块的 SDK 版本为 1.8.0，依赖存储格式为 IntelliJ IDEA (.iml)。

画面5：
- IDEA 项目结构视图，显示 `shanjupay-merchant-application` 项目下的 `shanjupay-transaction` 模块。
- 代码片段：`MerchantDetailDTO merchantDTO = new MerchantDetailDTO();` 等。

画面6：
- IDEA 项目结构视图，显示 `shanjupay-transaction-service` 模块下的 `SwaggerConfiguration` 类。
- 代码片段：
  ```java
  @Configuration
  @ConditionalOnProperty(prefix = "swagger", value = "enable", havingValue = "true")
  @EnableSwagger2
  public class SwaggerConfiguration {
      @Bean
      public Docket buildDocket() {
          return new Docket(DocumentationType.SWAGGER_2)
                  .select()
                  .apis(RequestHandlerSelectors.basePackage("com.shanjupay.transaction"))
                  .paths(PathSelectors.any())
                  .build();
      }
  }
  ```

画面7：
- PPT标题：5.2.2 搭建工程
- 内容要点：
  1. 复制提供的 shanjupay-transaction 目录到 shanjupay 根目录，导入 shanjupay-transaction 及 api 和 service 三个工程。
  2. 添加 Module 到 IDEA 中。
  3. 在 Nacos 中添加 transaction-service.yaml 配置，Group: SHANJUPAY_GROUP。
- 代码/配置：
  ```yaml
  port: 50050 #启动端口，命令行注入
  nacos:
    server:
      addr: 137.3.8.1:8848
  spring:
    application:
      name: transaction-service
    main:
      allow-bean-definition-overriding: true # Spring Boot 2.1 新增设置
  cloud:
    nacos:
      discovery:
        server-addr: ${nacos.server.addr}
        namespace: ${nacos.namespace}
        cluster-name: DEFAULT
      config:
        server-addr: ${nacos.server.addr}
        file-extension: yaml
        namespace: ${nacos.namespace}
        group: SHANJUPAY_GROUP # 默认支付服务组
        refresh: true
        data-id: spring-boot-http.yaml # spring boot http配置
  ```

画面8：
- Nacos 配置管理界面，显示多个配置项，包括 `spring boot http.yaml`、`merchant-application.yaml` 等。
- Group 为 `COMMON_GROUP` 或 `SHANJUPAY_GROUP`。

画面9：
- Nacos 新建配置界面，Data ID 为 `transaction-service.yaml`，Group 为 `DEFAULT_GROUP`，配置格式选择 YAML。

画面10：
- Nacos 新建配置界面，配置格式选择 YAML，配置内容为空。

画面11：
- IDEA 编辑器显示 `bootstrap.yml` 文件内容，包含端口、Nacos 配置等。
- 代码/配置：
  ```yaml
  server:
    port: 50050 #启动端口，命令行注入
  nacos:
    server:
      addr: 137.3.8.1:8848
  spring:
    application:
      name: transaction-service
    main:
      allow-bean-definition-overriding: true # Spring Boot 2.1 新增设置
  cloud:
    nacos:
      discovery:
        server-addr: ${nacos.server.addr}
        namespace: ${nacos.namespace}
        cluster-name: DEFAULT
      config:
        server-addr: ${nacos.server.addr}
        file-extension: yaml
        namespace: ${nacos.namespace}
        group: SHANJUPAY_GROUP # 默认支付服务组
        refresh: true
        data-id: spring-boot-http.yaml # spring boot http配置
  ```

画面12：
- IDEA 编辑器显示 `bootstrap.yml` 文件内容，包含端口、Nacos 配置等。
- 代码/配置：
  ```yaml
  discovery:
    server-addr: ${nacos.server.addr}
    namespace: ${nacos.namespace}
    cluster-name: DEFAULT
  config:
    server-addr: ${nacos.server.addr}
    file-extension: yaml
    namespace: ${nacos.namespace}
    group: SHANJUPAY_GROUP # 默认支付服务组
    refresh: true
    data-id: spring-boot-http.yaml # spring boot http配置
  ```

画面13：
- IDEA 编辑器显示 `TransactionBootstrap.java` 文件内容，包含 Spring Boot 启动类。
- 代码/配置：
  ```java
  package com.shanjupay.transaction;

  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.context.annotation.ComponentScan;

  @SpringBootApplication
  @ComponentScan(basePackages = "com.shanjupay.transaction")
  public class TransactionBootstrap {
      public static void main(String[] args) {
          SpringApplication.run(TransactionBootstrap.class, args);
      }
  }
  ```

画面14：
- PPT标题：5.3 应用绑定服务类型
- 内容要点：
  1. 首先理解服务类型。
  2. 服务类型是闪聚支付平台为商户提供的聚合支付服务通道，共分为线上和线下两大类：
     1) 手机APP支付
     2) PC网页支付
     3) 手机网页支付
     4) 小程序支付
     等

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：

已按上述各画面列出。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：

已按上述各画面列出。

5) 不要评价画面美观，不要输出与课程无关的内容。

已按上述各画面列出。
