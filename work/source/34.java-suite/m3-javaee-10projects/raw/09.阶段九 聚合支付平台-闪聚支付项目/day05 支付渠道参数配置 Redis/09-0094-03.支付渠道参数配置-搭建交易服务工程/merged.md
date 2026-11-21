# 03.支付渠道参数配置-搭建交易服务工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\03.支付渠道参数配置-搭建交易服务工程【海量资源尽在 666java.com】.mp4
- 时长 6分50秒（音频 410s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们就正式进入支付渠道参数配置的功能开发那根据刚才系统交互流程分析我们说这里面呢我们需要新增一个交易服务的工程好那么接下来我们来搭建交易服务工程那么我们在搭建这个工程的方式是什么呢给大家说一下啊在
[00:19] 实际的企业开发当中啊我们到企业当中这个工程啊都是已经大家好的大家只需要去Gate上拉取这个工程的代码就可以了像前边呢我是手动给大家创建商户平台应用和商务服务工程的那么从现在开始呢后边我们的工程呢就基本上采用导入的方式了好那么在给大家的这个代码资料当中啊有一个叫做看好啊有一个叫做闪聚配杠Transaction这个工程
[00:46] 然后呢我们把这个工程呢复制到你的这个代码目录当中复制进去好那现在呢我们就打开ID好然后这里面呢这时候我们要找到我们的这个什么这个设置模块的这个窗口那这里边我们要做的事呢是不是就是把刚才我考到目录里边的那个transaction那个工程要干嘛是不是要导入到我们的工程中啊好那现在呢我们来看一下找到我们现在这个工程的目录啊
[01:16] 在这刚才我们是不是在这里是不是拷贝到你看是不是在这然后下一步好继续那导进去了之后呢注意这里面呢你注意它包括两个嘛一个是API一个是什么API的实现所以这两个呢我们都一个一个的把它这样导进去好然后再继续这个是接口的实现好
[01:48] 那这样下一步啊最终呢我们就完成了整个工程的什么导入这时候呢我们再打开我们这个工程结构看啊那么我们刚才导进去的是不是就是这个交易服务哎我的问题来了请问这个交易服务里边的接口对外暴露的是什么是http还是double啊有同学还不知道你注意干application的是不是就是我们平台应用的这个层面
[02:17] 它是对接前端是不是提供HTTP而这个交易的你看它里边应该有很大一部分都是什么double服务因为我们说double接口是不是两个一个是API一个是Service对吧所以我们后边呢就会在这里边呢写很多的这种double服务的接口啊好那现在呢导进去的工程大家看一下里边有一些基础的配置这个应该就不用我
[02:39] 再多说了啊这是Meptis Plus的包括Swagger的啊还有什么呢还有它的一些转换的类包括它的实体类这些都是我们已经干嘛把它导进去的啊那么一会儿我们只需要在这个Service当中写代码就行了好那么我们把这个交易服务的工程导进去之后呢接下来我们有一些事要处理啊嗯处理哪些事啊你导一个工程你要注意虽然前面是你手动创建的工程啊这导进去的啊
[03:10] 你这个步骤也不能少哪些步骤啊你比如说你这个配置参数这儿看好它是不是需要去Necros当中来拉取配置啊所以啊你是不是要找到你的这个Necros然后呢干嘛是不是要找到我们说它需要配置的地方看现在我们由于原来没有交易服务这个配置文件是没有一个交易服务的配置文件啊对不对
[03:39] 那接下来我们要做的事是啥呢我们要做的事是不是就是给交易服务来配置一个配置文件对吧那怎么配置配置文件啊你首先找到他的这个这个服务名称然后呢你看这是不是有一个扩展名叫yaml那这个俩加起来就是他的配置文件当初我讲Nikos的时候我估计同学有些同学都忘了啊那注意注意听啊这时候呢我们在这儿
[04:09] 看yaml这个就对应于什么就是我们什么交易服务的配置文件了对将来交易服务呢就自动找到这个配置文件好那么继续我们说我们散具支付平台我们统一让他用这样的一个group所以你把这个default group给他改掉那里边呢还有一些什么有一些配置的信息
[04:36] 注意看讲义配置信息配哪些东西这里边应该大家也能看得懂一个是我们的contact pass将来我们如果要报有一些接口是http的话那么通过这个路径来访问还有要连接数据库的还有mybts plus的这些我们都把它给拷进去拷进去之后呢那我们简单说一下看一下
[04:59] 这个就不用说了content pass还有什么连接数据库的连接数据库这里边呢我们来看啊你要连接这个数据库这个数据库现在是不是已经有了就是它然后呢你的账号密码你这时候要改成你的账号和密码啊注意啊这要改一下啊好然后后边呢你就是我们说的那些什么Mapper呀映射文件呀是不是都在这个路径下这就不用管它了好这样的话我们把它发布
[05:26] 那么发布成功之后呢如果你想让我们的这个工程去找到这个配置文件你需要注意把这个namespace的这个ID啊你要配置正确看这懂吧这几个一系列的配置啊大家一定要知道怎么配好这样的话我们就完成了整个的这个交易服务的什么这个配置文件的配置就搞定了那搞定了之后呢
[05:55] 我们现在就可以来启动它虽然是我导入的一个工程里边很多代码没有啊但是它也是可以启动的对那现在呢我们来找到这个启动类Spring Boot的启动类然后呢我们去运行它启动了之后我们拿下个问题我怎么样知道这个服务已经启动成功了首先你看控制台报错不报错对不对这是一点其次你是不是要通过什么
[06:24] 通过哪里来看我们的服务是否注册成功呀对Necros所以我们呢当它启动成功了之后啊我们现在就可以打开Necros然后呢找到服务的什么列表然后呢大家看到此时呢这个Transaction Service都已经注册成功到这里呢我们是不是就完成了这个交易服务工程的搭建好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何搭建并配置一个基于 Spring Boot 和 Nacos 的交易服务工程，包括导入项目、配置 Nacos 服务发现与配置管理。

2) 按时间顺序列出每张画面的要点：

画面1：
- PPT标题：5.2.2 搭建工程
- 内容要点：
  1. 复制提供的 shanjupay-transaction 目录到 shanjupay 根目录，导入 shanjupay-transaction 及 api 和 Service 三个工程。
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
- IDEA 项目结构视图，显示 `shanjupay-transaction-Service` 模块下的 `SwaggerConfiguration` 类。
- 代码片段：
  ```java
  @Configuration
  @ConditionalOnProperty(prefix = "Swagger", value = "enable", havingValue = "true")
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
  1. 复制提供的 shanjupay-transaction 目录到 shanjupay 根目录，导入 shanjupay-transaction 及 api 和 Service 三个工程。
  2. 添加 Module 到 IDEA 中。
  3. 在 Nacos 中添加 transaction-Service.yaml 配置，Group: SHANJUPAY_GROUP。
- 代码/配置：
  ```yaml
  port: 50050 #启动端口，命令行注入
  Nacos:
    server:
      addr: 137.3.8.1:8848
  spring:
    application:
      name: transaction-Service
    main:
      allow-bean-definition-overriding: true # Spring Boot 2.1 新增设置
  cloud:
    Nacos:
      discovery:
        server-addr: ${Nacos.server.addr}
        namespace: ${Nacos.namespace}
        cluster-name: DEFAULT
      config:
        server-addr: ${Nacos.server.addr}
        file-extension: yaml
        namespace: ${Nacos.namespace}
        group: SHANJUPAY_GROUP # 默认支付服务组
        refresh: true
        data-id: spring-boot-http.yaml # Spring Boot http配置
  ```

画面8：
- Nacos 配置管理界面，显示多个配置项，包括 `Spring Boot http.yaml`、`merchant-application.yaml` 等。
- Group 为 `COMMON_GROUP` 或 `SHANJUPAY_GROUP`。

画面9：
- Nacos 新建配置界面，Data ID 为 `transaction-Service.yaml`，Group 为 `DEFAULT_GROUP`，配置格式选择 YAML。

画面10：
- Nacos 新建配置界面，配置格式选择 YAML，配置内容为空。

画面11：
- IDEA 编辑器显示 `bootstrap.yml` 文件内容，包含端口、Nacos 配置等。
- 代码/配置：
  ```yaml
  server:
    port: 50050 #启动端口，命令行注入
  Nacos:
    server:
      addr: 137.3.8.1:8848
  spring:
    application:
      name: transaction-Service
    main:
      allow-bean-definition-overriding: true # Spring Boot 2.1 新增设置
  cloud:
    Nacos:
      discovery:
        server-addr: ${Nacos.server.addr}
        namespace: ${Nacos.namespace}
        cluster-name: DEFAULT
      config:
        server-addr: ${Nacos.server.addr}
        file-extension: yaml
        namespace: ${Nacos.namespace}
        group: SHANJUPAY_GROUP # 默认支付服务组
        refresh: true
        data-id: spring-boot-http.yaml # Spring Boot http配置
  ```

画面12：
- IDEA 编辑器显示 `bootstrap.yml` 文件内容，包含端口、Nacos 配置等。
- 代码/配置：
  ```yaml
  discovery:
    server-addr: ${Nacos.server.addr}
    namespace: ${Nacos.namespace}
    cluster-name: DEFAULT
  config:
    server-addr: ${Nacos.server.addr}
    file-extension: yaml
    namespace: ${Nacos.namespace}
    group: SHANJUPAY_GROUP # 默认支付服务组
    refresh: true
    data-id: spring-boot-http.yaml # Spring Boot http配置
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

