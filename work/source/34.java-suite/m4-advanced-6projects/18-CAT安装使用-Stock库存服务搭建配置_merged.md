# 18-CAT安装使用-Stock库存服务搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着实现库存服务的搭建和配置

之前我们已经讲了account服务

order服务以及gateway的搭建和配置

在这里我们就快速实现一下

进入FastTalk工程服务当中

然后右键开的demo

创建一个模块

这个模块名称我们就叫做CAD

demo

stock

库存服务

点击next

注意它在这里面的话

是在CAD demo的目录下面

不要搞错了

报结构

然后点击finish

然后它生成了对应的工程结构

我们去创建对应的目录

new package

先让它导入生效

这个为什么不行呢

因为在这里面

我们要看一下CAD demo stock

对不对

要让它什么

不要忽略它

因为之前我们是在测试

这个时候创建过服务工程

对不对

我们再刷新项

neven

reimport

这个时候我们在new

就可以看到什么package

这一点大家注意一下

如果在自己工作当中

碰到这样的一个问题

还是检查一下neven

是不是把它忽略了

不要找了半天

不知道什么原因

我们去创建new package

然后com.itcast.boss

CAD demo.stock

然后我们可以看到这个项目了

我们在它的目录下面去make dir

startup

make dir

然后呢

CAD utils

创建对应的两个包

我们看到CAD utils跟startup

对不对

我们呢

就直接可以copy一下

找到account下面的CAD utils

然后呢

将它直接引入进来

注意了

这里面是没有intercept

没拦截器的

然后呢

我们再创建一个

cad demo.stock application

这个呢

就比较简单

我们copy一下就行了

在那个account下面

在stock

它同样也要提供一个接口

我们呢

将它直接引入进去

然后呢

要加上对应的注解

可以直接去account下面

把这个注解呢copy过来就行了

在这一块呢

是没有什么差异

就不重新去敲了

啊

然后在这里呢

是要开启事务部的服务

开启了Marcos服务注册

还有什么提供一个接口进行了外部的调用和访问

在这里我们提供的一个接口呢

是叫stock

名称的话

我们就改为stock

同样我们给他呢

休休眠200毫秒

证明了你在这里是有事情要做

对吧

在那个监控后台的时候

我们就可以看到他的一个耗时时间

否则的话呢

太短的话呢

就看得不明显

啊

这个呢

我们输入是一个塞不下就行了

加上对的注释

提供了

库存

那这个类的名称呢

我们也去调整一下

这样的就完成他的一个起动路口

我们的再创建一下他的一个配置配置换的

同样我们没有选中

让他选中

然后呢

粘贴

在我们的里说下面

这配置换的第一是他的开的上面的注册名称

对吧

我们就叫cat

demo

demostock

跟我们的模块名称保持一致

然后application呢

这里面是不端口

当然你写冒号也可以

我这里还是一下形成一个

一个规范

这样的我们就已经完成了

是托个服务库存服务的搭建和配置啊

往后面呢

我们就可以对整个的cat这一块呢

做一个揭露性的测试验证

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个名为 “CAT” 的微服务架构实战课程的第二部分，主要聚焦于 **工程结构设计与服务启动验证**。讲师通过 IntelliJ IDEA 开发环境，演示了如何为一个包含网关（Gateway）、订单（Order）、账户（Account）和库存（Stock）四个服务的微服务系统建立清晰的 Maven 项目结构。视频详细讲解了父工程（parent）与子模块（module）的配置、包结构的组织、以及如何为每个服务编写启动类和基础控制器。最后，视频通过查看 Nacos 控制台，验证了服务的注册情况，确保了整个微服务架构的正确性。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: **课程目标与工程结构概览**。讲师首先展示了课程大纲，明确本节目标是讲解工程结构。随后，通过 PPT 展示了整个微服务系统的架构图，包括网关、订单、账户和库存四个服务及其调用关系。
*   **00:16 - 00:45**: **父工程与子模块配置**。讲师在 IntelliJ IDEA 中打开 `cat-demo` 项目，展示了其目录结构。他重点讲解了 `pom.xml` 文件，演示了如何将 `cat-demo-gateway`、`cat-demo-order`、`cat-demo-account` 和 `cat-demo-stock` 等模块配置为父工程的子模块。
*   **00:46 - 01:20**: **子模块的独立配置**。讲师切换到 `cat-demo-stock` 模块，展示了其独立的 `pom.xml` 文件。他讲解了如何为子模块配置 `artifactId`、`version` 和 `groupId`，并强调了 `parent` 标签的引用。
*   **01:21 - 02:00**: **服务启动类与控制器编写**。讲师依次为 `cat-demo-account` 和 `cat-demo-stock` 两个服务编写了启动类 `DemoAccountApplication` 和 `CatDemoStockApplication`。他演示了如何使用 `@SpringBootApplication` 注解、`@RequestMapping` 注解和 `SpringApplication.run()` 方法来启动服务。
*   **02:01 - 02:30**: **服务启动类中的核心逻辑**。讲师在 `CatDemoStockApplication` 的 `main` 方法中，展示了如何通过 `SpringApplication.run()` 启动服务，并在控制器中添加了简单的 `Thread.sleep()` 逻辑来模拟服务的响应。
*   **02:31 - 02:50**: **启动验证与 Nacos 控制台**。讲师切换到 PPT，讲解了服务启动后的验证步骤。他强调了服务需要在 Nacos 注册中心进行注册，并展示了 Nacos 控制台的界面，说明了如何通过控制台查看服务的注册状态。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **架构图**: 展示了网关（Gateway）、订单（Order）、账户（Account）和库存（Stock）四个服务的三层调用关系。
    *   **工程结构大纲**: 列出了课程的章节，包括“目标”、“步骤”、“实现”、“服务设计”、“工程结构”、“CAT集成事项”和“启动验证”。
    *   **Nacos 控制台截图**: 展示了服务注册成功后的界面，包括服务名、IP 地址和端口等信息。
*   **代码关键内容**:
    *   **父工程 `pom.xml`**:
        ```xml
        <modules>
            <module>cat-demo-gateway</module>
            <module>cat-demo-order</module>
            <module>cat-demo-account</module>
            <module>cat-demo-stock</module>
        </modules>
        ```
    *   **子模块 `pom.xml`**:
        ```xml
        <parent>
            <artifactId>cat-demo</artifactId>
            <groupId>com.itcast.trade</groupId>
            <version>1.0.0</version>
        </parent>
        <artifactId>cat-demo-stock</artifactId>
        ```
    *   **服务启动类 `CatDemoStockApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast.bulls.cat.demo.stock")
        public class CatDemoStockApplication {
            @RequestMapping("/stock")
            public String stock() throws Exception {
                Thread.sleep(200);
                return "stock success";
            }
            public static void main(String[] args) {
                SpringApplication.run(CatDemoStockApplication.class, args);
            }
        }
        ```
    *   **服务启动类 `DemoAccountApplication.java`**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast.bulls.cat.demo.account")
        public class DemoAccountApplication {
            @RequestMapping("/account")
            public String serviceMethodInController() throws InterruptedException {
                Thread.sleep(150);
                return "account success";
            }
            public static void main(String[] args) throws Exception {
                SpringApplication.run(DemoAccountApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：工程结构设计**。讲师在 IntelliJ IDEA 中展示了 `cat-demo` 项目，通过鼠标点击和滚动，详细讲解了父工程和子模块的目录结构。他特别强调了 `pom.xml` 文件中 `<modules>` 标签的作用，以及如何为每个子模块配置独立的 `artifactId`。
*   **场景二：服务启动类编写**。讲师在 `cat-demo-stock` 模块中，通过鼠标点击和键盘操作，逐步编写了 `CatDemoStockApplication` 类。他演示了如何添加 `@SpringBootApplication` 注解、`@RequestMapping` 注解，并编写了 `main` 方法来启动服务。
*   **场景三：启动验证**。讲师切换到 PPT，展示了 Nacos 控制台的界面。他通过鼠标点击，讲解了如何在控制台中查看服务的注册状态，并强调了服务注册成功后，Nacos 控制台会显示服务的 IP 地址和端口信息。
*   **场景四：代码调试与运行**。讲师在 IntelliJ IDEA 中，通过点击 `Run` 按钮，启动了 `CatDemoStockApplication` 服务。他通过终端窗口，展示了服务启动后的日志信息，并在浏览器中访问了 `/stock` 接口，验证了服务的正常运行。

---

以上是根据视频画面进行的结构化分析，希望能帮助您更好地理解本节课程的内容。
