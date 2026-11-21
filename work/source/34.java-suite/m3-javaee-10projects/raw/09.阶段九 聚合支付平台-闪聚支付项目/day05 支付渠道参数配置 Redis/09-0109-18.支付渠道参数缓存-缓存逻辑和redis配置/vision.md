# 画面线理解：18.支付渠道参数缓存-缓存逻辑和redis配置

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\18.支付渠道参数缓存-缓存逻辑和redis配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:43, 02:16, 03:35, 04:09, 04:45, 05:11, 05:44, 06:19, 06:59, 07:30, 08:04, 08:43, 09:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:29:28

1) 这一组画面整体在讲什么（一句话）：
实现支付渠道参数缓存功能，通过 Redis 缓存提升查询性能，并展示如何在 Spring Boot 项目中配置和使用 Redis。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“5.6 支付渠道参数缓存”章节，重点是“5.6.1 需求分析”，说明将渠道参数缓存到 Redis 以提升查询性能。
画面2：在 IntelliJ IDEA 中查看 `PlatformParamController.java` 代码，展示查询支付渠道参数的接口方法。
画面3：在 IntelliJ IDEA 中查看 `PayChannelService.java` 代码，展示查询支付渠道参数的业务逻辑。
画面4：在 Postman 中测试支付渠道参数查询接口，参数包括 appid、payChannel、platformChannel。
画面5：在 Typora 中查看 Nacos 中的 Redis 配置文件 `spring-boot-redis.yaml`，配置了 Redis 的连接信息和连接池参数。
画面6：在 Typora 中展示如何在 `shanjupay-transaction-service` 工程的 `bootstrap.yml` 中引入 Redis 配置。
画面7：在 Typora 中展示如何在 `shanjupay-transaction-service` 工程的 `pom.xml` 中添加 Redis 依赖。
画面8：在 IntelliJ IDEA 中查看 `RedisEnum.java` 代码，定义了 Redis 缓存的键前缀、模块、方法名、描述等。
画面9：在 IntelliJ IDEA 中查看 `RedisEnum.java` 代码，展示其构造函数和 getPrefix 方法。
画面10：在 IntelliJ IDEA 中查看 `RedisCache.java` 代码，展示其 `set` 和 `get` 方法。
画面11：在 IntelliJ IDEA 中查看 `RedisCache.java` 代码，展示其构造函数和 `getKeys` 方法。
画面12：在 IntelliJ IDEA 中查看 `RedisConfig.java` 代码，展示其 `@Configuration` 注解和 `Cache cache()` 方法。
画面13：在 IntelliJ IDEA 中查看 `PayChannelService.java` 代码，展示其 `queryPayChannelParamsByAppIdAndPlatformChannel` 方法。
画面14：再次展示课程文档“5.6 支付渠道参数缓存”章节，重点是“5.6.1 需求分析”，说明将渠道参数缓存到 Redis 以提升查询性能。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```yaml
spring:
  redis:
    # Redis数据库索引（默认为0）
    database: 0
    host: 127.0.0.1
    port: 6379
    # 连接超时时间（毫秒）
    timeout: 1000ms
    password: 123456
  lettuce:
    pool:
      # 连接池中的最大空闲连接
      max-idle: 8
      # 连接池中的最小空闲连接
      min-idle: 0
      # 连接池最大连接数（使用负值表示没有限制）
      max-active: 8
      # 连接池最大阻塞等待时间（使用负值表示没有限制）
      max-wait: 1000ms
      shutdown-timeout: 1000ms
```

画面6：
```yaml
refresh: true
data-id: spring-boot-redis.yaml # redis配置
group: COMMON_GROUP # 通用配置组
```

画面7：
```xml
<!-- Redis启动器 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

画面8：
```java
package com.shanju.pay.common.util;

/**
 * @author Administrator
 * @version 1.0
 */
public class RedisEnum {
    /**
     * 缓存键前缀
     */
    private String keyPrefix;
    /**
     * 模块名称
     */
    private String module;
    /**
     * 方法名称
     */
    private String func;
    /**
     * 描述
     */
    private String remark;

    RedisEnum(String keyPrefix, String module, String func, String remark) {
        this.keyPrefix = keyPrefix;
        this.module = module;
        this.func = func;
        this.remark = remark;
    }

    public String getKeyPrefix() {
        return keyPrefix;
    }
}
```

画面10：
```java
/**
 * 简单的字符串设置
 * @param key
 * @param value
 */
void set(String key, String value);
```

画面11：
```java
package com.shanju.pay.transaction.common.util;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

@Component
public class RedisCache implements Cache {
    private RedisTemplate<String, Object> redisTemplate;

    public RedisCache(RedisTemplate<String, Object> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Override
    public Set<String> getKeys(String pattern) {
        return redisTemplate.keys(pattern);
    }
}
```

画面12：
```java
import com.shanju.pay.common.cache.Cache;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;

@Configuration
public class RedisConfig {
    @Bean
    public Cache cache(RedisTemplate<String, Object> redisTemplate) {
        return new RedisCache(redisTemplate);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、14：PPT 标题为“5.6 支付渠道参数缓存”，子标题“5.6.1 需求分析”和“5.6.2 搭建redis环境”。
画面5：PPT 标题为“5.6.2 搭建redis环境”，子标题“2. 在Nacos中添加Redis配置：spring-boot-redis.yaml, Group: COMMON_GROUP”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
