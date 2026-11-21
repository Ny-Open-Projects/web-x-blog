# 29-Gateway聚合配置-自定义OAuth2启动器封 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们去实现自定义OS2的启动器的封装和配置

首先咱们要去新建了一个模块

咱们回到代码当中

在咱们的自定义启动组件下面

去创建一个新的模块New Model

点击Next

这个名称咱们就叫做stock.start

这个是横线

然后是OS2

点击Next

点击Finish

因为之前咱们对OS2的集成配置做了一个讲解

在这里咱们就来快速配置和实现

咱们将它的依赖加入进来

加上Defenses标签

咱们大概看一下它需要哪些组件依赖

这个跟咱们之前的配置基本上都是类似的

像Spring Security相关的一些组件依赖

然后Spring Security OS2的自动化配置依赖

好

添加完成之后咱们还要去添加它的自动化配置类

在下面去创建一个包

New Package

这个就叫com.idcast.trad

stock.start.os

咱们创建一个包

New Package

com.idcast.boss.stock.os

然后咱们去创建它的自动化配置类

New

加上cast

创建完成之后咱们将代码直接扩制过来

做替换

咱们来具体看一下这个代码是如何去配置和实现的

在这里咱们将这个错误先消除一下

这个要导入Longboard的依赖

我们从上面看一下它的注解

这些注解的话我们之前都讲过了

对不对

这个要开启认证服务

然后要开启GlobalMask的Security

方法级别的一个安全扫描

然后这个是基于条件化的属性配置

也就是说我们在工程代码当中

如果是配置了对应的属性

下面的代码配置它就会扫描和生效

这个是一个属性的自动注入化配置

它会去读取对应的属性前缀

比如说这个属性前缀

它们配置Security,OS2,Client

然后下面的话再配置了

Enogy,ULS

那么它就会默认截取前面的属性

比如说在这里面是Enogy,ULS

它就会截取这一端

然后拿后面的属性跟代码当中的属性做一个匹配

如果是名称匹配上的话

那么它就会将它的值注入进去

好

这个注解是这么一个作用

那咱们来看一下它下面代码有哪些配置

这个是一个远程调用的

采用了Resttemplar的方式进行attp方式的配置

远程调用

下面是支援服务的安全性配置

咱们既然要做成了自定义启动器

那么就是统一的封装和配置

但是每个服务我们要保障给它一定的扩展性

对不对

每个服务它有些地址和接口可能不需要做认证

那怎么处理呢

我们就通过Enogy,ULS这个属性

能够让各自的服务去配置各自想要去排除的接口

这些话就是无需认证的一些ULS接口地址

下面的话

是一个公用性的配置

咱们可以看到

它会将Aggregator开头的路径

还有SWOG开头的地址路径以及静态支援路径全部放全

这个就不需要进行一个政权认证处理

然后其他的请求的话

都需要做健全处理

下面的话

就是它的登录

统一的一个登录页面

然后统一的一个登录失败的返回接口地址

默认成功的跳转地址

这些话都可以作为一个公用性的配置

对不对

放在咱们的

自定义启动器配置代码当中去做统一的实现

那么每个应用服务

就不需要再去做重复的配置

下面是Let'sTemplate的一个配置

这个是支持负载均衡的一个对应方式处理

load balance

那么我们可以看到

它会将这个并使力注入到上面的配置当中

会将它设置进去

这个封装

最重要的

咱们要知道

它的一些共性方面的配置

对不对

一些的话

个性方面的一些配置

我们呢

也要预留一些扩散方式

能够呢

让各自微服去做对应的实现

最后呢

咱们还增加它的启动扫描配置

在这里呢

创建一个文件目录

Meta-inf

创建一个配置文件

new file screen.fztu.ies

这个呢

咱们就直接copy过来

对于这个路径呢

我们要重新修改一下

copy reference

确保路径是正确的

conceal

可以找到

好

在这里呢

咱们就完成了

自定义OS2的启动器的封装

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段属于一个关于 Spring Cloud 微服务架构的高级技术课程，具体聚焦于 **如何自定义一个 OAuth2 认证启动器（Starter）**，并将其与后台管理服务集成。讲师通过 IntelliJ IDEA 开发环境，演示了从创建项目、配置 Maven 依赖、编写核心配置类 `AutoOAuth2Configuration`，到最终实现资源服务器（Resource Server）的权限控制策略的全过程。视频中特别强调了如何通过 `@ConfigurationProperties` 注解实现配置属性的自动绑定，并通过 `spring.factories` 文件实现自动配置（Auto-Configuration）的机制。整个过程旨在构建一个可复用的、与 Swagger2 集成的 OAuth2 认证模块。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:15**: 视频开场，讲师在 Typora 文档中概述了本节内容，即“自定义 OAuth2 启动器”，并说明将使用 `stock-starter-oauth2` 工程作为示例。
*   **00:00:16 - 00:00:30**: 讲师在 IDEA 中打开 `stock-starter-oauth2` 项目，展示其目录结构，并开始编辑 `pom.xml` 文件。
*   **00:00:31 - 00:00:45**: 讲师在 `pom.xml` 中添加了两个 Spring Cloud Security 的依赖项：`spring-cloud-starter-oauth2` 和 `spring-cloud-starter-security`。
*   **00:00:46 - 00:01:00**: 讲师将光标移至 `AutoOAuth2Configuration.java` 文件，准备编写核心配置类。
*   **00:01:01 - 00:01:15**: 讲师在 `AutoOAuth2Configuration.java` 中定义了类的包名、注解和成员变量，包括 `RestTemplate` 和 `ignoreUrls` 列表。
*   **00:01:16 - 00:01:30**: 讲师开始编写 `configure` 方法，使用 `HttpSecurity` 对象配置权限规则。
*   **00:01:31 - 00:01:45**: 讲师在 `configure` 方法中添加了对 `ignoreUrls` 的处理逻辑，允许指定路径无需认证。
*   **00:01:46 - 00:02:00**: 讲师继续配置权限规则，将 `/actuator/**`, `/v2/**`, `/doc.html`, `/swagger-ui.html`, `/css/**` 等路径设置为公开访问。
*   **00:02:01 - 00:02:15**: 讲师配置了登录页面和错误页面的跳转地址。
*   **00:02:16 - 00:02:30**: 讲师切换到 Typora 文档，展示 `spring.factories` 文件的内容，用于实现自动配置。
*   **00:02:31 - 00:02:45**: 讲师在文档中解释了 `@ConfigurationProperties` 注解的作用，以及如何通过 `spring.factories` 文件将自定义配置类注册到 Spring Boot 的自动配置机制中。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档内容**:
    *   **章节标题**: “3.2 自定义OAUTH2启动器” 和 “3.3 自定义OAUTH2启动器与后台管理服务集成使用”。
    *   **关键说明**:
        *   “采用Spring Session统一话认证，来进行鉴权，最少要保障登录和菜单权限的鉴权。”
        *   “启动器加了注解@ConfigurationProperties(prefix = 'security.oauth2.client')，根据属性名称会自动将配置映射处理。”
        *   “为减少配置，默认把‘/actuator/’, ‘/v2/’, ‘/doc.html’, ‘/swagger-ui.html’, ‘/css/**’这些路径放行。”
        *   **`spring.factories` 文件内容**:
            ```
            # Auto Configure
            org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
            com.itcast.trade.stock.starter.oauth.AutoOAuth2Configuration
            ```

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-oauth2</artifactId>
            <version>${spring-cloud-starter.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-security</artifactId>
            <version>${spring-cloud-starter.version}</version>
        </dependency>
        ```
    *   **`AutoOAuth2Configuration.java` 核心配置**:
        ```java
        @Configuration
        @EnableAutoConfiguration
        @EnableResourceServer
        @EnableGlobalMethodSecurity(prePostEnabled = true)
        @ConditionalOnProperty(name = "security.oauth2.resource.token-info-uri")
        public class AutoOAuth2Configuration implements ResourceServerConfigurer {

            @Autowired
            private RemoteTokenServices remoteTokenServices;

            @Autowired
            private RestTemplate lbRestTemplate;

            @Setter
            private List<String> ignoreUrls;

            @Override
            public void configure(HttpSecurity httpSecurity) throws Exception {
                ExpressionUrlAuthorizationConfigurer<HttpSecurity> registry = httpSecurity.csrf().disable()
                        .authorizeRequests();

                // 设置无须认证的url路径
                if (null != ignoreUrls && ignoreUrls.size() > 0) {
                    registry.antMatchers(ignoreUrls.toArray(new String[ignoreUrls.size()])).permitAll();
                }

                registry
                    .antMatchers("/actuator/**", "/v2/**", "/doc.html", "/swagger-ui.html", "/css/**")
                    .permitAll()
                    .anyRequest().authenticated()
                    .formLogin().loginPage("/login")
                    .failureUrl("/login/error")
                    .defaultSuccessUrl("/home");
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理** (00:00:16 - 00:00:45)
    *   讲师在 IDEA 中打开 `stock-starter-oauth2` 项目，展示了其标准的 Maven 项目结构。
    *   讲师在 `pom.xml` 中添加了 `spring-cloud-starter-oauth2` 和 `spring-cloud-starter-security` 依赖，为后续的 OAuth2 和安全功能做准备。

*   **场景二：核心配置类编写** (00:00:46 - 00:01:45)
    *   讲师创建并打开了 `AutoOAuth2Configuration.java` 文件。
    *   讲师定义了类，并添加了 `@Configuration`、`@EnableResourceServer`、`@EnableGlobalMethodSecurity` 等注解，表明这是一个资源服务器配置。
    *   讲师声明了 `RemoteTokenServices` 和 `RestTemplate` 两个成员变量，并添加了 `@Setter` 注解用于配置属性。
    *   讲师编写了 `configure` 方法，使用 `HttpSecurity` 对象配置权限规则，包括设置忽略的 URL 路径和公开的 API 路径。

*   **场景三：配置属性与自动配置** (00:01:46 - 00:02:30)
    *   讲师在 `configure` 方法中，通过 `antMatchers` 方法配置了多个路径的访问权限，包括 `/actuator/**`、`/v2/**`、`/doc.html`、`/swagger-ui.html` 和 `/css/**`，这些路径被设置为无需认证即可访问。
    *   讲师配置了登录页面和错误页面的跳转地址。
    *   讲师切换到 Typora 文档，展示了 `spring.factories` 文件的内容，解释了如何通过 `EnableAutoConfiguration` 注册自定义配置类，使其在 Spring Boot 启动时自动生效。

*   **场景四：配置属性绑定** (00:02:31 - 00:02:45)
    *   讲师在 PPT 中解释了 `@ConfigurationProperties` 注解的作用，即通过 `prefix` 属性将外部配置文件中的属性值自动绑定到类的成员变量上，从而实现配置的动态化和可管理性。
