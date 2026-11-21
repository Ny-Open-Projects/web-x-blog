# 61-规则引擎Drools-Spring整合Drools（Spring — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看Spring整合DRoads

那么第三种方式就是目前比较主流的

就是我们基于Spring Boot来整合DRoads

那么首先我们还是先来创建一个Mainware工程

咱们这个工程名就叫DRoads-Spring Boot

好,我们把这个Mainware工程来创建一下

把这个给停掉

然后我们创建一个新的

New一个Project

好,这儿的话就不用选取股价了

因为是一个Spring Boot的工程

Comp.it,黑码

然后呢,这是我们这个工程名

DRoads-Spring Boot

好,Next

这个位置呢就不用调了

直接完成

还是在当前这个窗口来打开我们新创建的这个工程

好,那么创建完之后呢

咱们是不是就可以来导入相关的一些坐标

因为这是一个Spring Boot的工程

所以首先呢

我们必须来通过一个Parent是不是来继承

继承我们这个Spring Boot Stutter

这么一个副工程

好,我把这块先拷过来

通过一个Parent来继承

下面这些呢都不用动了

然后呢再往下是不是就是Dependency

我们需要依赖的一些坐标

对吧,每个坐标

咱们先整体来过一下

这个是Spring Boot Stutter Web

这个我们应该是比较熟悉了

还有Stutter什么AOP的

还有什么Stutter Test的

这都是一些这个启动器对吧

还有这个Commons Lang语言包

然后再往下这个呢

就是我们这个DRoos它的这个核心包

其实呢大家可以看到啊

我们前面呢并没有导这个包

我们是不是直接导的是这个Compiler这个包啊

因为什么呢

因为我们在导入这个Compiler这个包的同时啊

其实就已经把这个Curl这个包呢

给通过Maven的依赖传递啊

给传递过来了

所以说呢我们这个地方呢

你可以不显示的去导它

因为我们在导这个Compiler这个包的时候呢

就会把它传递过来

当然你显示的把它导过来呢

也是可以的没问题

你看Curl这是核心包

而这个Compiler呢是不是编译包

然后还有一个这是我们新引入的一个包

叫Templates模板包

然后呢这个呢是

也是一个新的包

就是KIE API

里边定义的都是一些接口包

里边定义的都是一些接口包

再往下呢是不是就是我们整合的这个包啊

KIE跟Spring整合的这个包

还是需要来强调一下

前面我们其实已经提到过了

在我们导入这个包的时候呢

它会通过依赖传递啊

传递过来Spring的很多架包

这个呢我们必须得给它排除出去啊

这个呢我们必须得给它排除出去啊

好这是我们引入的Maven坐标

大概就是这些

再往后呢是不是就是关于我们这个资源的

一些过滤

这些呢都是一些常规的配置

然后再往下呢

是不是就是我们这个Maven的一个编译的插件

好

因为是一个Spring Boot的工程啊

所以我们这里边呢

就不用再通过Tomcat的插件来起了

直接通过Main方法对吧

我们Spring Boot来执行就可以了

它是使用了内置的Tomcat

好

咱们整个这块呢来复制一下就可以了

把整个Build

还有这个Dependency

一直到这儿对吧

把这块呢整个都复制过来

好粘贴到这儿就可以了

那这样的话呢

我们这个POM文件呢就已经配置好了

好

这是关于这个POM文件的配置

再往下呢

咱们是不是作为一个Spring Boot的工程啊

我们需要来提供Spring Boot

它的一个配置文件啊

一般呢

它的配置文件是不是有两种形式

一种是这种YML的

还有一种是属性文件

Properties

好

那么我们在这儿呢来创建这个

是这种YML这种形式的

就叫Application

Application.yml

这是咱们Spring Boot默认的这个配置文件名

找到我们的resources目录

对吧

在这儿呢把这个配置文件传进传进出来

传进出来之后呢

我们这里边啊

因为要配置的项很少啊

因为当前的我们并没有去集成其他的一些框架

所以现在我们配置的一个是我们这个ServerPod

对吧

就是我们TOMCAT的端口号

那是8080

还有一个呢

就是我们当前这个Spring应用的名称呢

好

一个是这个Server.Pod

对吧

这个呢

我们就写8080就可以了

然后呢

还有一个就是我们这个Spring

它的这个应用名称

对吧

应用名称呢

我们就跟咱们这个工程名呢

保持一致啊

好

也叫D-Rose-SpringBoot

当前我们这个YML文件呢

就已经配置好了

随着后边我们可能真正做项目的时候呢

要集成的框架越来越多

对吧

那么它这里面

它的配置项呢

也会越来越多

好

那这个呢

我们就已经搞定了

第三步呢

我们要做的是不是就来创建咱们这个规则文件

同样我们的规则文件呢

还是放在这个Rules目录下

咱们来创建这个helloworld.dl

那么这块呢

我们这个规则文件呢

还是简单处理一下

我就直接拷过来了

那么名字呢

还叫rules-helloworld

对吧

然后呢

直接匹配成功

对吧

这不是返回处吗

然后呢

直接输出这句话

好规则文件呢

我们就不再多说了

这个搞定

那么再往下呢

就是需要来提供一个配置类

是叫做derose-config

咱们使用过SpringBoot的应该都了解啊

一般呢

我们都会提供一个配置类

对吧

其实它起到的作用呢

就是配置文件的作用

只不过呢

我们在SpringBoot里面呢

都是提供Java类作为配置项

对吧

在这里面来进行配置类呢

它本质上其实就是一个配置文件的作用

好

那么我们给它创建在哪呢

咱们创建在这么一个包下边

我把这个包呢

先创建一下

来创建一个package

对吧

然后呢

在这下面呢

来创建出来这么一个类啊

就叫什么呢

derose-config

一看就是一个配置类

对吧

好

然后这个配置类呢

咱们可以直接考过来来看一下

这是规则引擎配置

对吧

这个配置类整个呢

我把它复制过来

然后呢

我们把这个代码大概读一下

但是对于这种配置类的代码呢

我们其实并不需要自己去把它背着写下来啊

其实没有多大意义

哎

因为呢

它相当于就是个配置文件

对吧

这些配置呢

相对来说都是比较固定的

呃

现在呢

它有一些类啊

没有自动导进来是因为什么呢

它有相同的类啊

呃

也就是说相同名字的

比如说我们这个resource啊

我们手动把它导一下

因为什么呢

你看你现在导入的时候呢

它是不是需要让我们去选

你要导哪几个

对吧

因为它现在比较多啊

那么实际上我们用的是这个好

现在呢

它是不是就不再报错了

好

咱们大概把这个代码读一下就可以了啊

这个代码呢

相对来说都是比较固定的

因为它就其实就相当于配置文件了啊

那么它作为一个配置类呢

必须得加这么一个注解

对吧

就是configuration

这本身是不是就是配置的意思

然后呢

我们在这呢

定义了这么一个常量啊

其实就是指定的

你看这是什么东西啊

ruler path

是不是指定的

就是我们创建的这个目录啊

目录

这样的话

它是不是就一会儿会用到这个常量

它会顺着我们指定的这个地方

是不是去找我们相关的这些规则文件

对吧

因为我们的规则文件呢

都要放在这个目录下边

一会儿呢

会用到这个常量

指定的就是规则文件

存放到目录

然后还有一个就是我们的KIE service

对吧

这个KIE service怎么获得的呢

这个代码咱们其实也都写过了

通过KIE service

然后呢

factory.get方法来获得KIE service

好

然后我们可以看到

在我们这个配置类里边呢

咱们其实提供了这么几个方法

这几个方法呢

其实就是用来获得某个对象的

这其实就相当于我们在插描配置里边

配置的一个bin标签

对吧

用来创建某个对象的

你看我们这方法上面是不是加了一个bin呢

这就相当于一个bin标签

好

然后呢

还加了这么一个注解啊

叫做conditional missing bin

大家还记得这个注解呢

这个注解呢

这个注解它的作用吧

这个注解它的作用是什么呢

首先呢

它不会说去调用这个方法

把这个对象创建出来

而是先到我们Spring工厂里面去查找

是不是已经存在这种类型的对象了

对吧

如果已经有这种类型的对象了

它就不再去初始化这个对象了

如果没有的时候才去初始化

这就防止我们是不是这个同一个对象

同一个类型的对象

在我们Spring工厂里面可能存在多个

所以说呢

一般呢

我们会加上这么一个注解

就是这个注解呢

就是当它这个什么呢

当它这个missing

missing是不是就是丢失

就是没有这种类型的bin的时候呢

才会去调用这个方法来创建

那么我们可以看到

它这一共是创建了这么几个对象

一个是KIE file system

这个字面翻译过来

是不是就是我们的文件系统

还有KIE container

就是我们的这个容器

然后呢

还有一个是KIE base

容器跟base呢

我们其实都已经接触过了

这个容器

然后呢

这个是base

通过base呢

可以创建session

还有就是这么一个

这是我们在Spring boot里边呢

必须要用到的

就是KModel

代表它是模块

这个呢

咱们直接配置就可以

直接NU出来就可以了

那这个类在哪呢

咱们可以直接点进来

你看一下

是不是就在我们这个ORE

KIE spring

在这个包下边

它是整合包里边的

这么一个类

那么需要把它创建出来

直接NU出来就行了

这就相当于我们一个并标签

配置了这么一个类型

那么我们现在就来看看

好

然后呢

我们来看一下这个file system

这个叫做文件系统

对吧

那也就意味着什么呢

我们需要到我们这个目录下边

去加载什么呢

加载我们的这些规则文件

然后把这个文件系统创建出来

它代表的是KIE的文件系统

好

咱们可以大概读一下这个代码

好

通过service来NU一个

KIE file system

对吧

那么创建出来这么一个文件系统

但是刚刚创建出来的文件系统里边呢

是没有东西的

对不对

所以说呢

我们需要

通过这个

这个大家可以看到

叫resource pattern resolver

这个其实就是用来

加载我们某个目录下边的资源的

你看先把它NU出来

NU出来之后呢

调用它的这个get resource方法

然后呢

到哪去找呢

到我们的class path下边去找

找哪个目录呢

大家看

ruler path

这是不是就是咱们定义的这个常量啊

这样的话

它是不是就找到了我们这个rules目录

然后rules目录下边

星点星

是不是就是匹配所有的文件

当然了

我们只会在这个文件

这个目录下边

放我们的这个DRL

就是这种规则文件啊

不会说放其他的这些类型的配置文件的

好

这样的话呢

我们这些规则文件是不是就都被加载到了

然后封装到了这么一个数组对象里边

resource数组对象里边

然后呢

接下来我们是不是便利这个数组

然后呢

通过把这个path加上

然后呢

file name

最终呢

这就是得到了我们每个规则文件

它的这个完整的一个路径

对不对

然后呢

通过我们这个file system

就是文件系统

对象呢

一个一个写

把我们加载到的这些文件

对吧

写到我们这个

写到我们的这个file system

就文件系统里边去

最终呢

把这个文件系统对象给我们返回

好

大概呢

它的一个

这个代码

它的实现思路是什么呢

其实就是到我们这个path下边

是不是去加载我们相关的这些规则文件

最终呢

把这些规则文件呢

写入到文件系统里边去

大概呢

这就是这个代码

它的

它的含义

但是对于这种类型的代码呢

我们其实不用自己去背着写

因为都是比较固定的写法

咱们直接呢

把这个配置类拷过来

唯一需要改的可能也就是这个目录

对不对

你的目录有可能不是rules

那么修改一下就可以了

好

这个呢

是创建的是我们的file system

就是文件系统

这个呢

是用来创建我们的container

就是我们的容器对象

对吧

创建我们的容器对象

好

把这个容器对象创建好之后呢

接下来

我们就会用这个容器对象

要创建的就是我们的这个base对象

而这个kebase呢

它是由容器对象来创建的

你看

先调用我们这个kecontainer的方法

其实就是这个方法

它就会返回一个container对象

然后呢

get kebase

这样拿到的就是一个base对象

有了这个kebase呢

我们就可以创建我们的session

OK

这就是咱们这个配置类啊

这里面可以看到代码量呢

其实挺多

但是呢

都是固定的代码

我们直接拷过来就可以用了

好

这是关于这个配置类的

那么再往下呢

咱们是不是来创建我们的service

还是叫ruler service

跟咱们上一个这个整合是一样的

那么我们需要来提供这么一个ruler service

放在哪个包下面呢

咱们就按照这个

讲一讲这个目录结构来创建了

来创建一个package

在这下面呢

我们来创建这个类啊

就叫ruler service

好

创建一个类

叫做ruler service

好

这个类呢

是不是还是需要

让我们的sprint来管理起来

对吧

所以说呢

我们需要给它加这么一个注解啊

service注解

好

直接写吧

在这来加一个service注解

然后呢

这里边咱们是不是需要注入我们刚才创建的这个什么呢

kebase

只不过大家可以看到

这儿我们用的注解呢

就又回归了我们sprint传统的这种outware的注解了

对吧

因为我们上面这两种方式呢

都是用的那个kebase啊

那个注解

大家还记得吧

咱们可以大概来看一下

就是我们在这个service类里面注入的时候呢

使用的是这个kebase注解

好

现在呢

我们在sprintboot这个整合里边呢

就又回归了我们传统的方式啊

所以说我们在这儿呢

用的还是outware的注解

从我们sprint工厂里面直接把这个kebase对象

这个注进来

然后呢

提供ruler方法对吧

这个代码还都是完全一样的

那我就直接

复制过来了

对于这种代码呢

我就不再手敲了啊

好

直接注进来

通过它呢

获得session对象

然后file all rulers

对吧

进行所有规则的匹配

匹配成功之后呢

就会触发

然后呢

我们最终呢

把session给这个释放掉

就可以了

这是关于我们这个service就已经搞定了

还是比较简单的

最后呢

我们是不是来编写一个controller

那么我们还是通过访问controller

有controller了

调用service啊

这么一个流程

先把这个controller包

啊

这就应该是一个包啊

我刚才创建错了

把它删除掉啊

应该是一个package啊

在这儿对吧

来创建一个package

好

controller创建出来

创建出来之后呢

我们这包创建出来了

咱们是不是需要把这个类也创建出来

就叫hello controller

然后呢

把这个request mapping是不是来写一下

嗯

直接抄过来吧

还有我们的controller注意点

但是咱们这儿呢

用的这个是一个rest的controller

这是目前我们更加流行的

对吧

因为你加了这个rest的controller呢

相当于它这里边是不是就集成了什么呢

controller还有response body

好

这样的话

这表示我们返回的是不是json对象

而不是跳转页面了

然后再往下呢

是不是把咱们这个service还有这个方法创建出来

这些demo呢

我也不再手敲了

autoware的把service创建出来

在这个注入进来

然后呢

创建一个ruler方法

它的请求路径呢

是这个路径

在这里边直接访问我们的service的ruler方法

对吧

最后return ok

但是这现在它在return ok的话呢

就不是在跳页面了

因为我们加的是rest的controller

对吧

所以它其实是通过输出流的方式啊

向我们客户端来写写回数据

对吧

一般的是json数据

那么这个controller呢

咱们就已经编写好了

最后呢

我们作为一个supreme boot的工程啊

要创建一个什么呢

derose

要创建一个启动类

对吧

创建一个启动类

那么这个启动类呢

我们就叫derose application

好

启动类放在哪呢

咱们一般呢

是放在这些类的上一层目录

那这样的话

我们是不是就不用再去手动配置扫描了

它自动呢

就会扫描到我们当前这个启动类所在包的所有的包

当前包以及它的子包

所以你看我们这些service的controller

就都可以被我们的supreme扫描到了

那么也就是说

我们需要放在它的上一层目录

也就是

我们derose这层目录里边来创建我们的启动类

这个启动类呢

就叫derose application吧

好

作为一个启动类呢

我们需要加一个什么注解呢

就叫supreme boot application

对吧

然后呢

我们来编写一个main方法

在这里面呢

来启动我们这个工程

这些呢

就比较简单了

我直接抄过来了

应该写一个main方法

对吧

然后呢

通过supreme application.run

把它main了

我们这个工程是不是给跑起来

好

那么到这儿的话呢

咱们这个开发呢

就已经搞定了

关于我们supreme boot整合derose

所有的代码开发就已经完成了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程旨在指导开发者如何在 Spring Boot 项目中集成 Drools 规则引擎。课程内容从零开始，逐步演示了整个集成流程，包括：创建 Maven 项目并配置依赖、编写规则文件（`.drl`）、配置 Spring Boot 的 `application.yml`、编写配置类 `DroolsConfig` 来初始化 KieContainer 和 KieFileSystem、创建服务类 `RuleService` 来执行规则、以及创建一个简单的 REST 控制器来触发规则。最后，课程还简要介绍了 Drools 的可视化开发工具 WorkBench。整个过程旨在帮助开发者将 Drools 的规则能力无缝地嵌入到现代的 Spring Boot 应用中。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程引言，介绍本节将讲解 Spring Boot 整合 Drools。
*   **00:05 - 00:15**: **第一步：创建 Maven 项目并配置 `pom.xml`**。展示如何添加 Spring Boot 和 Drools 的依赖。
*   **00:15 - 00:25**: **第二步：创建 `application.yml`**。配置 Spring Boot 的端口和应用名称。
*   **00:25 - 00:35**: **第三步：创建规则文件 `helloworld.drl`**。编写一个简单的规则，用于演示规则的触发。
*   **00:35 - 00:45**: **第四步：编写配置类 `DroolsConfig`**。展示如何使用 `@Bean` 和 `@ConditionalOnMissingBean` 注解来配置 KieContainer 和 KieFileSystem。
*   **00:45 - 00:55**: **第五步：创建服务类 `RuleService`**。展示如何通过 `KieBase` 创建 `KieSession` 并调用 `fireAllRules()` 方法。
*   **00:55 - 01:05**: **第六步：创建控制器 `HelloController`**。展示如何通过 `@RestController` 和 `@RequestMapping` 暴露一个 HTTP 接口来触发规则。
*   **01:05 - 01:15**: **第七步：创建启动类 `DroolsApplication`**。展示如何使用 `@SpringBootApplication` 注解启动 Spring Boot 应用。
*   **01:15 - 01:25**: **第八步：启动服务，访问 `http://localhost:8080/hello/rule`**。演示最终效果。
*   **01:25 - 01:35**: **第八章：WorkBench 简介**。介绍 Drools 的可视化开发工具 WorkBench。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: `7.3 Spring Boot整合Drools`
    *   **操作步骤**: 第一步、第二步、第三步、第四步、第五步、第六步、第七步、第八步。
    *   **WorkBench 简介**: “WorkBench是KIE组件的元素，也称为KIE-WB，是Drools-WB与BPM-WB的结合体。它是一个可视化的规则编辑器。”

*   **代码关键内容**:

    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>
        <!-- Drools 规则引擎 -->
        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-core</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-compiler</artifactId>
            <version>7.6.0.Final</version>
        </dependency>
        ```

    *   **`application.yml` 配置**:
        ```yaml
        server:
          port: 8080
        spring:
          application:
            name: drools_springboot
        ```

    *   **`helloworld.drl` 规则文件**:
        ```drl
        package helloWorld
        rule "rule_helloworld"
        when
            eval(true)
        then
            System.out.println("规则，rule_helloworld触发...");
        end
        ```

    *   **`DroolsConfig.java` 配置类**:
        ```java
        @Configuration
        public class DroolsConfig {
            private static final String RULES_PATH = "rules/";

            @Bean
            @ConditionalOnMissingBean
            public KieFileSystem kieFileSystem() throws IOException {
                KieFileSystem kieFileSystem = kieServices.newKieFileSystem();
                ResourcePatternResolver resourcePatternResolver = new ResourcePatternResolver();
                Resource[] files = resourcePatternResolver.getResources("classpath*:/" + RULES_PATH + "/*.drl");
                for (Resource file : files) {
                    String path = RULES_PATH + file.getFilename();
                    kieFileSystem.write(ResourceFactory.newClassPathResource(path, "UTF-8"));
                }
                return kieFileSystem;
            }

            @Bean
            @ConditionalOnMissingBean
            public KieContainer kieContainer() throws IOException {
                KieContainer kieContainer = kieServices.newKieContainer(kieFileSystem());
                return kieContainer;
            }
        }
        ```

    *   **`RuleService.java` 服务类**:
        ```java
        @Service
        public class RuleService {
            @Autowired
            private KieBase kieBase;

            public void rule() {
                KieSession kieSession = kieBase.newKieSession();
                kieSession.fireAllRules();
                kieSession.dispose();
            }
        }
        ```

    *   **`HelloController.java` 控制器类**:
        ```java
        @RestController
        @RequestMapping("/hello")
        public class HelloController {
            @Autowired
            private RuleService ruleService;

            @GetMapping("/rule")
            public String hello() {
                ruleService.rule();
                return "规则已触发";
            }
        }
        ```

    *   **`DroolsApplication.java` 启动类**:
        ```java
        @SpringBootApplication
        public class DroolsApplication {
            public static void main(String[] args) {
                SpringApplication.run(DroolsApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理** (00:05-00:15)
    *   **描述**: 讲师在 IDE 中打开 `pom.xml` 文件，逐步添加 Spring Boot Web 和 Test 的 Starter 依赖，以及核心的 Drools 依赖（`drools-core` 和 `drools-compiler`）。演示了如何通过 Maven 管理项目依赖。

*   **场景二：配置文件编写** (00:15-00:25)
    *   **描述**: 讲师在 `src/main/resources` 目录下创建 `application.yml` 文件，并配置了服务器端口为 `8080` 和应用名称为 `drools_springboot`。演示了 Spring Boot 的配置文件格式。

*   **场景三：规则文件创建与编写** (00:25-00:35)
    *   **描述**: 讲师在 `resources/rules` 目录下创建 `helloworld.drl` 文件，并编写了一个简单的规则。该规则的条件是 `eval(true)`，即永远为真，其效果是打印一条消息到控制台，用于演示规则的触发。

*   **场景四：配置类开发** (00:35-00:45)
    *   **描述**: 讲师创建 `DroolsConfig.java` 配置类。通过 `@Configuration` 注解将其标记为配置类。使用 `@Bean` 和 `@ConditionalOnMissingBean` 注解来定义 `KieFileSystem` 和 `KieContainer` 的 Bean。代码中展示了如何通过 `ResourcePatternResolver` 扫描 `rules` 目录下的所有 `.drl` 文件，并将它们写入 `KieFileSystem`。

*   **场景五：服务类开发** (00:45-00:55)
    *   **描述**: 讲师创建 `RuleService.java` 服务类。使用 `@Service` 注解将其标记为 Spring 服务。通过 `@Autowired` 注解注入 `KieBase`。在 `rule()` 方法中，创建 `KieSession`，调用 `fireAllRules()` 方法触发所有规则，然后调用 `dispose()` 方法释放资源。

*   **场景六：控制器开发与接口暴露** (00:55
