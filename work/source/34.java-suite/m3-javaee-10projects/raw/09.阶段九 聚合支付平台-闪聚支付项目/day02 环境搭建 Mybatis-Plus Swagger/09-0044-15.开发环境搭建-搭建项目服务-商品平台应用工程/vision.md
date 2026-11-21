# 画面线理解：15.开发环境搭建-搭建项目服务-商品平台应用工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\15.开发环境搭建-搭建项目服务-商品平台应用工程【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:24, 02:22, 03:32, 04:45, 05:52, 06:57, 08:09, 09:25, 10:57, 12:27, 14:01, 15:12, 16:17, 17:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:43:45

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中创建并配置商户平台应用工程，包括添加依赖、配置 Nacos 和 Spring Boot 启动类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程大纲，当前章节为“1.6 搭建项目服务”，列出三个服务：商户平台应用、商户服务API、商户服务及其职责。
画面2：在 IntelliJ IDEA 中右键点击项目，选择“New” -> “Module” 创建新模块，设置 Maven 和 JDK 1.8。
画面3：展示 `pom.xml` 文件内容，其中包含 `artifactId` 为 `shanjiupay-merchant-application` 的依赖，以及 Nacos 配置中心、服务发现、Dubbo 启动器等依赖。
画面4：展示 `pom.xml` 文件内容，其中包含 Spring Boot Actuator 依赖，并提示在 Nacos 中添加 `spring-boot-http.yaml` 配置，Group 为 `COMMON_GROUP`。
画面5：展示 `pom.xml` 文件内容，其中包含 Spring Boot Test 依赖。
画面6：在 Nacos 控制台中，选择“配置管理” -> “服务管理” -> “创建配置”，准备添加配置。
画面7：在 IntelliJ IDEA 中打开 `bootstrap.yml` 文件，显示项目结构和依赖。
画面8：展示 `bootstrap.yml` 文件内容，包含 `ext-config` 配置，引用 `spring-boot-http.yaml`，以及 `server` 和 `dubbo` 配置。
画面9：展示 `bootstrap.yml` 文件内容，包含 `logging` 配置，指定日志文件为 `log4j2.xml`。
画面10：在 IntelliJ IDEA 中右键点击项目，选择“New” -> “Package” 创建新包。
画面11：在 IntelliJ IDEA 中打开 `log4j2.xml` 文件，显示日志配置。
画面12：在 IntelliJ IDEA 中打开 `MerchantApplicationBootstrap.java` 文件，显示 Spring Boot 启动类。
画面13：展示 `bootstrap.yml` 文件内容，包含 `cluster-name`、`server-addr`、`namespace`、`ext-config` 等配置。
画面14：展示 `MerchantApplicationBootstrap.java` 文件内容，包含 `@SpringBootApplication`、`@EnableDiscoveryClient` 注解，以及 `main` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```xml
<artifactId>shanjiupay-merchant-application</artifactId>

<dependencies>
    <!--Nacos配置中心-->
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
    </dependency>

    <!--Nacos服务发现与配置中心-->
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
    </dependency>

    <!--Dubbo启动器-->
    <dependency>
        <groupId>com.alibaba.cloud</groupId>
        <artifactId>spring-cloud-starter-dubbo</artifactId>
    </dependency>

    <!--Web启动器-->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

画面4：
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<!--测试启动器-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

画面6：
```yaml
#HTTP格式配置
spring:
  http:
    encoding:
      charset: UTF-8
```

画面7：
```yaml
#HTTP格式配置
spring:
  http:
    encoding:
      charset: UTF-8
      force: true
      enabled: true
    messages:
      encoding:
        charset: UTF-8
```

画面8：
```yaml
ext-config:
  - refresh: true
  - data-id: spring-boot-http.yaml # spring boot http配置
  - group: COMMON_GROUP # 通用配置组
  - server:
    servlet:
      multipart:
        # 支持文件上传
        enabled: true
        # 支持文件写入磁盘
        file-size-threshold: 0
        # 上传文件的临时目录
        location: 
        # 最大文件大小
        max-file-size: 1MB
        # 最大支持请求数
        max-request-size: 5MB
```

画面9：
```yaml
#HTTP格式配置
spring:
  http:
    encoding:
      charset: UTF-8
      force: true
      enabled: true
    messages:
      encoding:
        charset: UTF-8
```

画面10：
```xml
<configuration>
    <appenders>
        <console name="Console" target="SYSTEM_OUT">
            <patternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </console>
    </appenders>
    <loggers>
        <root level="info">
            <appenderRef ref="Console"/>
        </root>
    </loggers>
</configuration>
```

画面12：
```java
package com.shanjiupay.merchant;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class MerchantApplicationBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(MerchantApplicationBootstrap.class, args);
    }
}
```

画面13：
```yaml
cluster-name: DEFAULT
server-addr: ${nacos.server.addr} # nacos服务地址
file-extension: yaml
namespace: ${nacos.namespace} # 命令行注入
group: SHANJIUPAY_GROUP # 聚合支付业务组
ext-config:
  - refresh: true
  - data-id: spring-boot-http.yaml # spring boot http配置
  - group: COMMON_GROUP # 通用配置组
  - server:
    servlet:
      multipart:
        # 支持文件上传
        enabled: true
        # 支持文件写入磁盘
        file-size-threshold: 0
        # 上传文件的临时目录
        location:
        # 最大文件大小
        max-file-size: 1MB
        # 最大支持请求数
        max-request-size: 5MB
```

画面14：
```java
package com.shanjiupay.merchant;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class MerchantApplicationBootstrap {
    public static void main(String[] args) {
        SpringApplication.run(MerchantApplicationBootstrap.class, args);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1.6 搭建项目服务”，表格内容为：
| 服务名 | 职责 |
| --- | --- |
| 商户平台应用(shanjiupay-merchant-application) | 为前端提供商户管理功能 |
| 商户服务API(shanjiupay-merchant-api) | 定义商户服务提供的接口 |
| 商户服务(shanjiupay-merchant-service) | 实现商户服务的所有接口 |

画面4：PPT 标题为“6. 在Nacos中添加spring-boot-http.yaml配置，Group：COMMON_GROUP”，并提示“这里统一使用dev命名空间，没有此命名空间则在Nacos中创建”。

画面7：PPT 标题为“6. 在Nacos中添加spring-boot-http.yaml配置，Group：COMMON_GROUP”，并提示“这里统一使用dev命名空间，没有此命名空间则在Nacos中创建”。

画面9：PPT 标题为“7. 在Nacos中添加spring-boot-http.yaml配置，Group：COMMON_GROUP”，并提示“这里统一使用dev命名空间，没有此命名空间则在Nacos中创建”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
