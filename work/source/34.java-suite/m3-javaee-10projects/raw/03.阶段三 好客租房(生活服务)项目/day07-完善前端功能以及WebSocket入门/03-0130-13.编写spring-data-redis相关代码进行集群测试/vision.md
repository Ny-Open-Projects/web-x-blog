# 画面线理解：13.编写spring-data-redis相关代码进行集群测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day07-完善前端功能以及WebSocket入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day07-完善前端功能以及WebSocket入门\13.编写spring-data-redis相关代码进行集群测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:50, 01:40, 02:16, 02:50, 03:24, 03:52, 04:10, 04:48, 05:29, 05:43, 06:18, 06:48, 07:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:26:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置和测试 Redis 集群，包括添加依赖、编写配置类、注册连接工厂和编写测试用例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Redis 集群节点信息，通过 `redis-cli` 查看，显示了多个节点的 IP 和角色（master、myself.master）。
画面 2: 展示了 Maven 依赖配置，用于引入 Spring Boot 的 Redis 支持。
画面 3: 展示了 Spring Boot 的 Redis 集群配置文件内容，包含连接池参数和节点地址。
画面 4: 展示了 IDE 中的项目结构，定位到 `ClusterConfigurationProperties` 类。
画面 5: 展示了 `ClusterConfigurationProperties` 类的代码，定义了 `nodes` 和 `maxRedirects` 字段。
画面 6: 展示了 IDE 中的右键菜单，用于对 `ClusterConfigurationProperties` 类进行操作。
画面 7: 展示了 `RedisClusterConfig` 配置类的代码，用于注册 Redis 连接工厂。
画面 8: 展示了 `ClusterConfigurationProperties` 类中添加了 `@Data` 注解。
画面 9: 展示了 `RedisClusterConfig` 类中定义了 `RedisTemplate` 的 Bean。
画面 10: 展示了测试类 `TestRedis` 的代码，用于测试 Redis 操作。
画面 11: 展示了测试类 `TestRedis` 的代码，使用 `@RunWith(SpringRunner.class)` 和 `@SpringBootTest` 注解。
画面 12: 展示了测试类 `TestRedis` 的代码，使用 `@Test` 注解定义测试方法。
画面 13: 展示了在终端中执行 Redis 命令，查询键值对。
画面 14: 展示了测试类 `TestRedis` 的代码，使用 `@RunWith(SpringRunner.class)` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
root@itcast:/data# redis-cli
127.0.0.1:6379> CLUSTER NODES
46e558c2d296a506955cc6e700834037c31d9 172.16.55.185:6380 172.16.55.185:6380 master - 0
1543766975796 2 connected 5461-10922
b42d6ccc54409f1d8f35fa/ad08b0962a6ac4a 1/2.16.55.185:6381 172.16.55.185:6381 master - 0
154376697489 3 connected 10923-16383
4c60f45d17277783181c64c6c141354f0e28d18 177.16.55.185:6379 177.16.55.185:6379 myself, master - 0
1543766974000 1 connected 0-5460
```

画面 2:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>2.9.0</version>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.10.0</version>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-io</artifactId>
    <version>2.6</version>
</dependency>
```

画面 3:
```properties
# redis集群配置
spring.redis.jedis.pool.max-wait = 5000
spring.redis.jedis.pool.max-idle = 100
spring.redis.jedis.pool.min-idle = 10
spring.redis.timeout = 10
spring.redis.cluster.nodes = 172.16.55.185:6379,172.16.55.185:6380,172.16.55.185:6381
spring.redis.cluster.max-redirects=5
```

画面 4:
```
package cn.itcast.haoke.dubbo.api.config;
```

画面 5:
```java
package cn.itcast.haoke.dubbo.api.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
@ConfigurationProperties(prefix = "spring.redis.cluster")
public class ClusterConfigurationProperties {
    private List<String> nodes;
    private Integer maxRedirects;
}
```

画面 6:
```
// 右键菜单内容
```

画面 7:
```java
package cn.itcast.haoke.dubbo.api.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisClusterConfiguration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.StringRedisSerializer;

@Configuration
public class RedisClusterConfig {
    @Autowired
    private ClusterConfigurationProperties clusterProperties;

    @Bean
    public RedisConnectionFactory connectionFactory() {
        RedisClusterConfiguration configuration = new RedisClusterConfiguration();
        configuration.setNodes(clusterProperties.getNodes());
        configuration.setMaxRedirects(clusterProperties.getMaxRedirects());
        return new RedisConnectionFactory(configuration);
    }
}
```

画面 8:
```java
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import java.util.List;

@Component
@ConfigurationProperties(prefix = "spring.redis.cluster")
@Data
public class ClusterConfigurationProperties {
    private List<String> nodes;
    private Integer maxRedirects;
}
```

画面 9:
```java
@Bean
public RedisTemplate<String, String> redisTemplate(RedisConnectionFactory redisConnectionFactory) {
    RedisTemplate<String, String> redisTemplate = new RedisTemplate<>();
    redisTemplate.setConnectionFactory(redisConnectionFactory);
    redisTemplate.setKeySerializer(new StringRedisSerializer());
    redisTemplate.setValueSerializer(new StringRedisSerializer());
    redisTemplate.afterPropertiesSet();
    return redisTemplate;
}
```

画面 10:
```java
import java.util.Set;

@RunWith(SpringRunner.class)
public class TestRedis {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @Test
    public void testSave() {
        for (int i = 0; i < 100; i++) {
            this.redisTemplate.opsForValue().set("key_" + i, "value_" + i);
        }
        Set<String> keys = this.redisTemplate.keys("key_*");
        for (String key : keys) {
            String value = this.redisTemplate.opsForValue().get(key);
            System.out.println(value);
        }
        this.redisTemplate.delete(key);
    }
}
```

画面 11:
```java
package cn.itcast.haoke.dubbo.api;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestRedis {
```

画面 12:
```java
@Test
public void testSave() {
    for (int i = 0; i < 100; i++) {
        this.redisTemplate.opsForValue().set("key_" + i, "value_" + i);
    }
    Set<String> keys = this.redisTemplate.keys("key_*");
    for (String key : keys) {
        String value = this.redisTemplate.opsForValue().get(key);
        System.out.println(value);
    }
    this.redisTemplate.delete(key);
}
```

画面 13:
```
172.16.55.185:6380> get key_58
"Value 58"
```

画面 14:
```java
package cn.itcast.haoke.dubbo.api;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TestRedis {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“5.4.2、编写配置文件”。
画面 3: PPT 标题为“5.4.2、编写配置
