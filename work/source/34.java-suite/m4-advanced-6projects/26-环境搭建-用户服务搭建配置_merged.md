# 26-环境搭建-用户服务搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着创建用户服务工程

之前呢,网关服务工程已经创建完成,对不对

那么呢,我们就要开始实现用户服务工程

由网关进行一个调用

接下来呢,就可以做一个测试和验证

那我们首先进入到服务工程当中

再创建一个模块,New Model

在这里呢,按照Model模板点击Next

给它一个模块名称,叫BuzzTalk User

就是我们的用户服务,点击Next

然后呢,Finish

好,可以看到,模块呢,就已经创建完成

创建完成之后呢,首先,同样我们先去增加它对应的依赖

那我们呢,将这个依赖呢,直接Copy过来

Copy过来之后呢,让它导入生效

我们看一下,用户服务里面主要有什么依赖呢

有两个依赖,一个呢,是属于Boot,对不对

因为它作为什么,Boot,微服务呢

去启动,然后呢,是Narcos服务的注射发现依赖

这一块呢,也要把它加入进去

好,加入完成之后呢,我们就来创建它对应的包结构

以及呢,它的启动内,创建Package

然后呢,com.itcast.buzzTalk.user

这里面呢,Startup,好

再创建启动内,New Class

好,启动内名称呢,就叫Stock User

Application

最好呢,跟我们的模块名称的后缀保持一致

好,Stock User Application,点击OK

我们呢,再创建它的启动方法入口

psvm,Tab键,然后自动补全

通过Slim Boot做一个启动

然后呢,run Stock User Application in Class

然后呢,Arc三处也传递进去

在上面呢,别忘记,加上对应的注解

一个呢,是Slim Boot Application,对不对

另外一个呢,是什么,开启Boot的注册发现

好,我们还有什么,再加上它的一个Baud扫描

这个呢,养成一个习惯

然后呢,那个Based Package

好,这个,我们去指定了,基准目录,com.itcast

开发环境当中呢,建议大家不要按照这种默认方式去做这个Baud扫描

一定要指定一个Baud路径扫描

这样呢,我们就比较明确一点,好吧

那接下来呢,我们还在提供一个介绍呢,就是呢,我们的Baud路径扫描

这个介绍的话呢,就是用于Gateway能够去做一个调用和验证测试

那么,还要再加上一个注解,是Vest Controller

我们呢,去定义一个方法,Pump Public,然后呢,Stream Welcome

在这里呢,我们就简单的转回一个打印语句

这个语句呢,我们就打印一下,叫Welcome Stock Fast Talk

Brand4,欢迎来到,是Niuku服务平台

那么呢,我们给它一个请求路径

请求路径呢,跟方法名保持一致

加上对应的注释

提供呢,访问接口

测试访问接口

好,这样呢,用户服务的它的取通类以及接口呢,就已经实现完成

那么呢,我们就要开始实现它的配置文件,New

File,然后呢,Application,点Properties

怎么知道有没有拼选错误呢,只要看到这个绿色的小图标,就说明你是拼选正确的

那么接下来呢,我们就要去配置它的一些端口

以及Nuqus的无信心,Spin,Servo,点Port

这个端口呢,我们就叫10681

然后Nuqus的信心,Spin点Cloud,点Nuqus

127

点0,点0,点1,端口8848

然后呢,我们的服务名称,对不对

Cloud,Nuqus,点Service

我们在这里写个编量

然后这个呢,我们还忘记写了

Spin Application Name,叫stock

Cock,User

那么在上面注册的名称呢,我们就叫

Spin,点Application,Name

到时候呢,如果是要修改服务名称,只要修改这一个地方就可以了

好,接下来的话呢,我们还要不要做其他配置呢

我们在这里的话呢,就已经完成了它的一个基本配置

这个的话呢,可以不需要

因为的话呢,如果是你要开启监控的话

比如说我要访问它的一个Aktuator

它的监控,就需要呢,开启暴露对应的接口和地址

我们这里呢,只是用于SpinCloud的阿里巴巴的微服务集成测试

所以这一块呢,可以不需要

当然,加上去也是可以的

好,那接下来呢,我们再看一下

整体功能都已经实现了,对不对

我们可以启动来验证一下这个用户服务是否正常了

右键,run运行

如果启动成功之后呢,同样在Nakos上面可以看到这样一个注册节点

好,它已经启动完成了,对不对

10681的端口

那么我们去Nakos上面刷新看一下

哎,这个时候是不是可以看到

User服务呢,就已经成功注册进来

这个名称的话呢,就是跟我们这里所编写的服务名称呢

是一样的,Stock User

好,那么我们呢,再访问一下这个接口是不是正常了,对不对

127.0.1 10681

然后呢,Welcome

好,可以看到,这个用户的请求接口呢,也是OK的

那么用户服务呢,我们就已经搭建,并且配置完成

这一讲呢,咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Cloud 的微服务架构教程，主要演示如何创建并配置一个名为 `stock-user` 的用户服务工程。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目的结构、依赖配置、主启动类的编写以及核心配置文件 `application.properties` 的设置。最终目标是让该服务能够成功启动，并在服务注册与发现中心（Nacos）中被正确注册，为后续的网关路由（`stock-gateway`）提供服务支持。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 开场，展示课程大纲，明确本节内容为“创建用户服务工程”。
*   **00:00:05 - 00:00:15**: 展示 `stock-user` 项目的目录结构，重点介绍 `src/main/java` 和 `src/main/resources` 文件夹。
*   **00:00:15 - 00:00:30**: 编辑 `pom.xml` 文件，添加 `spring-boot-starter-web` 和 `spring-cloud-starter-alibaba-nacos-discovery` 依赖。
*   **00:00:30 - 00:00:45**: 编写 `StockUserApplication` 主类，使用 `@SpringBootApplication`、`@EnableDiscoveryClient` 和 `@RestController` 注解。
*   **00:00:45 - 00:01:00**: 编写 `application.properties` 配置文件，设置服务端口 `server.port=10681` 和 Nacos 注册地址 `spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848`。
*   **00:01:00 - 00:01:15**: 在 `application.properties` 中配置 `spring.application.name=stock-user`。
*   **00:01:15 - 00:01:30**: 在 `application.properties` 中配置 `management.endpoints.web.exposure.include=*` 以暴露健康检查端点。
*   **00:01:30 - 00:01:45**: 在 `StockUserApplication` 主类中添加 `@RequestMapping("/welcome")` 注解，并编写对应的 `welcome()` 方法。
*   **00:01:45 - 00:02:00**: 启动 `stock-user` 服务，观察控制台日志，确认服务成功启动并注册到 Nacos。
*   **00:02:00 - 00:02:15**: 登录 Nacos 控制台，验证 `stock-user` 服务已成功注册。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   课程大纲：`3.6 项目技术特色`, `3.7 技术解决方案`, `3.8 如何技术选型`, `3.9 技术选型案例`, `4. 小结`。
    *   第二章标题：`第2章 工程规范与环境搭建`。
    *   本节目标：`1. 目标`, `2. 步骤`, `3. 实现`, `4. 小结`。
    *   本节小结：`StockUserApplication运行主类代码`，并展示 `@RequestMapping("/welcome")` 的代码片段。

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>
        ```
    *   **`StockUserApplication.java` 主类**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @RestController
        public class StockUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockUserApplication.class, args);
            }
        }
        ```
    *   **`application.properties` 配置**:
        ```properties
        server.port=10681
        spring.application.name=stock-user
        spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848
        management.endpoints.web.exposure.include=*
        ```
    *   **`welcome()` 接口方法**:
        ```java
        @RequestMapping("/welcome")
        public String welcome() {
            return "welcome bulls stock platform!";
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目创建与结构展示** (00:00:05)
    *   讲师在 IDEA 中打开并展示 `stock-user` 项目，重点指出 `src/main/java` 和 `src/main/resources` 目录，为后续代码编写做准备。

*   **场景二：依赖管理** (00:00:15)
    *   讲师在 `pom.xml` 中添加了两个关键依赖：`spring-boot-starter-web` 用于构建 Web 服务，`spring-cloud-starter-alibaba-nacos-discovery` 用于服务注册与发现。

*   **场景三：主类编写** (00:00:30)
    *   讲师在 `StockUserApplication.java` 中编写了主类，使用 `@SpringBootApplication` 注解启用自动配置，`@EnableDiscoveryClient` 注解启用服务发现功能，`@RestController` 注解声明这是一个 RESTful 控制器。

*   **场景四：配置文件编写** (00:00:45)
    *   讲师在 `application.properties` 中配置了服务端口 `server.port=10681`，服务名称 `spring.application.name=stock-user`，以及 Nacos 服务注册地址 `spring.cloud.nacos.discovery.server-addr=127.0.0.1:8848`。

*   **场景五：接口开发** (00:01:30)
    *   讲师在主类中添加了 `@RequestMapping("/welcome")` 注解，并编写了 `welcome()` 方法，用于提供一个简单的欢迎接口。

*   **场景六：服务启动与验证** (00:01:45)
    *   讲师点击运行按钮，启动 `stock-user` 服务。控制台显示服务成功启动并注册到 Nacos。
    *   讲师随后打开 Nacos 控制台，成功看到 `stock-user` 服务已注册，验证了服务发现功能正常工作。

---
