# 08-SpringBoot自动配置-自定义starter步骤分析

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\08-SpringBoot自动配置-自定义starter步骤分析_【海量资源尽在 ubkz.com】.mp4
- 时长 6分56秒（音频 416s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 介绍完Spring Boot自动配置的知识点之后接下来我们来做一个案例来强化一下自动配置的流程的学习首先我们先看一下需求需求说自定义Redis的Starter其实这个Redis的Starter呢Spring Boot已经给我们提供好了我们在这自定义呢只是为了强化知识点的学习那么当导入了刚才你自定义的这个Redis的Starter的坐标之后呢Spring Boot
[00:30] 它会自动的帮你创建一个Jadis的bin那么拿到Jadis的bin了之后我们就可以来操作Radis了OK其实看到这个需求之后我们大概心里能够知道该怎么做但是呢很多细节可能又把握不是很精准对吧其实呢没有关系我们知道Spring Boot它提供好了很多很多的Starter或者说很多的起步依赖
[00:59] 但是有一些起步依赖Spring Boot并没有提供而是由那个技术它本身自己写的它期望跟Spring Boot整合所以它自己写了个起步依赖那比如说MyBetis就是这样做的它自己写个起步依赖我让Spring Boot把我整合一下那么接下来我们就可以参考MyBetis的做法来去找到对应的思路那么参考它呢我们打开idea在我们的enable这个模块里边我们引入一下MyBetis的起步依赖
[01:30] 其实呢你如果记不住这个坐标没关系啊我们上网搜一下岂不依赖啊这个坐标还是比较难记的因为它跟他们的规则都不太一样所以我们上网搜一下打开浏览器然后呢在里边搜mvn repository其实你随便一搜都有很多热心观众给你提供啊我们在这搜呢相对于来说会专业一点在这里边我们搜mybiddies哎这个地方有历史记录啊就是搜的这个
[01:59] mybidstspring-boot然后我们找到这个stutter找到stutter之后你看这个地方我们找一个最多的105这个1.3.2这个版本把这个坐标复制过来放到我们的模块里边就可以了可以了之后我们来看这个dependency首先我们来看它的名字它叫org mybidstspring.boot这是它的group idartifact的id是mybidstspring-boot-stutter
[02:29] 你注意看这个Starter跟我们之前的这些Starter是不是名字都不太一样之前Spring官方所提供的它的功能是不是在最后边而MyBadges提供的呢它的功能是不是在前边中间是不是都是一样的对吧一般第三方的它的功能在前边然后呢官方提供的Spring Boot提供的功能在后边以示区分那么待会我们第一我们就可以叫Radius-Spring Boot
[02:58] 刚开始了对吧OK这是第一个事第二个事呢我们看一下它里边对应的这个起步依赖里边包含的坐标好来看这里边它有一个dependencies它包含了很多的坐标这些其他的坐标呢我们都可以不看我们看中间的这一个这个呢叫做mybidis supreme boot auto configurable从名字上我就可以知道这是mybidis来进行自动配置的
[03:27] 这么一个坐标OK那么其实呢这个Starter它把这个自动配置呢包含起来了将来呢我们引入了这个Starter之后那个自动配置的那个坐标和那些代码其实都能够加载的到了那么同样呢我们也可以打开对应的它的jar 包来瞧一瞧好找到买Batis的那个Starter往下找这个地方可以看Starter其实Starter这个jar 包里边什么都没干啊它干的事呢
[03:56] 就是将这些个东西给它整合到一起提供一个对外提供一个依赖坐标方便导入仅此而已最关键的是它依赖了这个autoconfigurationconfigure这么一个坐标可以看一下你看这里边没有代码就有个meta info文件夹对吧什么都没有没有代码它其实就是一个POM文件来整合依赖的OK那么接下来看最关键的就是这个autoconfigure那么这里边呢代码
[04:25] 就是很多了比如说它有一个叫做MyBitness的Auto Configuration那么这就是一个配置类MyBitness的自动配置类你看OK吧那么进行这个自动配置类将来要能够被Spring所识别从而加载这个配置类里边定义的这些个bin的话那么它的做法是在里边定义了一个MetaInfo这么一个文件夹里边不出意外的话会提供一个叫做Spring.Factories看到了吧
[04:55] 然后在这个SpringFactories里边很熟悉弄了一个键叫做Enable Auto Configuration跟我们刚才做的是一样的然后呢在这里边提供了一个叫做MyBattist Auto Configuration就是刚才我们看到的那个类对吧OK所以呢这样去做的话呢就能够在Spring Boot项目所启动的时候去加载到这个MetaInfo里边这个配置文件
[05:23] 从而呢识别到这个自动配置的类而且呢这个配置的类呢里边定义的B就会自动的被Spring加在到它的IOC的容器里边去了整个过程呢大概就是这么一个过程了解了这个买Betis的起步依赖的书写之后呢接下来我们就可以来写我们自己的一个Redis的起步依赖了那么首先我们来分析一下这个步骤参照买Betis首先第一步我们也创建一个模块
[05:54] 叫做redis-Spring Boot-autoconfigure在这个模块里边将来就写那些配置类第二个呢我们也创建一个Spring Boot的redis-Spring Boot-starter这个起步依赖这个起步依赖呢去依赖于这个自动配置的这个模块那么将来我们导这个starter这个就可以了那么第三个事呢我们在这个redis的Spring Boot
[06:20] auto-configural就是自动配置这个模块里边我们去初始化对应的Jadis的bin当然我们可以通过Redis的auto-configuration来做并且我们定义一个metainfo下定义一个sprint.factories这么一个文件让sprintboot能够扫描到我们自己写的那个配置类最后一步就是在我们的测试工程模块里边去引入Redis的starter依赖并且获取Jadis的bin来操作Redis
[06:49] 那么基本的思路我们分析完了之后接下来我们就来完成代码的编写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中引入 MyBatis Starter 依赖，并查看其内部自动配置类的结构。

2) 按时间顺序列出每张画面的要点：
画面 1: 在 IDEA 中打开 Spring Boot-enable 项目的 pom.xml 文件，显示了当前已有的两个依赖项。
画面 2: 浏览器打开百度链接，页面空白。
画面 3: 浏览器访问 Maven 中央仓库，查看 mybatis-spring-boot-starter 的版本列表，当前选中 1.3.2 版本。
画面 4: 在 IDEA 的 pom.xml 文件中，光标位于 </dependencies> 标签后，准备添加新的依赖。
画面 5: 在 IDEA 的 pom.xml 文件中，光标位于 </dependency> 标签后，准备添加新的依赖。
画面 6: 在 IDEA 中打开 mybatis-spring-boot-starter-1.3.2.pom 文件，查看其内部的依赖结构。
画面 7: 在 IDEA 中打开 mybatis-spring-boot-starter-1.3.2.pom 文件，光标位于 <dependency> 标签内，准备添加新的依赖。
画面 8: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 9: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 10: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 11: 在 IDEA 中查看项目依赖树，展开 mybatis-spring-boot-starter-1.3.2 的依赖项。
画面 12: 在 IDEA 中查看 mybatis-spring-boot-autoconfigure-1.3.2.jar 的 META-INF/spring.factories 文件内容。
画面 13: 在 IDEA 中查看 mybatis-spring-boot-autoconfigure-1.3.2.jar 的 META-INF/spring.factories 文件内容。
画面 14: 展示 PPT 页面，标题为“Spring Boot 自动配置”，内容为“案例：需求 自定义 redis-starter，要求当导入 redis 依赖时，Spring Boot 自动创建 Jedis 的 Bean。”

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>com.itheima</groupId>
    <artifactId>Spring Boot-enable-other</artifactId>
    <version>0.1-SNAPSHOT</version>
</dependency>
```

画面 4:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 5:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 6:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>1.3.2</version>
</parent>
<artifactId>mybatis-spring-boot-starter</artifactId>
<name>mybatis-spring-boot-starter</name>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-jdbc</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-autoconfigure</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis-spring</artifactId>
    </dependency>
</dependencies>
```

画面 8:
```xml
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>1.3.2</version>
</dependency>
```

画面 12:
```properties
# Auto Configure
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 14:
PPT 标题：Spring Boot 自动配置
PPT 内容：案例：需求 自定义 redis-starter，要求当导入 redis 依赖时，Spring Boot 自动创建 Jedis 的 Bean。

