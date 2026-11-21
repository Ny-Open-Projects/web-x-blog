# 16-全局权限控制-过滤器配置使用 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,接着咱们去实现过滤器的配置和使用

在这里咱们是通过注解方式来进行配置实现

这样会比较简单

不用再去写一系列的配置

比如说通过XML去做对应的配置

写起来会比较繁琐

那咱们来看一下通过SlimBoot注解方式如何去实现

那首先咱们要在过滤器上面增加WebFilter的注解

在Lead上面增加一个WebFilter的注解

这个咱们已经加上去了

咱们注意它的UIL的Pattern

这个是指过滤器它所能拦截的请求路径

杠心是代表拦截了所有的接口请求

这个和咱们之前在WebXML里面配置的Filter过滤器都是一样的

不同的是它现在是通过注解的方式

帮助咱们去自动扫描和实现

咱们可以看到它是在HomeKit这个包下面的

有了这个注解还不能保证这个过滤器能够正常生效

咱们还需要在启动内上面去增加一个扫描注解

这个扫描注解咱们加在下面

它是Severate Compact Skin

咱们给它一个基础的扫描路径

这里咱们就配置它的基础包

基础包是TOM.idcast

它的意思

它会去扫描路径

扫描Severate过滤器等相关的配置信息

它会根据咱们指定的路径进行了相应的扫描

这样的这个过滤器才能够真正生效

最后咱们还检查一下SplitDataCache这个组件依赖是否加入到咱们工程当中

咱们在这里采用的是SplitDataLadies做的实现

所以咱们要检查POM的依赖

在这里要确保

咱们的SplitDataLadies

这个组件加入成功

咱们检索一下

这个是SessionDataLadies

并非SplitDataLadies

咱们要将相关的依赖加入进去

加入进去之后

在过滤器当中

咱们才能够真正去操作对应的仿生数据

整个过滤器的配置使用就比较简单

首先咱们是要加上对应的WebField路径

接着咱们要指定它的扫描路径

这个扫描路径一定要包含咱们Field所在包下面的路径

最后因为Field当中咱们是用到了SplitDataLadies缓存功能

所以我们必须要将这个依赖添加进去

这样才可以实现对Ladies缓存的操作

好

这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 和 Spring Cloud 的“行情服务”系统的开发教程，主要讲解了如何实现一个全局的权限过滤器（`GlobalSecurityFilter`）。讲师通过代码演示，说明了如何使用 `@WebFilter` 注解将一个 Java Filter 注册为 Servlet 过滤器，并通过 `@Autowired` 注入 `CacheManager` 以支持基于 Redis 的缓存功能。同时，视频也展示了如何在 Spring Boot 启动类上使用 `@ServletComponentScan` 注解来扫描并注册自定义的 Servlet 组件，以及如何在 `pom.xml` 中配置必要的依赖，如 Spring Boot 的 Redis Starter 和 Spring Session。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 Typora 文档中展示课程大纲，当前章节为“3.3 过滤器的配置使用”。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示 `GlobalSecurityFilter` 类的代码，讲解其通过 `@WebFilter` 注解实现全局拦截。
*   **00:15 - 00:25**: 讲师在 `StockAdminUserApplication` 启动类中，演示如何使用 `@ServletComponentScan` 注解来扫描并注册 `GlobalSecurityFilter`。
*   **00:25 - 00:35**: 讲师在 `pom.xml` 文件中，展示并讲解了项目所需的依赖，包括 `spring-boot-starter-data-redis` 和 `spring-session-data-redis`。
*   **00:35 - 00:45**: 讲师继续在 `pom.xml` 中，展示并讲解了 `bulls-stock-common-web` 和 `bulls-stock-common-entity` 等公共模块的依赖。
*   **00:45 - 00:55**: 讲师回到 Typora 文档，总结了本节内容，强调了 `@ServletComponentScan` 注解的作用和 Redis 缓存的配置。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “3.3 过滤器的配置使用”。
    *   **关键说明**: “这里通过注解方式来实现，比较简单，不用再写一系列的配置。”
    *   **关键说明**: “要让过滤器生效，在启动类上面加上扫描`@ServletComponentScan`注解”。
    *   **关键说明**: “检查Redis缓存依赖是否加上，因为内部要用到Spring Cache，这里是采用Redis作为存储”。

*   **代码关键内容**:

    *   **`GlobalSecurityFilter` 类**:
        ```java
        @WebFilter(urlPatterns = "/*")
        public class GlobalSecurityFilter implements Filter {
            private static final Set<String> AUTH_PATHS = Collections.unmodifiableSet(new HashSet<>(Arrays.asList("/authority/*", "/auth/*")));
            @Autowired
            private CacheManager cacheManager;
            @Override
            public void init(FilterConfig filterConfig) throws ServletException {
                // 初始化
            }
        }
        ```
        *   `@WebFilter(urlPatterns = "/*")`: 定义了该过滤器将拦截所有请求。
        *   `AUTH_PATHS`: 一个不可变的集合，用于存储需要特殊处理的路径前缀。
        *   `@Autowired private CacheManager cacheManager;`: 注入 Spring Cache 的管理器，用于与 Redis 进行交互。

    *   **`StockAdminUserApplication` 启动类**:
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @ComponentScan(basePackages = "com.itcast")
        @Import(SpringDataRestConfiguration.class)
        @EntityScan(basePackages = "com.itcast")
        @EnableJpaRepositories(basePackages = "com.itcast")
        @EnableTransactionManagement
        @EnableRedisHttpSession
        @ServletComponentScan(basePackages = "com.itcast")
        public class StockAdminUserApplication {
            public static void main(String[] args) {
                SpringApplication.run(StockAdminUserApplication.class, args);
            }
        }
        ```
        *   `@ServletComponentScan(basePackages = "com.itcast")`: 用于扫描 `com.itcast` 包下的所有 `@WebFilter`、`@WebListener` 和 `@WebServlet` 注解的类，并将它们注册到 Servlet 容器中。

    *   **`pom.xml` 依赖配置**:
        ```xml
        <!-- 缓存依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
            <version>${spring-cloud-starter.version}</version>
        </dependency>

        <!-- Spring Session 组件依赖 -->
        <dependency>
            <groupId>org.springframework.session</groupId>
            <artifactId>spring-session-data-redis</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- 公共数据组件依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-common-dao</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- 实体依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-common-entity</artifactId>
            <version>${project.stock.version}</version>
        </dependency>

        <!-- 公用WEB层组件依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>bulls-stock-common-web</artifactId>
            <version>${project.stock.version}</version>
        </dependency>
        ```

---

### 4) 关键场景与演示描述

*   **场景一：全局过滤器的创建与配置** (00:05 - 00:15)
    *   **描述**: 讲师在 IntelliJ IDEA 中打开 `GlobalSecurityFilter.java` 文件，向观众展示如何通过 `@WebFilter` 注解将一个普通的 Java Filter 类注册为 Servlet 过滤器。他强调了 `urlPatterns = "/*"` 的作用，即对所有请求进行拦截。

*   **场景二：启动类的配置** (00:15 - 00:25)
    *   **描述**: 讲师在 `StockAdminUserApplication.java` 文件中，将光标移动到 `@ServletComponentScan` 注解上，向观众解释，只有在启动类上添加此注解，才能让 Spring Boot 容器识别并注册 `GlobalSecurityFilter`。他演示了注解的使用方式和作用范围。

*   **场景三：依赖配置** (00:25 - 00:45)
    *   **描述**: 讲师在 `pom.xml` 文件中，逐个展示并讲解了项目所需的依赖。他首先展示了 `spring-boot-starter-data-redis` 依赖，用于支持 Redis 缓存功能；接着展示了 `spring-session-data-redis` 依赖，用于实现基于 Redis 的会话管理；最后，他展示了 `bulls-stock-common-web` 和 `bulls-stock-common-entity` 等公共模块的依赖，说明了项目模块化的设计。

*   **场景四：文档总结** (00:45 - 00:55)
    *   **描述**: 讲师回到 Typora 文档，总结了本节内容。他再次强调了 `@ServletComponentScan` 注解的重要性，并指出项目中使用了 Redis 作为缓存存储，以支持后续的权限控制和会话管理功能。
