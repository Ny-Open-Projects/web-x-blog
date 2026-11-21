# 04-SpringBoot自动配置-切换内置web服务器

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\04-SpringBoot自动配置-切换内置web服务器_【海量资源尽在 ubkz.com】.mp4
- 时长 7分1秒（音频 422s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完condition这个条件功能之后接下来我们来介绍一下Spring Boot如何来切换内置的Web服务器其实呢Spring Boot它的Web环境它默认使用Tomcat作为内置服务器之前我们也看到了我们每一次启动Spring Boot的Web项目呢就是Tomcat Server Started是吧然后呢其实呢Spring Boot它提供了四种不同的内置服务器供我们选择我们可以很方便的来对它进行切换
[00:30] 接下来我们先来演示一下Web服务器Tomcat作为内置的服务器它启动了一个情况好嘞打开我们的工程还是这个condition的工程我们只需要在这个POM文件里面引入对应的Web对应的ELite就可以了好首先呢这样我们先把这个Web ELite给它放在这个地方放这个地方呢我们把它注释了注释了注释了之后呢我们来启动一下我们的工程
[01:00] 来看一下Tomcat的服务器会不会被骑起来呢其实刚才我们看到的其实并没有骑起来你看是不是没有Tomcat的日志被打印并且一启动这个项目就完事了因为web容器它才会一直让这个程序一直停在这个地方供我们访问对吧那么现在我们把web环境给它打开打开之后我们再来启动再来启动这个工程你会发现Tomcat就被骑起来了
[01:30] 还是缓存,我们在这个地方刷一下刷一下之后呢我们click清掉,清掉之后我们再来启动好,启动了之后呢,你注意看Tomcat started on ports,是不是就启动起来了那么这就证明了我们Spring Boot内置使用的是Tomcat作为服务器那么这个地方呢,我们首先来看一下在哪个地方去查看Spring Boot提供的内置服务器的种类我们打开这个额外的libraries
[02:06] 打开文化文化之后呢我们还是找到那个Spring Boot的Auto Configure那么一个jar 包找一下来看一下在这个地方Spring Boot Auto Configure跟刚才那个一样点开点开之后呢刚才我们看的是不是condition对吧那么接下来我们来看有一个叫做web在这个地方这个地方呢里边有一个包叫做embedded这个单词呢翻译过来就是嵌入式的内置的好那么这个嵌入式的里边呢
[02:40] 下面这四个就是对应的web服务器的工厂第一个是JTAG,JTAG Web Server Factory第二个是NATED,NATED是一个比较新的高版本才有的NATED Web Server FactoryTOMCAT,这是我们默认的还有一个是UNDERTOW我们今天并不来讲解这四种服务器我们只是来说怎么切换它们那么怎么切换呢我们找到最上面的一个它们的一个自动配置的配置类
[03:10] 找到这个配置类把它最大化最大化之后呢我们放到上面看配置类没问题然后呢第一个就是condition on web application通过名字我就能猜到它是干啥的干啥的呢是不是当是web环境的时候才会去加载这所有的bin对吧OK那当然我们刚才也演示过了那么第二个我们再下来看你看每一个是不是这Tomcat的初始化对应的Tomcat的
[03:39] 然后呢JT的工厂Undertow的工厂和Nated的工厂那么它们有条件条件就是第一个如果是Tomcat的工厂要被初始化的话呢必须condition on class在你的环境里边得有Tomcat的class和并且和这个的class那么这两个class只有当导入了Tomcat对应的坐标才会有的那么同理你要去初始化JT的
[04:08] 或者说你要去选择使用JT来作为你的web服务器那你必须存在这么一些class那些class呢只有在导入了对应的JT的坐标之后才会有的OK那么同理啊Undertow和Nated都是一模一样的那么也就是说我们只需要去导入不同的web服务器的坐标那么就可以来实现这种服务器的动态切换了非常的简单那么我们来看一下
[04:38] 在我们的Starter-Web里边它其实内部的就依赖了对应的Tomcat的坐标那么当然我们可以来分析一下这个依赖坐标好分析一下分析一下之后呢我们把它点大一点放大一点按Ctrl弄滚轮点大一点哎它有点模糊好差不多能看清了这个地方是我们的Starter-Web然后呢来看这个Starter-Web它依赖了这么多那么我们往上看拖一下
[05:07] 拖一下之后呢我们看一下Tomcat在哪个地方大一点好再拖一拖看一看在我们的Stutter Gun外部你看这个地方Tomcat在这你看这个箭头是不是指过来了这条线对吧指过来了那么这就是我们的Spring Boot的Stutter Gun TomcatOK吧那么现在我不期望用Tomcat了我想用JTA怎么办呢首先第一件事你把Tomcat排除掉
[05:35] 因为StutterGang web是必须存在的它又内置了或者内部依赖Tomcat我先把它排除掉怎么排呢右键然后把它排掉就可以了好排掉之后你现在看是不是不见了不见了之后我们来看在我们的配置文件POM文件里边是不是有一些改动这里边加了一个排除的这么一个选项排了谁呢排了Tomcat那么排完Tomcat之后接下来我只需要把我们的JTAG引进来就行了
[06:02] JT引的时候这个名非常简单也不用去背引过来之后这个地方改一下就行了叫做JT-JETTY好嘞这样就写完了那么我们加个注释这个地方第一件事是排除Tomcat的依赖这件事在干啥呢在引入JT的依赖引完了之后我们什么都不用干了我们直接来重启一下
[06:33] 重启一下你可以看到当前不再是Tomcat的而是JTA的服务器被启动了可以看你看JTA started on Pulse 8080弄完了吧你会发现Spring Boot来做切换非常简单它内部的原理依赖的原理其实还是我们刚才说的condition条件那个功能好嘞那么这一块我们就简单的介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 12: 显示 pom.xml 文件，其中在 spring-boot-starter-web 依赖中添加了 <exclusions> 标签，排除 spring-boot-starter-Tomcat。
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
            <artifactId>spring-boot-starter-Tomcat</artifactId>
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

