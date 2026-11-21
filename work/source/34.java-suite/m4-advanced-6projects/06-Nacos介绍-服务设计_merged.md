# 06-Nacos介绍-服务设计 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢,咱们就开始实现Nakos服务工程的搭建和配置

那首先呢,我们就按照整个的服务设计

先来实现了配置服务

接着的话呢,我们再实现注射服务的搭建和配置

好,那么我们回到支流股服务工程

在下面的话呢,创建一个新的模块

New Model

这里呢,就沿用Modeler点击Next

然后呢,给它一个模块名称叫Nakos Demo

接着的话点击Next

然后再用名称的话呢,做个调整

好,点击Finish

这样的话呢,Nakos Demo呢,就已经创建完成

那我们呢,再去下面创建它的子模块

这个source目录呢,就不需要

因为这个呢,是一个复制工程

我们再创建一个模块,叫配置模块

点击Next

然后呢,是Nakos Configure Demo

点击Next

名称做个调整

注意呢,它都放在Nakos Demo下面

点击Finish

好,这个呢,创建完成之后

我们就来实现它对应代码

首先呢,我们要把它的依赖加入进来,对不对

好,Nakos Demo当中呢

我们需要加入哪些依赖呢

我们从讲义当中做个Copy

这个依赖呢,是放置到复集工程当中

好,注意,不要搞错了

那么呢,放在Depensys

这里主要是有两个依赖

一个呢,是Splint Boot的

这个呢,是基础的依赖,对不对

因为我们要实现Splint Boot的相关接口了

然后呢,是Nakos服务注册发现的依赖

好,这个依赖的话呢

必须要把它加入进来

这个呢,是我们本章所要实现的核心主线

好,这个加入完成之后呢

我们就来去实现Configure的Demo配置

Configure Demo配置下面呢

也要加入对应的依赖

复集的话呢,是实现了注册和发现的,对不对

因为我们是要实现什么

配置服务的案例

所以呢,我们还要加入Nakos的配置依赖

怎么去加呢,Depensys

这里的话,给它一个增加新的依赖

叫com.alibaba.cloud

这个组件名称呢,叫Splint Cloud

Alibaba,然后是Nakos.configure

好,版本的话呢,我们可以不用设置

这个依赖呢,是什么呢

我们给它加个注册

它是呢,Nakos配置中心的依赖

也就是说,你在Nakos当中

你要实现它的一个配置统一管理

这个依赖呢,必须要把它加入进来

好,我们让它呢

去找寻对应的依赖加薄

找寻完成之后呢

我们再去Concute

看一下

我们通过Concute

鼠标移到上面呢,就能发现

它已经找到我们对应的

加薄依赖,对不对,版本是2.1.1

好,说明呢

这个已经正常加入,没有问题

那接下来的话呢,我们

我们把这个刷新一下

好,在这里面的话呢,它的

LiveWin并没有高亮显示,对不对

我们看一下其他的

比如像,在这里面的话呢

加薄是高亮显示,在这里没有高亮显示

为什么呢,因为我们这个MainWin当中的话呢

把它忽略掉了

我们也把它开启

禁止忽略

OnInno好

那么的话呢,它就能够真正识别为一个MainWin项目

我们将它呢,重新刷新一下

接下来的话呢,就高亮显示

大家碰到类似问题啊,要知道怎么去处理

那我们呢,还要给它什么

创建一个启动类

首先呢,我们创建一个包

这个包的话呢,叫cam-idcast-macros-configure.demo

好,OK

接下来我们再给它创建一个启动类

这个启动类的话呢

我们就叫macros-configure-demo-application

OK

这样呢,它已经创建完成

那创建完成之后呢

我们要给它做什么事情呢

因为我们是要验证它的一个配置的中心的使用

对不对

所以呢,你必须要给它一个属性

那通过这个属性的修改和调整呢

我们就能够验证了整个配置是否生效

我们给它定一个属性

叫stock-name

这个呢,也就是股票名称

我给它一个value-租借

这个呢,是在Split Framework下面的这个包

不要搞错了

然后呢,给它一个名称

value,要等于

给它一个变量名称

stock-name,对不对

那如果说我们没有配置这个变量名称呢

我们给它一个默认值

默认值的话呢

就比如说叫中国平安

这样的话呢

就实现了我们属性的一个配置出入

接下来的话呢

我们还要给它提供一个接口

对吧

能够让客户端进行一个调用和访问

next-conclude了

那么呢

提供一个访问接口

public-stream

然后呢

get stock-name

获取股票的名称

这里面呢

不需要传递任何闪注

我们呢

就直接进行这个配置

将股票名称从配置中心当中获取的

配置的股票名称

让他呢

直接返回出来

股票名称

然后做一个拼接

再加上对应的注释

这个呢

主要是提供一个

股票名称的访问接口

那么我们这个接口已经实现完成之后

还要再给他做上一个基本的注解核配置

使用这个配置

对吧

还有什么呢

大家别忘了

如果说我们要实现动态配置

大家想想

Marcus的一个动态配置

他发生了变化

我们怎么知道他有没有做修改和调整呢

对不对

怎么去接收呢

那么我们要给他一个新加一个注解

这个注解的话呢

是叫reflash scope

也就是说他可以支持什么

支持他的一个动态刷新

那么的话呢

Marcus如果是修改了他对应的一个配置属性

他呢

会将消息

返回给也就是说返回给服务节点

比如说我们Marcus config demo

他就会告诉给Marcus config demo

我在这里面的话

已经修改了stock name

你在这里呢

也要做相应的接收和更新

好

这个呢

就是他的一个启动内

那再往下面的话呢

我们还要给他配置一个什么

还要给他配置一个配置文件

创建一个新的文件

叫bootstrap

strap.properties

就采用这种方式来做一个配置

那么我们呢

要给他定一个无端口

server.port

给他端口

给他那个serv

serv不是service

serv

vr

port

然后端口呢

是8080

这个呢

是无端口

我们还给他一个应用名称

对不对

应用名称

应用名称的话呢

我们就叫他的模块名称

Marcus

config demo

然后呢

就指的注册发现地址

注册地址的话呢

我们也给他指定下

指向的是本地的Marcus服务

点击Marcus

discovery

ins

discovery

cloud.marcus.discovery

大家有没有发现

我这个discovery呢

他点不出来

对不对

没有对应的一个提示

那什么问题呢

那是因为的话呢

我们这个1呢

要去做一个检查

对不对

他是否正常能够导入进来

我们点击那个conclude键

然后发现这上面的话呢

并没有找到他对应的依赖

那么我们怎么办呢

我们要去检查一下

拼写是否OK的

因为的话呢

splitcloud的

阿里巴巴

他是从splitframework下面的话呢

做了一个遗址

已经完全的是独立出来

所以呢

他的groupid发生了一个改变

叫做com.alibaba.cloud

这一点呢

大家一定要注意好

import changes

接下来我们带个鼠标

conclude

可以看到已经找到了

对不对

好

我们来再继续实现他的一个配置

nucles.discovery

这个时候大家看到是不是能够找到了

对不对

discovery.serveoutjust

然后呢

是127.0.0.1

这个端口呢

就用mode端口8848

接着的话呢

是nucles的配置中心

同样在这里面的话呢

他的地址也是一样的

不过他的属性配置不一样

对不对

这个呢

是config

好

然后呢

还有什么

我们还要去拉取nucles的配置数据源名称

也就是说

我在这里面的这些配置的话呢

会放在nucles上面

那么我应该要去nucles上面读取他对应的配置

对不对

好

那么就去拉取nucles的配置数据源名称

因为他上面的话呢

有很多个配置

我要指定一个具体某一下

属性某项名称

看到的

nucles.discovery.serveoutjust

nucles.configureshared.ids

这个呢

就是一个数据ID标识

就是标识的这个配置的

唯一性

那么就是nucles.configuredemo.properties

这个话呢

他有一个后缀

后缀的话呢

我们建议呢

就是根据我们的一个需要

如果说大家配置的是yam

那么同意叫yam

如果说工程当中的话呢

在nucles里面配置的是properties

那么我们统一呢就叫properties

好

只要保持了统一规范就可以了

并没有说明确固定要用哪一种配置类型的文件

这个是nucles

好

再往下面的话呢

我们还要做一个配置

做什么配置呢

在这里我能够读到配置

对不对

但是只是说在启动的时候能够读到

如果说在启动完成之后

我要做一个动态修改

你怎么能够知道呢

这个时候

我们是不是要去做一个动态的刷新啊

对不对

所以还需要一项配置

就是配置需要动态刷新的数据

这里呢

和上面这个配置保持一样就可以了

我们将它拷贝一下

然后在这个配置属性呢

大家注意一下

属性要改成reflash

好

reflash可以支持刷新的这台ID

这样呢

我们就完成了config demo的一个配置

好

我们回到讲义当中

再来回顾一下整个的实现流程

在这里面呢

我们首先实现了复集工程

然后加入了对应的一个依赖

对不对

然后config demo工程呢

我们给它提供了一个接口

这个接口的话呢

会去读取一项配置

就是股票的名称

那这个配置的话呢

会放到Marcus当中

那Marcus的话呢

接下来在下面启动验证的时候呢

我们会去讲解如何去启动运行

并且做相应的一个配置

那么在这里面配置完成之后呢

大家一定要注意

我们要加上什么refresh scope的一个注解

如果说动态修改了Marcus的配置

发现没有变化

那要检查是否加上了这个对应的注解

然后呢

加了对应注解之后呢

还需要做一项配置

就是说要去指向了需要刷新的配置中心文件ID

那比如说我们是读取了这个配置

对不对

那你就要把这个配置文件名称呢

也要配置上去

让它能够支持动态的一个刷新

这里面需要指定

Marcus的配置DataID

注意了

我们需要加上完整的扩展名

对不对

这个呢可能大家有点不习惯

一般的话呢

我们只要一个文件名称对就行了

对不对

为什么还有一个扩展名

因为在这里面的话呢

它是通过这两个呢

组合在一起形成一个完整的标识

然后呢

需要加上refreshDataID

这个呢

它是可以支持多个配置文件的

如果是我们有很多项配置

都需要去支持动态刷新的

就通过逗号分割就可以了

这一点呢

大家要注意一下

我们一定要采用woodstrap

作为我们的文件基础性配置文件

因为它比ApplicationProperties的

启动优先级要高

远程配置要优先读取的

它是远程配置呢

它要优先先去读取你本地的一个信息

对不对

你读取到本地信息之后

你才知道怎么去连接到

那个Marcus配置中心上面去

大家明不明白

对不对

好

这个呢

就是我们的基础的一个配置文件

然后呢

在上面的话呢

可以再配置我们的一些

页面

业务属性也好

配置我们的其他的一些信息都可以

好

这些呢

就是我们Marcus的一个配置中心的案例搭建

好

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 Spring Cloud Alibaba Nacos 服务注册与配置中心的实战教学。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个基于 Nacos 的配置服务（`nacos-config-demo`），并讲解了其核心工程结构、依赖配置、配置文件（`bootstrap.properties`）以及如何通过 `@RefreshScope` 注解实现配置的动态刷新。整个过程旨在帮助开发者理解 Nacos 在微服务架构中的应用，特别是配置管理功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示了一个包含“客户”、“Nacos 注册中心”和“股票价格服务”的架构图，用于说明 Nacos 在微服务架构中的角色。
*   **00:05 - 00:15**: 讲师切换到项目结构视图，展示 `nacos-demo` 项目下的两个核心子模块：`nacos-config-demo`（配置服务）和 `nacos-discovery-demo`（服务发现服务），并介绍了本节将重点讲解 `nacos-config-demo`。
*   **00:15 - 00:25**: 讲师演示了如何在 IntelliJ IDEA 中创建一个新模块，并选择 Spring Initializr 作为项目模板，为后续开发做准备。
*   **00:25 - 00:35**: 讲师在 `pom.xml` 文件中添加了 Nacos 服务注册与发现的依赖（`spring-cloud-starter-alibaba-nacos-discovery`）。
*   **00:35 - 00:45**: 讲师展示了 `nacos-config-demo` 的 `pom.xml` 文件，其中定义了父项目为 `spring-cloud-alibaba`，并添加了 Nacos 配置中心的依赖（`spring-cloud-starter-alibaba-nacos-config`）。
*   **00:45 - 00:55**: 讲师在 `bootstrap.properties` 文件中配置了 Nacos 服务注册中心和配置中心的地址（`127.0.0.1:8848`），并设置了应用名称。
*   **00:55 - 01:05**: 讲师在 `NacosConfigDemoApplication` 类中添加了 `@RestController` 和 `@RefreshScope` 注解，并定义了一个 `@Value` 注解的属性 `stockName`，用于从 Nacos 配置中心获取股票名称。
*   **01:05 - 01:15**: 讲师在 `bootstrap.properties` 文件中添加了 `spring.cloud.nacos.config.server-addr` 配置，用于指定 Nacos 配置中心的地址。
*   **01:15 - 01:25**: 讲师在 `NacosConfigDemoApplication` 类中添加了 `@SpringBootApplication` 注解，并在 `main` 方法中调用 `SpringApplication.run` 启动应用。
*   **01:25 - 01:35**: 讲师在 `NacosConfigDemoApplication` 类中添加了 `@RequestMapping("/getStock")` 注解，定义了一个获取股票名称的 REST 接口。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **架构图**: 展示了“客户”通过 HTTP 请求调用“股票价格服务”，而“股票价格服务”通过“Nacos 注册中心”进行服务发现和配置管理。
    *   **工程结构图**: 展示了 `nacos-demo` 项目下的 `nacos-config-demo` 和 `nacos-discovery-demo` 两个子模块的目录结构。
*   **代码**:
    *   **`pom.xml` (nacos-config-demo)**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-config</artifactId>
        </dependency>
        ```
    *   **`pom.xml` (nacos-config-demo)**:
        ```xml
        <parent>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba</artifactId>
            <version>2.2.3.RELEASE</version>
        </parent>
        ```
    *   **`bootstrap.properties`**:
        ```properties
        server.port=8080
        spring.application.name=nacos-config-demo
        spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
        spring.cloud.nacos.config.server-addr=127.0.0.1:8848
        ```
    *   **`NacosConfigDemoApplication.java`**:
        ```java
        @SpringBootApplication
        @RestController
        @RefreshScope
        public class NacosConfigDemoApplication {
            @Value(value = "${stockName:中国平安}")
            private String stockName;

            public String getStock() {
                return "股票名称：" + stockName;
            }

            public static void main(String[] args) {
                SpringApplication.run(NacosConfigDemoApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (00:05 - 00:15)
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `nacos-demo` 项目，通过项目结构视图展示了 `nacos-config-demo` 和 `nacos-discovery-demo` 两个模块。他强调了 `nacos-config-demo` 是本节的重点，用于演示配置中心功能。
*   **场景二：添加依赖** (00:25 - 00:35)
    *   **描述**: 讲师在 `nacos-config-demo` 的 `pom.xml` 文件中，通过鼠标选中并添加了 `spring-cloud-starter-alibaba-nacos-discovery` 依赖，用于服务注册与发现。
*   **场景三：配置文件设置** (00:45 - 00:55)
    *   **描述**: 讲师在 `bootstrap.properties` 文件中，通过鼠标选中并添加了 `spring.cloud.nacos.discovery.server-addr` 和 `spring.cloud.nacos.config.server-addr` 配置项，用于指定 Nacos 服务注册中心和配置中心的地址。
*   **场景四：代码编写与注解** (00:55 - 01:15)
    *   **描述**: 讲师在 `NacosConfigDemoApplication.java` 文件中，通过鼠标选中并添加了 `@RestController`、`@RefreshScope` 和 `@Value` 注解。他解释了 `@RefreshScope` 注解的作用是让配置在运行时动态刷新，而 `@Value` 注解用于从配置文件中注入值。
*   **场景五：启动应用** (01:15 - 01:25)
    *   **描述**: 讲师在 `NacosConfigDemoApplication.java` 文件中，通过鼠标选中并添加了 `@SpringBootApplication` 注解，并在 `main` 方法中调用 `SpringApplication.run` 启动应用。
*   **场景六：接口定义** (01:25 - 01:35)
    *   **描述**: 讲师在 `NacosConfigDemoApplication.java` 文件中，通过鼠标选中并添加了 `@RequestMapping("/getStock")` 注解，定义了一个获取股票名称的 REST 接口。他解释了该接口可以通过 HTTP 请求获取股票名称。
