# 31-网关服务-核心实现与工程配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就对核心类做个具体实现

首先回到我们的工程当中

去创建一个新的模块

这个模块就是Gateway

点击Next

然后给它一个名称

叫Bus Stock Gateway

点击Next

将名称改一下

Finish

好

创建完工程服务模块之后

咱们要把它的对应一代加入一下

对不对

那在这里

咱们就手动天下处理一下

这里一代的话不多

首先的话

Defense也是标签

然后我们看一下

将网关的依赖加入进来

在这里面的话

给了一个Defense

Group ID的话

是8G.SpringPlaneWork

点Cloud

下面的话

这是它的一个网关组件

SpringCloud

然后是Start

这里面的话

对Gateway做了一个同名同桩

这个是网关的一个依赖

我们加上对应的

注释

这个就是Gateway

网关依赖组件

接着咱们再添加

SpringBoot的依赖

在这里

仍然是一样的

org.SpringFramework的主编下面

主编是SpringFramework

下面是SpringFramework的主编

下面是SpringFramework的主编

然后我们再给它一个Artifact ID

是SpringBoot

Start

然后在这里是Actor

这个是SpringBoot的监控依赖

下面的话

是Marcos的服务依赖

给它一个注释说明

Marcos的服务注释发现依赖

这里面也给它一个Group ID

是com.alibaba.cloud

这里面也给它一个Group ID是com.alibaba.cloud

下面

那么在下面的话是Artifact ID

Spring.cloud.alibaba.marcos.discovery

这样咱们就把它的必要依赖

全部给添加进来

按住Ctrl检查一下

是否能够正常找到

PoM依赖实现完成之后

咱们就来去实现它的启动内

首先咱们要去创建一下它的一个包

回到工程当中

在这里

并没有识别出Maven项目

他们要在这里检查一下

让它禁止忽略

接着的话重新刷新一下

Maven import

这样的话就能够正常生效

我们就可以创建一个package

这个package叫com.itcast.shared

boss.stock.gateway

咱们再给它创建两个包

通过终端来创建一下

make dir big.hulu

然后再创建一个

builtas 过滤器

再创建一个启动内的包

那么我们将这三个包创建完成之后

然后可以去创建成内

那么new java class

这个启动内的话也比较简单

它能直接扣除过来

咱们要注意它的一个扫描的

基础包

然后它的助剪要把那个enable

discavlycounter加入进来

因为你作为gateway网络服

必须要找到其他的微服信息

对不对

好

接着的话就要去创建一个全局过滤器

我们

放在那个filter包下面

new class

这个全局过滤器它要去实现了global filter

以及它的一个order

我们将这个代码

copy过来

录制到我们的工程当中

我们来看一下

这一块的具体实现是怎么做的

那咱们可以看到

在这里面的话它定义了一个常量是headname对不对

这个的话

我们看一下有没有引用到

下面的话并没有使用对吧

我们先把它删除掉

这块可以不需要

因为之前是做过一定的调试

所以在这一块的话

有些代码如果是没有使用到的

咱们可以把它清理掉

那在下面咱们来看一下

最主要就是看filter的

它具体实现

它怎么去做的

在filter里面咱们可以看到

它要从头部里面

去获取什么

获取它的一个名称为

Orthodentization的一个值

那么拿到这个值之后就判断一下是否为空对不对

如果说在这里面的话

is now or empty

不为空对吧

不为空的话咱们会打一个log日志

然后

通过这个extend

来将它的头部信息进行一个转发

这样的话

就相当于说它头部信息的转发是什么样的

如果说它头部信息的话

通过咱们Gateway去转发的时候

就不会什么

不会产生丢失问题

明白吗

所以这个是它过滤器的一个最主要作用

好

这个呢

我们就

将它

配置完成

接着的话

咱们再来看一下

要实现

Application工程的一个配置

咱们来创建一下

new

fire

那咱们呢

将这一块代码先扩一扩来

咱们来看一下

stock gateway

它在这里呢

是怎么配置的

在这里呢

它主要分为两大部分

一部分是服务的基本配置

下面的话呢

是路由的转发配置

咱们可以看一下

在这一块路由的话呢

它怎么去转发的呢

我们可以看到下面一个gateway

因为

Now the discovery

它在这里呢

是通过nagos服务名称进行一个

发现了

去找到呢

对应的

要转发的服务节点信息

Vocate

Enable

等于chew是什么意思呢

它是允许通过服务名称进行路由转发访问

也就是说咱们呢

就不需要去指定具体的IP

对不对

如果指定IP呢

将来的服务发生了变更和修改呢

我们的应用服呢

也接下来调整会比较麻烦

所以在这里呢通过名称

第一呢

既可以保证它的高可用

第二的话呢

咱们呢

又可以方便

去做后续的维护

那下面呢就是路由的具体配置

路由这一块呢

是什么意思呢

这个的话呢

是路时对不对

路时的话呢

它是一个复数

顾名思义呢

在这里面它可以配置多条路由

对吧

那么以这个横线

开头的话呢

就是一组路由配置

咱们可以看到

在这里面的话呢

有两组对不对

那么两组路由配置的话呢

他们开头是有横线

作为开始

注意中间的话呢

有个空格

然后的话呢

是它的一个ID标识

这个的话呢

因为有多个组别

必须要给它一个唯一的标识

接着的话呢就是它的UI

你要去请求

哪个服务

对不对

那么我们呢

是针对于用户服务以及认证服务

做了一个路由转发

所以呢咱们要将这两组配置呢

加入进来

在这里呢

一个是用户服务

一个是认证服务

那么Practice

这个是什么意思呢

也就是说

用户服务里面

它肯定会有很多的资源接口

对不对

比如说用户的登录啊

用户的注册

那么通过这个的话呢

它会去指定

哪些路径

哪些接口的话呢

要进行转发

那在这里

这个User

在这里呢

这个User

后面呢-星星

它的意思就是说

只要

在我们Gateway当中

它是以User-星星去访问的

比如说咱们呢

可以例举一下

如果说

客户端在这里呢

它发了个请求

然后呢

咱们呢比如说咱们的那个

网关服务

它呢如果是端口是1000

那它访问到我们网关服务呢是User

然后呢Login

那在这里呢

它能匹配到哪一条啊

是不是匹配到这一条

因为这里呢是User开头的

看到没有

然后的话呢后面星星

就是User后面呢

可以跟任何的路径

那在这里呢它匹配到这条规则之后呢

就会转发到哪里呢

转发到咱们的

User服务

这个呢是它Path配置的一个

主要的作用

那在这里也可以配置多个Path

比如说

你在这里呢

又有一些那个开放型的接口对不对

还有一些接口的话呢

是有

比如说用户的一些管理啊

那么涉及到一些

权限控制的一些接口

你可以呢

都分门别类的把它呢

做不同的控制

再往下面呢是认证服务

认证服务同样的道理

在这里面的话呢

只要以User开头的路径访问

都会转发到User认证服务当中

那么Message在这里呢

如果说

咱们在这里

不需要特殊的这种请求

方法类型的控制

咱们在这里不需要开启

这个呢也是做过摸索和尝试的

如果你在这里的话呢

指定的话

那它呢

就只会支持你所指定的这种请求类型

比如说

在这里有Get Compose

对不对

那么

如果用户的话呢

它发起了一个Delete的这种类型请求

这个是不会接收

也不会进行转发的

这一点呢要明白清楚

下面的话呢就是Login Level

它的一个

日志级别的控制

这里是Info的级别

好

在这里呢就是

咱们

网关服务的一个核心类实现

以及呢

它整体的工程配置

我们呢是定义了两个路由

对不对

一个呢是Stop User

映射路径为User开头的

转发至用户服务

另外一个呢是Cheat Auth

它的映射路径呢是干Auth

转发至认证服务

注意呢不要开启Message

给你Get或Post

默认咱们可以允许所有的请求方式

如果你不指定它什么请求类型

都可以支持

比如像Put Delete

这个呢认证的时候

不用的

比如说

咱们要去申请Token对不对

咱们要去Refresh Token

在这里面的话呢

可能会有不同的请求类型

所以呢咱们建议呢

还是先让它开启

如果生产级别呢

有特殊严格的要求呢

咱们再按具体要求去做相应的配置

好

这一块呢

咱们呢就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于 Spring Cloud Gateway 网关服务的实战教学，重点讲解了如何集成 Druid 监控功能。讲师通过 IntelliJ IDEA 开发环境，演示了如何为网关服务配置依赖、创建自定义过滤器、配置路由规则以及启动服务进行验证。视频内容覆盖了从项目结构、依赖管理、核心代码实现到配置文件设置的完整流程，旨在帮助开发者掌握 Spring Cloud Gateway 的核心功能和监控能力。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开场，展示项目结构，重点介绍 `bulls-stock-gateway` 模块。
*   **00:05 - 00:15**: 展示 `pom.xml` 文件，讲解 Spring Cloud Gateway 的核心依赖 `spring-cloud-starter-gateway` 和服务发现依赖 `spring-cloud-starter-alibaba-nacos-discovery`。
*   **00:15 - 00:25**: 在 `src/main/java` 目录下创建 `filters` 包，并编写自定义过滤器 `StockRequestGlobalFilter`。
*   **00:25 - 00:35**: 编写 `StockRequestGlobalFilter` 类，实现 `GlobalFilter` 接口，用于统一处理请求头中的 `Authorization` 信息。
*   **00:35 - 00:45**: 编辑 `application.yml` 配置文件，定义两个路由规则：`/user/**` 路由到 `stock-user` 服务，`/oauth/**` 路由到 `trade-auth` 服务。
*   **00:45 - 00:55**: 配置日志级别，设置 `logging.level.root: info`。
*   **00:55 - 01:05**: 通过 `Day7.md` 文档回顾核心知识点，包括自定义过滤器、路由配置和启动验证步骤。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档 (Day7.md)**:
    *   **章节 3.6 启动与验证**: 详细说明了启动网关服务的端口（10680）和申请 token 的访问地址。
    *   **章节 3.5 核心类实现说明**: 介绍了 `StockRequestGlobalFilter` 的作用和实现逻辑。
    *   **章节 3.3 工程结构**: 展示了项目目录结构，包括 `src/main/java` 和 `src/main/resources`。
    *   **章节 3.2 Druid集成配置**: 提及了 Druid 监控的配置项，如 `filters: stat, wall, log4j` 和 `stat-view-servlet` 的配置。

*   **代码片段**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-alibaba-nacos-discovery</artifactId>
        </dependency>
        ```
    *   **`StockRequestGlobalFilter.java`**:
        ```java
        @Component
        public class StockRequestGlobalFilter implements GlobalFilter, Ordered {
            @Override
            public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
                String authentication = exchange.getRequest().getHeaders().getFirst("Authorization");
                if (StringUtils.isEmpty(authentication)) {
                    log.info("enter stockRequestGlobalFilter filter method: " + authentication);
                    exchange.getRequest().mutate().header("Authorization", authentication);
                }
                return chain.filter(exchange.mutate().build());
            }

            @Override
            public int getOrder() {
                return 0;
            }
        }
        ```
    *   **`application.yml` 路由配置**:
        ```yaml
        gateway:
          discovery:
            enabled: true
          routes:
            - id: stock-user
              uri: lb://stock-user
              predicates:
                - Path=/user/**
            - id: trade-auth
              uri: lb://trade-auth
              predicates:
                - Path=/oauth/**
        logging:
          level:
            root: info
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖管理** (00:05 - 00:15)
    *   讲师在 IntelliJ IDEA 中打开 `bulls-stock-gateway` 项目，展示其目录结构。
    *   在 `pom.xml` 文件中，讲师添加了 Spring Cloud Gateway 和 Nacos 服务发现的依赖，并演示了 Maven 依赖的自动解析过程。

*   **场景二：自定义过滤器开发** (00:15 - 00:25)
    *   讲师在 `src/main/java/com/icast/trade/bulls/stock/gateway/filters` 目录下创建 `StockRequestGlobalFilter.java` 文件。
    *   讲师编写了 `StockRequestGlobalFilter` 类，实现了 `GlobalFilter` 接口，用于在请求进入网关时，检查并设置 `Authorization` 请求头。

*   **场景三：路由配置与日志设置** (00:35 - 00:45)
    *   讲师编辑 `application.yml` 文件，配置了两个路由规则，分别将 `/user/**` 和 `/oauth/**` 路径转发到对应的服务。
    *   讲师设置了 `logging.level.root: info`，以便在服务启动后能够看到详细的日志信息。

*   **场景四：启动与验证** (00:45 - 01:05)
    *   讲师通过 `Day7.md` 文档回顾了启动网关服务的步骤，包括启动端口和申请 token 的地址。
    *   讲师强调了在配置文件中注释掉 `Method=GET,POST` 的重要性，以避免认证服务被未授权访问。

---

以上是根据视频画面整理出的技术课程结构化分析。
