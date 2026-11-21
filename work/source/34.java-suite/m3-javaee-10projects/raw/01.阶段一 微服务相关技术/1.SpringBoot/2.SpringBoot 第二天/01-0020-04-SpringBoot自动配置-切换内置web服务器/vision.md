# 画面线理解：04-SpringBoot自动配置-切换内置web服务器

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\04-SpringBoot自动配置-切换内置web服务器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:05, 01:41, 02:13, 02:28, 02:57, 03:29, 03:57, 04:38, 05:05, 05:40, 05:52, 06:33, 06:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:51:36

1) 这一组画面整体在讲 Spring Boot 项目中如何通过条件化配置（@ConditionalOnClass、@ConditionalOnBean）来控制嵌入式 Web 服务器（Tomcat、Jetty）的自动装配与排除。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示项目结构和 pom.xml 文件，其中包含 spring-boot-starter-data-redis 和 spring-boot-starter-web 依赖。
画面 2: 控制台输出显示 Spring Boot 应用启动，使用默认配置，未指定 profile。
画面 3: 控制台输出显示 Spring Boot 应用启动，使用默认配置，未指定 profile。
画面 4: 项目结构中选中了 spring-boot-autoconfigure 模块，展示其内部的嵌入式 Web 服务器相关类。
画面 5: 项目结构中选中了 spring-boot-autoconfigure 模块下的 web 包，展示其内部的 EmbeddedWebServerFactoryCustomizerAutoConfiguration 类。
画面 6: 项目结构中选中了 EmbeddedWebServerFactoryCustomizerAutoConfiguration 类。
画面 7: 显示 EmbeddedWebServerFactoryCustomizerAutoConfiguration.java 文件内容，其中包含 @Configuration 和 @ConditionalOnClass 注解，用于条件化配置。
画面 8: 显示 EmbeddedWebServerFactoryCustomizerAutoConfiguration.java 文件内容，其中包含 @Configuration 和 @ConditionalOnClass 注解，用于条件化配置。
画面 9: 显示 pom.xml 文件，其中包含 spring-boot-starter-web 依赖。
画面 10: 显示 Spring Boot 项目的依赖关系图，展示 spring-boot-starter-web 依赖的各个模块。
画面 11: 显示 Spring Boot 项目的依赖关系图，展示 spring-boot-starter-web 依赖的各个模块。
画面 12: 显示 pom.xml 文件，其中在 spring-boot-starter-web 依赖中添加了 <exclusions> 标签，排除 spring-boot-starter-tomcat。
画面 13: 显示 pom.xml 文件，其中添加了 spring-boot-starter-jetty 依赖。
画面 14: 控制台输出显示 Spring Boot 应用启动，使用 Jetty 作为嵌入式 Web 服务器。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

画面 7:
```java
/**
 * @link EnableAutoConfiguration for embedded servlet and reactive
 * web servers customizers.
 * @author Phillip Webb
 * @since 2.0.0
 */
@Configuration
@ConditionalOnWebApplication
@EnableConfigurationProperties(ServerProperties.class)
public class EmbeddedWebServerFactoryCustomizerAutoConfiguration {

    /**
     * Nested configuration if Tomcat is being used.
     */
    @Configuration
    @ConditionalOnClass({ Tomcat.class, UpgradeProtocol.class })
    public static class TomcatWebServerFactoryCustomizerConfiguration {
        @Bean
        public TomcatWebServerFactoryCustomizer tomcatWebServerFactoryCustomizer(Environment environment, ServerProperties serverProperties) {
            return new TomcatWebServerFactoryCustomizer(environment, serverProperties);
        }
    }

    /**
     * Nested configuration if Jetty is being used.
     */
    @Configuration
    @ConditionalOnClass({ Server.class, Loader.class, WebAppContext.class })
    public static class JettyWebServerFactoryCustomizerConfiguration {
```

画面 12:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

画面 13:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jetty</artifactId>
</dependency>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10: 依赖关系图，展示 spring-boot-starter-web 依赖的各个模块。
画面 11: 依赖关系图，展示 spring-boot-starter-web 依赖的各个模块。

5) 不要评价画面美观，不要输出与课程无关的内容。
