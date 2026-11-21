# 15-分布式链路追踪（入门案例_导入maven工 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢咱们继续来看我们这个分布式链路追踪的入门案例

刚才呢我们是把Zipkin这个服务是不是已经跑起来了

并且呢我们通过这个页面呢是不是能够访问到的

能访问到这个页面

这就说明服务启动没问题

好那接下来呢我们就需要来导入这个Maven工程

这是为了演示什么呢我们这个链路追踪效果对吧

所以我们在这呢提供了这么四个Maven工程

这个四个工程啊

它其实是一个副工程

然后下面套了这么三个子工程

这个副工程呢叫做Sluice-Parent

它是一个副工程统一管理依赖的

同时呢聚合下面这三个子工程

然后Client1呢这就是链路追踪客户端工程对吧

我们下面这三个呢其实都是客户端工程

说白了就是都是产生链路数据提供给Zipkin来展示的对吧

所以这就是链路追踪的客户端工程

然后呢在Client1里面呢

它会通过REST呢来调用Client2

对吧

然后在Client2里面呢

再通过REST调用Client3

然后在Client3里面呢

是不是就直接返回就可以了对吧

它就不用再去远程调用了

所以说呢应该是Client1调Client2

然后Client2呢调Client3

是这么一个调用关系

那么我们这个代码呢

其实已经为大家提供好了

就是这个Sluice-Parent

大家呢直接把这个代码呢

把它导到你的开发工具当中来就可以了

我这个呢提前已经导好了

咱们来看一下

挑着重要的代码呢

来大概读一下就可以了

那这个代码呢

我们就不再去手写了

你看这是我们这个Parent的工程

对吧

然后这里边呢

重点我们来看的是什么呢

这两个坐标

一个是Spring Cloud的Starter Sluice

对吧

这就是Sluice它的这个支持包

核心架包

然后下面这个呢

这就是Sluice跟Zipkin整合的这个架包

所以我们重点

看的是这两个架包

这两个坐标

下面这个呢

这就是普通的对吧

Spring Cloud的Starter Web

因为我们是一个web工程

还有可能做测试对吧

所以说呢

把这个导进来就可以了

然后呢

继承了我们这个Spring Cloud的Starter Parent

然后呢

聚合了这三个子工程

这是复工程里边呢

主要就是这个POM文件

其他的就没什么东西了

然后呢

我们来看client1里边

client1里边这个POM文件其实就没什么东西了

然后呢

我们重点看什么呢

看src下面

它这个配置文件

这个地方你看啊

这是设置这个client1对吧

它的端口号呢

是9101

然后呢

它这个应用名呢

叫做trace-1

然后这块

这就是关于Sluice它的配置对吧

然后配置的这一项

这叫什么呢

就是收集比例

也就是说

它产生的这种链路追踪的数据

如果我在这配置1的话

就是百分之百收集

因为有些情况下

考虑到我们这个系统它的性能啊

它并不需要把所有追踪的数据呢

全都去把它提交了

并不是需要收集所有的数据

那么这个地方我们写1的话呢

就表示百分之百全部收集数据

但是这样的话呢

可能对我们这个系统性能呢

是有一定损耗的

因为呢

收集数据呢

也是需要消耗时间的

对吧

然后呢

注意看这个地方呢

我们收集好了这个数据呢

是不是需要提供给我们的Zipcan

来收集呢

存储包括来展示对不对

都是在Zipcan这边

所以说呢

我们需要知道Zipcan在什么位置

现在呢

我是不是已经跑起来了

就在我们本地啊

所以我在这写的是什么呢

Localhost的

然后端口号呢

就是这个9411

这是指定我们Zipcan

它的这个信息

然后呢

我们来看

在我们这个Client1里边

这个呢

是启动类

这个应该没什么好说的

只不过呢

在启动类里边呢

我们创建出来了这么一个

叫做

Rest Template

这么一个对象

这么一个类

这个呢

大家应该是比较熟悉了

我们要发一个Rest的方式请求

对吧

我是不是就可以

直接使用这个对象

这样的话呢

你看我在这这个Test Client

它其实本质上就是一个Controller

你看到没有

它其实就是一个Controller

然后呢

我们在这呢

把这个Rest Template的对象呢

注进来

注进来之后呢

我们在这个Test的方法里边

干什么呢

注意看

通过Rest Template.getForce

Entity

它其实就发了一个请求

对吧

那么你看它这个接口的地址

是localhost的9102

这个其实是调到谁了

是调到我们这第二个微服务去了

调到第二个微服务去了

因为刚才我们也说了

咱们在这是不是有这么三个客户端工程

然后Client1是不是会通过Rest的来调什么呢

Client2对吧

所以从这呢

它其实就是在调用

好

然后呢

我们来看Client2

Client2呢

都是非常类似了

它这个配置文件呢

端口你看是不是就是9102

然后呢

这些地方配置其实都是一样的

对吧

然后呢

它也是需要产生这个链路追踪数据

最终呢

也是需要提供给Zipkin

所以需要去描述Zipkin在什么位置

然后呢

我们来看

它这里边是不是也有一个启动类

用来启动服务的

包括它这是不是也注入了一个Rest的Template

因为什么呢

因为这个Client2是不是会去调Client3去

对吧

所以说呢

在我们这个地方

你注意看

这是不是

它这个请求路径是不是杠Trace2啊

那么刚才我们看到了

在Client1里边对吧

这个地方你看

它是不是9102

然后Trace2

这样的话

它其实就调到了谁呢

就调到了我们当前这个方法

通过Rest是不是来调用

然后呢

在这个2这儿呢

没停

它是不是又调了谁呢

9103

Trace3

这是不是又发了一个请求对吧

去调我们第三个微服务

所以接下来呢

我们再来看

我们的这个方法呢

我们的这个方法呢

第三个微服务

第三个微服务呢

因为也要产生这个链路追踪的数据

所以呢

这块配置都是一样的

对吧

这个已经说过两遍了

然后呢

它这边是不是也应该有一个什么呢

启动类

对吧

也有个启动类

但是它这边的话

其实这个Rest就不是必须的了

因为什么呢

它已经调到头了

它不要不再去调其他的了

所以这边呢

你看这是Trace3对吧

它在这呢

直接返回一个

这个

字符串

对吧

对象

直接返回一个字符串

就可以了

它就不再去调了

所以这边的话

其实我们这个Rest的template呢

既是没有也没有关系

因为它已经调到头了

对吧

好

这就是我们把这个代码呢

整体梳理了一下

整个代码其实是非常简单的

对吧

因为我们重点

想演示的是

它们之间

这三个微服务之间

一调用二

二调用三

它们之间能调通就可以了

对吧

好

重点呢

就是看一下这个Sluice

还有这个Rest

还有这个Rest

还有这个Rest

还有这个Rest

还有Zipkin这块的配置

这个呢

其实也是比较直观的

好

这就是我们导入的这个什么呢

Maven工程

对吧

这个代码呢

咱们提前都已经提供好了

好

然后呢

我们把这个代码呢

读一下

重点的地方呢

来看一下

然后一会儿呢

我们就来实际操作一下

看看我们这个数据呢

能不能收集到

好

这是关于Maven工程的导入

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 Spring Cloud Sleuth 链路追踪功能的入门教程，重点演示了如何通过 Maven 项目结构搭建一个包含父工程和三个客户端工程的链路追踪系统，并集成 Zipkin 作为追踪收集器。讲师通过 IntelliJ IDEA 编辑器，逐步展示了父工程 `sleuth_parent` 的依赖配置、三个客户端工程 `sleuth_client1`、`sleuth_client2`、`sleuth_client3` 的配置文件（`application.yml`）和核心代码（`Application.java`、`TestClient.java`），并说明了各工程的职责和配置差异。整个过程旨在帮助学习者理解分布式链路追踪的基本架构和配置方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，定位到“3.3.2 导入maven工程”章节。
*   **00:00:05 - 00:00:15**: 讲师在 Typora 中解释了将导入四个 Maven 工程（`sleuth_parent`, `sleuth_client1`, `sleuth_client2`, `sleuth_client3`）的原因，是为了演示链路追踪效果。
*   **00:00:15 - 00:00:30**: 讲师切换到 IntelliJ IDEA，打开 `sleuth_parent` 项目，并展示其 `pom.xml` 文件中的依赖配置。
*   **00:00:30 - 00:00:45**: 讲师在 `sleuth_parent` 的 `pom.xml` 中，重点讲解了 `spring-cloud-starter-sleuth` 和 `spring-cloud-sleuth-zipkin` 依赖项，用于启用链路追踪和集成 Zipkin。
*   **00:00:45 - 00:01:00**: 讲师切换到 `sleuth_client1` 工程，展示其 `application.yml` 配置文件，其中设置了服务端口、应用名称、采样率和 Zipkin 服务地址。
*   **00:01:00 - 00:01:15**: 讲师展示 `sleuth_client1` 的 `Application.java`，这是一个标准的 Spring Boot 启动类，用于启动服务。
*   **00:01:15 - 00:01:30**: 讲师切换到 `sleuth_client2` 工程，展示其 `application.yml` 配置，与 `sleuth_client1` 类似，但应用名称不同。
*   **00:01:30 - 00:01:45**: 讲师展示 `sleuth_client2` 的 `TestClient.java`，其中定义了一个 `@GetMapping("/trace-2")` 的测试接口。
*   **00:01:45 - 00:02:00**: 讲师切换到 `sleuth_client3` 工程，展示其 `application.yml` 配置，应用名称为 `trace-3`。
*   **00:02:00 - 00:02:15**: 讲师展示 `sleuth_client3` 的 `TestClient.java`，其中定义了一个 `@GetMapping("/trace-3")` 的测试接口。
*   **00:02:15 - 00:02:30**: 讲师在 Typora 文档中总结了三个客户端工程的配置差异，并强调它们都指向同一个 Zipkin 服务地址 `http://localhost:9411`。
*   **00:02:30 - 00:02:45**: 讲师在 Typora 中指出，接下来将分别启动这三个客户端工程，并通过访问 `http://localhost:9101/trace-1` 等地址来测试链路追踪功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **课程大纲**: “3.3.2 导入maven工程”。
    *   **工程说明**:
        *   `sleuth_parent`: 父工程，统一管理依赖。
        *   `sleuth_client1`: 链路追踪客户端工程，通过 REST 调用 `sleuth_client2`。
        *   `sleuth_client2`: 链路追踪客户端工程，通过 REST 调用 `sleuth_client3`。
        *   `sleuth_client3`: 链路追踪客户端工程。
    *   **配置注释**: `#这个是收集比例，1表示100%，全部收集`。
    *   **关键注释**: `注：sleuth_client1, sleuth_client2, sleuth_client3的application.yml中的端口和应用名称配置不同，其他都相同。`

*   **代码内容**:
    *   **`sleuth_parent/pom.xml` 依赖配置**:
        ```xml
        <!--spring-cloud sleuth 支持包-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-sleuth</artifactId>
        </dependency>

        <!--spring-cloud sleuth zipkin 整合-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-sleuth-zipkin</artifactId>
        </dependency>

        <!--spring-boot-starter-web-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!--spring-boot-starter-test-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        ```
    *   **`sleuth_client1/application.yml` 配置**:
        ```yaml
        server:
          port: 9101
        spring:
          application:
            name: trace-1
        sleuth:
          sampler:
            probability: 1 #这个是收集比例，1表示100%，全部收集
        zipkin:
          base-url: http://localhost:9411
        ```
    *   **`sleuth_client2/application.yml` 配置**:
        ```yaml
        server:
          port: 9102
        spring:
          application:
            name: trace-2
        sleuth:
          sampler:
            probability: 1 #这个是收集比例，1表示100%，全部收集
        zipkin:
          base-url: http://localhost:9411
        ```
    *   **`sleuth_client3/application.yml` 配置**:
        ```yaml
        server:
          port: 9103
        spring:
          application:
            name: trace-3
        sleuth:
          sampler:
            probability: 1 #这个是收集比例，1表示100%，全部收集
        zipkin:
          base-url: http://localhost:9411
        ```
    *   **`sleuth_client1/Application.java`**:
        ```java
        @SpringBootApplication
        public class Application1 {
            @Bean
            RestTemplate restTemplate() { return new RestTemplate(); }
            public static void main(String[] args) { SpringApplication.run(Application1.class, args); }
        }
        ```
    *   **`sleuth_client2/TestClient.java`**:
        ```java
        @RestController
        public class TestClient {
            @Autowired
            RestTemplate restTemplate;
            @GetMapping("/trace-2")
            @ResponseBody
            public String test(HttpServletRequest request) {
                //logger.info("===call trace-3, TraceId={}", request.getHeader("X-B3-TraceId"));
                //System.out.println(1.0);
                return "Trace";
            }
        }
        ```
    *   **`sleuth_client3/TestClient.java`**:
        ```java
        @RestController
        public class TestClient {
            @Autowired
            RestTemplate restTemplate;
            @GetMapping("/trace-3")
            @ResponseBody
            public String test(HttpServletRequest request) {
                //logger.info("===call trace-3, TraceId={}", request.getHeader("X-B3-TraceId"));
                //System.out.println(1.0);
                return "Trace";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖配置** (00:00:15 - 00:00:45)
    *   讲师在 IntelliJ IDEA 中打开 `sleuth_parent` 项目。
    *   通过鼠标滚轮和点击，导航到 `pom.xml` 文件。
    *   通过高亮和滚动，重点讲解了 `spring-cloud-starter-sleuth` 和 `spring-cloud
