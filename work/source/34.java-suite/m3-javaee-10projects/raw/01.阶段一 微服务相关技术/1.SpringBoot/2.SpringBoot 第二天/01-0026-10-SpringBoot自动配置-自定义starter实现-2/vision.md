# 画面线理解：10-SpringBoot自动配置-自定义starter实现-2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\10-SpringBoot自动配置-自定义starter实现-2_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 00:41, 01:34, 02:04, 02:47, 03:03, 03:37, 04:12, 04:40, 05:13, 05:31, 05:49, 06:13, 06:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:00:56

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过自定义配置类和配置属性类，实现对 Redis 客户端（Jedis）的自动配置与注入。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印，演示了手动获取 Bean 的方式。
画面 2: 在主类中调用 jedis.set("name", "itcast");，向 Redis 写入数据。
画面 3: 展示了 application.properties 文件，用于配置 Spring Boot 应用。
画面 4: 在 application.properties 文件中，设置了 redis.port=6379。
画面 5: 展示了 RedisAutoConfiguration.java 文件，其中包含 @Configuration 和 @EnableConfigurationProperties(RedisProperties.class) 注解，用于自动配置 Redis。
画面 6: 在 RedisAutoConfiguration.java 中，定义了 @Bean 方法，用于创建 Jedis Bean。
画面 7: 在 RedisAutoConfiguration.java 中，为 Jedis Bean 添加了 @ConditionalOnMissingBean(name = "jedis") 注解，确保只有当没有同名 Bean 时才创建。
画面 8: 展示了 RedisProperties.java 文件，用于定义 Redis 的配置属性。
画面 9: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 10: 在 RedisAutoConfiguration.java 中，为 Jedis Bean 添加了 @ConditionalOnMissingBean(name = "jedis") 注解。
画面 11: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 12: 在 Spring Boot 应用的主类中，通过 context.getBean(Jedis.class) 获取 Jedis 实例并打印。
画面 13: 展示了 Spring Boot 自动配置的源码结构，其中包含 RedisAutoConfiguration 类。
画面 14: 展示了 RedisProperties.java 文件，其中定义了 Redis 的配置属性，如 host、port、password 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 2:
```java
jedis.set("name", "itcast");
```

画面 3:
无代码，仅展示 application.properties 文件。

画面 4:
```properties
redis.port=6379
```

画面 5:
```java
package com.ltheima.redis.config;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import redis.clients.jedis.Jedis;
@Configuration
@EnableConfigurationProperties(RedisProperties.class)
public class RedisAutoConfiguration {
```

画面 6:
```java
@Bean
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 7:
```java
@Bean
@ConditionalOnMissingBean(name = "jedis")
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 8:
无代码，仅展示 RedisProperties.java 文件。

画面 9:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 10:
```java
@Bean
@ConditionalOnMissingBean(name = "jedis")
public Jedis jedis(RedisProperties redisProperties){
    return new Jedis(redisProperties.getHost(),redisProperties.getPort());
}
```

画面 11:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 12:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

画面 13:
无代码，仅展示 Spring Boot 自动配置的源码结构。

画面 14:
```java
private String host = "localhost";
private int port = 6379;
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无 PPT 标题、架构图/流程图或表格数据。

5) 不评价画面美观，不输出与课程无关的内容。
