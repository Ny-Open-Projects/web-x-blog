# 画面线理解：11_爬虫数据排重_redis集成

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\11_爬虫数据排重_redis集成【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:37, 00:56, 01:10, 01:20, 01:42, 02:00, 02:11, 02:30, 02:48, 02:56, 03:14, 03:33, 03:49, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:06:39

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Redis，包括配置文件设置和自定义配置类的编写。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程文档，介绍“2.1 集成redis”，并显示 `redis.properties` 配置文件内容。
画面2: 在 IntelliJ IDEA 中右键点击 `redis.properties` 文件，弹出操作菜单。
画面3: 在项目结构中选中 `redis.properties` 文件，准备进行操作。
画面4: 在项目结构中选中 `redis.properties` 文件，准备进行操作。
画面5: 展示 `redis.properties` 文件内容，其中包含 Redis 连接配置。
画面6: 在 `RedisConfiguration.java` 文件中，查看 `RedisAutoConfiguration` 类的继承关系。
画面7: 在 `RedisConfiguration.java` 文件中，查看 `@Configuration` 和 `@PropertySource` 注解。
画面8: 在 `RedisConfiguration.java` 文件中，输入 `@ConfigurationProperties(prefix = "spring_redis")` 注解。
画面9: 在 `RedisConfiguration.java` 文件中，确认 `@ConfigurationProperties(prefix = "spring_redis")` 注解。
画面10: 查看 `RedisAutoConfiguration` 类的源码，其中包含 `@Bean` 注解和 `RedisTemplate` 的创建。
画面11: 查看 `RedisAutoConfiguration` 类的源码，其中包含 `StringRedisTemplate` 的创建。
画面12: 在项目结构中选中 `heima-leadnews-crawler` 模块。
画面13: 在 `RedisConfig.java` 文件中，输入 `@Configuration` 注解。
画面14: 在 `RedisConfig.java` 文件中，输入 `@ComponentScan` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```
#redis config
spring.redis.host=127.0.0.1
spring.redis.port=6379
spring.redis.password=123456
spring.redis.timeout=90000
spring.redis.lettuce.pool.max-active=8
spring.redis.lettuce.pool.max-idle=8
spring.redis.lettuce.pool.min-idle=0
spring.redis.lettuce.pool.max-wait=-1
```

画面5:
```
#redis config
spring.redis.host=127.0.0.1
spring.redis.port=6379
spring.redis.password=123456
spring.redis.timeout=90000
spring.redis.lettuce.pool.max-active=8
spring.redis.lettuce.pool.max-idle=8
spring.redis.lettuce.pool.min-idle=0
spring.redis.lettuce.pool.max-wait=-1
```

画面6:
```
package com.heima.common.redis;
public class RedisConfiguration extends RedisAutoConfiguration {
```

画面7:
```
@Configuration
@PropertySource("classpath:redis.properties")
@ConfigurationProperties(prefix = "spring_redis")
public class RedisConfiguration extends RedisAutoConfiguration {
```

画面8:
```
@Configuration
@PropertySource("classpath:redis.properties")
@ConfigurationProperties(prefix = "spring_redis")
public class RedisConfiguration extends RedisAutoConfiguration {
```

画面9:
```
@Configuration
@PropertySource("classpath:redis.properties")
@ConfigurationProperties(prefix = "spring_redis")
public class RedisConfiguration extends RedisAutoConfiguration {
```

画面10:
```
@Configuration
@Import({LettuceConnectionConfiguration.class, RedisConnectionConfiguration.class})
public class RedisAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    name = "redisTemplate"
    public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
        RedisTemplate<Object, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(redisConnectionFactory);
        return template;
    }
}
```

画面11:
```
@Configuration
@Import({LettuceConnectionConfiguration.class, RedisConnectionConfiguration.class})
public class RedisAutoConfiguration {
    @Bean
    @ConditionalOnMissingBean
    name = "redisTemplate"
    public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
        RedisTemplate<Object, Object> template = new RedisTemplate<>();
        template.setConnectionFactory(redisConnectionFactory);
        return template;
    }
}
```

画面13:
```
@Configuration
public class RedisConfig {
```

画面14:
```
@Configuration
@ComponentScan
public class RedisConfig {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
