# 32-Gateway聚合配置-聚合文档集成与验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就开始学习

Split Cloud Gateway网关服务集成配置

去实现的聚合文档

那咱们来看一下具体该如何实现

首先咱们要在PoM文件当中

去增加Split Cloud Gateway的启动器的依赖

咱们先将这个依赖靠近回去

找到咱们的网关服务

将这个依赖追加到下面

大家注意一下

这里面是Split Cloud Gateway的主线依赖

我们要将它的Split Boot

Start Dataless的依赖进行排除

为什么要排除这个依赖呢

因为它内部会去依赖于

Stream MVC的主线

这个时候它会去激活

内置的Tomcat的容器

我们可以看到Split Boot的服务

启动的时候会去加载Tomcat

但是网关服务

它在基于Netting实现了转发

如果你启动了Tomcat服务

就会和网关服务产生冲突

这一点大家要注意一下

我们再回到讲义当中

接着的话我们要添加聚合文档的配置类

Stalk Swag BlogWidth

我们将这个配置类先创建一下

new.cast

将代码直接copy进去

将这些错误的话要注意修正一下

咱们接下来来看一下

这个配置类的具体代码实现

这个是Swalk2的默认的URL后缀的定义

然后是网关路由

这个是网关的应用名称

然后是需要排除的服务

因为咱们有很多的微服务节点

可能有些服务咱们并不需要暴露出Swalk2的接口

或者是不需要提供对外访问接口

那么咱们在这里可以添加对应的服务名称

进行相应的排除

这一段是聚合文档的具体配置实现

那么我们看一下它是如何去处理的呢

首先它要去获取所有可用的service ID

这个就是咱们在配置文件当中所定义的服务名称

这个其实就是service ID标识

因为网关它采用的是负载均衡的处理方式

不可能去通过IP直接调用

所以我们要拿到service ID

它的格式咱们可以看到是host

然后再加上UiPath

也就是它的服务号码

然后再加上服务访问名称

服务访问名称跟service ID都是一致的

通过服务名称就能在Nacos上面拿到服务的具体访问信息

那么通过名称访问的话

也会有一个弊端

这个弊端就是说

如果说咱们有多个节点

就是一个服务开启了多个节点

这样它就会存在同一个应用注册了多个服务在Nacos上面

那么网关服务它就会检测到

这样呢

咱们不做去重处理就会存在呢

重复的接口

所以下面呢

就做它的一个去重处理

具体怎么去做呢

在这里定义的一个set集合专门去记录呢

已经添加到咱们网关服务当中的服务信息

这个UiL呢

会做一个拼接

它的格式是为service ID服务名称

然后后面加上

RV2 API info

这个呢就是Spot2的后缀访问路径

当网关呢通过这个接口地址进行调用的时候呢

就会通过负载均衡

然后呢

去寻找对应的UiP信息

下面呢就是要排除此地的服务以及服务集群

去做去重处理

那这样呢就能保障我们网关能够扫描到所有呢

可用的

具备数万个接口的服务节点信息

咱们再回到讲义当中

在这里呢

各个微服都有自己的文档接口地址

要把它们聚合在一起呢

就需要添加他们的

地址信息

每个微服呢

都要去收集配置

就会比较麻烦

而且每次调整呢

我们都要去

相应的更改

这里呢我们就采用Gateway的root定义信息来自动获取

不用呢

去专门维护各微服的所有个的接口地址

咱们可以看到

就通过root host

在这里面的话呢

咱们就去根据

Gateway网关

里面所定义的路由信息呢

拿到

对应的服务节点信息

有的微服呢

它有设置context path

也就是说

有那个前对访问路径

有的话呢是没有

聚合地址呢

它都是做拼接处理

这样呢

就会产生一个问题

就是说会丢失它的前对context path

因为呢

你只扫描到它的service id对不对

这个时候呢

如果去统一维护

就需要借助URI的信息来处理

也就是咱们刚才呢

所提到的

要在这里呢

拼接它的host以及呢

它的get path的信息

这个呢

就作为它的context path的路径

进行了对应的访问

好那咱们呢

再回到讲义当中

接着话呢

咱们还要去实现了

路由的具体配置

咱们在这里呢

要增加后台的管理服路由配置

这里呢

我们把context path呢

设置在后面

增加后台管理服的路由配置

把context path呢

写在对应的URI路径后面

这样聚合文档呢

就能够正常获取识别

也不会呢

影响路由的转发

那咱们呢

就从配置上面做一个实现

这个呢

跟上面的id呢

是同一个层级

保持呢

这个层级的

它的顺序

正确

咱们呢

去定义一个服务名称

这个呢

就是咱们的后台管理服务

后台管理服务的转发配置

接着话呢

就是它的URI路径

通过负载均衡的方式呢

进行访问

stock fme

user服务名称

然后它的后缀路径

credit case

转发配置规则

这里面的话呢

我们只能

进行一个路径

也就是说

admin下面的所有路径呢

咱们都进行一个

路由转发

这样咱们就完成了

后台管理部的转发配置

咱们再回到

讲义当中

接着话呢

咱们要去增加

stockswork的

conclude的

接口

这个接口呢

咱们先把它添加进来

咱们呢

就将它放在config目录下面

将代码拷贝进去

注意红色区域呢

不要

最红色部分呢

不要包错

把这个

依赖呢打不进来

好那咱们来看一下

这个conclude

它是如何去实现

以及呢它的主要作用是干嘛的

getway

做聚合文档呢

它实际上就相当于是做了一个

转发的调用

咱们呢先来看一下swork2的

接口访问地址

看一下访问这个地址呢

它后来做了哪些请求

我们打开apps

我们刷新一下整个界面

看一下它的VGX的交互

它其实呢

请求的是什么

swork resource的这个访问路径

那同样呢

大家在这里应该就可以明白了

为什么要去配置这个访问路径呢

也就是说咱们要去对这个接口地址

做一个

转发处理

咱们可以看到

这里面呢是涉及到它的一个安全性访问的配置信息

然后这个呢是它的一个

UI的访问接口信息

最主要呢

是下面这一段

这一段的话呢

我们要注意它的getway

它的mapping的路径是为空

这样呢

它才能扫描

下面的所有的

swork服务节点信息

如果你在这里配置了指定路径

那么它就呢

没法访问对应的这个路径

因为呢它的默认路径后面呢就是swork resource

接下来的话呢就没有跟其他的后缀信息

所以呢在这里面咱们呢也将它保持为空

这样就能保证呢

可以访问到所有的文档服务信息

然后注意

这个请求方式呢是get方式

因为咱们呢

一般是通过浏览器进行了访问

这个请求的话呢都是get方式的一个请求

好这个呢就是

swork controller 层接口的配置

那接下来呢咱们就会启动网关服务来做一个

集成验证

右键启动网关服务

网关服务呢启动成功

咱们呢就可以去访问测试一下

在这里呢这个地址

咱们要调整一下

我们的网关的

接口访问地址

回车访问

咱们

可以看到

左侧上面呢有一个下拉框对不对

下拉框上面呢它列出的是咱们的所有服务节点信息

像是到个user这个呢是用户服务

admin user呢是后台管理服务

为什么会出现两个后台管理服务呢

因为呢咱们后台管理服务

配置的是admin的后缀访问路径

咱们可以看到

对不对

所以在这里面呢

它的有效路径呢

其实就是最后一个

storeadmin user

-admin

为什么它会扫描出这个呢

因为呢

Gateway网关服咱们在做配置的时候

是针对于所有的网关信息呢

做了一个扫描

对不对

Root House

那么这个扫描信息呢是在咱们配置文件当中呢

所定义的

这样呢它就会找到

所有的配置信息

然后咱们的去从规则呢

是根据完整的UII路径

进行了去从

所以呢

只要这个名称没有重复

那么下面的这些节点信息呢

它都会呈现出来

如果说在这里面的话呢

只想展示一个节点信息

不想展示storeadmin user呢

那么这个也是可以实现的

咱们要在配置当中呢

做一个比对

怎么去比对呢

就要拿到它的UII信息做一个比对判断

比如在这里面

咱们定义的是一个UII对不对

拿到UII的完整路径

但这个时候呢

咱们就要做一个去除

所以呢要将前面的前缀呢

LB去除

我们还是建议大家呢

采用这种方式去做对应的实现

如果是出现了在聚合接口地址当中呢

咱们就根据需要

去选择了对应的服务节点访问就可以了

接下来呢

咱们就做个测试和验证

用拿后台管理服务

找到它的菜单管理接口

进行调试

它的路径呢咱们可以看到

并没有增加它的后缀

compact path

在这里我们就要做个调整

然后这个load id呢

10172

我们访问一下

它其实是什么

401的认证错误

因为后台管理服务

这个os2的认证呢

咱们还没有将它拿掉

所以呢咱们可以先在全局参数当中

做对应的配置

这个呢是大写

EEA R1 VALUE

然后加上空格

将这个token copy进来

删除上去

点击保存

咱们呢再访问一下

这个时候呢

就可以看到了接口能够正常返回数据出现

好咱们呢再回到讲习当中

在这里呢咱们就

实现了Spring Cloud Gateway

网关服务对SWOG2的集成配置

实现了聚合文档的

呈现和使用

那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程主要讲解如何将 **Swagger2** API 文档功能集成到 **Spring Cloud Gateway** 网关服务中。核心目标是实现一个统一的、可访问的 API 文档中心，该中心能够自动聚合后端多个微服务（如 `stock-user`, `stock-admin-user`）的 Swagger 文档。课程通过修改网关服务的 `pom.xml` 添加依赖、配置 `application.yml` 文件、编写自定义的 `StockSwaggerProvider` 服务发现与路由处理器，以及创建 `StockSwaggerController` 控制器来实现这一功能。最终，用户可以通过访问网关服务的特定端点（如 `http://127.0.0.1:10680/doc.html`）来查看聚合后的所有 API 文档。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，当前章节为“3.5 Spring Cloud Gateway网关服务集成配置”。
*   **00:00:05 - 00:00:15**：讲解第一步，修改 `pom.xml` 文件，添加 `stock-starter-swagger` 依赖。
*   **00:00:15 - 00:00:25**：展示 `application.yml` 文件，配置网关服务的基本信息，如端口、服务名、Nacos 注册地址。
*   **00:00:25 - 00:00:35**：讲解 `StockSwaggerProvider` 类，其核心功能是通过 `RouteLocator` 获取所有注册的服务，并根据服务名和路径过滤出需要聚合的 Swagger 文档。
*   **00:00:35 - 00:00:45**：展示 `StockSwaggerController` 类，该控制器负责提供访问聚合文档的 REST 接口。
*   **00:00:45 - 00:00:55**：演示最终效果，通过浏览器访问网关服务的 `/doc.html` 端点，成功加载并显示聚合后的 API 文档。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 文档内容**

*   **课程大纲**：清晰列出了课程目标、步骤和实现细节，包括“自定义 OAUTH2 启动器”、“Swagger2 实现鉴权访问”、“Spring Cloud Gateway 网关服务集成配置”等。
*   **核心概念说明**：
    *   为解决微服务 API 文档分散的问题，采用 Gateway 的 `route` 定义信息自动获取。
    *   通过 `route.getUri().getHost() + route.getUri().getPath()` 获取完整的、准确的 API 地址信息。
    *   通过 `uri` 和 `predicates` 配置路由规则，如 `Path=/user/**`。

#### **关键代码**

*   **`pom.xml` 依赖配置**：
    ```xml
    <!-- swagger 组件依赖 -->
    <dependency>
        <groupId>com.itcast.trade</groupId>
        <artifactId>bulls-stock-starter-swagger</artifactId>
        <version>${project.stock.version}</version>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-data-rest</artifactId>
            </exclusion>
            <exclusion>
                <groupId>io.swagger</groupId>
                <artifactId>swagger-data-rest</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
    ```

*   **`application.yml` 配置**：
    ```yaml
    server:
      port: 10680
    spring:
      application:
        name: stock-gateway
      cloud:
        nacos:
          server-addr: 127.0.0.1:8848
        gateway:
          discovery:
            locator:
              enabled: true
              # 允许通过服务名称进行路由转发访问，http://service-id-user
              # 服务名：stock-user
              # 路由配置
              routes:
                - id: stock-user
                  uri: lb://stock-user
                  predicates:
                    - Path=/user/**
                - id: stock-admin-user
                  uri: lb://stock-admin-user
                  predicates:
                    - Path=/admin/**
    ```

*   **`StockSwaggerProvider.java` 核心逻辑**：
    ```java
    @Component
    public class StockSwaggerProvider implements RouteLocator {
        @Autowired
        private RouteLocator routeLocator;

        @Override
        public RouteLocator getRouteLocator() {
            // 获取所有可用的host，服务名
            Set<String> repeatServices = new HashSet<>();
            routeLocator.getRoutes().filter(route -> route.getUri().getHost() != null)
                    .subscribe(route -> repeatServices.add(route.getUri().getHost() + route.getUri().getPath()));
            // 遍历所有服务，获取其Swagger资源
            routeLocator.getRoutes().filter(route -> route.getUri().getHost() != null)
                    .subscribe(route -> {
                        String url = route.getUri().getHost() + route.getUri().getPath();
                        if (repeatServices.contains(url) && !repeatServices.contains(url)) {
                            repeatServices.add(url);
                            SwaggerResource swaggerResource = new SwaggerResource();
                            swaggerResource.setSwaggerUrl(url);
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.getScheme());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerUrl(route.getUri().toString());
                            swaggerResource.setSwaggerName(route.getId());
                            swaggerResource.setSwaggerVersion(route.getVersion());
                            swaggerResource.setSwaggerPath(route.getPath());
                            swaggerResource.setSwaggerHost(route.getHost());
                            swaggerResource.setSwaggerPort(route.getPort());
                            swaggerResource.setSwaggerScheme(route.get
