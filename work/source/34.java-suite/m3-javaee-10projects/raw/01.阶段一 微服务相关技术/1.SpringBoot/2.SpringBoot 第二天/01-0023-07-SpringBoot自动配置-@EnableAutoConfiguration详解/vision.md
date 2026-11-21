# 画面线理解：07-SpringBoot自动配置-@EnableAutoConfiguration详解

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\07-SpringBoot自动配置-@EnableAutoConfiguration详解_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:29, 01:27, 02:02, 03:09, 03:29, 03:43, 03:54, 04:06, 04:12, 04:35, 04:54, 05:13, 05:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:58:50

1) 这一组画面整体在讲 Spring Boot 自动配置机制，重点分析 @EnableAutoConfiguration 注解的源码实现及其如何加载和筛选自动配置类。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Spring Boot 项目结构，包含 src/main/java 和 src/main/resources 目录，以及运行成功的控制台日志。
画面 2: 查看 Spring Boot 源码中 EnableAutoConfiguration.java 文件，展示了 @EnableAutoConfiguration 注解的定义，其中包含常量 ENABED_OVERRIDE_PROPERTY = "spring.boot.enableautoconfiguration"。
画面 3: 查看 AutoConfigurationImportSelector.java 文件，展示了 getAutoConfigurationEntry 方法的实现，其中包含对配置类的筛选和过滤逻辑。
画面 4: 继续查看 AutoConfigurationImportSelector.java 文件，展示了 isAutoConfigurationEnabled 方法，用于判断是否启用自动配置。
画面 5: 查看 getAutoConfigurationEntry 方法中 getCandidateConfigurations 方法的实现，展示了如何加载候选配置类。
画面 6: 查看项目依赖，确认 Spring Boot 的自动配置相关依赖已引入。
画面 7: 查看 META-INF/spring.factories 文件，确认其中包含了自动配置类的定义。
画面 8: 展示了 spring.factories 文件中列出的自动配置类，包括 ApplicationListener、AutoConfigurationImportListener、ConditionEvaluationReportConfigurationImportListener 等。
画面 9: 展示了 spring.factories 文件中列出的更多自动配置类，包括 SpringApplication、SpringBootAutoConfiguration、EmbeddedAutoConfiguration 等。
画面 10: 展示了 spring.factories 文件中列出的更多自动配置类，包括 Mongo、Quartz、Security 等。
画面 11: 查看 RedisAutoConfiguration.java 文件，展示了 @Configuration 注解和 @ConditionalOnClass 注解的使用。
画面 12: 继续查看 RedisAutoConfiguration.java 文件，展示了 @ConditionalOnBean 注解的使用。
画面 13: 查看 HazelcastAutoConfiguration.java 文件，展示了 @Configuration 注解和 @ConditionalOnClass 注解的使用。
画面 14: 展示了 PowerPoint 幻灯片，标题为“SpringBoot 自动配置”，副标题为“@EnableAutoConfiguration 注解”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```java
String ENABLED_OVERRIDE_PROPERTY = "spring.boot.enableautoconfiguration";
```

画面 3:
```java
protected AutoConfigurationEntry getAutoConfigurationEntry(AutoConfigurationMetadata autoConfigurationMetadata,
        AnnotationMetadata annotationMetadata) {
    if (isEnabled(annotationMetadata)) {
        return EMPTY_ENTRY;
    }
    AnnotationAttributes attributes = getAttributes(annotationMetadata);
    List<String> configurations = getCandidateConfigurations(annotationMetadata, attributes);
    configurations = removeDuplicates(configurations);
    Set<String> exclusions = getExclusions(annotationMetadata, attributes);
    configurations = remove(configurations, exclusions);
    configurations = filter(configurations, autoConfigurationMetadata);
    return new AutoConfigurationEntry(configurations, exclusions);
}
```

画面 4:
```java
protected boolean isAutoConfigurationEnabled(AnnotationMetadata metadata) {
    if (getClass() == AutoConfigurationImportSelector.class) {
        return getEnvironment().getProperty(EnableAutoConfiguration.ENABLED_OVERRIDE_PROPERTY, Boolean.class, defaultValue: true);
    }
    return true;
}
```

画面 5:
```java
protected List<String> getCandidateConfigurations(AnnotationMetadata metadata, AnnotationAttributes attributes) {
    List<String> configurations = SpringFactoriesLoader.loadFactoryNames(getSpringFactoriesLoaderFactoryClass(), getBeanClassLoader());
    Assert.notEmpty(configurations, "No auto configuration classes found in META-INF/spring.factories. If you are using a custom packaging, make sure that file is correct.");
    return configurations;
}
```

画面 7:
```
META-INF
├── spring.factories
├── spring-autoconfigure-metadata.properties
└── spring-configuration-metadata.json
```

画面 8:
```
org.springframework.context.ApplicationListener=
org.springframework.boot.autoconfigure.backgroundpreinitializer=
org.springframework.boot.autoconfigure.AutoConfigurationImportListener=
org.springframework.boot.autoconfigure.condition.OnBeanCondition=
org.springframework.boot.autoconfigure.condition.OnCondition=
```

画面 9:
```
org.springframework.boot.autoconfigure.SpringApplicationAdminAutoConfiguration=
org.springframework.boot.autoconfigure.SpringBootAutoConfiguration=
org.springframework.boot.autoconfigure.amqp.AmqpAutoConfiguration=
org.springframework.boot.autoconfigure.batch.BatchAutoConfiguration=
org.springframework.boot.autoconfigure.cassandra.CassandraAutoConfiguration=
```

画面 10:
```
org.springframework.boot.autoconfigure.quartz.QuartzAutoConfiguration=
org.springframework.boot.autoconfigure.reactor.core.ReactorAutoConfiguration=
org.springframework.boot.autoconfigure.security.SecurityAutoConfiguration=
org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration=
org.springframework.boot.autoconfigure.security.servlet.SecurityFilterAutoConfiguration=
```

画面 11:
```java
@Configuration
@ConditionalOnClass(RedisOperations.class)
@EnableConfigurationProperties(RedisProperties.class)
@Import({ LettuceConnectionConfiguration.class, redisConnectionConfiguration.class })
public class RedisAutoConfiguration {
```

画面 12:
```java
@Bean
@ConditionalOnBean(name = "redisTemplate")
public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory) throws UnknownHostException {
    RedisTemplate<Object, Object> template = new RedisTemplate<>();
    template.setConnectionFactory(redisConnectionFactory);
    return template;
}
```

画面 13:
```java
@Configuration
@ConditionalOnClass(HazelcastClient.class)
@ConditionalOnMissingBean(HazelcastInstance.class)
@ConditionalOnAvailableCondition
static class HazelcastClientConfiguration {
    @Bean
    public HazelcastInstance hazelcastInstance(HazelcastProperties properties) throws IOException {
        Resource config = properties.resolveConfiguration();
        if (config != null) {
            return new HazelcastClientFactory(config).getHazelcastInstance();
        }
        return null;
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 14:
- PPT 标题: SpringBoot 自动配置
- 副标题: @EnableAutoConfiguration 注解

5) 无。
