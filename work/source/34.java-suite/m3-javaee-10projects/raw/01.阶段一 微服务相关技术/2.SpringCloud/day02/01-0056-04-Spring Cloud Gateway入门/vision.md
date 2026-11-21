# 画面线理解：04-Spring Cloud Gateway入门

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day02
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day02\04-Spring Cloud Gateway入门_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:59, 01:46, 02:06, 02:31, 03:26, 03:46, 04:18, 05:07, 07:46, 08:38, 09:24, 10:09, 10:17, 10:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:22:33

1) 这一组画面整体在讲如何在 Spring Cloud 项目中配置和启动一个使用 Eureka 服务发现的 Spring Cloud Gateway 网关，实现将 /user 请求路由到后端 user-service。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT，标题为“3. Spring Cloud Gateway网关简介”和“4. Spring Cloud Gateway入门”，其中“入门”部分描述了需求：通过网关系统 heima-gateway 将包含 /user 的请求路由到 http://127.0.0.1:9091/user。
画面2: 在 IntelliJ IDEA 中，右键点击项目“heima-springcloud”下的“consumer-demo”模块，弹出菜单，准备进行操作。
画面3: 在 IntelliJ IDEA 中，弹出“Module name”对话框，模块名设置为“heima-gateway”，点击“Finish”完成模块创建。
画面4: 在 IntelliJ IDEA 中，打开“heima-gateway”模块的 pom.xml 文件，显示了 Spring Cloud Gateway 的依赖配置。
画面5: 在 IntelliJ IDEA 中，打开“GatewayApplication.java”文件，显示了启用服务发现、配置属性、自动代理、定时任务、Eureka 客户端、负载均衡、断路器、服务注册与发现等注解。
画面6: 在 IntelliJ IDEA 中，打开“application.yml”文件，正在编辑配置，设置了 server.port 为 10010。
画面7: 在 IntelliJ IDEA 中，继续编辑“application.yml”，配置了 Eureka 客户端，设置了服务名、注册中心地址、服务发现间隔、连接数等。
画面8: 在 IntelliJ IDEA 中，继续编辑“application.yml”，配置了 Spring Cloud Gateway 的路由规则，设置了路由 ID、URI、predicates。
画面9: 在 IntelliJ IDEA 中，右键点击“GatewayApplication.java”，弹出菜单，准备运行或调试。
画面10: 在 IntelliJ IDEA 中，运行“GatewayApplication”，控制台显示网关服务启动成功，注册到 Eureka 服务，端口为 10010。
画面11: 在 IntelliJ IDEA 中，编辑“application.yml”，配置了路由规则，注释说明了路由 ID、URI、predicates。
画面12: 在 IntelliJ IDEA 中，打开“heima-gateway”模块的 pom.xml 文件，显示了 Spring Cloud Gateway 的依赖配置。
画面13: 在 IntelliJ IDEA 中，编辑“application.yml”，配置了路由规则，注释说明了路由 ID、URI、predicates。
画面14: 展示课程 PPT，标题为“Spring Cloud 第二天课堂笔记”，其中“实现步骤”部分列出了创建工程、添加启动器依赖、编写启动类和配置文件、修改配置文件、启动测试等步骤，并展示了具体的路由测试地址。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
logging:
  level:
    com.itheima: debug
```
画面4:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-parent</artifactId>
        <version>2.0.0.M4</version>
        <relativePath/>
    </parent>

    <groupId>com.itheima</groupId>
    <artifactId>heima-gateway</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>heima-gateway</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```
画面5:
```java
package com.itheima.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.cloud.client.loadbalancer.LoadBalancerInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequest;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponse;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseHandler;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseInterceptor;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerResponseFactory;
import org.springframework.cloud.client.loadbalancer.LoadBalancerRequestHandler;
import org.springframework
