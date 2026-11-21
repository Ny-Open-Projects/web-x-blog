# 28-环境搭建-小结 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们对第二章内容做个回顾和小结

首先我们看一下第二章的主要学习目标

第一点我们要掌握工程代码的编解规范

这个虽然比较简单

但是是很基础重要的东西

然后要掌握工程环境的搭建

完成SpinCloud的阿里巴巴微服的集成

首先我们对工程结构规范

做了一个详细的讲解

在这里面的话

比如说应用分层我们该怎么去做

对吧

分层领域模型规范的具体约束是怎样的

各个之间的对象之间

他们有怎样的关系

所负责的职责范围是怎样

然后呢

Neven的一些版本规范

这个呢

大家要注意一下

然后是我们开发的编写规范

在这里呢

只是简要的说明一下

但是更详细的规范呢

还请大家去参考阿里巴巴加网开发手册

在这里面的话呢

写的更加详细

这个呢

建议大家仔细阅读一下

再往下面

就是整个环境的插件

这个环境呢

我们要先做好基本的准备

对不对

你的开发工具

你的相关的组件

然后呢

启动Narcos服务

我们采用了无密码登录方式

进行了一个配置和验证

然后呢

是工程的插件

工程插件呢

首先我们创建了复集工程

复集工程呢

在这里面集成了十分高的阿里巴巴的

Home的依赖配置

这个呢

也是一个核心重要的地方

大家呢

要多去理解一下

网络服务呢

它的功能主要是对请求做一个转发处理

那么再往下面呢

是我们的用户服务工程

用户服务工程呢

我们提供了一个简单的接口

便于我们的测试和验证

就是验证呢

我们这套微服务呢

是否能够正常运转

好

那通过呢

工程的启动

我们做了一个测试和验证

这个结果呢

都是符合预期的

最后我们再小结一下

在这里呢

我们一定要掌握一个良好的工程结构规范

同时呢

要去遵循像阿里巴巴这种加网开发手册

在这里面呢

它写了很多的比较有价值的这个器质

大家呢

都可以好去阅读一下

养成一个良好的编程风格

最后呢

SpringCode的阿里巴巴微服务环境呢

我们要去手动把它创建

配置好

完成了网关的搭建

用户服务

以及呢

Narcos服务注册发现

这些最基础的功能

这样呢

才能够便于我们接下来

对项目功能的一个更加深入的开发和学习

好

这个呢

就是对第二章内容的回顾和小结

那这讲呢

我们就讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“交易系统 - Day 1”课程的第2章，主题为“工程规范与环境搭建”。讲师旨在引导学习者掌握Java工程开发中的核心规范，包括分层架构、命名规范和依赖管理，并搭建一个基于Spring Cloud Alibaba和Nacos的微服务开发环境。课程通过创建两个示例工程（网关服务和用户服务）来演示如何配置和启动服务，并最终在Nacos注册中心验证服务注册成功。整个过程强调遵循《阿里巴巴Java开发手册》的规范，以养成良好的工程实践习惯。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示本章标题“第2章 工程规范与环境搭建”。
*   **00:05 - 00:15**: 讲解本章目标：掌握工程代码编写规范和环境搭建配置。
*   **00:15 - 00:30**: 详细讲解“工程结构规范”，包括分层架构（终端展示层、业务逻辑层、数据持久层）和各层的职责。
*   **00:30 - 00:45**: 讲解“编写规范”，包括类名与方法名的命名规则、接口与实现类的命名规则，并引用《阿里巴巴Java开发手册》。
*   **00:45 - 01:00**: 讲解“环境搭建”部分，首先介绍开发环境要求（JDK 1.8+、MAVEN 3.5+、NACOS 1.0.1）。
*   **01:00 - 01:15**: 讲解如何在IDEA中安装`maven helper`和`lombok`插件。
*   **01:15 - 01:30**: 讲解如何配置Nacos，修改`application.properties`文件，关闭安全认证。
*   **01:30 - 01:45**: 讲解如何启动Nacos服务，通过访问`http://127.0.0.1:8848/nacos`进入管理后台。
*   **01:45 - 02:00**: 讲解如何创建网关工程（`stock-gateway`）和用户服务工程（`stock-user`）。
*   **02:00 - 02:15**: 展示`stock-gateway`工程的`pom.xml`文件，配置Spring Cloud Gateway依赖。
*   **02:15 - 02:30**: 展示`stock-user`工程的`pom.xml`文件，配置Spring Boot Web和Nacos Discovery依赖。
*   **02:30 - 02:45**: 展示`stock-gateway`工程的`application.properties`配置文件，设置路由规则。
*   **02:45 - 03:00**: 展示`stock-user`工程的`application.properties`配置文件，设置服务端口、名称和Nacos地址。
*   **03:00 - 03:15**: 展示`stock-user`工程的`StockUserApplication`主类代码，添加`@RestController`注解并提供`/welcome`接口。
*   **03:15 - 03:30**: 讲解如何启动两个工程，并在Nacos管理后台验证服务注册情况。
*   **03:30 - 03:45**: 展示Nacos后台界面，确认`stock-gateway`和`stock-user`两个服务均已成功注册。
*   **03:45 - 04:00**: 总结本章内容，强调掌握工程规范和搭建环境的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “第2章 工程规范与环境搭建”。
    *   **目标**: 掌握工程代码编写规范；掌握工程环境搭建。
    *   **实现部分**:
        *   **3.1 工程结构规范**: 终端展示层、业务逻辑层、数据持久层。
        *   **3.2 环境搭建**: JDK 1.8+、MAVEN 3.5+、NACOS 1.0.1。
        *   **3.3 编写规范**: 类名与方法名采用驼峰命名法，接口以`I`开头，实现类以`Impl`结尾。
        *   **4. 小结**: 掌握工程结构规范，遵循《阿里巴巴Java开发手册》的规范，养成良好的编程风格；完成Spring Cloud Alibaba微服务环境搭建。

*   **代码关键内容**:
    *   **Nacos 配置文件 (`application.properties`)**:
        ```properties
        spring.security.enabled=false
        management.security.enabled=false
        security.basic.enabled=false
        nacos.security.ignore.urls=/**
        ```
    *   **Spring Cloud Gateway 路由配置**:
        ```properties
        spring.cloud.gateway.routes[0].id=stock-user
        spring.cloud.gateway.routes[0].uri=lb://stock-user
        spring.cloud.gateway.routes[0].predicates[0]=Path=/stock-user/**
        ```
    *   **StockUserApplication 主类代码**:
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
    *   **StockUserApplication 提供的接口**:
        ```java
        @RequestMapping("/welcome")
        public String welcome() {
            return "welcome bulls stock platform!";
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：工程结构规范演示** (00:15-00:30)
    *   讲师在PPT上展示分层架构图，明确区分终端展示层、业务逻辑层和数据持久层。
    *   通过文字描述各层的职责，强调数据持久层与数据库表结构的一一对应关系。

*   **场景二：编写规范演示** (00:30-00:45)
    *   讲师在PPT上列出“编写规范”的要点，包括类名和方法名的命名规则。
    *   举例说明：用户接口命名为`UserService`，实现类命名为`UserServiceImpl`。
    *   强调规范的重要性，并引导学习者参考《阿里巴巴Java开发手册》。

*   **场景三：Nacos 环境搭建演示** (01:15-01:30)
    *   讲师在PPT上展示Nacos的配置文件内容，重点讲解如何关闭安全认证。
    *   通过修改`application.properties`文件，关闭`spring.security.enabled`等安全配置项。

*   **场景四：工程创建与配置演示** (02:00-02:30)
    *   讲师在IDEA中演示创建`stock-gateway`和`stock-user`两个工程。
    *   展示`pom.xml`文件，配置`lombok`插件和Spring Cloud Alibaba依赖。
    *   展示`application.properties`文件，配置服务名称、端口和Nacos地址。

*   **场景五：服务注册与验证演示** (03:15-03:30)
    *   讲师在Nacos管理后台界面展示，确认`stock-gateway`和`stock-user`两个服务均已成功注册。
    *   通过点击“服务列表”按钮，查看服务详情，验证服务注册成功。

*   **场景六：接口测试演示** (03:30-03:45)
    *   讲师在IDEA中展示`StockUserApplication`的`/welcome`接口代码。
    *   通过访问该接口，验证服务是否正常运行。

---

以上是根据视频画面进行的结构化分析，旨在帮助学习者系统地理解课程内容和关键操作步骤。
