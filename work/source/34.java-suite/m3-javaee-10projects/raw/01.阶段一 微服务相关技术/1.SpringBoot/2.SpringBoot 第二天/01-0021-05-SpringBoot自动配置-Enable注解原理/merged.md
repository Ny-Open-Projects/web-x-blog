# 05-SpringBoot自动配置-Enable注解原理

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\05-SpringBoot自动配置-Enable注解原理_【海量资源尽在 ubkz.com】.mp4
- 时长 13分27秒（音频 808s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们接着来说Spring Boot自动配置里边的另外一个支持点Enable开头的这几个注解其实在Spring Boot里边自动配置这个功能完全就是依赖于一个注解叫做Enable Auto Configuration我们可以来简单的看一下在我们的Spring Boot的引导类上边然后呢这个地方加了一个注解叫做Spring Boot Application我们可以点进去看一下看一下之后呢这个注解上面一大堆注解
[00:31] 那么它是组合的一个注解功能上面这些原注解我们就不再看了这个地方有一个叫做Spring Boot Configuration点进去看一下它其实就是Configuration那么也就意味着你当前的类上如果加了这么一个Spring Boot Application那么你这个类是不是加了一个注解那你这个类就是一个配置类在这里边直接可以定义bin的好这个我们说一下然后接着看
[00:59] 这个里边这个注解很重要了叫做Enable Auto Configuration那么这个注解就是核心的这么一个注解待会来看最后呢有一个Complements Scan就是一个包扫描的这么一个注解那么其实呢这个Enable Auto Configuration就是整个的这个自动配置的一个关键所在了所以呢我们要来聊一聊这个Enable开头的这个注解那么这个注解底层呢其实它也是个组合注解上边的原注解
[01:29] 然后呢这里边有一个importok它底层原理就是使用这个import注解来导入一些东西的好嘞接着回到资料我们来说在Spring Boot里边提供了很多的enable开头的注解这些注解呢都是用于动态的开启某些功能的而底层呢它使用的是import注解来导入一些配置的类啊等等这些东西来实现并的动态的加载那么这一段话可能你仅仅是见到一下不太好理解
[01:58] 那为了更清楚的我们能知道Enable的一些功能我们先来思考一个问题Spring Boot的工程是否可以直接来读取乍包里边定义的bin呢也就是说我是不是可以拿到你其他人定义的包里边第三方包里边的那个bin呢直接获取到当然我能提这个问题肯定是不可以那么如果不可以这个地方问题就非常严重了比如说刚才我们说的我们的Redis Template获取
[02:27] 是不是人家jar 包里面的Redis template定义的bin那为什么我的工程引入了Redis的起步依赖我就直接可以获取到呢来看一下Spring Boot是如何来做这个事的那么我们首先来演示一下这个不能获取第三方jar 包里面定义的bin这么一个特点我们在里边还是一样创建这么一个模块要演示
[02:54] 第三方的我们就得创建两个模块我们来写一下好第一个呢我们叫com.it黑码然后呢这个地方叫Spring Boot.com这个地方我们讲的是enable相关的注解叫enable好那么这里边呢什么都不加了我们直接就ok就可以了好ok就可以了ok了之后呢接下来我们再写一个工程或者说我们现在这里边好这里边你看这里边呢我们现在
[03:29] 来获取一下并获取个什么并呢我们比如说在这里边呢我们来获取一个并获取这个并呢是其他工程定义的但是呢其他工程我们还没有编写嘛我们先把这个代码写上比如说我们叫user将来我们在另外一个工程里边定义一个并起名叫user然后呢我们在这个工程里边来获取一下看能不能获取到那么当然现在还没有其他的工程我们把一个另外的一个工程呢给它也创建出来
[03:59] 这个工程呢其实只是来提供一些个bin所以呢简单的写一下就可以了好com.it黑码然后这个地方叫做Spring Boot-比如说enable-other吧好下一步下一步弄完了之后呢也没有导入任何的坐标啊好OK那么这个工程呢其实就是来提供一些个bin的定义的所以呢我们也不需要什么其他的功能了
[04:30] 比如说什么测试啊这坐标啊都可以删掉当然你想留着也是没有什么问题的把BU的插件呢也都给它删掉越简单越好然后呢这里边呢测试的代码呢其实我们也不需要去加了好把它删掉为了让它更快一点删掉然后呢这里边的一个引导类呢也不需要因为又不起动这个项目好都不需要这个包也干掉都给它删掉好删的差不多了之后呢我们来写一个B
[04:59] 比如说我们叫做com.it黑码.duman下的user这个类就是这个类没问题吧好那么这个类定义好了之后那么我们再写一个配置类把它加载到当前的这个项目的Sprint IOC容器里边去那么我们再写一个配置类的话呢我们就得写一个com.it黑码.config这个包叫做
[05:28] userconfig用完了之后呢它是一个配置类我们就写configuration好配置类弄完了之后接下来我们提供一个方法public user返回一个userreturn new一个user代码非常简单就写完了然后加一个atb给它注入一下弄完了之后呢这个代码写完了之后那么我们只需要干一件事
[05:59] 我们让我们当前这个Enable这个项目获取并的这个项目依赖刚才我们写的那个第三方的项目Dependency叫做EnableOtherOKEnableOther就这个坐标没有问题对吧弄完了之后好代码基本上就写完了我们来测试这里边的user的获取我们已经写好了写好了我们来运行一下看一下现在刚才我们得出
[06:26] 我们说不能够直接获取那这个地方就会报错对吧他说没有一个名叫userbin被可用是吧OK那么这个地方我们看到了这个问题啊就是说Spring Boot的工程呢它不能直接获取获取哪个呢获取我们在其他的工程里边定义的这个bin不能直接获取原因是什么呢原因就是在我们这个Spring Boot Application
[06:53] 这么一个注解里边的complement scan这么一个注解上这个注解说一下这个Spring Boot的complement scan它扫描它是扫描的范围扫描的一个范围扫描范围是当前引导类所在包及其子包也就是说这个
[07:21] 当前的complex scan这个包的这个这个注解的扫描的一个范围呢是个引导类在的这个包或者它的子包都可以那么我们来看好我们定义的这个configure里边这个user configure它的包是啥呢它的包是不是这个包对吧它的包是这个吧那这个包那么我们现在当前的包是不是这个包对吧是子包吗没有一个包含的关系吧没有对吧所以呢它加载不到
[07:51] 那么我们第一种做法想解决这个问题我们其实有很多做法我们很多做法我们可以这样我们可以使用import使用这个叫做component scan来去扫再把这个包扫描一下就行了来扫描一下扫描这个我们所在的配置类这个包这个包就可以了可以试一下好at component scan
[08:22] 把当前的刚才我们说配置类所在的这个包呢也给它加入到扫描的范围里边去就可以了好复制过来复制过来之后呢我们再来启动看一下可不可以呢来看user是不是获取到了OK啊非常简单啊那这样的解决方案或者说这个原因我相信大家应该很好理解啊但是这个解决方案其实有点有点太low了是吧你比如说将来你要应用一个第三方的一个功能你要获取人的
[08:55] 人家的一些个功能或者说获取人家的一些个对象注入的对象OK你还需要把包扫描一下那你这玩意得写一排了对不对而且呢你咋知道这个包是啥呢你得记多少个东西啊很难记住啊所以这种方案呢我们肯定不会去直接使用的对吧那么除了这种方案之外呢还没有没有什么其他比较好的方案呢当然是有的第二种呢就可以好就可以来使用我们的import注解
[09:24] 注解加载类
[09:53] 的容器所自动创建并且加载到Spring容器里面去所以呢我们说一下说Import注解加载类这些类这些类都会被被Spring创建并放入IOC容器那么放入IOC容器有什么就可以获取到了那么Import我们现在导入谁呢我们可以把这个user configure来导入进来这里边写user
[10:24] configure their classOK了吧OK了之后呢来看我们现在再来去获取再来获取你看是不是还是获取到了也是没有什么问题的是吧那么这样的方式比刚才的方式是不是就好一些了对吧但是呢还是同样的问题啊我使用import对吧我要用一个功能我得用import的搞一下对吧那这样好像也不是特别的方便因为我要记这个类的名字对不对
[10:55] 那还有没有更好的方式呢当然是有的那么第三种第三种方案第三种方案呢我可以对import这个注解进行一个封装怎么个封装法呢比如说你不是要写这个注解吗比如说我要用user这个这个bin的话那我就要写这个东西那这个东西有点长啊怎么办呢我可以在第三方比如说提供这个userbin这个
[11:23] 里边这个项目里边我提供一个功能什么功能呢注意看哈我们写一个注解叫做EnableEnable什么呢userOK那么这玩意是个注解的话我们就用add interface来标识标识了之后呢我们自己再导入导入导入这个user的configure.class好导完了之后呢这个注解要像正常使用这些原注解还必须得给它加上放这个地方OK
[11:54] 那么这个EnableUser就写完了写完了之后那么将来我要用User的bin怎么办呢我就不用引破写这么长一串了对吧我怎么办我直接用atEnableUserOK了那么这个和这个其实是一回事只不过是简化了一下而已那么再来获取你可以看一下效果是不是又可以获取到了你看没问题吧
[12:23] 所以你会发现Enable这个注解我们现在再回到PPTB来看Enable开头的注解它是用来动态开启某些功能的比如说你不加这个注解你是不是就获取不到这个user的对象获取不到那个功能你是不是开启不了而这个底层是用什么呢使用Import注解来导入一些配置的类当然不一定是配置类我们还有很多种方式的来实现变得动态加载
[12:52] 那么我们可以来看Spring Boot Application这个核心的注解里边来看Enable Auto Configuration你看它里边是不是也用了Import注解它只不过导入了另外一个其他的类其实里边比较核心的不是Enable这个注解怎么怎么去用而是Import这个注解怎么怎么去用OK那么接下来我们就要讲的就是Import的一些
[13:21] 不同的使用方式那么这一块我们先讲解到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 中 @Enable* 注解的原理，通过创建示例项目、配置类和主类，展示如何使用 @ComponentScan 和 @Import 注解来实现自动装配和组件扫描。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IDEA 项目结构，选中 com.ithema.springbootcondition 包，准备创建或修改相关代码。
画面 2: PPT 标题页，显示“Spring Boot 自动配置”和“@Enable*注解”，说明本节内容。
画面 3: 在 IDEA 中创建新模块，选择 Spring Boot 2.1.8 版本，准备构建项目。
画面 4: 在 IDEA 中通过“Project Structure”菜单创建新模块，选择依赖项。
画面 5: 显示项目 pom.xml 文件内容，包含 Spring Boot Starter Parent 和 Spring Boot Starter Web 依赖。
画面 6: 在 IDEA 中编辑 pom.xml 文件，显示 Spring Boot Starter Web 依赖。
画面 7: 显示 UserConfig.java 文件内容，包含 @Configuration 注解和类定义。
画面 8: 显示 pom.xml 文件内容，包含 Spring Boot Maven Plugin 依赖。
画面 9: 显示 SpringbootEnableApplication.java 文件内容，包含 @ComponentScan 注解和 main 方法，运行后报错“没有名为 'user' 的 bean”。
画面 10: 显示 SpringbootEnableApplication.java 文件内容，修改 @ComponentScan 扫描包路径，运行后成功启动。
画面 11: 显示 SpringbootEnableApplication.java 文件内容，添加 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 12: 显示 EnableUser.java 文件内容，包含 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 13: 显示 SpringbootEnableApplication.java 文件内容，添加 @Import 注解导入 UserConfig 类，运行后成功启动。
画面 14: 显示 Import.java 文件内容，包含 @Import 注解的源码，说明其作用。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ithema</groupId>
    <artifactId>Spring Boot-enable-other</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>Spring Boot-enable-other</name>
    <description>Domain project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>
    </dependencies>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.5.8.RELEASE</version>
        <relativePath/>
    </parent>
</project>
```

画面 8:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.ithema</groupId>
        <artifactId>Spring Boot-enable-other</artifactId>
        <version>0.0.1-SNAPSHOT</version>
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

画面 10:
```java
package com.ithema.springbootenable;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.ithema.config")
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 11:
```java
package com.ithema.springbootenable;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.ithema.config")
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
package com.ithema.config;

import org.springframework.context.annotation.Import;

@Import(UserConfig.class)
public class EnableUser {
}
```

画面 14:
```java
package org.springframework.context.annotation;

import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Import {

    Class<?>[] value();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题页，标题为“Spring Boot 自动配置”，副标题为“@Enable*注解”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

