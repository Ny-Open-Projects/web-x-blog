# 画面线理解：day02-6-搭建统一账户微服务

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-6-搭建统一账户微服务_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:32, 02:23, 03:19, 03:54, 04:39, 06:05, 06:37, 07:15, 08:37, 10:21, 11:52, 12:38, 13:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:16:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置并运行一个基于 Spring Cloud 和 Apollo 配置中心的微服务项目，并在 Apollo 控制台中创建和管理配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 项目结构，根目录为 `wanning2p-apollo`，包含多个子模块，如 `wanning2p-account-service`、`wanning2p-consumer-service` 等。
画面 2: 在项目结构中，选中 `Modules`，并设置 `wanning2p-account-service` 的源码路径为 `C:\Users\xu\...\wanning2p\day02\...\wanning2p-account-service`。
画面 3: 在 `pom.xml` 文件中，显示了 `wanning2p-account-service` 的依赖项，包括 `rocketmq-spring-boot-starter`、`jethrians-annotations`、`kryo` 等。
画面 4: 在 `pom.xml` 文件中，显示了 `spring-boot-maven-plugin` 插件的配置。
画面 5: 在 `application-dev.properties` 文件中，配置了 `dev.meta`、`fat.meta`、`uat.meta` 等环境变量。
画面 6: 在 `Wanning2pAccountServiceApplication` 类中，显示了 Spring Boot 的主类结构。
画面 7: 在 `pom.xml` 文件中，显示了 `spring-cloud-starter-netflix-eureka-client` 依赖项。
画面 8: 在 `wanning2p-common` 模块的 `pom.xml` 文件中，显示了 `parent` 和 `dependencies` 配置，其中 `artifactId` 为 `wanning2p-account-service`。
画面 9: 在浏览器中，显示了 Apollo 配置中心的“创建项目”页面，包含“部门”、“应用ID”、“应用名称”、“应用负责人”、“项目管理员”等字段。
画面 10: 在浏览器中，显示了 Apollo 配置中心的“创建 Namespace”页面，应用 ID 为 `account-service`，环境为 `DEV`，默认 namespace。
画面 11: 在浏览器中，显示了 Apollo 配置中心的“公共配置”页面，包含 `spring.http.encoding.enabled`、`spring.http.encoding.charset`、`spring.http.encoding.force` 等配置项。
画面 12: 在浏览器中，显示了 Apollo 配置中心的“application”配置页面，包含 `micro_service.spring-boot-http`、`micro_service.spring-eureka`、`micro_service.spring-hystrix`、`micro_service.spring-ribbon`、`micro_service.spring-boot-redis` 等配置项。
画面 13: 在浏览器中，显示了 Apollo 配置中心的“公共配置”页面，包含 `spring.datasource.type`、`spring.datasource.driver-class-name`、`spring.datasource.url`、`spring.datasource.username`、`spring.datasource.password`、`spring.datasource.druid.initial-size` 等配置项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
</dependency>
<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
</dependency>
<dependency>
    <groupId>org.jethrians</groupId>
    <artifactId>annotations</artifactId>
    <version>RELEASE</version>
    <scope>compile</scope>
</dependency>
<dependency>
    <groupId>com.esotericsoftware</groupId>
    <artifactId>kryo</artifactId>
    <version>4.0.2</version>
</dependency>
```

画面 4:
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
</plugin>
```

画面 5:
```properties
dev.meta=http://localhost:8080
fat.meta=http://211.103.136.242:7134
uat.meta=http://172.17.0.83:8080
pro.meta=http://10.10.10.10:8080
```

画面 6:
```java
package cn.itcast.wanning2p.account;

import ...

@SpringBootApplication
@EnableDiscoveryClient
public class Wanning2pAccountServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(Wanning2pAccountServiceApplication.class, args);
    }
}
```

画面 7:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
```

画面 8:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>wanning2p</artifactId>
        <groupId>cn.itcast.wanning2p</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>wanning2p-account-service</artifactId>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>cn.itcast.wanning2p</groupId>
            <artifactId>wanning2p-api</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</project>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
