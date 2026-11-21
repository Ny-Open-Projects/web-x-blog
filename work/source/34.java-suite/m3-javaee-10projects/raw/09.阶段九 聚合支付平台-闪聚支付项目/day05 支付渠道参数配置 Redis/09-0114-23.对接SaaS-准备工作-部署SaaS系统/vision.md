# 画面线理解：23.对接SaaS-准备工作-部署SaaS系统

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\23.对接SaaS-准备工作-部署SaaS系统【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 02:13, 03:13, 04:22, 05:36, 06:43, 08:07, 09:03, 09:52, 10:35, 11:28, 12:22, 13:16, 14:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:33:30

1) 这一组画面整体在讲如何通过 Nacos 配置中心管理微服务的配置，并演示了 Spring Cloud Gateway 服务的启动与配置加载过程。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示项目目录结构，包含多个子模块如 shanjupay-transaction、shanjupay-merchant-application 等。
画面 2: 在 IDEA 中查看 PayChannelServiceApi.java 代码，其中包含从缓存中获取支付渠道参数的逻辑。
画面 3: 在 IDEA 中右键项目，弹出菜单，鼠标悬停在“Reimport”选项上。
画面 4: 在 IDEA 中打开 pom.xml 文件，显示了项目依赖和模块结构，同时弹出“Invalid VCS root mapping”提示。
画面 5: 在 Nacos 配置管理页面，显示了多个配置文件列表，包括 spring-boot-http.yaml、merchant-application.yaml 等。
画面 6: 在 Nacos 配置管理页面，鼠标光标位于“Data ID”输入框内，准备输入或修改配置。
画面 7: 在 Nacos 配置管理页面，选择“user-service.yaml”配置文件，显示其内容为 username: root 和 password: yourpassword。
画面 8: 展示 PPT 页面，标题为“1.4 对接SaaS代码实现”，内容包含 Nacos 配置的详细说明。
画面 9: 在 IDEA 中打开 GatewayBootstrap.java 文件，显示了 Spring Boot 应用的启动类代码。
画面 10: 在 IDEA 中查看调试日志，显示了 Dubbo 服务注册和连接的详细信息。
画面 11: 在 IDEA 中查看调试日志，显示了数据库连接失败的异常信息。
画面 12: 在 IDEA 中打开 bootstrap.yaml 文件，显示了 Nacos 配置的详细内容，包括 server-addr、namespace、cluster-name 等。
画面 13: 在 IDEA 中查看调试日志，显示了服务启动成功的信息，包括 Nacos 注册、Dubbo 服务等。
画面 14: 在 IDEA 中查看调试日志，显示了服务启动完成的信息，包括 Dubbo 服务、QueueProvider 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2 代码：
```java
if (exists) {
    //从redis获取支付渠道参数列表（json串）
    String PayChannelParaDTO.String = cache.get(rediKey);
    //将json转成List<PayChannelParaDTO>
    List<PayChannelParaDTO> payChannelParaDTOs = JSON.parseArray(PayChannelParaDTO, String);
    return payChannelParaDTOs;
}
```

画面 4 pom.xml 结构：
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>
    <groupId>com.shanjupay</groupId>
    <artifactId>shanjupay-user-service</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>shanjupay-user-service</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-consul-discovery</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-rocketmq</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-registry</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-ribbon</artifactId>
        </
