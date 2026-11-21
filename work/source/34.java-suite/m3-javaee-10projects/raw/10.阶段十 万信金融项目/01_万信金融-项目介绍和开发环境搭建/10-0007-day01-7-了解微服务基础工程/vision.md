# 画面线理解：day01-7-了解微服务基础工程

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-7-了解微服务基础工程_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:16, 01:24, 01:49, 02:57, 03:54, 05:27, 05:57, 07:07, 07:48, 08:44, 10:01, 10:28, 12:21, 13:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:04:00

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的微服务架构项目，包括服务注册发现（Eureka）、网关（Zuul）、消费者服务（Feign + Hystrix）等模块的 Maven 依赖配置和核心配置文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：打开 IntelliJ IDEA，项目结构显示，当前选中模块为 `wanningzp-api`，右侧弹出提示“Invalid VCS root mapping”。
画面2：在 `pom.xml` 中，高亮显示 `elastic-job-lite-spring-boot-starter` 依赖，版本为 `2.1.5`。
画面3：在 `pom.xml` 中，高亮显示 `spring-security-oauth2` 依赖，版本为 `1.0.9.RELEASE`。
画面4：在 `pom.xml` 中，高亮显示 `sharding-jdbc-spring-boot-starter` 依赖，版本为 `2.1.5`。
画面5：在 `pom.xml` 中，高亮显示 `spring-cloud-starter-netflix-eureka-client` 依赖，版本为 `2.1.5`。
画面6：在 `application.yml` 中，高亮显示 `spring.application.name: hrmab-discovery` 和 `server.port: 53000`。
画面7：切换到 `wanningzp-discovery-server` 模块，显示其目录结构。
画面8：在 `application.properties` 中，高亮显示 `spring.application.name=gateway-server`。
画面9：在 `application.properties` 中，高亮显示 `zuul.routes.consumer-service.path=/consumer/**`。
画面10：在 `ZuulConfig.java` 中，高亮显示 `config.setAllowedOrigins("*");`。
画面11：在 `pom.xml` 中，高亮显示 `spring-cloud-starter-netflix-hystrix` 依赖。
画面12：在 `application.properties` 中，高亮显示 `ribbon.MaxAutoRetries=2`。
画面13：在 `pom.xml` 中，高亮显示 `artifactId` 为 `wanningzp-consumer-service`。
画面14：切换到多个窗口，包括项目结构、PPT、浏览器、日志等，显示项目整体架构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<dependency>
    <groupId>com.dangdang</groupId>
    <artifactId>elastic-job-lite-spring-boot-starter</artifactId>
    <version>2.1.5</version>
</dependency>
```

画面3：
```xml
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-oauth2</artifactId>
    <version>1.0.9.RELEASE</version>
</dependency>
```

画面4：
```xml
<parent>
    <artifactId>wanningzp</artifactId>
    <groupId>cn.iteast.wanningzp</groupId>
    <version>1.0-SNAPSHOT</version>
    <modelVersion>4.0.0</modelVersion>
</parent>
```

画面5：
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.6.1</version>
</dependency>
```

画面6：
```yaml
spring:
  application:
    name: hrmab-discovery
  server:
    port: 53000
eureka:
  server:
    enable-self-preservation: false
    eviction-interval-timer-in-ms: 10000
  client:
    register-with-eureka: false
    fetch-registry: false
    serviceUrl:
      defaultZone: http://localhost:8761/eureka/
    instance:
      hostname: ${spring.cloud.client.ip-address}
```

画面8：
```properties
# 应用程序名称
spring.application.name=gateway-server

# 静态资源访问路径
server.servlet.context-path=/


# 开启Swagger
swagger.enable=true

# 日志配置
logging.config=classpath:log4j2-dev.xml

# springCloud 全局异常处理
spring.mvc.throw-exception-if-no-handler-found=true

# 中文编码处理
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
spring.http.encoding.enabled=true

# springCloud zuul配置
```

画面9：
```properties
# 请求超时时间设置
ribbon.ConnectTimeout=3000
# 对所有操作请求都进行重试，如果isGet可以，如果是post、put等操作有实际幂等的情况是重试的，所以设置为false
ribbon.OkToRetryOnAllOperations=false
# 请求重试的超时时间
ribbon.ReadTimeout=20000
# 实际类型的重试次数
ribbon.MaxAutoRetriesNextServer=1

# springCloud zuul相关配置
# 请求没有前端，不用去除前缀，进行请求转发
zuul.routes.consumer-service.path=/consumer/**
# 网关会转发请求头信息
zuul.add-host-header=true
# 大部分自动路由匹配，全部手动匹配，完全
zuul.ignoredServices=
```

画面10：
```java
package cn.iteast.wanningzp.gateway.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class ZuulConfig {

    @Bean
    public FilterRegistrationBean corsFilter() {
        final UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        final CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(true);
        config.addAllowedOrigin("*");
        config.addAllowedHeader("*");
        config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE"));
        config.setMaxAge(1800L);
        source.registerCorsConfiguration("/**", config);
        FilterRegistrationBean bean = new FilterRegistrationBean();
        bean.setFilter(corsFilter);
        bean.setOrder(Ordered.HIGHEST_PRECEDENCE);
        return bean;
    }
}
```

画面11：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```

画面12：
```properties
# springCloud ribbon配置
# 最大重试次数，当Eureka中可以找到服务，但是服务不上的时候会重试
ribbon.MaxAutoRetries=2
# 对所有操作请求都进行重试，如果isGet可以，如果是post、put等操作有实际幂等的情况是重试的，所以设置为false
ribbon.OkToRetryOnAllOperations=false
# 请求重试的超时时间
ribbon.ReadTimeout=20000
# 实际类型的重试次数
ribbon.MaxAutoRetriesNextServer=2
```

画面13：
```xml
<parent>
    <artifactId>wanningzp</artifactId>
    <groupId>cn.iteast.wanningzp</groupId>
    <version>1.0-SNAPSHOT</version>
    <modelVersion>4.0.0</modelVersion>
</parent>
```

画面14：
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：显示多个窗口，包括项目结构、PPT、浏览器、日志等，但未显示具体 PPT 标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
