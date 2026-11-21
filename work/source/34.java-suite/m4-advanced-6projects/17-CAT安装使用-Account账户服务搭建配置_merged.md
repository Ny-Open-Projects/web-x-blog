# 17-CAT安装使用-Account账户服务搭建配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们呢,开始实现账户服务,账户服务跟库存服务呢,都是整个调用链当中最末端的服务,那么它们跟它的上层订单服务和网关服务之间呢,有没些什么区别呢?这个呢,还是会有一些区别的,那么具体是在哪里呢?我们回到代码当中来看一下。

之前呢,我们实现了网关服务跟订单服务,对不对?在这里面的话呢,我们集成了CAD的电路监控,那么可以看到订单服务呢,跟网关服务,它们的CAD集成呢,都是一致的,没有些什么区别,对吧?

但是呢,接下来的账户服务跟库存服务呢,大家要注意一下,它们在这一块呢,不需要实现CAD REST INCEPT,为什么呢?大家可以看到。

在这里呢,Gateway它是要下发到order服务,对不对?那么order服务这边的话呢,它要增加一个拦截器。

这个拦截器呢,它要做什么事情呢?要记录CHESS ID,对吧?PALLELINED ID以及SPAN ID,要把这三个信息呢,记录,记录,然后呢,是要传递给账户服务和库存服务。

所以呢?

这个呢,就是CAD拦截器的最主要作用。

但是呢,账户服务跟库存服务,它们还需要拦截器吗?

它们就不需要了,因为它们下面呢,没有其他的要调用的服务。

所以在这一块呢,它们就不需要拦截器。

那么其他的,过滤器这一块呢,它还是需要的,对不对?

因为它要过滤器,要去接收对应的TID,TID等相关的一些信息。

好,这一块呢,是最摩登的服务跟上层调用链它们的一些区别。

这一点呢,大家要注意一下。

接下来呢,我们就来实现账户服务。

我们选中CAD Demo,New Model。

在这里呢,我们仍然选用它默认的模板,点击Next。

然后呢,CAD Demo Account,点击Next。

这里呢,注意一下,它的附近呢,是在CAD Demo下面。

大家不要搞错路径了哈。

如果说你放在PathTog下面呢,那整个工程结构呢,就乱掏了。

点击Finish。

好,账户服务呢,就已经创建完成。

对吧,我们呢,把它的包结构再创建一下,New Package。

在这里呢,先让它Maven导入生效,然后给New Package。

com.itcast.boss。

然后呢,CAD Demo,CAD Startup。

在这里呢,我们还一直创建它的一个CAD Utils。

再增加一个包。

DRR。

CAD Utils。

好,在这里呢,就已经创建完了两个包。

我们在这一块呢,可以直接将CAD的集成配置呢,引入进来。

但是呢,刚才已经讲了,对不对,不需要Intercept,不需要拦截器。

好,引入进来之后呢,我们就去创建一下它的启动内。

New Class。

然后呢,是CAD Demo Account Application。

好,这个时候呢,我们再给它一个新的名称。

我们再给它一个启动入口。

PSVM。

然后呢,Screen Application。

自身的内。

然后呢,Class。

这个时候呢,我们再加上对应的Screen Port的固件。

Enable.

Scan.

Clump。

还有包的扫描,对不对。

Content.

Scan。

然后呢,就是Base Packages。

在这里呢,给它一个大框。

它可以自身的多个包的入境扫描。

我们还需要给它一个什么?

再给它编写一个结构。

就是账户服务所提供的结构。

由订单服务进行调用。

那么呢,再去实现。

Screen Port的一个结构。

给它提供出来。

Apple.

Screen.

好,Count.

方法名称就叫做Count.

Choose.

Exception.

加上对应的请求入境。

这个呢,跟方法名保持一致就可以了。

然后我们要给它返回一个结果,对不对。

Account.Success。

就告诉你啊,Account服务调用处理成功。

对吧。

那么呢,如果是你在这里面直接打印这个的,返回起来会很快。

对吧。

那我们呢,给它一个睡眠。

Sleep 500毫秒。

这个500毫秒可能有点长。

只是说在我们那个CAD监控上面,能看到它一个调用的时间段就可以了。

对吧。

否则的话,你很快,一到两个毫秒就已经没有了。

在这个时间段的区域当中呢,可能就很微小。

可能呢,看得起来不直观。

所以我们呢,在这里睡眠150毫秒。

模拟呢,第五个处理。

再给它加上对应的数字。

提供呢,账户。

服务接口。

好。

在这里呢,配置完成之后。

接下来呢,我们还要去配置它的配置文件。

对不对。

New。

然后呢,是Application。

点Properties。

好。

为了快速写件呢,这边的话呢,我就直接去拷贝对应的代码。

这个呢,是我们之前已经实现过的CAD的测试服务。

好。

将最快呢,拷贝过来。

好。

这些意思的话呢,大家都比较清楚。

对吧。

这个呢,是SoulPort端口。

然后呢,ApplicationName。

是它的一个名称。

这个名称的话呢,就跟我们的模块名称保持一致。

这个呢,是NUCLS的地址。

然后这个呢,是暴露监控的接口。

这里面我们是暴露所有的。

好。

然后呢,还有什么。

还有我们的MATINF。

然后呢,要去定义CAD的注册的名称对类。

我们也把它拷贝过来。

还有LogBack。

这些呢,都加入进去。

那,账户服务这一块呢,我们就已经搭建和配置完成。

这个的话呢,Home这一块,我们可以看到是不需要对应的依赖。

它会直接去继承我们的附近模块所提供的相关依赖。

像那个Splendor、NUCLS、Splendor的监控、组件依赖等等。

好。这一块呢,就已经实现了账户服务的搭建。

那这一讲呢,我们就先讲到这里。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“CAT”微服务框架（可能为“Catastrophic”或“Cloud Application Toolkit”的缩写，但在此上下文中指代一个特定的微服务框架）的实战教学，重点讲解其服务设计与工程结构。讲师通过演示一个包含“网关（Gateway）”、“订单服务（Order）”、“账户服务（Account）”和“库存服务（Stock）”的微服务架构，展示了如何使用 Spring Cloud Alibaba 的 Nacos 作为服务注册与发现中心，并通过 CAT 框架的过滤器（Filter）对请求进行拦截和处理。课程内容覆盖了项目结构、依赖配置、服务注册、以及如何在网关中集成 CAT 过滤器，旨在帮助开发者理解并实践一个完整的微服务系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示课程大纲，当前章节为“3.3 服务设计”。
*   **00:03 - 00:08**: 展示服务架构图，包含“客户端”、“网关（Gateway）”和“订单服务（Order）”。
*   **00:08 - 00:12**: 展示服务架构图，增加“账户服务（Account）”和“库存服务（Stock）”，形成完整的微服务调用链。
*   **00:12 - 00:16**: 切换到 IDE，展示 `cat-demo-order` 项目的结构，并打开 `CatFilterConfigure.java` 文件，演示如何配置 CAT 过滤器。
*   **00:16 - 00:20**: 展示 `cat-demo-account` 项目的 `pom.xml` 文件，讲解其依赖项，特别是 `spring-cloud-starter-alibaba-nacos-discovery`。
*   **00:20 - 00:24**: 展示 `cat-demo-account` 项目的 `application.properties` 文件，配置服务名和 Nacos 服务地址。
*   **00:24 - 00:28**: 展示 `cat-demo-account` 项目的 `CatDemoAccountApplication.java` 主类，讲解 `@EnableDiscoveryClient` 注解的作用。
*   **00:28 - 00:32**: 展示 `CatDemoAccountApplication.java` 中的 `@RestController` 和 `@RequestMapping` 注解，演示一个简单的 HTTP 请求处理方法。
*   **00:32 - 00:36**: 展示 `cat-demo-account` 项目的 `META-INF` 目录下的 `application.properties` 文件，用于配置服务。
*   **00:36 - 00:40**: 展示 `cat-demo-account` 项目的 `pom.xml` 文件，再次强调其依赖项。
*   **00:40 - 00:44**: 展示 `cat-demo-order` 项目的 `pom.xml` 文件，展示其依赖项。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**:
    *   **服务架构图**:
        *   **初始架构**: 客户端 -> 网关（Gateway） -> 订单服务（Order）。
        *   **扩展架构**: 客户端 -> 网关（Gateway） -> 订单服务（Order）-> 账户服务（Account）和库存服务（Stock）。
    *   **依赖关系图**: 通过 IDE 展示了 `cat-demo-account` 项目对 `spring-cloud-starter-alibaba-nacos-discovery` 的依赖。

*   **代码**:
    *   **CAT 过滤器配置 (`CatFilterConfigure.java`)**:
        ```java
        @Bean
        public FilterRegistrationBean filterRegistrationBean() {
            FilterRegistrationBean registration = new FilterRegistrationBean();
            CatServletFilter filter = new CatServletFilter();
            registration.setFilter(filter);
            registration.addUrlPatterns("/*");
            registration.setName("cat-filter");
            registration.setOrder(1);
            return registration;
        }
        ```
    *   **服务启动类 (`CatDemoAccountApplication.java`)**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = {"com icast"})
        @RestController
        public class CatDemoAccountApplication {
            @RequestMapping("/account")
            public String service() throws Exception {
                return "account success";
            }
        }
        ```
    *   **配置文件 (`application.properties`)**:
        ```properties
        server.port=8083
        spring.application.name=cat-demo-account
        spring.cloud.nacos.discovery.server-add=10.10.20.1:8848
        management.endpoints.web.exposure.include=*
        ```

---

### 4) 关键场景与演示描述

*   **场景 1: 服务架构展示** (00:03-00:08)
    *   讲师首先展示了一个简单的服务架构图，其中客户端通过网关访问订单服务。这为后续的复杂架构奠定了基础。

*   **场景 2: 架构扩展** (00:08-00:12)
    *   讲师在架构图中添加了“账户服务”和“库存服务”，并用箭头表示它们由订单服务调用。这展示了微服务架构中服务间调用的典型模式。

*   **场景 3: CAT 过滤器配置** (00:12-00:16)
    *   讲师切换到 IDE，打开 `CatFilterConfigure.java` 文件，演示如何通过 `@Bean` 注解注册一个 `FilterRegistrationBean`，并将 `CatServletFilter` 注册为全局过滤器，作用于所有 URL。

*   **场景 4: 项目依赖配置** (00:16-00:20)
    *   讲师展示 `cat-demo-account` 项目的 `pom.xml` 文件，重点讲解了 `spring-cloud-starter-alibaba-nacos-discovery` 依赖，说明其用于服务发现。

*   **场景 5: 服务配置** (00:20-00:24)
    *   讲师展示 `application.properties` 文件，配置了服务端口、服务名和 Nacos 服务地址，这是服务注册到 Nacos 的关键配置。

*   **场景 6: 服务启动类** (00:24-00:28)
    *   讲师展示 `CatDemoAccountApplication.java`，讲解 `@EnableDiscoveryClient` 注解的作用，即启用服务发现功能。

*   **场景 7: 服务接口定义** (00:28-00:32)
    *   讲师在 `CatDemoAccountApplication.java` 中定义了一个 `@RequestMapping("/account")` 的方法，用于处理 HTTP 请求，并返回一个简单的字符串。

*   **场景 8: 配置文件细节** (00:32-00:36)
    *   讲师展示 `META-INF` 目录下的 `application.properties` 文件，用于配置服务。

*   **场景 9: 依赖项确认** (00:36-00:40)
    *   讲师再次展示 `pom.xml` 文件，确认依赖项配置无误。

---

以上是根据视频画面进行的结构化分析，旨在帮助理解课程内容和关键技术点。
