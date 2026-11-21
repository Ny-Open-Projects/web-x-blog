# 52-SpringBoot整合Drools_1 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们来看一下我们规则引擎D-Rose最后一个小节

最后一个小节就是在我们Spring Boot项目当中来使用D-Rose

也就是Spring Boot整合D-Rose

这也是后边咱们在TMS项目当中使用D-Rose的方式

因为我们现在的项目都是基于Spring Boot开发平台来开发我们的项目

这是我们主流的应用方式

好,那接下来我们就来通过这么一个小的案例来演示一下

如何通过Spring Boot在Spring Boot项目当中来整合D-Rose

首先我们来创建这么一个工程

这个工程我已经创建好了

并且第一步已经做完了

就是这个POM文件也已经导入了

这里面就导入的坐标都是我们常见的Spring Boot,Starter,Web等等这些

然后就是我们D-Rose相关的这些坐标

这就不用再说了

这是第一步

然后接下来第二步的话

咱们需要来提供一个Spring Boot的配置文件

对吧

对吧

对吧

就是这个application.yml

好,然后我们在这来创建一下

然后具体的内容我就不再手敲了

就是配置了一个服务的端口号

还有一个应用的名称

好,直接粘贴在这个位置就可以了

好,这个也不用解释了

然后接下来我们来看第三步的话

咱们来编写一个规则文件

当然我们这个小节主要展示的是我们整合的方式

对吧

所以说我们这个规则文件就整一个最简单的

大家看

第四步

我们先定义这么一个规则文件

然后规则名称是这个

对吧

问

然后直接是不是相当于是个处

然后直接Zen

执行的代码其实就是一个输出语句

所以这块我们规则文件就使用最简单的规则文件就可以

然后在这个位置还是在resource下边来创建一个Rules目录

在下边来创建一个目录

然后在目录里边我们来创建这个叫做hello world.dl

好

那么这个文件内容我就直接复制了

直接拿过来

Ctrl C

好

这是规则文件也就提供好了

然后再往下呢

我们就需要来提供相应的配置类了

这是主要呢

我们在Spring Boot项目当中啊

使用DLs主要就是靠这个配置类是不是来进行整合

当然这个配置类呢

我们其实并不需要自己去手敲

因为基本上也都属于模板化的代码

它其实它的作用呢就相当于配置文件

对不对

所以说呢

我们只要能看懂

然后呢

能进行相应的改造就可以了

咱们可以大概来读一下

这个文件

这里面其实主要就是什么呢

创建了我们这个DLs当中啊

非常核心的几个类

对吧

一个是这个KIE File System

文件系统

然后呢

还有一个就是KIE Container

对吧

容器

还有一个是KIE Base

这是规则库

还有一个呢

是一个处理

其实是一个后处理器

对吧

那么我们直接把这个代码拷过去

然后呢

先把这个包创建一下吧

好

这么一个Config包

然后呢

咱们在这来创建一下

然后这个类名呢

我们也考一下

叫做DRoads Config

具体的代码

对吧

咱们直接拿过来

整个都复制过来

这就相当于是我们的配置文件了

对吧

相当于它起的作用

就是配置文件的作用

好

然后呢

在这个规则文件里边

在这个配置类里边呢

咱们来看一下

它会读取什么呢

读取我们这个Rules

目录下边所有的规则文件

然后呢

把我们这个KIE Base

KIE Container等等

这些对象啊

核心的对象

都创建成为了这个规则文件

它会创建出来

你看

在这咱们定义了这么一个常量

对吧

它指向的就是我们这个目录

这就意味着我们编写的

所有的规则文件呢

一定要保证是在这个目录下边

否则是读取不到的

否则是读取不到的

好

然后具体怎么创建的话

这个代码

大家如果有兴趣呢

可以自己来读一下

都属于模板化的代码

那么通过

你看这些方法上面

是不是都加了相应的注解

对吧

Bit

这就表示啊

我们在加在这个配置类的时候呢

它就会

执行我们的规则文件

这个方法

把这个KIE

File System对象

是不是来实例化

但是它是有条件的

是什么呢

当我们Spring容器里边

没有这种对象的时候

是不是才会创建

如果已经存在这种对象了

它就不会执行这个方法了

这不是Conditional

Missing Bin

对吧

当没有这个Bin的时候呢

它才会创建

然后这些都加了这些注解呢

都有条件

对吧

其实就是保证什么呢

保证我们这些实例啊

它是一个单例的

它是一个单例的

好

那么这个

这个配置类直接拿过来就可以了

那么我们唯一可能需要修改的呢

也就是这么一个路径

对吧

其他的都是固定的代码

那么不用做任何修改

最终呢

我们这些对象呢

都被实例化出来了

好

然后呢

接下来呢

我们就可以来创建一个Service类

对吧

然后在Service类里边呢

直接注入什么呢

KIE Base就可以

注入KIE Base

然后呢

通过这个Base呢

就可以直接New一个什么Session

好

那么我们把这个Service类

这个Service包呢

来创建一下

来看一下这个Service包

是直接选中这儿

来创建这个包结构

好

Ruler Service

然后这类里边这个代码呢

我也直接拿过来

这个类呢

也比较简单啊

咱们就是注入了一个什么呢

这个KIE Base

对吧

那么刚才也说了

为什么能够注入成功呢

就是因为我们在这个地方

是不是已经实例化了

咱们这个KIE Base了

好

那么就会把这个对象呢

给我注进来

注进来之后呢

在我们调用这个Ruler方法的时候

它是不是就会来New一个KIE Session

然后呢

调用这个Session之后呢

咱们直接执行File All Rulers

咱们并没有去调用Insert

就是因为我们当前这个规则文件呢

非常简单对吧

咱们这匹配的时候呢

其实直接就匹配成功了

所以说呢

这个地方并没有去Insert一个Fake的对象

好

然后接下来呢

我们来创建一个Controller

主要就是来触发一下对吧

因为在我们Controller当中啊

我可以去调这个Service

调用Service的Ruler方法

这样呢

就可以

触发规则了

好

在咱们这个D-Rose包下边来

创建一个Controller包

这个类呢

叫做HelloController

所以这些代码呢

都比较简单

所以我就不再手敲了

整个把这个代码复制过来

好

在这里边呢

就注入我们的Service

对吧

注入我们的Service

把这个Service对象注进去

然后呢

我们直接调用它的这个Ruler方法

一调Ruler方法呢

它就会获得一个Session

对吧

然后呢

来触发我们的规则

好

好

好

好

最后呢

我们是不是还差一个什么呢

还差一个这个启动类

对吧

好

把这个启动类呢

来创建一下

好

把它拿过来

那么到这儿的话呢

咱们这个整合呢

其实就已经完成了

对吧

其实在Spring Boot项目当中

整合D-Rose

主要的代码呢

就是在这个配置类这儿

对吧

主要就是靠这个配置类

好

大家一定要注意

我们这个配置类

别忘了加这个注解

对吧

如果你不加这个注解

它是不起作用的

好

好

cast

好

这个配置类

但是这个配置类刚才也强调了

其实用不着我们自己去编写

它的作用就相当于配置文件

所以我们直接拷过来

就把这个地方呢

给它改对了

就可以了

好

咱们这个代码已经写完了

那么一会儿呢

我们来测试一下

看看我们这个整合行不行

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于如何在 Spring Boot 项目中集成 Drools 规则引擎的实战教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从创建项目、配置 Maven 依赖、编写配置类、创建规则文件、编写服务类到最终启动应用并测试规则触发的完整流程。核心内容是展示如何利用 Spring Boot 的自动配置和条件注解来简化 Drools 的集成，以及如何在 Java 代码中调用规则引擎执行规则。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:02**: 视频开场，展示一个空的 Spring Boot 项目结构。
*   **00:02 - 00:05**: 讲师在 Typora 文档中展示课程大纲，明确本节内容为“Spring Boot 整合 Drools”。
*   **00:05 - 00:08**: 展示项目 `pom.xml` 文件，重点讲解了用于排除 Spring Framework 依赖的 `<exclusions>` 配置，以及用于构建的 Spring Boot Maven 插件。
*   **00:08 - 00:12**: 讲师在 Typora 文档中展示创建 `application.yml` 配置文件的步骤。
*   **00:12 - 00:15**: 展示了在 IntelliJ IDEA 中创建 `DroolsConfig.java` 配置类的代码，其中包含了 `@Configuration` 注解和 `@ConditionalOnMissingBean` 注解。
*   **00:15 - 00:18**: 讲师在代码中高亮显示了 `@ConditionalOnMissingBean` 注解，解释其作用是确保只有在没有默认 Bean 时才创建该 Bean。
*   **00:18 - 00:22**: 展示了 `DroolsConfig.java` 中的 `kieFileSystem` 方法，用于扫描并加载规则文件。
*   **00:22 - 00:25**: 讲师在代码中高亮显示了 `ResourcePatternResolver` 的使用，用于获取资源文件。
*   **00:25 - 00:28**: 展示了 `DroolsConfig.java` 中的 `kieContainer` 方法，用于创建并初始化 Drools 的 KieContainer。
*   **00:28 - 00:31**: 讲师在代码中高亮显示了 `kieBase` 方法，用于获取规则库。
*   **00:31 - 00:34**: 展示了 `RuleService.java` 类的代码，其中包含了 `fireAllRules()` 方法用于触发规则。
*   **00:34 - 00:37**: 展示了 `helloworld.drl` 规则文件的内容，其中定义了一个简单的规则 `rule "rule_helloworld"`。
*   **00:37 - 00:40**: 讲师在 Typora 文档中展示创建 `DroolsApplication.java` 启动类的步骤。
*   **00:40 - 00:43**: 展示了 `DroolsApplication.java` 的代码，其中包含了 `@SpringBootApplication` 注解。
*   **00:43 - 00:46**: 展示了 `HelloController.java` 的代码，其中包含了 `@Autowired` 注解的 `RuleService`。
*   **00:46 - 00:49**: 讲师在代码中高亮显示了 `@RequestMapping` 注解，用于定义 HTTP 请求映射。
*   **00:49 - 00:52**: 展示了 `HelloController.java` 中的 `hello` 方法，用于返回一个简单的字符串。
*   **00:52 - 00:55**: 讲师在 Typora 文档中展示启动应用并访问 `http://localhost:8080/hello` 的步骤。
*   **00:55 - 00:58**: 展示了在浏览器中访问 `http://localhost:8080/hello` 后的响应结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：包含“问题引出”、“规则引擎概述”、“Drools入门案例”、“Drools基础语法”、“规则属性”和“Spring Boot整合Drools”等章节。
    *   Maven 依赖配置：展示了排除 Spring Framework 依赖的 `<exclusions>` 和使用 Spring Boot Maven 插件的 `<plugin>` 配置。
    *   `application.yml` 配置：展示了 `server.port` 和 `spring.application.name` 的配置。
    *   `DroolsConfig.java` 配置类：展示了 `@Configuration`、`@ConditionalOnMissingBean`、`@Bean` 等注解的使用，以及 `kieFileSystem`、`kieContainer`、`kieBase` 等方法的实现。
    *   `RuleService.java` 服务类：展示了 `fireAllRules()` 方法的实现。
    *   `helloworld.drl` 规则文件：展示了 `rule "rule_helloworld"` 的定义。
    *   `DroolsApplication.java` 启动类：展示了 `@SpringBootApplication` 注解。
    *   `HelloController.java` 控制器类：展示了 `@Autowired`、`@RequestMapping` 等注解的使用。

*   **代码关键内容**:
    *   **Maven 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.7.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
        ```
    *   **`DroolsConfig.java` 配置类**:
        ```java
        @Configuration
        public class DroolsConfig {
            private static final String RULES_PATH = "rules/";
            private final KieServices kieServices = KieServices.Factory.get();
        
            @Bean
            @ConditionalOnMissingBean
            public KieFileSystem kieFileSystem() throws IOException {
                KieFileSystem kieFileSystem = kieServices.newKieFileSystem();
                ResourcePatternResolver resourcePatternResolver = new PathMatchingResourcePatternResolver();
                Resource[] files = resourcePatternResolver.getResources("classpath:*" + RULES_PATH + "/*.drl");
                String path = null;
                for (Resource file : files) {
                    path = RULES_PATH + file.getFilename();
                    kieFileSystem.write(ResourceFactory.newClassPathResource(path, "UTF-8"));
                }
                return kieFileSystem;
            }
        
            @Bean
            @ConditionalOnMissingBean
            public KieContainer kieContainer() throws IOException {
                KieRepository kieRepository = kieServices.getRepository();
                KieBuilder kieBuilder = kieServices.newKieBuilder(kieRepository);
                kieBuilder.buildAll();
                return kieServices.newKieContainer(kieRepository.getDefaultReleaseId());
            }
        
            @Bean
            @ConditionalOnMissingBean
            public KieBase kieBase() throws IOException {
                return kieContainer().getKieBase();
            }
        }
        ```
    *   **`RuleService.java` 服务类**:
        ```java
        @Service
        public class RuleService {
            @Autowired
            private KieContainer kieContainer;
        
            public void fireAllRules() {
                KieSession kieSession = kieContainer.newKieSession();
                kieSession.fireAllRules();
                kieSession.dispose();
            }
        }
        ```
    *   **`helloworld.drl` 规则文件**:
        ```drl
        package heloworld
        rule "rule_helloworld"
            when
                eval(true)
            then
                System.out.println("规则：rule_helloworld触发...");
            end
        ```
    *   **`HelloController.java` 控制器类**:
        ```java
        @RestController
        @RequestMapping("/hello")
        public class HelloController {
            @Autowired
            private RuleService ruleService;
        
            @RequestMapping("/hello")
            public String hello() {
                ruleService.fireAllRules();
                return "Hello World!";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖配置**
    *   **描述**: 讲师首先在 IntelliJ IDEA 中创建了一个名为 `springboot_drools` 的 Spring Boot 项目。然后，他打开了 `pom.xml` 文件，演示了如何添加 Spring Boot 的父依赖，并配置了用于排除 Spring Framework 依赖的 `<exclusions>` 和用于构建的 Spring Boot Maven 插件。

*   **场景二：配置类开发**
    *   **描述**: 讲师创建了 `DroolsConfig.java` 配置类。他使用 `@Configuration` 注解将其标记为配置类，并使用 `@ConditionalOnMissingBean`
