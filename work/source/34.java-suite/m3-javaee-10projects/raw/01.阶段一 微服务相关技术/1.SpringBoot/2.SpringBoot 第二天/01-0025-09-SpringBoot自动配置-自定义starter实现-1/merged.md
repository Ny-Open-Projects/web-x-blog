# 09-SpringBoot自动配置-自定义starter实现-1

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\09-SpringBoot自动配置-自定义starter实现-1_【海量资源尽在 ubkz.com】.mp4
- 时长 11分38秒（音频 698s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完Spring Boot自定义Redis的Starter这个思路分析和实现的步骤那么接下来我们就来去在代码里边去演示一下打开IDEA首先呢我们先来创建这么两个工程第一个工程刚才我们说过第一个我们创建一个Starter对吧然后呢我们还可以创建一个Auto Configure让Starter呢去依赖于Auto Configure先创建哪个都可以我们先来创建这个
[00:31] it黑码刚才我们说的先创建这个autoconfigure对吧起名叫做redis-sprint-boot-auto-configure这个名呢这个包名比较长看着不舒服我们给它删一部分改一下叫做configure好短一点然后呢一路下一步就OK了
[00:59] 这个模块创建完事之后它将来是来写这些核心的自动配置类的那么接下来再来创建一个模块这个模块我们就叫Starter来做依赖的整合将来我们就引入这个就可以了com.it 黑码然后叫做redis-spring-boot-starter好这个名也很长我们把它删一部分
[01:28] 好下一步下一步就叫这个名没问题这两个模块都创建完事之后我们首先先把这两个模块给它清理一下把这些没用的都干掉这个也删掉mvn这个也删掉删掉之后呢我们在porm文件里边把它收一下声这个starter呢其实呢它肯定是不需要测试相关的东西的对吧将来呢不需要测然后呢这里边弄完了starter那么这个starter呢
[01:59] 是需要的,Spring Boot-StarterSpring Boot的核心的起步的依赖然后这个Build是不需要的把它干掉就留这个一个核心的就可以了然后在这里边要注意我们要引入啊引入我们的ConfigureRAW这有RE啊我们自定义的这个ConfigureRAW要引进来引进来之后Dependency稍等,按快了Dependency然后呢这个叫做Redis的Auto Configure
[02:32] -Spring Boot提示一下有了之后接下来我们这个项目就弄完了那么接下来来看AutoConfigure一样给它删掉把下面这些都给它删掉然后这个PoM文件里边也给它收一下身这个删掉然后Build这个插件也删掉在这里边我们将来要去创建Jadis的bin所以我们在这里边把Jadis导进来导进来之后我们写一个叫做
[03:03] 叫做引入Jadis的依赖OK代码坐标都弄完了那么接下来我们就可以来在autoconfigure里边去写对应的代码了那么这个代码呢首先呢我们先把这个启动类我们给它删掉然后呢测试类里边呢这些类呢都要删掉因为我们把测试的坐标删掉了之后呢测试类如果不删的话就会报错的好干掉来看
[03:35] 你看现在其实呢加载不了这些注解啊所以报错了我们把它删掉就行了删掉都删干净了之后呢我们在这个auto-configure里边来写一个核心的redis的自动配置类啊AOTOconfigureconfigure这有configuration它是个配置类那么我们来加个注解configurationok弄完了之后只需要让它里边去提供我们写一个注释
[04:07] 提供这个Jadis的bin就可以了提供Jadis的bin非常简单public返回这个JadisJadis就可以了起名也叫Jadis吧return一个new一个Jadis里边有很多的构造其实这个Jadis的方法有很多构造我们用空餐的还是用有餐的一般情况下我们都用
[04:40] 有参的并且是两个参数那个两个参数这个呢一个是host一个是pod一个是主机名一个是端口号OK那么这个主机和端口到底咋传呢我们可以这样写localhost对吧然后呢写6379这样写没问题吧那么这样写呢就相当于你创建的出来的这个Jadis客户多呢将来只能操作本机的6379的这个Radis吧
[05:09] 那这是什么玩意儿对吧那将来你这个自动配置的Jadis的客户端是不是应该由用户去指定他想操作哪个IP下的Jadis都可以啊你不能写死了吧这应该当过参数传进来的而这个参数呢应该从用户定义的项目的配置文件中获取吧那么怎么获取呢我们需要让我们的一个实体类和配置文件想绑定这个之前我们是说过的
[05:38] 在这个地方我们定义一个redis的properties好 定义完了之后为了让它跟配置文件相绑定我们就定义一个configuration properties就可以了并且只定义这么一个前卷profix好 等于redis将来以redis开头的这些个配置都会和我们当前这个实体类里边的属性对应起来那么属性我们定义两个private string类型的
[06:08] host private int port主机名端口号这个地方和红条我们之前说过它是一个提示的处理器我们没有加当然也不需要去加好那么这样就写完了写完了之后我们给它提供一个setter和getter方法就写完了写完了之后将来我们可以让这两个值用户如果不配置我们默认为本机可不可以
[06:38] 没有配置默认为本机的话我们就让它给个默认值不就行了吗对吧我们就给它这样localhost然后这个值呢我们默认为6379好嘞这个properties写完了写完了之后还有一个小的问题就是说这个properties现在它并不能被标识为Spring Boot的一个bin也就是说将来Spring的IOC容器呢可能加载不了它因为我们上面没有加complet的注记
[07:08] 即使你加了这个注解呢其实呢将来Spring那个项目也不一定能怎么的到因为它的包呢不太一样那么为了让这个Configuration Properties被启用所以呢我们可以在这个地方在这个地方在我们的核心的配置这个位置来启用一下启用呢用Enable它定义好的一个Configuration Properties这么一个注解把刚才我们定义的这个Redis的Properties给它加进来就行了好
[07:38] properties第二class相当于这样呢就让这个properties被sprint所识别了就这么一个注解啊要注意加完了之后将来程序一起动这个bin就被放到了我们的sprint的IOC的容器里面那么在创建这个bin的过程中我们是不是可以把它注入进来好创建这个bin的过程中我们就可以把它通过参数的方式给它注入进来了注入进来之后我们就可以
[08:06] 动态的来指定host.gethost然后端口也同样通过redisproperty.getport来动态指定这样这个bin就写好了那么写好了之后这个代码是没有什么问题了那么下来我们就可以来完成一个配置配置我们参照一下不要写错这个地方如果你实在是不知道或者说记不知道怎么写
[08:33] 有两个办法第一个办法我们去看这个源码第二个我们去参照买Battist对吧都可以那么我们一般情况下呢就看源码怎么弄了我们随便找一个源码打开打开看这个地方的这么一个我们把这个类呢这个注解给它写到这OK然后呢我们点这个引导类的核心这个注解点进去点进去之后呢Enable auto configuration点进去然后呢
[09:02] 加载的这个auto configuration import selector点进去再来看再来看里边获取的这么一个entry点进去对吧之前我们点过点过了之后呢我们再来看一下这里边所有的配置选项然后呢这个方法这个方法呢其实它有一个提示这个提示呢就是meta info下的sprint.factories这个文件那么现在呢我们需要的就是创建这么一个文件好把这个文件呢放
[09:32] 创建出来,new一个file,粘过来,不要写错,千万不要写错一个字,粘过来,粘过来之后呢,OK,放这个地方,那这个文件是不是就有了,有了之后呢,接下来键你肯定不会写吧,键不会写呢,没关系啊,我们还是点在这个地方来,它这个键呢,其实就是这个名啊,就是这个名,enable auto configuration,就这个名,然后这个注解呢,我们点进来之后呢,复制它的全名称,copy reference,点进来,好,放到这个地方,
[10:02] 等于谁呢?
[10:03] 等于你自己写的这个类复制一下全名称然后放到这个地方你如果觉得这个太长了你可以给它换一行换一行都是可以的没有问题这个表示换行误问完了之后接下来我们就可以来演示了获取Jadis了好,Starter呢我们也依赖了Count To Configuration没问题吧那么我们自己的这个里边MyBitness这个岂不依赖注释掉
[10:32] 如果你不出示会出问题的因为它会找数据库的资源没有数据库的配置它就会报错了那么我们来依赖对应的我们自己定义的Redis的StarterOK这个要注意是我们自定义的Redis的Starter有了这个之后我们下来就可以来写代码演示了我们在这里边通过context.get并我们通过去这个Redis
[11:03] Jadis.class好Jadis有了之后我们先来打印一下看一下能不能获取到来启动一下这么一个程序启动一下来我们看一下这个Jadis这个B是不是就获取到了没有问题没有问题了之后这个代码基本上的流程是不是就是通着呢那么接下来我们来对这个整体来做一个小小的优化

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Spring Boot 的自动配置机制，自定义一个 Redis 客户端的配置并使其在应用启动时自动生效。

2) 按时间顺序列出每张画面的要点：
画面 1: 打开 IntelliJ IDEA，显示项目结构，包含 Spring Boot-condition、Spring Boot-enable-other 等模块。
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

