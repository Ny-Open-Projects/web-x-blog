# 画面线理解：03-SpringBoot自动配置-Condition-2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\03-SpringBoot自动配置-Condition-2_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 02:07, 03:46, 04:21, 05:23, 07:17, 08:54, 09:49, 10:41, 11:42, 13:10, 14:09, 15:18, 16:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:49:16

1) 这一组画面整体在讲 Spring Boot 自动配置中的条件化 Bean 创建机制，通过 @ConditionalOnClass 等注解实现根据类存在与否动态创建 Bean。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 项目结构显示 `src/main/java/com.ithema.springbootcondition/config/UserConfig.java`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition.config;
  import com.ithema.springbootcondition.condition.ClassCondition;
  import com.ithema.springbootcondition.condition.domain.User;
  import org.springframework.context.annotation.Conditional;
  import org.springframework.context.annotation.Configuration;
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      public User user() {
          return new User();
      }
  }
  ```

画面 2:
- 项目结构中选中 `UserConfig`。
- 代码内容：
  ```java
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("redis.clients.jedis.Jedis")
      public User user() {
          return new User();
      }
  }
  ```

画面 3:
- 项目结构中选中 `SpringbootConditionApplication`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition;
  import ...
  @SpringBootApplication
  public class SpringbootConditionApplication {
      public static void main(String[] args) {
          // 可以看到注释掉的代码
          // @Bean redisTemplate
          // Object redisTemplate = context.getBean("redisTemplate");
          // System.out.println(redisTemplate);
          ConfigurableApplicationContext context = SpringApplication.run(SpringbootConditionApplication.class, args);
          Object user = context.getBean("user");
          System.out.println(user);
      }
  }
  ```

画面 4:
- 项目结构中选中 `SpringbootConditionApplication`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition;
  import ...
  @SpringBootApplication
  public class SpringbootConditionApplication {
      public static void main(String[] args) {
          ConfigurableApplicationContext context = SpringApplication.run(SpringbootConditionApplication.class, args);
          Object user = context.getBean("user");
          System.out.println(user);
      }
  }
  ```

画面 5:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName("redis.clients.jedis.Jedis");
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 6:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName("redis.clients.jedis.Jedis");
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 7:
- 项目结构中选中 `ClassCondition.java`。
- 代码内容：
  ```java
  public class ClassCondition implements Condition {
      public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
          // 获取注解属性值
          Map<String, Object> map = metadata.getAnnotationAttributes(ConditionalOnClass.class.getName());
          String value = map.get("value");
          // 检查类是否存在
          boolean flag = true;
          try {
              Class<?> cls = Class.forName(value);
          } catch (ClassNotFoundException e) {
              flag = false;
          }
          return flag;
      }
  }
  ```

画面 8:
- 项目结构中选中 `UserConfig.java`。
- 代码内容：
  ```java
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("redis.clients.jedis.Jedis")
      public User user() {
          return new User();
      }
  }
  ```

画面 9:
- 项目结构中选中 `pom.xml`。
- 代码内容：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
  </dependency>
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-redis</artifactId>
      </dependency>
  </dependencies>
  ```

画面 10:
- 项目结构中选中 `pom.xml`。
- 代码内容：
  ```xml
  <dependencies>
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-data-redis</artifactId>
          <version>2.1.8.RELEASE</version>
      </dependency>
  </dependencies>
  ```

画面 11:
- 项目结构中选中 `ConditionalOnClass.java`。
- 代码内容：
  ```java
  @Target({ElementType.TYPE, ElementType.METHOD})
  @Retention(RetentionPolicy.RUNTIME)
  @Documented
  @Conditional(OnClassCondition.class)
  public @interface ConditionalOnClass {
      Class<?>[] value() default {};
  }
  ```

画面 12:
- 项目结构中选中 `RedisAutoConfiguration.java`。
- 代码内容：
  ```java
  @Configuration
  @ConditionalOnClass(RedisOperations.class)
  @ConditionalOnBean(RedisConnectionFactory.class)
  @Import({LettuceConnectionConfiguration.class, JedisAutoConfiguration.class})
  public class RedisAutoConfiguration {
      @Bean
      @ConditionalOnMissingBean
      public RedisTemplate string(RedisConnectionFactory redisConnectionFactory) throws UnknownHostException {
          StringRedisTemplate template = new StringRedisTemplate();
          template.setConnectionFactory(redisConnectionFactory);
          return template;
      }
  }
  ```

画面 13:
- 项目结构中选中 `UserConfig.java`。
- 代码内容：
  ```java
  package com.ithema.springbootcondition.config;
  import com.ithema.springbootcondition.condition.ClassCondition;
  import com.ithema.springbootcondition.condition.domain.User;
  import org.springframework.context.annotation.Conditional;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.Bean;
  import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
  @Configuration
  public class UserConfig {
      @Bean
      @Conditional(ClassCondition.class)
      @ConditionalOnClass("com.alibaba.fastjson.JSON")
      public User user() {
          return new User();
      }
      @Bean
      public User user2() {
          return new User();
      }
  }
  ```

画面 14:
- PPT 标题：SpringBoot 自动配置。
- PPT 内容：
  - Condition
  - Condition 是在 Spring 4.0 增加的条件判断功能，通过这个功能可以实现选择性的创建 Bean 操作。
  - 思考
  - SpringBoot 是如何知道要创建哪个 Bean 的？比如 SpringBoot 是如何知道要创建 RedisTemplate 的？
