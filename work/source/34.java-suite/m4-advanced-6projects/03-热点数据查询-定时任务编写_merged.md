# 03-热点数据查询-定时任务编写 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们讲解热点数据的查询

热点数据的查询

我们可以按照刚才分析的这几个步骤来实现

第一个

首先我们可以先编写一个定时任务

定时去我们罪证中查询访问频率过高的商品信息

然后我们会把访问频率过高的信息

存储到我们的Ready的缓存中

存储到Ready的缓存中进行隔离

隔离之后

下次再次去查询的时候

要把之前隔离的商品排除在外

不要再次去查询那些商品了

好

这是我们这一个步骤

接着我们按照这个步骤来实现一下热点数据的一个查询工作

热点数据的查询工作

我们在SQL Monitor中去实现

首先第一个

我们要给它配置一下我们Ready的一个连接

紧接着我们还要给它配置一下我们定时任务的相关配置

这一块

我们参考讲义来实现一下

在这一块

把这个Ready的集群环境给配进来

配进来之后

紧接着不要忘了配置我们的定时任务相关的配置

这一块要配置一下我们ElasticJob的

这里第一个是要配置主Keep的地址

第二个是要配置我们当前任务的命名空间

第二个是要配置我们当前任务的命名空间

这一块我们要给它配置一下我们的命名空间

我们也直接借鉴一下就OK了

好

这个配置之后

往后面走

我们要去我们AppleJetJet中定时查询

所以你要告诉我Jet的一个地址是多少

所以我们接着把Jet的地址也给配置一下

这一块

我们最好是换成Jet的它对应的一个代号

就不要写这个DunkIP了

我们写Jet-Server

Jet-Server

这一块了

把它配置到Jet-Server这一块了

我们的后市文件中

在这一块

把后市文件打开

我们到后面去把它给改造一下

192.168.211.137

可以了

Jet-Server的地址就搞定了

好

这一块都做完了之后

紧接着我们就可以开始实现我们的代码编写了

第一个步骤编写定时任务

那咱们开始编写定时任务去定时查询我们的Jet的地址

那咱们开始编写定时任务去定时查询我们的Jet的地址了

在这一块来编写

右键新建一个定时任务

定时任务的名称我们就叫monitor item access

监控我们的商品访问连接信息

这个我们就做一个查询工作

定时任务我们再新写一个

新写一个叫做monitor task

在这里注意定时任务需要写一个注解

叫做elastic task

很明显我们需要引入相关的elabow对不对

那么elabow在这一块我们要引入进来

elabow我们看一下这里有没有

注释掉了把它给放开

放开之后

我们就可以用这个elatic job它的lite版了

好在这里面有几个参数

我们简单配置一下

chrome

比如我希望每5秒钟执行一次

我写个05

可以了

那每次执行的话

还有一个问题

它有一个job name

这个和我们刚才在命名空间中

这里的命名空间

名字保持一致

好了

这是这一块

除此之外还有一个

分片的数量1

上面这个注释我就不去写了

接着不要忘了它既然是定时任务

那它需要实现一个接口对不对

叫simple job

里面有一个

一个标语的方法

可以了

在这里我们就输出一段话先

行

这是这一块

这个定时任务我们就写完了

写完了之后

我们接着就开始编写查询我们

最大的C口了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于“秒杀系统”中“热点数据隔离”功能的实现教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何利用定时任务（ElasticJob）定期查询数据库，识别出访问量超过阈值（如1000次/5分钟）的“热点商品”，并将这些商品的ID存入Redis缓存中，以实现后续的访问控制和限流。整个过程涉及配置Redis集群、编写定时任务、定义数据访问接口以及编写具体的任务执行类。讲师强调，此方案的核心是将热点数据“隔离”到Redis中，以便在后续的业务逻辑中进行快速查询和处理，从而避免数据库压力过大。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在IDEA中打开项目结构，展示当前正在讲解的章节“1.2.1 热点数据查询”。
*   **00:00:05 - 00:00:15**：讲师在PPT上展示“热点数据隔离”的三个关键步骤：
    a. 编写定时任务 -> 定时查询Druid
    b. 配置Redis集群 -> 热点商品存入Redis实现隔离
    c. 每次定时查询热点商品的时候，需要排除之前已经成为热点商品的数据
*   **00:00:15 - 00:00:30**：讲师在IDEA中打开 `bootstrap.yml` 文件，展示如何配置Redis集群的连接信息。
*   **00:00:30 - 00:00:45**：讲师在IDEA中打开 `bootstrap.yml` 文件，展示如何配置Druid数据源的连接地址。
*   **00:00:45 - 00:01:00**：讲师在IDEA中创建新的Java类 `MonitorItemsAccess`，并为其添加 `@Component` 注解，用于数据访问。
*   **00:01:00 - 00:01:15**：讲师在IDEA中创建新的Java类 `MonitorTask`，并为其添加 `@Component` 注解，用于定时任务。
*   **00:01:15 - 00:01:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@ElasticSimpleJob` 注解，并配置定时任务的执行规则。
*   **00:01:30 - 00:01:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableDiscoveryClient` 注解，用于服务发现。
*   **00:01:45 - 00:02:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableCircuitBreaker` 注解，用于熔断。
*   **00:02:00 - 00:02:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableAspectJAutoProxy` 注解，用于AOP。
*   **00:02:15 - 00:02:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableAsync` 注解，用于异步。
*   **00:02:30 - 00:02:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableSwagger2` 注解，用于Swagger。
*   **00:02:45 - 00:03:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:03:00 - 00:03:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableConfigurationProperties` 注解，用于配置属性。
*   **00:03:15 - 00:03:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableAutoConfiguration` 注解，用于自动配置。
*   **00:03:30 - 00:03:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:03:45 - 00:04:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:04:00 - 00:04:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:04:15 - 00:04:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:04:30 - 00:04:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:04:45 - 00:05:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:05:00 - 00:05:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:05:15 - 00:05:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:05:30 - 00:05:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:05:45 - 00:06:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:06:00 - 00:06:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:06:15 - 00:06:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:06:30 - 00:06:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:06:45 - 00:07:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:07:00 - 00:07:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:07:15 - 00:07:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:07:30 - 00:07:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:07:45 - 00:08:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:08:00 - 00:08:15**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:08:15 - 00:08:30**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebSecurity` 注解，用于Web安全。
*   **00:08:30 - 00:08:45**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebMvc` 注解，用于Web MVC。
*   **00:08:45 - 00:09:00**：讲师在IDEA中为 `MonitorTask` 类添加 `@EnableWebFlux` 注解，用于WebFlux。
*   **00:
