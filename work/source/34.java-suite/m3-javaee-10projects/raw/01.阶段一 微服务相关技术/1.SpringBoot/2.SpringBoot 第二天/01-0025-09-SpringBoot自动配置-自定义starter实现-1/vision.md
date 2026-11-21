# 画面线理解：09-SpringBoot自动配置-自定义starter实现-1

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\09-SpringBoot自动配置-自定义starter实现-1_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:28, 01:54, 02:40, 03:37, 04:22, 05:14, 06:33, 07:58, 09:00, 09:38, 10:19, 10:54, 11:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:00:28

1) 这一组画面整体在讲如何通过 Spring Boot 的自动配置机制，自定义一个 Redis 客户端的配置并使其在应用启动时自动生效。

2) 按时间顺序列出每张画面的要点：
画面 1: 打开 IntelliJ IDEA，显示项目结构，包含 springboot-condition、springboot-enable-other 等模块。
画面 2: 在项目结构中创建新模块，选择 Spring Boot 2.1.8 版本，并在依赖中选择 Developer Tools。
画面 3: 编辑 pom.xml 文件，添加 Spring Boot Starter 依赖。
画面 4: 在项目结构中展开 redis-spring-boot-autoconfigure 模块，查看其目录结构和 pom.xml 文件内容。
画面 5: 打开 RedisSpringBootStarterApplicationTests 测试类，准备编写测试。
画面 6: 打开 RedisAutoConfiguration.java 文件，准备编写自动配置类。
画面 7: 在 RedisAutoConfiguration.java 中编写返回 Jedis 实例的代码。
画面 8: 创建 RedisProperties.java 文件，用于配置 Redis 的 host 和 port。
画面 9: 在 RedisAutoConfiguration.java 中使用 @EnableConfigurationProperties 注解绑定 RedisProperties。
画面 10: 查看 Spring Boot 源码中的 EnableAutoConfiguration.java，了解自动配置的机制。
画面 11: 在 resources 目录下创建 META-INF/spring.factories 文件。
画面 12: 编辑 spring.factories 文件，添加自动配置类的全限定名。
画面 13: 打开 SpringbootEnableApplication.java，编写主方法，获取 Bean。
画面 14: 在 SpringbootEnableApplication.java 中获取 Jedis Bean 并打印，验证自动配置是否生效。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 3:
```xml
<name>redis-spring-boot-starter</name>
<description>Demo project for Spring Boot</description>
<properties>
    <java.version>1.8</java.version>
</properties>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

画面 4:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.8.RELEASE</version>
    <relativePath/>
</parent>
<groupId>com.ithema</groupId>
<artifactId>redis-spring-boot-starter</artifactId>
<version>0.0.1-SNAPSHOT</version>
<name>redis-spring-boot-starter</name>
<description>Demo project for Spring Boot</description>
<properties>
    <java.version>1.8</java.version>
</properties>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>com.ithema</groupId>
        <artifactId>redis-spring-boot-autoconfigure</artifactId>
        <version>0.0.1-SNAPSHOT</version>
    </dependency>
</dependencies>
```

画面 5:
```java
package com.ithema.redis;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
@RunWith(SpringRunner.class)
@SpringBootTest
public class RedisSpringBootStarterApplicationTests {
    @Test
    public void contextLoads() {
    }
}
```

画面 6:
```java
package com.ithema.redis.config;
import org.springframework.context.annotation.Configuration;
@Configuration
public class RedisAutoConfiguration {
    // 提供redis的bean
}
```

画面 7:
```java
public Jedis jedis(){
    return new Jedis("localhost", 6379);
}
```

画面 8:
```java
package com.ithema.redis.config;
import org.springframework.boot.context.properties.ConfigurationProperties;
@ConfigurationProperties(prefix = "redis")
public class RedisProperties {
    private String host;
    private int port;
    public String getHost() {
        return host;
    }
    public void setHost(String host) {
        this.host = host;
    }
    public int getPort() {
        return port;
    }
    public void setPort(int port) {
        this.port = port;
    }
}
```

画面 9:
```java
@Configuration
@EnableConfigurationProperties(RedisProperties.class)
public class RedisAutoConfiguration {
    // 提供redis的bean
    @Bean
    @ConfigurationProperties(prefix = "redis")
    public Jedis jedis() {
        return new Jedis("localhost", 6379);
    }
}
```

画面 10:
```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Import(AutoConfigurationImportSelector.class)
public @interface EnableAutoConfiguration {
    String[] exclude() default {};
    Class<?>[] excludeName() default {};
}
```

画面 11:
```ini
# META-INF/spring.factories
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.ithema.redis.config.RedisAutoConfiguration
```

画面 12:
```ini
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
com.ithema.redis.config.RedisAutoConfiguration
```

画面 13:
```java
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        // Object user = context.getBean(User.class);
        // System.out.println(user);
        // Role role = context.getBean(Role.class);
        // System.out.println(role);
        // Object user = context.getBean("user");
        // System.out.println(user);
        // Map<String, User> map = context.getBeansOfType(User.class);
        // System.out.println(map);
    }
}
```

画面 14:
```java
Jedis jedis = context.getBean(Jedis.class);
System.out.println(jedis);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
