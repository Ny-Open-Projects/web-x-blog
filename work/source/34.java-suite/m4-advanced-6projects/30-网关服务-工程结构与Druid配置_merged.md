# 30-网关服务-工程结构与Druid配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们来讲解一下工程结构的说明

上面咱们搭建了认证服务

以及用户资源服务

并且做了测试验证

能够成功使用OS2进行了认证健全

那么作为微服来讲的话

我们有两种健全处理方案

第一种我们可以通过网关进行了统一健全

另外一种就是由各自的微服节点

去做一个健全处理

在这里咱们就采用了各自的微服节点

去进行了健全处理

也是为了保证各微服节点

他们的一个安全可靠性

另外的话

那么是由网关进行统一转发处理

网关在这里的话

它不会去做健全的一个校验

它只会去负责我们请求的一个统一转发

这个就是网关所要做的事情

接下来我们就要改进网关服务

通过路由去转发

能够支持OS2的一个认证使用

我们该怎么去改造呢

在这里经过实践和摸索

如果说我们网关只是转发

这样做起来就会比较简单

按照我们OS2的设计方案

Spring Cloud Gateway

它可以不用去集成了Spring Security

因为在这里我们做过尝试

网关的职责

它只是接收客户的请求并进行转发

因为你在这里并不需要去做OS2健全

所以我们不需要Spring Security的组件

这个只是在网关层面

但是微服

因为你自身各微服节点要进行健全处理

所以微服它还是需要Spring Security的OS2组件

所以健全这一块

我们可以不用放在网关去做对应的处理

各个微服去直接作为资源服务进行认证

也就是说如果发送的受保护的资源请求

那么微服它会去直接通过你发送来的token

通过网关这边转发接收过来的token

然后再发送给认证服务做对应的一个交易

这样也可以避免微服直接对外暴露产生的安全性问题

大家想想

如果说咱们在这里通过网关统一健全

对不对

如果说各微服节点在外网上面进行了暴露

那么其他的一些第三方访问

他们就可以直接访问我们的微服的资源接口

所以在这里咱们要学习

发请求实现了AuthTutor认证

好

在这里还要备注说明一下

工程当中存有MOSO实现的一些代码和配置

已经做了注释

这样的话流存在代码当中

是为了便于大家的一个扩展

如果后续大家要实现更丰富的一些功能的话

也可以借鉴和参考

好

那么接下来咱们先来实现了德路1的集成配置

那么德路1的集成配置是在用户服务工程去集成了德路1的监控台配置

对不对

这个咱们之前在用户服务实现的时候

已经加入进去了

但是当时并没有做一个过多详细的讲解

对不对

那么在上一讲咱们对监控参数做了一个详细的说明

大家可以再去根据我们的实际配置

然后结合这个参数配置说明表去做一个对比和学习

知道咱们是如何去配置

如何去配置

好

好

好

好

这一块就是德路1的一个监控集成配置

那么咱们是把它放在用户服务当中

对不对

Gateway的话是不需要

因为Gateway的话

它只是负责一个转发

并不需要跟数据库产生连接和交互

那么咱们来看一下

因为我们是要配置德路1的监控管理后台

所以在这里咱们要注意一下

怎么去开启它的监控管理后台

主要是StateViewSolid

我们可以找到

在这里面的话就是它的监控管理后台相关的一些设定

比如说你要开启它的访问路径

对不对

这个访问路径的话

一定要指定正确

我们就根据这个路径进行了相应的访问

然后它的一个IP白名单的设定

IP的黑名单

下面的话就是是否禁用HTML页面上的ResultAll功能

这个的话咱们可以不用禁用

然后就是它的登录名

登录密码

这些都是一些基础必要性的配置

咱们按照这用户服务工程当中的配置来去实践就可以了

接下来的话

咱们就要去实现了它的一个核心类

这个核心类的话

就是Store Gateway的启动

以及它的全局过滤器

虽然咱们在这里并不需要去集成SpringSecurityOS2

但是咱们为了要支持OS2的这种认证录音

我们就要去实现了这个核心类的转发

我们在Gateway上面还是要做一定的处理和转换

那么就通过FILTER这个过滤器去帮助我们实现OS2的认证信息的转发和处理

因为OS2认证的时候

它会附带一些额外信息

那么我们要保证它认证的一个校验完整性

所以要在过滤器当中做一些处理

能够将它上游的请求信息

就是将客户端包括来的请求信息的源源盆盆的

然后发送给我们的应用服务

在这一块就是对工程结构以及德鲁伊它的一个集成配置说明

那么接下来的话咱们就会去实现了它的一个核心类

以及相关的配置

这一讲咱们先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个微服务架构中“网关服务”与“Druid监控”集成的实战教程。讲师首先回顾了用户服务的工程结构，然后重点讲解了如何在网关服务中集成Druid监控，以实现对后端服务的性能监控和安全访问控制。核心内容包括：配置Druid数据源、设置监控过滤器（`stat`, `wall`, `log4j`）、配置Druid监控的Web视图（`stat-view-servlet`）以及设置登录凭证。视频通过IDE（IntelliJ IDEA）展示配置文件 `bootstrap.yml` 的详细内容，并解释了每个配置项的作用，旨在帮助开发者掌握在Spring Cloud Gateway网关中集成Druid监控的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示用户服务的工程结构，引出本节主题：改进网关服务以支持OAuth2认证。
*   **00:05 - 00:15**: 过渡到“第4章 网关服务与Druid监控数据”，并介绍本节目标：集成Druid监控。
*   **00:15 - 00:30**: 展示 `bootstrap.yml` 文件，讲解Druid数据源配置（`type`, `driver-class-name`, `url`, `username`, `password`）。
*   **00:30 - 00:45**: 继续讲解Druid连接池配置，包括 `initial-size`, `min-idle`, `maxActive` 等参数。
*   **00:45 - 01:00**: 讲解Druid监控过滤器配置，包括 `filters: stat, wall, log4j`。
*   **01:00 - 01:15**: 讲解Druid监控的Web视图配置（`stat-view-servlet`），包括 `url-pattern`, `exclusions`, `allow`, `deny` 等。
*   **01:15 - 01:30**: 讲解Druid监控的登录凭证配置（`login-username`, `login-password`, `enabled`）。
*   **01:30 - 01:45**: 过渡到“3.5 核心类实现说明”，展示 `StockGatewayApplication` 启动类。
*   **01:45 - 02:00**: 展示 `StockRequestGlobalFilter` 全局过滤器的代码结构。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT内容**:
    *   左侧导航栏显示了课程大纲，包括“第3章 用户服务”和“第4章 网关服务与Druid监控数据”。
    *   当前章节为“3.4 Druid集成配置”和“3.5 核心类实现说明”。

*   **代码内容**:
    *   **Druid数据源配置** (位于 `bootstrap.yml`):
        ```yaml
        spring:
          datasource:
            type: com.alibaba.druid.pool.DruidDataSource
            driver-class-name: com.mysql.cj.jdbc.Driver
            url: jdbc:mysql://192.168.19.150:3306/trade_stock?useUnicode=true&characterEncoding=utf8
            username: root
            password: 654321
        ```
    *   **Druid连接池配置** (位于 `bootstrap.yml`):
        ```yaml
        # 连接池配置
        initial-size: 5
        min-idle: 5
        maxActive: 20
        maxWait: 60000
        timeBetweenEvictionRunsMillis: 60000
        minEvictableIdleTimeMillis: 300000
        validationQuery: SELECT 1 FROM DUAL
        testWhileIdle: true
        testOnBorrow: false
        testOnReturn: false
        poolPreparedStatements: true
        maxPoolPreparedStatementPerConnectionSize: 20
        ```
    *   **Druid监控过滤器配置** (位于 `bootstrap.yml`):
        ```yaml
        filters: stat, wall, log4j
        # 通过connectProperties属性来打开mergeSql功能，慢SQL记录
        connectionProperties: druid.stat.mergeSql=true;druid.stat.slowSqlMillis=5000
        ```
    *   **Druid监控Web视图配置** (位于 `bootstrap.yml`):
        ```yaml
        web-stat-filter:
          enabled: true
          url-pattern: /*
          exclusions: "*.js,*.gif,*.jpg,*.bmp,*.png,*.css,*.ico,/druid/*"
        stat-view-servlet:
          url-pattern: /druid/*
          # IP白名单(没有配置或者为空，则允许所有访问)
          allow:
          # IP黑名单 (存在共同时，deny优先于allow)
          deny:
          # 禁用HTML页面上的“Reset All”功能
          reset-enable: false
          # 登录名
          login-username: admin
          # 登录密码
          login-password: admin123
          # 监控后台开关，开启后可通过后台管理查看
          enabled: true
        ```
    *   **核心类实现**:
        *   **启动类 `StockGatewayApplication`**:
            ```java
            @SpringBootApplication
            @EnableDiscoveryClient
            @ComponentScan(basePackages = {"com.icast"})
            public class StockGatewayApplication {
                public static void main(String[] args) {
                    SpringApplication.run(StockGatewayApplication.class, args);
                }
            }
            ```
        *   **全局过滤器 `StockRequestGlobalFilter`**:
            ```java
            @Component
            @Log4j2
            public class StockRequestGlobalFilter implements GlobalFilter, Ordered {
                private static final String HEADER_NAME = "X-Forwarded-Prefix";
                // 通过filter来自定义配置转发信息
                @Override
                public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
                    // 过滤器实现逻辑
                    return chain.filter(exchange);
                }
            }
            ```

---

### 4) 关键场景与演示描述

*   **场景一：工程结构展示 (00:00-00:05)**
    *   讲师在IDE中打开 `Day7.md` 文件，展示“第3章 用户服务”的工程结构。
    *   通过目录树展示 `stock-gateway` 项目，包括 `src/main/java` 和 `src/main/resources` 目录。
    *   说明了网关服务的职责是转发请求，并引出本节将集成Druid监控。

*   **场景二：Druid配置文件详解 (00:15-01:30)**
    *   讲师在IDE中打开 `bootstrap.yml` 文件，逐段讲解配置。
    *   **数据源配置**: 展示了 `spring.datasource` 下的 `type`, `driver-class-name`, `url`, `username`, `password`。
    *   **连接池配置**: 详细解释了 `initial-size`, `min-idle`, `maxActive`, `maxWait`, `timeBetweenEvictionRunsMillis`, `minEvictableIdleTimeMillis`, `validationQuery` 等参数。
    *   **监控过滤器**: 重点讲解了 `filters: stat, wall, log4j`，并解释了 `connectionProperties` 用于开启慢SQL记录。
    *   **监控Web视图**: 详细讲解了 `web-stat-filter` 和 `stat-view-servlet` 的配置，包括 `url-pattern`, `exclusions`, `allow`, `deny`, `login-username`, `login-password`, `enabled`。
    *   **演示**: 讲师使用鼠标高亮并逐行解释配置项，如 `maxActive: 20`、`login-password: admin123` 等。

*   **场景三：核心类实现 (01:30-02:00)**
    *   讲师切换到“3.5 核心类实现说明”。
    *   展示了 `StockGatewayApplication` 启动类，解释了 `@SpringBootApplication`, `@EnableDiscoveryClient`, `@ComponentScan` 注解的作用。
    *   展示了 `StockRequestGlobalFilter` 全局过滤器的代码结构，解释了 `@Component`, `@Log4j2`, `implements GlobalFilter, Ordered` 等注解和接口。
    *   通过代码高亮和注释，说明了过滤器的用途和实现方式。

整个视频通过IDE界面和代码高亮，以清晰、直观的方式讲解了如何在Spring Cloud Gateway网关中集成Druid监控，为开发者提供了实用的配置参考。
