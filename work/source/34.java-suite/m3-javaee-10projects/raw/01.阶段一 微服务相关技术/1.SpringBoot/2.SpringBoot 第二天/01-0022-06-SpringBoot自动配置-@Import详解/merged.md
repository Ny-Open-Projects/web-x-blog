# 06-SpringBoot自动配置-@Import详解

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\06-SpringBoot自动配置-@Import详解_【海量资源尽在 ubkz.com】.mp4
- 时长 13分53秒（音频 833s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完Enable注解的一些功能我们发现Enable相关注解它就底层用的就是Import这个注解所以接下来我们就来说一下Import注解它的一些个用法那么Enable底层它使用Import导入一些类使用Enable导入的类会自动的被Spring加载到IOC的容器中我们就可以来获取这些个bin而Import体用了四种不同的导入方式我们接下来挨个的
[00:32] 说一下第一个呢就是导入直接导入BIN比如说刚才我们有个user我们直接可以把这个user导进来然后第二种呢是导入一些配置类就是导入一些configuration的一些个配置类那么它会把这个配置类里边定义的所有的BIN呢都可以注入到IOC的容器里边去然后呢第三个呢是导入一个叫做import selector的实现类这是一个接口将来呢可以导入这个实现类那么这个东西呢待会我们重点来演示
[01:02] 第四个可以导入一个import bin definition register的实现类这两个待会我们来演示前面两个是比较好理解的那么接下来我们就在代码中挨个的演示一下import註解的用法打开idea然后刚才我们在这个other里边我们继续来写这个代码好在这个里边来在这个里边来我们在这儿定义了一个叫做user configure然后这里边还有一个是user ok
[01:30] 那么接下来我们来先来演示import的前边两种的用法好然后呢前面两种用法呢我们把这个呢这几个呢我们都给它放在这个地方放在这个地方之后呢接下来我们在这个地方再写一个注释再写个注释好importimport的四种用法OK那么第一种呢它可以来导入导入导入
[02:04] 导入bin就说一下比如说我们在这个地方把这些都给它注释掉注释掉之后我们直接来import导入user.class导入完user之后我们来获取一下看一下能不能获取到这个bin呢当然不一定能获取到因为它的名字有可能不叫user来看是不是获取不到获取不到呢
[02:31] 这个user class导进来之后呢人家帮你创建这个bin叫不要user呢不一定啊所以呢我们在这个地方把它注释了注释了注释了之后呢我们通过类型来获取context.getbin比如说叫做user.class这样获取这样获取如果可以获取到的话呢就证明它确实导入成功了好sout一下user来运行一下
[03:00] 运行之后我们来看一下效果能不能获取到呢?
[03:03] 你看是不是可以获取到呀?
[03:06] 但是你想知道这个bin的名字的话呢你就可以这样获取比如说你context.get它有个方法叫做bin-of-type通过这个这个它返回的是一个这个bin-of-type返回的是一个map集合然后我们把这个map打印一下其实就可以看到比如说叫做user.class你可以看到
[03:30] 所有user对应的一个这么一个类包括它的键的名称就是spring那个容器里边bin的名称和bin对应的一个值都可以看到可以看一下你可以看一下这个地方呢它的名称是包名对吧点类名这个bin的名称叫这个名所以呢不叫那个短那个user名它的值呢就是这么一个ok所以呢这个地方呢第一种用法呢直接导入bin是ok的没有问题好嘞那么接下来我们来说第二种
[04:01] 第二种我们说了,我们导入一个配置类导入配置类,这个配置类就是配置类我们直接复制过来就可以看出来这个效果有点configure当然导入配置类这一块这个地方注意这个地方配置类里边我们现在是不是只有一个我们可以再搞一个叫做row
[04:28] 搞个row之后呢我们在这个configure page类里边呢我们可以复制这么一份复制一份复制一份之后呢我们这个地方叫row起个名呢也叫rownew了一个row弄完了之后将来这个page类里边其实就有这么两个对象了ok你一导入之后呢这两个是不是user和row是不是都可以被加在到sprint的IOC容器里边去那么接下来我们可以来演示一下好
[04:59] 在这个地方我们导完了之后我们就用这个了上面这个下面这个我们把它注释掉注释掉之后我们再来获取一下context.getB好 这个地方写rodearclassrodearclassrodearclassro需要先导包要不是它联想不出来这个地方因为ro它其实有很多个对应的一个
[05:28] 类都有Roe这个东西所以呢这个地方我们来重新写一下Roe你看是不是有很多所以呢你写的时候注意不要导错包要不是你可能加载不到这个币样加载到Roe之后呢我们把Roe也S-O-U-T打印一下运行一下运行一下之后呢你看我们导了这个配置类之后呢其实呢它可以去导入这么多币样OK而且呢这个地方注意啊
[05:55] 如果你是使用import这种方式来导入的话呢这个配置类上面的这个注解是可以不加的可以不加的话呢它也是可以没有问题的所以呢我们再来运行来看是不是也是没有问题的OK吧那么这两种用法比较简单我们都快速的说完了然后第三种呢就比较麻烦一些了那么它要导入一个类的一个接口的实现类我们先把这个接口看一下叫做import
[06:27] Selector就这么一个接口这个接口里边有这么一个方法叫做Select ImportOK它有个参数这个参数就是一个注解的一个刚他们说了Meta Data是吧OK它可以来获取注解的一些个值先不说那么你看它是返回值返回值是一个字符串的数组那么其实这个方法将来要被实现实现了之后它可以来导入当前这个方法返回值里边
[06:57] 的类名也就是说将来这个返回值呢你要返回一大堆的一个类的全天地名OK它是这么一种用法那么我们就可以来写一下这个注释了我们要导入导入导入这个import selector的实现类OK那么我们在这个地方呢再来写一个写一个呢比如说我们叫做my import selector
[07:27] 然后我们去实现这个importSelector好实现了之后呢复写对应的这个selectImport方法那么return这个地方呢new了一个字符串数组它是零空的我们给它干掉我们给它写这么一个比如说我们导两个一个导一个user导一个ro我们把它复制一下这个权的限定名好给它放这之后给它放这个地方然后呢还有一个还有一个呢是ro
[07:57] 我们也给它导入进来那么这个时候呢它就会去加载user和对应的row了那么下来呢我们来用import把这个select的实现类导进来把这个地方呢给它注释掉注释掉之后呢我们再来写at import那么刚才那个类呢叫做mice import selector.classOK弄完了之后接下来我们就可以来看一下user和row是否都能获取的到
[08:26] 运行一下来看U字和肉你看是不是都可以获取到也是没有问题的而这种方式呢其实呢就比较关键了那你说这跟刚才那个有什么区别呢还挺麻烦的这个地方要注意啊这个地方写的是字符串啊那么将来这个字符串的来源地方可能就不是你写死的了我们可以写到配置文件里边去那么配置文件里边有啥你就可以动态的去把这个类呢给它加载出来哎非常的方便啊
[08:56] 除了这种方式呢还有一种方式就是最后一种最后一种呢也是一样它要导入一个实现类这个实现类呢我们再来可以先看一下叫做import definitionbeam definition register就这么一个接口这个接口呢它也有一个方法这个方法呢叫做register beam definitions这个方法呢将来它在里边有一个参数其实第一个参数是一样的就是
[09:23] 这个注解获取值的这个metadata这个对象后来有一个registrate这个对象这个对象呢就可以向你的IOC容器里边去注入某一些个对象了OK将这个方法一直行就可以注入一些对象我们可以来演示一下把这个类名呢给它复制一份复制一份之后呢我们先把这个注释写上就是导入导入这个的实现类OK然后呢我们在这里边还是一样写个class
[09:54] 叫做my然后实现一下这么一个接口接口实现完了之后呢同样的把这个未实现的方法给它重写一下重写一下之后呢比如说现在我们需要在这个IOC工厂里边去注册一个bin怎么注册呢Registry可以帮我们来完成这个事它叫做Registry Bin Definition好给一个给你要注册的这个bin呢起个名字然后呢给一个bin的definition
[10:24] 起名字,比如说我们就起名为user刚才我们获取的user对象是不是很长一串我们现在bin的名称是个简短的名就叫user然后接下来第二个参数bin definition那么这个玩意就需要通过一个builder来获取了叫做bin definition builder.root bin definition然后叫做user.classuser 倒个包这个玩意倒一下
[10:54] 倒一下点classclass完事了之后呢我们给它弄一个getbin definition好 返回返回了之后呢把这个参数呢就给它放这个位置就可以了OK那么这样就相当于在我们的IOC容器里边去注册了这么一个bin这个bin的名称呢叫user类型呢就是个user.class那么接下来我们就可以在这里边来去导入了把这个注释掉注释掉之后呢at import叫做myimport
[11:26] 这个玩意第二个class写完了之后接下来我们再来看现在我们来获取这两个对吧row是没有导入的所以它会失败而user导入了它是成功的我们可以来运行一下看一看效果来看user是不是没有问题但是呢我们对应的那个地方的row是不是就失败了你可以看一下它说没有这个类型row的一个类型可用
[11:58] 而且userbin的名称我们也可以演示一下名称就是context.getbin名称就是刚才我们起的字幕上的usersot把user弄一下来,再运行刚才user是不是起的bin名称是userok是不是也是ok的,没有问题那么这四种方式我们都介绍了一下介绍了一下之后我们可以来翻一翻对应的
[12:29] 这个Spring application就是我们的Spring boot最核心的这个注解我们点进去看一看效果来看一下它的一个Enable auto-configure它底层依赖是import好点进去看一下你看这个import它导入了一个类导入谁呢导入的是这么一个auto-configuration import selector通过名字我们其实就可以发现它应该是我们的第三种方式
[12:55] 第三种方式就是导入ImportSelector的实现类对象可以点进去看一下是不是这个类实现了这么一个Selector再点进去之后你看这个Selector又继承了ImportSelector最终就是用了我们的第三种ImportSelector的方式来完成这些启动的时候的类的自动的加载那么至于这个里边的一些个代码
[13:25] 比如说我们刚才看到的我们这个里边的稍等我们点进去看至于说接下来我们就来说一下这个importSelector里边到底完成了一些什么事情那么我们就要来分析一下它的一个底层的实现原理了那么这一小节import我们讲了这么四种的用法我们就先说到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Boot 中 @Import 注解的四种使用方式，包括导入 Bean、配置类、ImportSelector 实现类和 ImportBeanDefinitionRegistrar 实现类。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 IntelliJ IDEA 项目结构，项目名为 Spring Boot-enable，包含 src/main/java 和 src/main/resources 目录，以及 pom.xml 文件。
画面 2: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 @Import(User.class) 注解导入 User 类。
画面 3: 显示运行结果，控制台输出了获取到的 User 对象信息。
画面 4: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(User.class) 获取 User 对象。
画面 5: 显示 UserConfig.java 文件内容，其中定义了 @Configuration 注解的类，并使用 @Bean 注解定义了 User 和 Role 两个 Bean。
画面 6: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(Role.class) 获取 Role 对象。
画面 7: 显示在 IDEA 中搜索 @Import 注解相关的类，结果中包含 ImportBeanDefinitionRegistrar、AutoConfigurationImportSelector 等类。
画面 8: 显示项目结构，其中包含 MyImportSelector.java 文件。
画面 9: 显示 ImportBeanDefinitionRegistrar.java 文件内容，其中定义了 registerBeanDefinitions 方法。
画面 10: 显示 MyImportBeanDefinitionRegistrar.java 文件内容，其中实现了 registerBeanDefinitions 方法，用于注册 User Bean。
画面 11: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 @Import(MyImportBeanDefinitionRegistrar.class) 注解导入自定义的 Bean 定义注册器。
画面 12: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(name: "user") 获取 Bean，但控制台提示找不到类型为 com.ithema.domain.Role 的 Bean。
画面 13: 显示 ImportSelector.java 文件内容，其中定义了 selectImports 方法。
画面 14: 显示 PowerPoint 幻灯片，标题为“Spring Boot 配置”，内容为“@Import 应层依赖于 @Import 注解导入一些类，使用 @Import 导入的类会被 Spring 加载到 IOC 容器中。而 @Import 提供 4 中用法：① 导入 Bean ② 导入配置类 ③ 导入 ImportSelector 实现类。一般用于加载配置文件中的类 ④ 导入 ImportBeanDefinitionRegistrar 实现类。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 2:
```java
@Import(User.class)
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 4:
```java
Map<String, User> map = context.getBeansOfType(User.class);
System.out.println(map);
```

画面 5:
```java
package com.ithema.config;

import com.ithema.domain.Role;
import com.ithema.domain.User;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class UserConfig {
    @Bean
    public User user() {
        return new User();
    }
    @Bean
    public Role role() {
        return new Role();
    }
}
```

画面 6:
```java
Role role = context.getBean(Role.class);
System.out.println(role);
```

画面 7:
```java
@Import(User.class)
@ComponentScan("com.ithema.config")
@EnableAutoConfiguration
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 10:
```java
package com.ithema.config;

import org.springframework.beans.factory.support.BeanDefinitionBuilder;
import org.springframework.context.annotation.ImportBeanDefinitionRegistrar;
import org.springframework.core.type.AnnotationMetadata;

public class MyImportBeanDefinitionRegistrar implements ImportBeanDefinitionRegistrar {
    @Override
    public void registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry) {
        registry.registerBeanDefinition("user", BeanDefinitionBuilder.rootBeanDefinition().getBeanDefinition());
    }
}
```

画面 11:
```java
@Import(User.class)
@Import(UserConfig.class)
@Import(MyImportBeanDefinitionRegistrar.class)
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 12:
```java
Object user = context.getBean(name: "user");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: PPT 标题为“Spring Boot 配置”，内容为“@Import 应层依赖于 @Import 注解导入一些类，使用 @Import 导入的类会被 Spring 加载到 IOC 容器中。而 @Import 提供 4 中用法：① 导入 Bean ② 导入配置类 ③ 导入 ImportSelector 实现类。一般用于加载配置文件中的类 ④ 导入 ImportBeanDefinitionRegistrar 实现类。”

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

