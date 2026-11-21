# 15-CAT安装使用-GateWay网关服务与CAT集成 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

咱们接着对CAT做一个集成实现

上一讲我们对CAT的Gateway

做了一个搭建配置

完成了基本的功能接口

那么接下来我们就要去实现了CAT的相关的配置

在这里咱们先创建一个CAT的上下文

叫CAT Context

好CAT Context

在这里面要去定义

它的一个Map

这个Map的话是干嘛用的呢

它要去追踪和记录CAT监控相关的一些属性和信息

那么我们来实现一下MapString

然后String

它的结构的话

Key跟Value都是String

然后名称我们叫Properties

New HashMap

这个的话就采用HashMap就可以了

它的主要作用就是

存储

链路

监控相关信息

好

那么的话呢

我们要给它呢

做一个接口的实现

这个接口呢

我们要去实现了CAT所提供出来的CAT.Context

在接口上面的话呢

让它实现了

Add跟那个GetProperties的方法

就是操作具体的

Map的属性信息

AddProperties呢

这个比较简单

对不对

Properties

然后我们将属性的存进去就可以了

Key跟Value

那么的话呢

Get这一块呢

也比较简单

我们只要呢

将信息读取出来就可以

GetKey

这个就是我们自定义的它的上下文信息的一个配置实现

那接着的话呢

我们还要去实现呢

CAT的常量配置

同样创建一个

Class加CATHTTP

Consistence

这个主要作用呢

就是记录HTTP的一些常量

Public static

Final

Stream

然后呢是CATHTTP

这个呢是它的一个头部信息

头部信息里面的话呢

就包括像TreadMessage

ID

然后呢

还有这个就是它具体的值

这个值的话呢我们就给它一个数字的值

给它

标识一下叫XCAT

然后ChartID

好

这个呢是一个常量

那我们呢再将它Copy一下

然后呢

还要定义两个常量

另外两个常量呢

一个是HTTP

Pellet

因为我们之前讲过了

有PID的记录

对不对

有ChessID

SpamID

还有PID

那这个的话呢就是Pellet

Pellet

Pellet

MessageID

这个的话呢我们把它

属性直接改一下

就叫Pellet

好有了PelletID之后呢

我们还应该有一个什么

就是它的ChessID

也就是它的一个根基的

消息ID的标识

就叫XCAT

那RootID

好这样呢

我们就定义了CAT的

它的主要的

链路跟踪的属性常量

那接着的话呢

我们还要去做什么

就要去真正的去实现它的过滤器

相关的配置

那过滤器呢

我们回到讲义当中

可以看到

首先呢

我们要给它一个配置

CATFILTER

Config

那我们去实现一下

new class

java class

然后呢

CATFILTER

Config

在这里面呢

我就将它直接Copy过来

然后呢

再给大家做详细讲解

节省一些时间

好

config

config

config

这个呢

还要实现什么

CATSERVERLETFILTER

对不对

CATSERVERLETFILTER呢

在下面

就是具体的

过滤器的

它怎么去处理

它要做哪些事情

我们呢

将CATFILTER

Copy过来

new class

好

它要去什么

实现javaX

就是SERVERLET里面的FILTER

然后呢

是它具体的代码实现

我们将它呢

Copy过来

好

然后呢

自动帮我们引入

那整个的话呢

就已经引入进来

最后呢

还要加上一个CATLIST INTERCEPT

就是它的拦截器

我们也同样创建一下

new

javaX

CATSERVERLETFILTER

那这个拦截器呢

接下来我们会给它做一个讲解

就是结合呢

我们这几个内

然后一起给大家做一个讲解介绍

这样呢

结合起来的话呢

才能够帮助大家更好地去理解

好

那这边呢

我把这个代码相对比较多一点

我这边呢

就直接将它复制引用过来

然后在这里呢

是

采用HTTP

是被framework下面了

这个包呢

不要引用错误

context

这个呢

也要将它导入进来

好

这些常量的话呢

可以看到

就是我们在这里面所定义的

对不对

这个context呢

我也将它导入

CAT CONTEXT

好

那我看一下

还有没有什么

还有一点事

我们的记得

它要去

继承

对不对

它继承

就是实现了

CAT所提供的拦截器接口

那这一块的话呢

我们就已经把他的相关的

过滤器和拦截器的处理代码呢

继承加入进来

那么看一下

它整体是怎么做的呢

过滤器这边的话呢

我们看到它有什么

FUELT

REGISTRATION

BIN

对不对

先去创建一个

一个注册对象

在注册对象里面的话呢

里面的话呢

他要做什么事情呢

他要将CAT的FILTER过滤器加入进来

然后呢

是他的一些注册配置信息

也就是说这个过滤器呢

你要去拦截哪些路径

对吧

你的名称是什么

你的拦截顺序是怎样的

这个呢

就是CAT过滤器的配置

注册配置

好

那在这里面的话呢

我们再看一下CAT Servered Filter

它具体是怎么做的

这个呢

就跟我们的之前所学习Severed Filter里面呢

处理顺序是一样的

先要去ENIT初始化方法

对不对

要做初始化的一些配置

配置些什么信息呢

我们可以看到

他要去加载CAT的一些初始化参数

也就是说这里面的话呢

有些Model URL Pattern

比如说你要去针对一些URL Pattern

做一些过滤啊

做一些拦截控制啊

对不对

这边的话呢

就要做具体的配置

如果说你没有配置这个东西

的话呢

也没有关系

好

那我们再看一下

请求过滤的一个具体处理

这个呢

就是过滤器的核心处理逻辑

它怎么做的呢

它首先就是判断我们URL Pattern有没有

对不对

刚才已经讲了

如果你不配置也没有关系

它就不会去根据你这个URL

做一个过滤判断

那我们再看一下

再往下面的话呢

是什么呢

下面呢

是CAT的上下文信息的配置

那在这里呢

我们将这里调整

调整一下

让大家看的更加全面一点

这个呢

是初始化CAT的一个context

就创建一个新的CAT context对象

对不对

之前的话呢

我们也给大家做了一个讲解和实现

那么CAT context呢

它要存取什么信息呢

就是存取我们链路最终的三个关键信息

一个呢

Root相当于就是Chess ID

一个是Parent PID

还有什么Chad Spam ID

在这里面的话呢

都会有记录

好

然后呢

它会将这些信息什么发送给远程服务

对不对

然后呢

再开启一个什么

开启一个全section

一个事务去做了具体的记录

这个呢

我们看一下他怎么去做呢

在这里面呢

他有CAT的日子记录

CAT的日子记录呢

他会去记录了你的调用方法

你是进入哪个方法做了什么事情

对不对

然后呢

你的处理结果是怎样的

你的URL请求信息又是怎样的

那么

在这里面还会记录他的client的一些信息

就是你的客户端

他的远程地址

那么在这里呢

就是进入到我们具体的业务逻辑的接口

业务逻辑这边处理完成之后呢

他会将结果设置为成功

对不对

如果是你业务这边处理异常了

大家想想

他就不会进入到这里

对不对

那么他就会标记为失败

然后呢

同样会呢

发送到我们的CAT服务当中

好

这块呢

是过滤器的一个处理逻辑流程

那么

再看一下还有个拦截器

对不对

这个拦截器是做什么用呢

这个拦截器呢

大家想想

那么的话呢

我们有多个服务节点

每个服务节点呢

他都是整个链路上的一个环节

对吧

那么我们有个过滤器

这个过滤器呢

是拦截呢

你本地服务节点的业务处理逻辑的

那么在这里面的话呢

他有做详细的一些记录

记录完成之后呢

我留准了一个记录

我们来到下一个节点

你这个拦截器的作用

这个一个CAP的作用是干嘛呢

他就要去记录和传递你的

就是我们前面所讲的TID

PID

以及SPAN ID的信息

这样呢

就是用于跟踪和标记

我们整体的一个链路

好

那么呢

我们再往下面看一下具体代码

代码这一块呢

可以看到

它叫什么

保存和传递CAT电源链的

上下文对不对

那CAT电源链的上下文呢

就是这个ROOT ID

HELEN ID

以及呢

CHEL ID

就是SPAN ID

接下来呢

就继续执行请求

它呢

不会去干扰你业务逻辑的处理

只是说我在这里打个标记就可以了

便于呢

我后续服务节点

接收到这个请求之后

我就知道是从哪里来的

它的一个电源链

它的上下文是怎样的

明白吧

好

是这样一个作用

那这一块呢

就是我们Gateway服务网关

对Gateway的服务网关的作用

CAT列入了一个监控集成的配置

好

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析。

---

### 1) 视频摘要

本视频课程聚焦于在 Spring Cloud 微服务架构中集成阿里巴巴的 CAT（全链路监控）系统。讲师通过一个名为 `cat-demo-gateway` 的网关服务项目，演示了如何从零开始配置和实现 CAT 的监控功能。核心内容包括：添加 CAT 依赖、定义 CAT 上下文和常量、编写拦截器来自动注入 CAT 上下文、以及配置 RestTemplate 以支持 CAT 的链路追踪。整个过程旨在展示如何在微服务中无缝集成监控，从而实现对服务调用链路的完整追踪和性能分析。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:02:00**：课程开场，讲师介绍本节内容是关于 CAT 集成，主要演示如何在网关服务中集成 CAT。
*   **00:02:00 - 00:04:00**：展示 `pom.xml` 文件，添加 CAT 客户端依赖 `cat-client`。
*   **00:04:00 - 00:06:00**：讲解 `CatContext` 类，用于创建和管理 CAT 上下文。
*   **00:06:00 - 00:08:00**：定义 `CatHttpConstants` 类，用于存储 CAT 监控所需的 HTTP 头部常量。
*   **00:08:00 - 00:10:00**：编写 `CatFilterConfigure` 配置类，用于注册拦截器。
*   **00:10:00 - 00:12:00**：编写 `CatServletFilter`，实现 `doFilter` 方法，用于在请求处理前设置 CAT 上下文。
*   **00:12:00 - 00:14:00**：编写 `CatRestInterceptor`，实现 `ClientHttpRequestInterceptor` 接口，用于在 REST 调用前后注入 CAT 上下文。
*   **00:14:00 - 00:16:00**：配置 `RestTemplate`，添加 `CatRestInterceptor` 以支持 CAT 监控。
*   **00:16:00 - 00:18:00**：讲解 CAT 客户端的配置文件 `client.xml`，并说明其在不同版本中的配置方式。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **依赖配置**：`<dependency> <groupId>com.dianping.cat</groupId> <artifactId>cat-client</artifactId> <version>3.0.0</version> </dependency>`
    *   **CAT 常量定义**：`static final String CAT_HTTP_HEADER_CHILD_MESSAGE_ID = "X-CAT-CHILD-ID";`
    *   **CAT 上下文配置**：`CatContext catContext = new CatContext();`
    *   **CAT 事务创建**：`Transaction t = Cat.newTransaction(CatConstants.TYPE_URL, url);`
    *   **CAT 日志事件**：`Cat.logEvent(type, request.getRemoteHost());`
    *   **CAT 客户端配置**：
        ```xml
        <config xmlns:xsi="http://www.w3.org/2001/XMLSchema" xsi:noNamespaceSchemaLocation="config.xsd">
            <servers>
                <server ip="10.10.20.10" port="2280" http-port="8080" />
            </servers>
        </config>
        ```

*   **代码关键内容**：
    *   **`CatContext` 类**：
        ```java
        private Map<String, String> properties = new HashMap<>();
        public void addProperty(String key, String value) {
            properties.put(key, value);
        }
        ```
    *   **`CatHttpConstants` 类**：
        ```java
        public class CatHttpConstants {
            static final String CAT_HTTP_HEADER_ROOT_MESSAGE_ID = "X-CAT-ROOT-ID";
            static final String CAT_HTTP_HEADER_PARENT_MESSAGE_ID = "X-CAT-PARENT-ID";
            static final String CAT_HTTP_HEADER_CHILD_MESSAGE_ID = "X-CAT-CHILD-ID";
        }
        ```
    *   **`CatServletFilter` 类**：
        ```java
        @Override
        public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
            // 获取 URL
            String url = request.getRequestURL().toString();
            // 创建 CAT 上下文
            CatContext catContext = new CatContext();
            // 设置上下文属性
            catContext.addProperty(CatConstants.CAT_HTTP_HEADER_ROOT_MESSAGE_ID, request.getHeader(CatHttpConstants.CAT_HTTP_HEADER_ROOT_MESSAGE_ID));
            catContext.addProperty(CatConstants.CAT_HTTP_HEADER_PARENT_MESSAGE_ID, request.getHeader(CatHttpConstants.CAT_HTTP_HEADER_PARENT_MESSAGE_ID));
            catContext.addProperty(CatConstants.CAT_HTTP_HEADER_CHILD_MESSAGE_ID, request.getHeader(CatHttpConstants.CAT_HTTP_HEADER_CHILD_MESSAGE_ID));
            // 创建事务
            Transaction t = Cat.newTransaction(CatConstants.TYPE_URL, url);
            try {
                // 记录日志事件
                Cat.logEvent(CatConstants.TYPE_SERVICE, "Service.method", request.getMethod(), request.getRemoteHost());
                // 继续过滤
                chain.doFilter(request, response);
            } catch (Exception e) {
                t.setStatus(e);
                Cat.getProducer().logError(e);
                throw e;
            } finally {
                t.complete();
            }
        }
        ```
    *   **`CatRestInterceptor` 类**：
        ```java
        @Component
        public class CatRestInterceptor implements ClientHttpRequestInterceptor {
            @Override
            public ClientHttpResponse intercept(HttpRequest request, byte[] body, ClientHttpRequestExecution execution) throws IOException {
                // 创建事务
                Transaction t = Cat.newTransaction(CatConstants.TYPE_CALL, request.getURI().toString());
                try {
                    // 获取请求头
                    HttpHeaders headers = request.getHeaders();
                    // 设置上下文
                    CatContext ctx = new CatContext();
                    ctx.addProperty(CatConstants.CAT_HTTP_HEADER_ROOT_MESSAGE_ID, headers.get(CatHttpConstants.CAT_HTTP_HEADER_ROOT_MESSAGE_ID));
                    ctx.addProperty(CatConstants.CAT_HTTP_HEADER_PARENT_MESSAGE_ID, headers.get(CatHttpConstants.CAT_HTTP_HEADER_PARENT_MESSAGE_ID));
                    ctx.addProperty(CatConstants.CAT_HTTP_HEADER_CHILD_MESSAGE_ID, headers.get(CatHttpConstants.CAT_HTTP_HEADER_CHILD_MESSAGE_ID));
                    CatRemoteCallServer.setContext(ctx);
                    // 执行请求
                    ClientHttpResponse response = execution.execute(request, body);
                    t.setStatus(Transaction.SUCCESS);
                    return response;
                } catch (Exception e) {
                    t.setStatus(e);
                    Cat.getProducer().logError(e);
                    throw e;
                } finally {
                    t.complete();
                }
            }
        }
        ```
    *   **`RestTemplate` 配置**：
        ```java
        @Bean
        RestTemplate restTemplate() {
            RestTemplate restTemplate = new RestTemplate();
            restTemplate.setInterceptors(Collections.singletonList(new CatRestInterceptor()));
            return restTemplate;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：添加 CAT 依赖** (00:02:00)
    *   讲师在 `pom.xml` 文件中添加了 `com.dianping.cat:cat-client:3.0.0` 依赖，并解释了其作用是为项目引入 CAT 客户端库。

*   **场景二：定义 CAT 常量** (00:06:00)
    *   讲师创建了 `CatHttpConstants` 类，并定义了三个静态常量：`CAT_HTTP_HEADER_ROOT_MESSAGE_ID`、`CAT_HTTP_HEADER_PARENT_MESSAGE_ID` 和 `CAT_HTTP_HEADER_CHILD_MESSAGE_ID`，用于标识链路中的不同层级。

*   **场景三：编写拦截器** (00:10:00)
    *   讲师编写了 `CatServletFilter`，它实现了 `doFilter` 方法。在方法中，它首先获取请求的 URL，然后创建一个 `CatContext` 对象，并根据请求头设置其属性。接着，它创建一个 `Transaction` 事务，并在 `try-catch-finally` 块中记录日志、执行过滤器链，并在最后完成事务。

*   **场景四：配置 RestTemplate** (00:14:00)
    *   讲师在配置类中定义了一个 `@Bean` 方法，用于创建 `RestTemplate` 实例。他将 `CatRestInterceptor` 添加到 `RestTemplate` 的拦截器列表中，以确保所有通过 `RestTemplate` 发起的 HTTP 请求都能被 CAT 监控。

*   **场景五：配置 CAT 客户端** (00:16:00)
    *   讲师展示了 CAT 客户端的配置文件 `client.xml`，并说明了在不同版本中配置文件的位置和格式。他强调了在 Linux 系统上运行服务的重要性，因为 Windows 系统可能无法正确识别某些路径。

通过以上演示，讲师完整
