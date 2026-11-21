# 07-热点数据实时收集实时分析实时隔离测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们测试一下日志时事收集

热点数据时事分析和时事隔离

我们在这一块给它创建一个启动类

启动类就叫monitor application sprint

好 给个主方法

这里写个sprint application.run

当前这个对象的直接码给它

好 这是这一块

我们这里用到了一个分接口

我们要把这个分接口对应的包给写进来

包在哪里呢

包在这一块

调这个分接口

调这个方法

好 这里缺了个sku

补上去

把这个接口的全系列名

对应的包路径给拷过来

好了

这一块就搞定了

那么还有一个地方要改造一下

就是我们这一块去查询我们罪的的时候

没有

没有用到我们数据供应链接词

但其实我们应该要用数据供应链接词

那怎么办呢

在这里我们把这个配置给取消掉

这个就是我们数据源的配置

但是注意一下

这个驱动就不要写成别的了

写它

好 OK

我们紧接着来把这一块给改造一下

注入我们的数据源

privacy

data source

或者你写个叫罪的data source都可以

这个是

888的罪的

那这一块呢

我们可以把它换一下

不用之前那种方式

用我们的data source

点get connection

这种方式

链接词来管理我们对应的链接就会好一些

好

我们来启动测试一下

看看效果

它会去调我们的故事服务

故事服务先启动

紧接着再启动我们当前这个服务

等故事服务启动

再启动当前这个服务

好

故事服务启动了

我们开始启动当前这个monitor监控服务

启动一下

启动之后呢

我们来测试一下热点数据的实时收集和实时分析

以及实时隔离

等它启动

我们看一下这一块这个数据

刷新一下

目前只有这一个对不对

好

程序起来了

等它起来

好

那么起来之后呢

我们看一下

它一会儿呢

会掉那边的查询

行

掉了一次

我们看这个ready的缓存里面

数据有没有刷新

有一条记录

但是这是之前的

对吧

我们看这个

44

看这有没有44

没有44

说明这个数据是不是没有进行隔离操作

没有进行隔离操作

我们看这个数据是不是有问题

我们查询一下

slack的

信号from

我们放大一点

tbskuwellid.in

行

我们先查询一下这条记录

看它是不是数据有问题

这里已经锁定

所以是改不了的

把它换一下

好

再看这一块

看这一块现在还

哎

那说明那个商品刚才就已经隔离了

好

刷新一下

44来了吧

数据也来了

OK

那我们的热点数据

热点数据隔离

也搞定了

那是不是实时隔离了

我们来做一个测试

我们换一个商品

就拿这个商品为例吧

这一个

我们查询一下这个商品的状态

查询一下

没有锁定

对不对

我们把这个商品模拟个页面

在这边去模拟一个对应的页面好

这块我们找到了一个静态页

看一下这一块

我们把这个页面的变化

当前的这个页面给拷贝一份

拷贝成

这个页面

好拷贝了

拷贝了呢我们这个时候

来访问一下这个页面

回车页面是可以访问的

但是我们看一下现在会不会

被收集到

只访问了一次是不会被收集的

对不对这里肯定也不会有数据

想都不用想对吧

再刷新一次

也不会有因为只访问了

两次对不对也没有

好我们开始刷新

第三次大家看

我现在再来刷新第三次

你看他马上收集到了

对吧马上收集了

看这边是不是马上隔离了

隔离了吧热点数据实时收集

热点数据实时分析

热点数据实时隔离

这一块我们就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一个关于 Spring Cloud 微服务架构的实战教学片段，主要演示了如何构建一个商品监控系统。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目的目录结构、核心配置文件（如 `bootstrap.yml`）、主启动类（`MonitorApplication` 和 `GoodsApplication`）以及服务间的调用关系。视频重点讲解了如何使用 `@EnableFeignClients` 注解启用 Feign 客户端，并通过 `@SpringBootApplication` 和 `@EnableDiscoveryClient` 注解来配置服务发现与启动。同时，讲师也展示了如何通过 `@Value` 注解注入配置项，以及如何使用 `@Autowired` 注解注入 `DataSource` 和 `RedisTemplate` 等 Bean。视频中还涉及了数据库查询、Redis 数据操作以及通过浏览器访问服务的场景，旨在帮助学习者理解微服务项目的实际开发与部署流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示项目结构，鼠标选中 `seckill-monitor` 模块。
*   **00:00:05 - 00:00:10**：展示 `MonitorApplication.java` 的主类，重点讲解 `@SpringBootApplication` 和 `@EnableFeignClients` 注解。
*   **00:00:10 - 00:00:15**：切换到 `MonitorItemsAccess.java`，展示 `@Value` 注解注入 `druidurl` 和 `@Autowired` 注解注入 `RedisTemplate`。
*   **00:00:15 - 00:00:20**：展示 `MonitorItemsAccess.java` 中的 `loadData()` 方法，演示如何通过 JDBC 连接数据库并解析结果集。
*   **00:00:20 - 00:00:25**：展示 `MonitorItemsAccess.java` 中的 `@Autowired DataSource dataSource;` 代码，并列出 `DataSource` 的多种实现类。
*   **00:00:25 - 00:00:30**：回到 `MonitorApplication.java`，展示 `@EnableFeignClients(basePackages = "com.seckill.goods.feign")` 的配置。
*   **00:00:30 - 00:00:35**：展示 `GoodsApplication.java`，讲解 `@SpringBootApplication` 和 `@EnableDiscoveryClient` 注解。
*   **00:00:35 - 00:00:40**：在 Run Dashboard 中，启动 `MonitorApplication` 和 `GoodsApplication`。
*   **00:00:40 - 00:00:45**：在 Console 中查看应用启动日志，确认服务已成功启动。
*   **00:00:45 - 00:00:50**：展示多个开发工具窗口，如 IntelliJ IDEA、Docker、Navicat Premium 等。
*   **00:00:50 - 00:00:55**：在 Navicat Premium 中查看数据库表 `seckill_goods` 的数据。
*   **00:00:55 - 00:01:00**：在浏览器中访问服务，页面显示“商品详情”。
*   **00:01:00 - 00:01:05**：在 Redis Desktop Manager 中查看 Redis 数据，展示 `info` 和 `mset` 命令的执行结果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   项目结构图：展示了 `seckill-monitor` 模块下的 `src/main/java/com/seckill/monitor` 和 `src/main/resources` 目录结构。
    *   服务启动日志截图：展示了 `MonitorApplication` 和 `GoodsApplication` 启动时的控制台日志。
    *   数据库表截图：展示了 `seckill_goods` 表中的数据，包含商品 ID、价格、库存等字段。
    *   Redis 数据截图：展示了通过 Redis Desktop Manager 查看的 Redis 数据，包括 `info` 和 `mset` 命令的执行结果。

*   **代码**：
    *   `MonitorApplication.java`：
        ```java
        @SpringBootApplication
        @EnableFeignClients(basePackages = "com.seckill.goods.feign")
        public class MonitorApplication {
            public static void main(String[] args) {
                SpringApplication.run(MonitorApplication.class, args);
            }
        }
        ```
    *   `MonitorItemsAccess.java`：
        ```java
        @Value("${druidurl}")
        private String druidurl;

        @Autowired
        private RedisTemplate redisTemplate;

        @Autowired
        private DataSource dataSource;

        public List<String> loadData() throws Exception {
            Connection connection = (AvaticaConnection) DriverManager.getConnection(druidurl);
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(druidSQL);
            List<String> ids = new ArrayList<>();
            while (resultSet.next()) {
                String uri = resultSet.getString(columnLabel).replace(target, replacement).replace(target, ".html");
                ids.add(uri);
            }
            return ids;
        }
        ```
    *   `GoodsApplication.java`：
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        public class GoodsApplication {
            public static void main(String[] args) {
                SpringApplication.run(GoodsApplication.class, args);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与启动配置**（00:00:00 - 00:00:30）
    *   讲师首先展示了项目的整体结构，重点介绍了 `seckill-monitor` 模块。
    *   接着，讲师在 `MonitorApplication.java` 中演示了如何使用 `@SpringBootApplication` 注解来启动 Spring Boot 应用，并通过 `@EnableFeignClients` 注解来启用 Feign 客户端，用于服务间的调用。
    *   随后，讲师切换到 `MonitorItemsAccess.java`，演示了如何使用 `@Value` 注解注入配置项 `druidurl`，以及如何使用 `@Autowired` 注解注入 `RedisTemplate` 和 `DataSource`。

*   **场景二：数据库与 Redis 操作**（00:00:30 - 00:01:00）
    *   讲师在 `MonitorItemsAccess.java` 中演示了如何通过 JDBC 连接数据库，并执行 SQL 查询。
    *   讲师展示了 `loadData()` 方法中如何解析查询结果，并将结果存储到 `List<String>` 中。
    *   讲师在 Navicat Premium 中查看了 `seckill_goods` 表的数据，展示了商品的详细信息。
    *   讲师在 Redis Desktop Manager 中执行了 `info` 和 `mset` 命令，查看了 Redis 中的数据。

*   **场景三：服务启动与访问**（00:01:00 - 00:01:05）
    *   讲师在 Run Dashboard 中启动了 `MonitorApplication` 和 `GoodsApplication`。
    *   讲师在 Console 中查看了服务启动日志，确认服务已成功启动。
    *   讲师在浏览器中访问了服务，页面显示了商品详情。

---

以上是根据视频画面进行的结构化分析，希望对您有所帮助。
