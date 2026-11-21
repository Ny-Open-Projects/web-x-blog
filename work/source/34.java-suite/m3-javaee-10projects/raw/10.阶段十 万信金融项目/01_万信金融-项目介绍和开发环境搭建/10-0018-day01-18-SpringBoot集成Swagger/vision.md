# 画面线理解：day01-18-SpringBoot集成Swagger

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-18-SpringBoot集成Swagger_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:52, 01:09, 01:53, 02:03, 02:49, 03:08, 03:54, 05:52, 06:10, 06:55, 07:27, 08:08, 08:44, 09:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:11:07

1) 这一组画面整体在讲如何在 SpringBoot 项目中集成 Swagger2 以实现 API 文档自动生成。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示项目结构，包含 `wanningzp-common` 和 `wanningzp-consumer-service` 模块，IDEA 界面展示 Maven 项目依赖和目录结构。
画面 2: PPT 页面标题为“2.1.2 SpringBoot集成Swagger”，内容讲解引入 Swagger 依赖，展示 Maven 依赖配置代码。
画面 3: IDE 中打开 `wanningzp-consumer-service` 的 `pom.xml` 文件，显示项目依赖，包括 `spring-cloud-starter-netflix-eureka-client` 和 `spring-boot-starter-web`。
画面 4: IDE 中 `wanningzp-common` 的 `pom.xml` 文件，高亮显示 `springfox-swagger2` 和 `springfox-swagger-ui` 依赖。
画面 5: IDE 中 `wanningzp-common` 的 `pom.xml` 文件，高亮显示 `springfox-swagger2` 和 `springfox-swagger-ui` 依赖。
画面 6: IDE 中 `wanningzp-consumer-service` 的 `application.properties` 文件，配置 Swagger 启动开关 `swagger.enable=true`。
画面 7: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解和 `@EnableSwagger2` 注解。
画面 8: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `paths(PathSelectors.any())` 方法。
画面 9: JavaDoc 界面，显示 `String` 类的文档，解释其不可变性。
画面 10: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `ApiInfo` 的 `title` 和 `description` 字段。
画面 11: IDE 中 `application.properties` 文件，显示 `swagger.enable=true` 配置。
画面 12: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解。
画面 13: IDE 中 `SwaggerConfiguration.java` 文件，高亮显示 `@ConditionalOnProperty` 注解。
画面 14: PPT 页面，标题为“2.1.2 SpringBoot集成Swagger”，内容讲解引入依赖和配置。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

画面 3:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>
<dependency>
    <groupId>com.netflix.hystrix</groupId>
    <artifactId>hystrix-javanica</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
</dependency>
```

画面 6:
```properties
# 应用程序名称
spring.application.name=consumer-service
# 需要服务访问路径
server.servlet.context-path=/consumer
# 开启swagger
swagger.enable=true
# 日志配置
logging.config=classpath:log4j2-dev.xml
# spring 全局异常处理
spring.mvc.throw-exception-if-no-handler-found=true
# 中文乱码处理
spring.http.encoding.charset=UTF-8
spring.http.encoding.force=true
# springCloud eureka
eureka.client.serviceUrl.defaultZone=http://localhost:53000/eureka/
```

画面 7:
```java
@ConditionalOnProperty(prefix = "swagger", value = "enable", havingValue = "true")
@EnableSwagger2 // 开启swagger支持
public class SwaggerConfiguration {
```

画面 8:
```java
.paths(PathSelectors.any())
```

画面 10:
```java
.title("万信金融P2P平台-用户服务API文档")
.description("包含用户服务api")
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 2: PPT 标题为“2.1.2 SpringBoot集成Swagger”，内容包括“1. 引入依赖”和“2. 在wanningzp_consumer工程的application.properties中配置swagger的启动开关”。
画面 14: PPT 标题为“2.1.2 SpringBoot集成Swagger”，内容包括“1. 引入依赖”和“2. 在wanningzp_consumer工程的application.properties中配置swagger的启动开关”。

5) 无。
