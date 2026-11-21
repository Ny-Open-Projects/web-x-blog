# 12-用户上传与下载功能-Ceph自动化封装 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着的话呢,咱们开始学习和讲解save封装以及呢,自动化装配的实现

首先呢,咱们去新建一个自定义服务管理工程,叫stockstart

我们呢,创建对应的服务工程模块

new model

点击next

这名称呢,我们就以bios开头

stockstart

专门用于实现了自定义的封装组件

点击next

将名称调整一下,点击finish

好

模块呢,就已经创建完成

接下来呢,咱们再创建一个子模块

右键

new,选择一个新的模块,我们点击next

这个名称呢,我们就叫biosstockstart

然后是专门用于

使用的

save的封装

点击next

将名称调整一下,点击finish

创建完成之后呢

咱们再将它的依赖呢

添加进来

在讲义当中,将对应的依赖呢

copy进去

这个呢

放在start save form文件下面

我们看一下,它具体有哪些依赖呢

咱们可以看到,在这里呢

主要有save相关的依赖组件

第一个呢是radar

这个之前呢咱们做了讲解

然后呢是fs

这个是对fs,savefs的一个依赖组件

下面的话呢就是swift

也是前面章节呢

咱们对swift API进行的封装

这个呢所需要用到的组件依赖

那咱们把这些依赖添加完成之后呢

就可以开始对代码做个封装实现

我们创建对应的包

package

名称叫cardpack

这个呢是它的包路径

然后呢

咱们再去创建它的封装接口

这个选择class

那么我们之前呢

是对save做了一个封装调用

对不对

我们可以在savedemo下面呢

将swift operator先将它copy过来

名称的话呢

我们做个调整叫做save

swift operator

好

点击ok

大家注意一下

通过splint boot start的方式呢

是如何进行封装

跟我们之前的这种实现方式呢

有哪些差别

那么我们就来具体做个调整和修改

在这里呢

我们就不需要compent这个注解

因为它通过start呢

会自动去扫描和加载

要做到自动化封装呢

这个参数就不能写实了

对不对

这个用户名称呢

我们叫做

从配置文件当中去读取

所以呢

我们不需要给它配置一个固定的值

内幕的话呢

这个password也是一样

在这里面的话呢

都给它默认为空

下面这些属性呢

咱们全部调整一下

将它这个值呢

全部去除

这个的话呢

默认就是no

我们可以不需要

好

调整完成之后呢

初始化连接配置呢

咱们也做一个调整

修改在这里呢

就不采用这种方式了

我们呢

将它呢

封装一下

通过了一个方法去做一个调用

创建一个init的方法

然后呢

我们外层加个check cache

在这里呢

咱们可以看到没有L方法

为什么呢

因为long book这个插件呢

没有正常生效

咱们在这里只添加了save

那么呢

我们换一种方式

就直接呢

使用static的方式呢

去定义一个log对象

好

那么咱们呢

再回过头来继续编写初始化连接代码

这一块代码呢

跟咱们之前save操作演示的代码呢

基本类似

咱们呢

可以去复用过来

copy到咱们刚才的代码中来

咱们呢

再添加一个日志

这样的话呢

咱们就知道初始化的时候呢

它到底有没有创建

对不对

很突然呢

这个是提示呢

它已经是存在

那我们将来呢

将错误信息呢

打印出来

这里呢

我们就不打印出整个异常站信息

只将它的主要错误提示呢

打印出来

save

连接初始化异常

好

这个呢

是不用再修改

咱们呢

再去重载它的方法

让它能够支持呢

文件流的形式

这里呢

就是直接输出

imput stream

直接输出形式

它们就不需要file

直接呢

去传递imput stream

下载接口

咱们也做个重载

我们也增加

流逝的下载

将它对象呢

改成imput stream

这里面呢

就不需要outpass

那么呢

我们就来

将它对象呢

做个返回

这个呢

就不需要

就直接呢

将这个方法呢

做一下

作为呢

imput stream的流逝呢

将对象信息呢

返回出去

这个呢是

下载

文件

转换为

文件流的

形式

那有了上传和下载呢

咱们是不是应该还要提供一个什么

删除指定文件的

对象接口

这样呢

在咱们save集群当中就不会存在过多的垃圾文件

我们先先开一个

出来这个

0出生

出生

他就是

出生

出生

出生

我们先把这个

删除的文件

删除

主要的话呢

就是

我们会在这个

可以打开来

点击

这个

然后点击

删除

我们就会看到

出生

出生

出生

出生

出生

出生

出生

出生

出生

出生

出生

出生

然后我们要将外围异常的捕获一下

通过log将异常信息

输出

删除文件

失败

最后返回一个错误

处理失败的标识

这个就是删除指定的文件对象

这样咱们就完成了Swift API的封装

咱们再回到讲义当中

做个回顾

在这里封装接口

我们将它纳入Split容器管理

也就是为单立的方式

构造函数

它会初始化SWIFT认证连接信息

也就在这里面

咱们通过一个引力的方法

对不对

所以在这里

我们还把引力的方法

放在构造方法当中

让它进行一个调用

然后我们要将这些属性注入进来

这个就不是默认的构造方法

我们要将它的参数调入进来

Uzlim

Password

认证地址

默认的容器名称

给它输导成员变量当中

这些就是主要的连接配置信息

最后一个就是

before container

默认的容器名称

构造函数

它就会初始化SWIFT认证连接等相关信息

再将Account与Container设为成员变量

便于复用去减少它们的开销

咱们可以看到

对不对

通过单立的形式

在这里面

它只会初始化一个操作对象

初始化会默认一个容器名称

一般每个服务都会设置一个容器名称

比如说用户服务

对应的会有用户服务名称

对不对

那么订单服务

会有订单服务的容器名称

如果业务部分比较庞大的

可以每个业务模块去设置一个容器

就像咱们刚才所说的

针对于不同业务

去定义不同的容器名称

SWIFT API已经做到最完善的封装

我们内部使用起来比较简单

不要封装上传和下载的接口

那么如果大家还想去扩展

在这里面

还有很多的一些API接口

可以再去做具体的研究和学习

在这里

它存在了很多方法

接口来讲也是比较丰富

那么我们接着的话

就来实现SWIFT自动化的装备

我们来看一下

它这一块具体是如何实现的

在这里

我们要创建一个AutoSWIFT

SWIFT的Configure

动画

配置类

我们来创建一下

这个配置类当中

有对应的属性连接配置信息

咱们可以看到

我们可以先将代码拷贝过来

咱们可以看到

在这里定义了SWIFT的连接配置属性

在这一块

报错

我们要将对应的依赖加入进去

Depensys加入自动化配置的依赖

SWIFT

自定义启动器的依赖组件

Group ID是在SWIFT Framework下面

Hardifax ID是SWIFT-Auto-Configure

好

我们让它导入生效

Ctrl可以看到这个依赖已经加入成功

我们再回到刚才的配置列当中

好

这一块就没有报错

这个是什么意思呢

它会将配置文件当中定义的这些属性

注入到咱们的成员变量当中

可以看到

对不对

那么它在这里会将SWIFT Operator

作为一个接口

加入到咱们的SWIFT容器当中

这个是它的一个自动化配置

在这里提示错误

因为导入的包

我们可以看到

它的提示错误

是没有找到对应的方法值

那么咱们要将这个包重新导入下

要引入SWIFT Framework下面的

好

这样的话就没有报错

那么我们就已经完成了自动化的Configuration的配置

接着的话

我们还要去实现Meta配置文件

这个的话是基于SPI机制实现的

那么怎么去做呢

我们在这里去创建一个目录

目录名称是叫Meta-inf

点击OK

下面我们给它创建一个文件

这个文件叫Spring.Factories

大家注意

正是基于SPI机制

Spring Boot Start的主线

才能够自动化装配和扫描

加入对应的配置

咱们可以看到在这里面

如果其他主线引入了咱们制定的配置的话

咱们可以看到在这里面如果其他主线引入了咱们制定的配置的话

咱们可以看到在这里面如果其他主线引入了咱们制定的配置的话

就会有一个Start Save依赖

但是咱们没有去配置对应的主线

就算在这里面配置到Configuration

但是咱们没有指定它的包扫描路径

那么它怎么会去加载它的配置呢

其实就是通过Spring.Factories这个文件进行了扫描

也是基于SPI机制做的实现

这个就是SPI的处理实现机制

咱们在这里接下去定义它的配置内的完整路径

这个是在Spring.Framework下面

点Boot

Auto Config

下面有一个Enable Auto Configuration

这个如果是有多个咱们可以进行半行处理

然后再将它的包路径执行权

将它的Copy过来

Ctrl可以看到这个路径没有问题

那么定义完成Spring.Factories自动注入文件之后

咱们还要去定义工程配置文件

在这里我们是有

很多的属性需要注入进来

在这里我们是有Safe的连接配置属性

需要从配置文件当中读取并注入进去

那么咱们就要在用户的Resource下面

将配置文件的属性加入进去

不是在组件的Resource目录下面

这个要注意

因为每个服务它都有自己的Safe连接属性配置

咱们在User的Resource目录下面找到配置文件

在最末尾咱们要加入Safe的连接配置

这个咱们就从讲解当中直接扩展进来

它的层级的话就是Safe开头

下面的话就是定义的具体的连接属性

跟咱们在这里面的属性定义是一样的

可以看到对不对

它的完整的话就是Safe开头

后面就是具体的属性名称

好

在这里地址我们要配置正确

还有你的默认的容器名称

用户名和密码

好

这样咱们就完成了Safe的封装

以及它的自动化装配实现

大家回顾一下

我们要注意AutoSafeSwiftConfig

这个自动化装配类的实现

ConditionOnProperty

它是根据SafeOSUI的L的属性

来决定是否要加载这个配置

它的作用就是说

如果咱们在工程配置当中

没有找到SafeOSUIL的属性定义

那么它就不会激活Safe的配置

这样的话就可以便于咱们的工程配置

让我们灵活的管理

对不对

好

这一讲就是对Safe的封装

以及自动化装配的实现

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析报告。

---

### 1) 视频摘要

本视频课程聚焦于如何在 Spring Boot 项目中封装和自动化集成 Ceph Swift 对象存储服务。讲师通过一个名为 `bulls-stock-starter-ceph` 的 Starter 工程，演示了如何创建一个可复用的自动化配置模块。该模块的核心是 `AutoCephSwiftConfiguration` 类，它通过 `@ConditionalOnProperty` 注解根据配置属性（如 `ceph.authUrl`）决定是否加载，从而实现非侵入式的功能启用。课程详细展示了如何在 `pom.xml` 中引入 Ceph 的依赖（如 `rados` 和 `libcephfs`），如何在 `META-INF/spring.factories` 文件中声明自动配置类，以及如何在业务代码中使用 `CephSwiftOperator` 对象进行文件的上传、下载和删除操作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**：课程开场，展示项目结构和当前章节 `3.2 Ceph封装与自动化装配`。
*   **00:00:15 - 00:00:40**：介绍新建 `stock-starter` 工程用于封装自动化组件，并展示其目录结构，包括 `src/main/java` 下的 `AutoCephSwiftConfiguration` 和 `CephSwiftOperator` 类，以及 `resources/META-INF/spring.factories` 文件。
*   **00:00:40 - 00:01:00**：展示 `pom.xml` 文件，重点讲解 `ceph` 相关的依赖，包括 `rados` 和 `libcephfs`。
*   **00:01:00 - 00:01:30**：进入 `CephSwiftOperator` 类的代码实现，展示其内部的私有属性，如 `authUrl`、`defaultContainerName`、`account` 和 `container`。
*   **00:01:30 - 00:02:00**：演示 `CephSwiftOperator` 的初始化方法 `init()`，其中包含设置认证信息和创建容器的逻辑。
*   **00:02:00 - 00:02:30**：展示 `retrieveObject` 方法，用于从 Ceph 容器中下载文件。
*   **00:02:30 - 00:03:00**：展示 `deleteObject` 方法，用于删除 Ceph 容器中的文件。
*   **00:03:00 - 00:03:30**：回到 `AutoCephSwiftConfiguration` 类，展示其通过 `@Value` 注解注入配置属性，并通过 `@Bean` 注解创建 `CephSwiftOperator` 实例。
*   **00:03:30 - 00:04:00**：讲解 `@ConditionalOnProperty` 注解的作用，说明其根据 `ceph.authUrl` 属性决定是否加载自动化配置，从而实现灵活的条件加载。
*   **00:04:00 - 00:04:30**：展示 `META-INF/spring.factories` 文件的内容，确认其声明了 `AutoCephSwiftConfiguration` 类。
*   **00:04:30 - 00:05:00**：总结本章节内容，强调自动化配置的核心思想和实现方式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **章节标题**：`3.2 Ceph封装与自动化装配`。
    *   **关键概念**：`ConditionalOnProperty` 注解用于条件加载。
    *   **核心思想**：通过 `spring.factories` 文件和 `@Configuration` 注解实现自动化装配。

*   **代码关键内容**：

    *   **`pom.xml` 依赖**：
        ```xml
        <dependency>
            <groupId>com.ceph</groupId>
            <artifactId>rados</artifactId>
            <version>0.6.0</version>
        </dependency>
        <dependency>
            <groupId>com.ceph</groupId>
            <artifactId>libcephfs</artifactId>
            <version>0.80.5</version>
        </dependency>
        ```

    *   **`CephSwiftOperator.java` 类**：
        ```java
        private String authUrl = "http://10.10.20.11:7480/auth/1.0";
        private String defaultContainerName = "user_datainfo";
        private Account account = null;
        private Container container;

        public void init() {
            // 设置认证信息
            config.setAuthenticationMethod(AuthenticationMethod.BASIC);
            account = new AccountFactory(config).createAccount();
            // 获取容器对象
            Container newContainer = account.getContainer(defaultContainerName);
            if (!newContainer.exists()) {
                newContainer.create();
            } else {
                container = newContainer;
            }
        }

        public InputStream retrieveObject(String objectName) {
            StoredObject object = container.getObject(objectName);
            return object.downloadObjectsAsInputStream();
        }

        public boolean deleteObject(String objectName) {
            StoredObject object = container.getObject(objectName);
            object.delete();
            return object.exists();
        }
        ```

    *   **`AutoCephSwiftConfiguration.java` 类**：
        ```java
        @Configuration
        @EnableAutoConfiguration
        @ConditionalOnProperty(name = "ceph.authUrl")
        public class AutoCephSwiftConfiguration {

            @Value("${ceph.username}")
            private String username;

            @Value("${ceph.password}")
            private String password;

            @Value("${ceph.authUrl}")
            private String authUrl;

            @Value("${ceph.defaultContainerName}")
            private String defaultContainerName;

            @Bean
            public CephSwiftOperator cephSwiftOperator() {
                return new CephSwiftOperator(username, password, authUrl, defaultContainerName);
            }
        }
        ```

    *   **`META-INF/spring.factories` 文件内容**：
        ```
        org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
        com.icast.bulls.stock.starter.ceph.AutoCephSwiftConfiguration
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:00:00-00:00:15)**：
    讲师首先在 Typora 文档中展示了课程的目录结构，明确指出当前讲解的是 `3.2 Ceph封装与自动化装配` 章节。随后，他切换到 IntelliJ IDEA，展示了 `stock-starter` 工程的目录结构，重点突出了 `src/main/java` 下的两个核心类 `AutoCephSwiftConfiguration` 和 `CephSwiftOperator`，以及 `resources/META-INF/spring.factories` 文件，为后续的自动化配置埋下伏笔。

*   **场景二：依赖管理演示 (00:00:40-00:01:00)**：
    讲师在 IDEA 中打开 `pom.xml` 文件，通过鼠标悬停和高亮显示，详细讲解了 `rados` 和 `libcephfs` 两个 Ceph 相关依赖的配置。他强调了这些依赖是后续功能实现的基础，必须正确引入。

*   **场景三：核心类代码实现 (00:01:30-00:02:30)**：
    讲师在 `CephSwiftOperator.java` 文件中，逐行讲解了类的私有属性和方法。他首先展示了 `init()` 方法，演示了如何通过 `AccountFactory` 创建 `Account` 对象，并根据容器是否存在来决定是创建新容器还是获取现有容器。接着，他演示了 `retrieveObject` 方法，说明了如何从容器中获取对象并下载为输入流，以及 `deleteObject` 方法，展示了如何删除对象并返回布尔值。

*   **场景四：自动化配置类 (00:03:00-00:04:00)**：
    讲师切换到 `AutoCephSwiftConfiguration.java` 文件，重点讲解了 `@ConditionalOnProperty` 注解。他解释了该注解的作用是根据 `ceph.authUrl` 属性的值来决定是否加载此配置类。如果该属性未设置，即使项目中引用了 `bulls-stock-starter-ceph`，Spring Boot 启动时也不会报错，从而实现了灵活的条件加载。他同时展示了 `@Value` 注解如何注入配置属性，并通过 `@Bean` 注解创建 `CephSwiftOperator` 实例。

*   **场景五：配置文件关联 (00:04:30-00:05:00)**：
    讲师在 IDEA 中打开了 `META-INF/spring.factories` 文件，展示了其内容。他解释了该文件是 Spring Boot 自动配置机制的关键，它声明了 `AutoCephSwiftConfiguration` 类，使得 Spring Boot 在启动时能够自动发现并加载此配置类，从而完成整个自动化装配过程。最后，他总结了本章节
