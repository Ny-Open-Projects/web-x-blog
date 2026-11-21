# 05-热点数据实时发现测试 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们测试一下这一块

这一块呢

注意我们写掉了一个URI

因为我要查询URI

对吧

好

接着我们开始启动我们这一块

那么启动这一块呢

我们就得给它写一个启动类

对不对

启动类呢

我就写个monitor application

在这一块加个sperm boot application

注意我们是要禁止数据源的一个加载的

点class

psvm

sperm application.run

当前这它的字节码给它

点class

ax

好

不要忘了

我这里用到了我们的

我这里用到了我们的redis

这里呢

我们需要把redis相关的配置给加载一下

这里有一个叫做redis configure

这里呢

并没有让它自动加载

因此我们这里需要手动让它加载

在这里我们写一个bin

public

public

public

public

public

public

public

public

public

public

好

直接遛一个redis configure就可以了

这里呢

写一个bin

OK

紧接着我们再来启动我们的程序

看一下效果怎么样

启动一次

那么启动一次呢

我们来看一下这里

刷新一下这个商品详情

多刷两下

让他一会儿能够找到这个热点

好

找到了

对吧

我们再做另外一个事情

再增加一个热点商品

怎么增加呢

usr local server web这里

做这么一个事情

把它拷贝一份

1.html

这是1.html

我们来看一下

这里有没有1.html

目前这里是没有输出1.html的

对不对

那1.html我们访问一次

回车访问了

它这个时候不是热点数据

所以查不到是正常的

接着我们开始做另外一个事情

把它给多刷两次

大家看

我多刷两次

它是不是就应该变成热点呢

目前还是没有变成热点

因为我还没有刷

刷新一次

两次了还不是热点

要大于两次才是热点

那我再刷一次

它就是热点了

好大家看能不能发现

发现了吧

热点数据实时发现

于是就搞定了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 Java 项目，其核心功能是实现一个“热点商品监控”系统。该系统通过定时任务（Quartz）定期查询数据库中的商品访问量，并将访问量超过阈值的商品 ID 存入 Redis 集群，以供前端或其他服务实时查询。视频主要演示了如何在 Spring Boot 项目中配置定时任务、编写数据查询逻辑、以及将结果存入 Redis。整个过程在 IntelliJ IDEA 开发环境中进行，涉及了 Java 代码编写、项目结构管理、Spring Boot 启动和 Redis 数据操作。

---

### 2) 按时间顺序的章节（带时间点）

由于无法精确获取视频的时间戳，以下章节基于画面内容和逻辑顺序进行划分：

*   **章节 1：项目结构与启动配置 (0:00 - 0:05)**
    *   展示了项目的整体目录结构，包括 `seckill-service`, `seckill-monitor` 等模块。
    *   选中 `MonitorApplication.java` 文件，准备进行代码编写。

*   **章节 2：编写定时任务核心逻辑 (0:05 - 0:15)**
    *   在 `MonitorApplication.java` 中，使用 `@SpringBootApplication` 注解启动 Spring Boot 应用。
    *   为 `MonitorApplication` 类添加 `@Component` 注解，使其成为一个 Spring Bean，以便被定时任务扫描到。

*   **章节 3：编写数据查询与 Redis 存储逻辑 (0:15 - 0:30)**
    *   在 `MonitorApplication.java` 中，编写了核心的 SQL 查询语句，用于统计过去一小时内访问量大于 2 的商品。
    *   代码中使用了 `redisTemplate.keys(pattern: "SKU_*")` 方法，从 Redis 中获取所有以 "SKU_" 开头的 key。
    *   通过 `for` 循环遍历这些 key，构建 SQL 查询语句，最终将查询结果拼接成一个完整的 SQL 语句。

*   **章节 4：配置 Redis 集群与启动应用 (0:30 - 0:45)**
    *   在 `RedisConfig.java` 文件中，配置了 Redis 的连接信息。
    *   为 `MonitorApplication` 类添加 `@Configuration` 注解，使其成为一个配置类。
    *   在 `MonitorApplication.java` 中，通过 `@Bean` 注解定义了一个 `RedisConfig` 的实例。

*   **章节 5：运行应用与结果演示 (0:45 - 1:00)**
    *   点击运行按钮，启动 Spring Boot 应用。
    *   在浏览器中访问 `/items/` 接口，查看返回的热点商品 ID。
    *   在控制台中，可以看到应用启动成功，并输出了热点商品 ID。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1：SQL 查询语句**
    ```java
    String prefix = "SELECT COUNT(*) AS 'viewCount' FROM logsItems WHERE _time > CURRENT_TIMESTAMP - INTERVAL '1' HOUR";
    String suffix = " GROUP BY uri HAVING viewCount > 2";
    ```

*   **代码片段 2：Redis Key 查询与处理**
    ```java
    Set<String> keys = redisTemplate.keys(pattern: "SKU_*");
    if (keys != null && keys.size() > 0) {
        for (String key : keys) {
            sql += "/web/items/" + key.substring(4) + ".html";
        }
        sql = sql.substring(beginIndex, endIndex);
    }
    ```

*   **代码片段 3：Spring Boot 启动类**
    ```java
    @SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
    public class MonitorApplication {
        public static void main(String[] args) {
            SpringApplication.run(MonitorApplication.class, args);
        }
    }
    ```

*   **代码片段 4：Redis 配置类**
    ```java
    @Configuration
    public class RedisConfig {
        @Bean
        public RedisConfig redisConfig() {
            return new RedisConfig();
        }
    }
    ```

*   **PPT / 图表内容：**
    *   **标题：** “热点数据隔离”
    *   **要点 a：** “编写定时任务 -> 定时查询 Druid”
    *   **要点 b：** “配置 Redis 集群 -> 热点商品存入到 Redis”
    *   **要点 c：** “每次定时查询热点商品的时候，需要排除”

---

### 4) 关键场景与演示描述

*   **场景 1：项目结构展示**
    *   **描述：** 视频开始时，展示了 IntelliJ IDEA 中的项目结构，重点突出了 `seckill-monitor` 模块下的 `MonitorApplication.java` 文件。这表明了当前操作的焦点。

*   **场景 2：定时任务配置**
    *   **描述：** 在 `MonitorApplication.java` 中，开发者为类添加了 `@Component` 注解，使其能够被 Spring 定时任务框架识别。这一步是实现定时任务的基础。

*   **场景 3：SQL 语句与 Redis 逻辑编写**
    *   **描述：** 开发者在代码中编写了用于查询热点商品的 SQL 语句，并通过 `redisTemplate.keys()` 方法获取 Redis 中的 SKU Key。随后，通过 `for` 循环将这些 Key 拼接成完整的 SQL 查询语句，最终返回一个完整的 SQL 语句。

*   **场景 4：Redis 配置与启动**
    *   **描述：** 在 `RedisConfig.java` 文件中，开发者通过 `@Configuration` 注解定义了一个配置类，并通过 `@Bean` 注解定义了一个 `RedisConfig` 实例。这一步是为了在 Spring Boot 应用中配置 Redis 连接。

*   **场景 5：应用运行与结果展示**
    *   **描述：** 点击运行按钮后，Spring Boot 应用成功启动。在浏览器中访问 `/items/` 接口，返回了热点商品 ID。在控制台中，可以看到应用启动成功，并输出了热点商品 ID。这表明了整个系统功能的实现。

---

以上是根据视频画面进行的结构化技术分析报告。
