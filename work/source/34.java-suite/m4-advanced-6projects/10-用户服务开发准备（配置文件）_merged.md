# 10-用户服务开发准备（配置文件） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,我们是完成了这个用户服务数据模型的讲解,在这块呢,我们一共涉及到了这么两张表,对吧,一个是PD Address Book,这个呢是我们这个地址簿,这么一张表,还有一个是PD Member,这个呢是用户表,好,那么接下来呢,我们就需要来搭建一下我们这个用户服务开发准备,对吧,那么看一下我们这个用户服务呢,开发之前呢,需要准备哪些环境呢,一个是这个配置文件,对吧,这个配置文件呢,包括我们的POM文件,

还有就是什么呢,我们Spring Boot的,也就是Boosttrap相关的配置文件,然后呢,还有服务启动类,还有配置类,等等,好,那接下来呢,我们先来看啊,第一个呢,就是配置文件,咱们需要什么呢,在咱们这个PD User,我们这个服务里边来加入这两个配置,对吧,这是我们J2Catch缓存相关的,前面我们都已经讲过了,所以我们在这呢,直接复制一下,把这个两个Mainware坐标,把它复制到什么呢,PD User,这个Mainware工程的

POM文件当中来,好,咱们就直接往下放就可以了,直接放在这个位置,好,贴到这儿,好,这是第一步,然后接下来呢,我们,下一个配置文件呢,就是关于我们这个Boosttrap.yml,对吧,这是我们这个入口文件,Spring Boot入口文件,然后复制一下,好,在咱们这个PD User下边呢,我们来创建一下,好,然后呢,具体的内容呢,我就不再手敲了,咱们直接把它复制过来就可以了,好,复制一下,好,

直接贴在这儿,好,然后呢,我们这个服务呢,端口号呢,是这个,8189,啊,8189,然后呢,这个应用名称,对吧,就叫PD-User,然后呢,我们当前这个激活的环境呢,是D1V环境,这就意味着我们是不是需要再来创建啊,D1V,也就是开发环境的这个配置文件,对吧,应该根据这个规则呢,应该叫做Boosttrap-D1V,好,咱们把这个配置文件呢,把它文件名,先复制一下,

好,然后在这儿直接来创建一下,这样的话呢,在我们这个当前开发环境下呢,它除了加在这个文件之外呢,还要加在我们这个文件,而在这个文件里面才是我们具体的绝大部分的配置项,都是在这个文件里面,好,从这个量上大家也能看出来,对吧,这里面配置的内容还是非常多的,然后呢,复制一下,直接贴到这儿来,好,咱们来看一下,大概读一下,

好,我们来看一下,

好,我们来看一下,

好,我们来看一下,

好,然后呢,我们进到什么呢,这个咱们当前使用的这个品达-TMS这个命名空间下边,那么它读取的文件呢,应该就是这个,叫做PD-User-D1V,对吧,好,然后呢,我们可以来看一下,它这里边是不是配置了品达Redis,IP,part,具体的配置是不是在这儿呢,具体的配置在这儿,好,所以后期呢,我们如果要改动的话呢,是不是直接改这个位置就可以了,我们项目里边这个位置呢,

我们项目里边这个位置呢,是不是改这个位置呢,是不是改这个位置呢,

好,然后呢,我们进到这个文件呢,是不用做任何修改的,对吧,因为它全都是引用,好,然后呢,这是我们这个Redis相关的配置,回到这边来,然后这是Spring Cloud,对吧,Narcos,这些呢,我们都见过了,Discovery,这是作为这个服务注册中心,对吧,相关的配置,这是配置中心相关的,好,然后接下来是Jackson,这个还有什么Data Source,数据源,对吧,再往下呢,就是关于我们J2Cache的,对吧,J2Cache的,一级缓存,二级缓存,等等这些,Cafini,Lecture,好,

下面呢,这是关于MyBadPlus的,好,那这些配置呢,前面咱们也都见过了,大概浏览一下就可以,好,那么对于这些配置呢,我们其实没有必要自己去手敲啊,只要能看懂,然后呢,我们直接复制过来就可以了,好,这是关于这个配置文件,以及呢,我们刚才看了一下这个配置中心,对吧,还要读取这个文件,好,然后呢,还有一个呢,需要放在我们项目内部的,就是什么呢,就是咱们这个Cafini.pro,

就是这个文件,好,那接下来呢,我们需要把这个文件呢,也来复制一下,文件名复制一下,然后呢,在这儿来创建,好,放在这儿就可以了,然后呢,具体的内容呢,咱们直接拿过来,好,复制一下,在这个地方呢,我们看啊,除了有一个默认的这个region区域之外呢,咱们自己定义了这么一个叫做address book,这个是不是叫做地址部,对吧,地址部,好,然后呢,这是存放的这个size,对吧,

数量,还有这个是什么呢,过期时间,这两个小时,好,但是这个时间呢,可以自己去调整啊,那么到这儿的话呢,我们这个PD user相关的这些配置文件呢,我们就已经配置好了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“品达物流TMS项目”第3章“用户服务开发”系列课程的开篇部分，主要讲解了用户服务开发前的环境准备和配置工作。讲师通过演示如何在 Maven 项目中引入 `j2cache` 作为缓存框架，并配置其依赖的 `slf4j` 日志库（排除冲突），以及如何编写 `bootstrap.yml` 和 `bootstrap-dev.yml` 等 Spring Boot 启动配置文件。内容涵盖了服务的启动配置、数据库连接池（Druid）、Redis 缓存、Nacos 服务发现、以及二级缓存（Caffeine）的配置。整个过程旨在为后续的用户服务开发打下坚实的基础。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程开场，介绍本章主题“用户服务开发准备”，并展示项目目录结构。
*   **00:16 - 00:30**：讲解如何在 `pom.xml` 中添加 `j2cache` 的 Maven 依赖，并排除 `slf4j` 的冲突。
*   **00:31 - 00:45**：展示 `bootstrap.yml` 文件，配置服务器、Spring 应用名、环境（dev）和允许 Bean 重写。
*   **00:46 - 01:00**：展示 `bootstrap-dev.yml` 文件，配置 Nacos 服务发现、数据库连接池（Druid）和 Redis。
*   **01:01 - 01:15**：讲解 `j2cache` 的配置，包括缓存模式、Redis 客户端（Lettuce）、二级缓存（Caffeine）的广播策略和提供者。
*   **01:16 - 01:30**：展示 `caffeine.properties` 文件，配置 Caffeine 缓存的默认大小和过期时间。
*   **01:31 - 01:45**：演示如何在 IntelliJ IDEA 中打开项目并查看配置文件。
*   **01:46 - 02:00**：展示 Nacos 服务注册与发现的登录界面，准备后续的注册操作。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档结构**：
    *   项目目录结构：`品达物流TMS项目 > 第3章 用户服务开发(pd-user) > 3. 用户服务开发准备 > 3.1 配置文件`
    *   配置文件列表：`bootstrap.yml`, `bootstrap-dev.yml`, `caffeine.properties`

*   **关键代码片段**：

    *   **Maven 依赖 (pom.xml)**：
        ```xml
        <dependency>
            <groupId>net.oschina.j2cache</groupId>
            <artifactId>j2cache-spring-boot2-starter</artifactId>
            <version>2.8.0-release</version>
        </dependency>
        <dependency>
            <groupId>net.oschina.j2cache</groupId>
            <artifactId>j2cache-core</artifactId>
            <version>2.8.0-release</version>
        </dependency>
        <exclusions>
            <exclusion>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-simple</artifactId>
            </exclusion>
            <exclusion>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-api</artifactId>
            </exclusion>
        </exclusions>
        ```

    *   **Spring Boot 配置 (bootstrap.yml)**：
        ```yaml
        server:
          tomcat:
            uri-encoding: UTF-8
            max-threads: 1000
            min-spare-threads: 30
            port: 8189
            connection-timeout: 50000ms
        spring:
          application:
            name: pd-user
            # 环境 dev/test/prod
            profiles: dev
            main:
              allow-bean-definition-overriding: true
        ```

    *   **开发环境配置 (bootstrap-dev.yml)**：
        ```yaml
        spring:
          redis:
            host: ${pinda.redis.ip}
            password: ${pinda.redis.password}
            port: ${pinda.redis.port}
            database: ${pinda.redis.database}
          cloud:
            nacos:
              username: tms
              password: itheima123
            discovery:
              server-addr: 68.79.63.42:8848
              group: pinda-tms
              namespace: 6107f553-3214-48d8-89c3-945f8446e3d9
            config:
              server-addr: 68.79.63.42:8848
              file-extension: yaml
              group: pinda-tms
              namespace: 6107f553-3214-48d8-89c3-945f8446e3d9
        ```

    *   **j2cache 配置 (bootstrap-dev.yml)**：
        ```yaml
        j2cache:
          cache-clean-mode: passive
          allow-null-values: true
          redis-client: lettuce # 指定redis客户端使用lettuce，也可以使用Jedis
          l2-cache-open: true # 开启二级缓存
          broadcast: net.oschina.j2cache.cache.support.redis.SpringRedisPubSubPolicy
          provider_class: caffeine
          config_section: lettuce
          sync_ttl_to_redis: true
        ```

    *   **Caffeine 缓存配置 (caffeine.properties)**：
        ```properties
        # (name) size, xxxx[s|m|h|d]
        default=2000, 2h
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**：
    *   讲师首先在 Typora 编辑器中展示项目的大纲，明确本章目标。
    *   接着切换到 IntelliJ IDEA，打开项目 `pinda-tms-java`。
    *   在 `pom.xml` 中，讲师演示如何添加 `j2cache` 的依赖，并通过 `<exclusions>` 标签排除 `slf4j` 的冲突，确保项目依赖的兼容性。

*   **场景二：配置文件编写与管理**：
    *   讲师在 IDEA 中打开 `bootstrap.yml` 文件，逐行讲解其配置项，如服务器端口、Spring 应用名、环境变量等。
    *   随后，讲师切换到 `bootstrap-dev.yml` 文件，演示如何配置 Nacos 服务发现、Redis 和数据库连接池。
    *   讲师特别强调了 `file-extension: yaml` 和 `namespace` 的配置，这是 Spring Cloud Config 从 Nacos 获取配置的关键。

*   **场景三：缓存配置与验证**：
    *   讲师在 `bootstrap-dev.yml` 中配置了 `j2cache` 的相关参数，如缓存模式、Redis 客户端、二级缓存等。
    *   讲师在 IDEA 中打开 `caffeine.properties` 文件，演示如何配置 Caffeine 缓存的默认大小和过期时间。
    *   讲师在 `bootstrap-dev.yml` 中添加了 `sync_ttl_to_redis: true`，用于同步缓存过期时间。

*   **场景四：服务注册与发现**：
    *   讲师在 IDEA 中打开 `bootstrap-dev.yml`，并切换到 `bootstrap.yml` 文件，展示其配置。
    *   讲师在浏览器中打开 Nacos 的登录页面，准备后续的服务注册与发现操作。

---

以上是根据视频画面整理出的技术课程结构化分析。
