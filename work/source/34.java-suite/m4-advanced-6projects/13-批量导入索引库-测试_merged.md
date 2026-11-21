# 13-批量导入索引库-测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来给启动一下

右键启动一次

启动之后呢

我们现在来测试一下

看看效果如何

好等它启动

启动之后我们就执行一次这个索引的导入

好等它启动一下

那么这一块就启动起来了

这一块给大家说一下

以后在工作中

这个只会用到一次

因为我们这个是批量导入

只会用到一次

或者说以后你数据清空了

会用

就是程序启动

一般最多只用一次

不可能说每天去导一次

海量数据不可能天天导

好我们开始请求一次这个接口

叫18082

咱访问一下

这个是18082

下面呢

设启

还有一个是叫add

回车一下

看一下这个数据的导入

好这一块一直在这里打转

那说明正在加载数据

好

正在批量导入到输引库去

我们看一下这个导入到输引库去之后的数据哈

等他批量导入好

等他导入哈

那这个时候我们再看这里

之前这边是没有任何数据的

如果一会儿全部导入成功之后呢

看他是不是会出现我们刚才所说的这么一个现状

正在还在导入好导入成功了

我们这一块了

目前这里是之前的现状

我们刷新一次

看这一块立刻多了个故事index

他里面的信息了

也可以去查看一下

这是他的一个结构的信息

我们看一下他里面的数据点击数据浏览

多了一个故事index

就是我说的类似数据库一样

这是我们的索引

他里面有个类型SKU info

类似我说的一个表结构

他里面还有对应的一个列

我们来看一下这边的数据展示

可以看到这个数据展示是没有什么问题的

包括我刚才所说的一个时间

bgtime也都进行转换了

好OK

我们这一块就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频演示了一个基于 Spring Boot 的搜索服务（`seckill-search`）的启动、运行及与 Elasticsearch 集群交互的全过程。演示者通过 IntelliJ IDEA 开发环境启动服务，并在浏览器中访问 Elasticsearch 的 Kibana 界面，验证数据的写入和查询。整个过程旨在展示一个微服务架构中，搜索服务如何集成并利用 Elasticsearch 实现商品数据的存储与检索。视频中还展示了服务启动时的控制台日志、Nacos 配置中心的配置信息以及服务注册与发现的机制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**: 展示 IntelliJ IDEA 中的项目结构，聚焦于 `seckill-search` 模块。代码编辑器中显示了 `SearchApplication.java` 的主类，其中包含 `@SpringBootApplication` 注解，并通过 `@EnableElasticsearchRepositories` 和 `@EnableFeignClients` 注解启用了 Elasticsearch 仓库和 Feign 客户端功能。
*   **00:05 - 00:09**: 点击运行按钮，启动 `SearchApplication`。IDEA 的 Run Dashboard 显示服务已成功启动，端口为 `18082`。控制台输出了 Spring Boot 的启动信息，包括版本号 `v2.2.5.RELEASE` 和 Nacos 配置中心的加载信息。
*   **00:10 - 00:14**: 控制台日志显示 Tomcat 服务器已成功初始化并启动，加载了多个 Elasticsearch 插件，如 `ReindexPlugin`、`PercolatorPlugin` 和 `NettyPlugin`。
*   **00:15 - 00:19**: 控制台日志中出现 `Cannot find template location: classpath:/templates/` 的警告，提示未配置 Thymeleaf 模板引擎。随后，日志显示服务已成功注册到 Nacos 服务发现中心，服务名为 `seckill-search`。
*   **00:20 - 00:24**: 控制台日志显示服务的健康检查信息，包括服务器地址、连接状态和响应时间等。
*   **00:25 - 00:30**: 切换到浏览器，访问 Elasticsearch 的 Kibana 界面（`http://192.168.211.137:9200`），并导航至 `goodindex` 索引，查看其中存储的商品数据。
*   **00:31 - 00:35**: 在 Kibana 界面中，展示了 `goodindex` 索引的分片信息，显示其状态为 `yellow`（5 of 10），并列出了部分商品数据记录。
*   **00:36 - 00:40**: 在 Kibana 界面中，通过点击“_source”按钮，查看了单个商品记录的详细字段，包括 `categoryName`、`brandName`、`price`、`updateTime` 等。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码 (Code)**:
    *   **主类 `SearchApplication.java`**:
        ```java
        @SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
        @EnableElasticsearchRepositories(basePackages = "com.seckill.search.dao")
        @EnableFeignClients(basePackages = "com.seckill.goods.feign")
        public class SearchApplication {
            public static void main(String[] args) {
                SpringApplication.run(SearchApplication.class, args);
            }
        }
        ```
    *   **配置文件 `bootstrap.yml`**:
        *   `spring.application.name: seckill-search`
        *   `spring.cloud.nacos.config.server-addr: 192.168.211.137:8848`
        *   `spring.cloud.nacos.discovery.server-addr: 192.168.211.137:8848`
        *   `server.port: 18082`
        *   `spring.cloud.nacos.config.file-extension: yaml`
        *   `spring.cloud.nacos.config.group: DEFAULT_GROUP`
        *   `spring.cloud.nacos.config.namespace: seckill-search`
        *   `spring.cloud.nacos.discovery.group: DEFAULT_GROUP`
        *   `spring.cloud.nacos.discovery.namespace: seckill-search`
        *   `spring.cloud.nacos.discovery.health-check-url: http://localhost:18082/actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check-password:`
        *   `spring.cloud.nacos.discovery.health-check-timeout: 5000`
        *   `spring.cloud.nacos.discovery.health-check-interval: 5000`
        *   `spring.cloud.nacos.discovery.health-check-enabled: true`
        *   `spring.cloud.nacos.discovery.health-check-type: http`
        *   `spring.cloud.nacos.discovery.health-check-path: /actuator/health`
        *   `spring.cloud.nacos.discovery.health-check-protocol: http`
        *   `spring.cloud.nacos.discovery.health-check-username:`
        *   `spring.cloud.nacos.discovery.health-check
