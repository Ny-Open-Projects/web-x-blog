# 07-SpringBoot自动配置-@EnableAutoConfiguration详解

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\07-SpringBoot自动配置-@EnableAutoConfiguration详解_【海量资源尽在 ubkz.com】.mp4
- 时长 6分55秒（音频 416s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完import这个注解的四种用法之后接下来我们就重点来讲一下Spring Boot自动配置的核心注解Enable Auto Configuration这么一个注解打开idea我们来圆码里边看一把好我们点到这个Spring Boot Application这么一个引导类上的注解点进去之后呢我们最大化来看这上面就有一个Enable Auto Configuration点进去之后呢我们可以看到它使用了一个import
[00:30] 导入了这么一个自动配置的selector点进去点进去之后呢我们可以知道这个selector里边有个方法叫import selector我们直接看到selector import就这个方法而这个方法它返回一个字符串的竖组在这个竖组里边定义了很多的需要被加载的类对吧OK那么我们看一下这个代码里边比较核心的你到底加载了哪些类我想知道
[00:58] 那么当然这个地方就是做了一个判断这个也没有什么意义那么我们往下看在这个地方呢加载其实是在这个地方这行代码就是get auto config entity加载加载完事之后呢它返回了这么一个entity的对象这个entity对象呢将来通过string有tools的to string array把它的一个configurations转换成一个字符树组返回了其实核心的代码呢就这个里边
[01:26] 那么点进去跟源码跟进去之后呢我们再来看在这里边呢这有很多很多的代码我们只说关键的代码关键代码在哪呢我们可以看这个地方看好这个地方叫做这个方法呢将来返回一个list集合这个集合就是configurations然后呢这个configurations它排除了一些你需要排除的东西然后呢最后呢给你创建了一个autoconfigurationentity
[01:55] 就是刚才我们看到的 entity 对象给你创建出来把集合放进去对吧OK那么其实最核心的就是这么一个代码这个代码我们把它原码跟进去跟进去之后它通过了这个地方的代码我们要看一下这个地方它通过sprint factories loader来去加载加载之后返回了一个configuration一个list集合OKlist集合里边其实就是所有需要加载的类
[02:24] 从哪加载的呢这个地方注意下边很有意思他说如果不存在他会报一个错一个断言assert断言not empty如果你当前这个玩意儿是个空的就是这个集合是个空的没有获取到那么他给你报了个异常异常的提示呢就是不能自动配置一些classes放的就是没有发现一个自动配置的classes
[02:49] 在哪呢在metainfo这个目录下的有一个叫做spring.factories这么一个文件下边这个文件非常的关键啊非常的关键如果你没有定义这个文件或者这个文件定义的有问题那么他就会说这个集合加载不到加载不到他就断言失败断言失败的话呢他就会报一个异常
[03:12] 那么接下来我们就来看一下这个文件里边到底定义了哪些个需要被自动加载的类好这个文件metainfo.sprint.factories点一下点进来之后呢我们在外部的这些文件里边可以看一下其实呢所有叫做autoconfigure的这个包都有来看一下我们看autoconfigure点进去点进去来看叫metainfo对吧
[03:42] 它里边有一个Sprinter Factories有吧有了之后呢来看这一大堆一系列的东西前边的这些呢我们先不管先不管到这个地方这个名字叫做Enable Auto ConfigurationOK这下边配置的所有的这些个Configuration都是要被加载的你可以看我的天很多很多一大堆一大堆这么多对吧这么多
[04:09] 那么这些configuration其实将来都是会被加载的对吧ok那么我们随便找一些configuration我们可以看一下找一个我们相对来说比较熟悉的看过的你看redis的auto configuration好ctrl c把它看一下看一下之后呢你注意那么多个configuration每一个configuration里边又定义了很多的bin那么在supreme boot
[04:37] 启动的时候都会去加载吗当然不是的因为呢大家都有一些condition的条件注解那么只有满足这些条件才会去初始化这些病的他很智能的对吧OK那你看一下condition on class对吧这个我们看过的其实呢很多随便找都是一样的比如说我们随便找一个学没学过没有关系我们随便找都是这个意思可以看一下
[05:06] condition on class当它存在的时候这个哥们很有意思它什么都没干但是呢它又导入了一个其他的配置类看导入一个其他配置类这个配置类里边是不是定义了很多的bin而且呢它也是一样加了一些条件所以总的来说我们对于sprint boot它的一个自动的配置的一个流程我们大概就清晰了第一个事呢就是通过enable auto-configure注解它使用import这个注解
[05:36] 然后导入了这么一个自动配置的这么一个类就是Auto Configure Import Selector这么一个类来加载一些配置类加载了配置类之后呢这个地方这个类里边它要去在MetaInfo这个配置文件就是MetaInfo下的Spring.Factories这个配置文件里边这个配置文件里边呢定义了一系列的配置类而Spring Boot启动的时候会自动加载这些配置类来初始化对应的币
[06:06] 而这些bin都会初始化吗?
[06:08] 不一定不是所有的bin都会被初始化的只有满足condition条件的bin才会被初始化那要不是Spring Boot启动的时候加在那么多bin多慢所以我们基本上就能了解Enable Auto-configural这个注解或者说Spring Boot的自动配置的核心原理了它其实底层用了很多的知识总的来说就这么三部分内容
[06:35] 第一部分就是condition第二部分就是import導入了import選擇的自動配置類第三部分整合了enable註解對於Spring Boot自動配置的原理我們就講完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 14: 展示了 PowerPoint 幻灯片，标题为“Spring Boot 自动配置”，副标题为“@EnableAutoConfiguration 注解”。

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
- PPT 标题: Spring Boot 自动配置
- 副标题: @EnableAutoConfiguration 注解

5) 无。

